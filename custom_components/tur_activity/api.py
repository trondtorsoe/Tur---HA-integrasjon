"""HTTPS client. Keys are sent only in the Authorization header to the Tur server."""
import asyncio
import json
import math
import re
import aiohttp
from .const import API_URL, FIELDS, METRICS

class InvalidAuth(Exception):
    """The sharing key is invalid or revoked."""
class CannotConnect(Exception):
    """The server is unavailable or returned invalid data."""

def validate_key(key):
    if not isinstance(key, str) or not re.fullmatch(r'tur_ha_[A-Za-z0-9_-]{43}', key.strip()):
        raise InvalidAuth
    return key.strip()

def validate_payload(data):
    if not isinstance(data, dict) or data.get('ok') is not True or data.get('schema') != 1:
        raise CannotConnect
    ident=data.get('access_id')
    if not isinstance(ident,str) or not re.fullmatch(r'[a-f0-9]{32}',ident):
        raise CannotConnect
    fields=data.get('fields')
    if not isinstance(fields,list) or any(f not in (*FIELDS,'leadership') for f in fields):
        raise CannotConnect
    if not isinstance(data.get('values'),dict) or not isinstance(data.get('stale'),bool):
        raise CannotConnect
    for key,value in data['values'].items():
        if key not in FIELDS or key not in fields:
            raise CannotConnect
        if value is not None and (isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0):
            raise CannotConnect
    stamp=data.get('updated')
    if stamp is not None and (isinstance(stamp,bool) or not isinstance(stamp,int) or not 0<stamp<10**15):
        raise CannotConnect
    if stamp is not None:
        from datetime import date
        from zoneinfo import ZoneInfo
        try:
            ZoneInfo(data['timezone']);date.fromisoformat(data['date'])
        except (ValueError,KeyError,TypeError):
            raise CannotConnect from None
    leadership=data.get('leadership')
    if leadership is not None:
        if 'leadership' not in fields or not isinstance(leadership,dict) or not isinstance(leadership.get('groups'),list):
            raise CannotConnect
        for group in leadership['groups']:
            if not isinstance(group,dict) or not isinstance(group.get('group'),str) or len(group['group'])>100 or not isinstance(group.get('results'),list):
                raise CannotConnect
            if 'name' in group and (not isinstance(group['name'],str) or len(group['name'])>1000):
                raise CannotConnect
            for result in group['results']:
                if not isinstance(result,dict) or result.get('period_days') not in (1,7,30) or result.get('metric') not in METRICS or result.get('mode') not in ('measured','goal') or result.get('status') not in ('leading','tied_lead','not_leading','unknown'):
                    raise CannotConnect
    return data

class TurApi:
    def __init__(self, session, key):
        self.session=session
        self._key=validate_key(key)
    async def fetch(self):
        try:
            async with self.session.get(API_URL,headers={'Authorization':'Bearer '+self._key,'Accept':'application/json'},timeout=aiohttp.ClientTimeout(total=20),allow_redirects=False) as response:
                if response.status in (401,403):
                    raise InvalidAuth
                if response.status!=200:
                    raise CannotConnect
                chunks=[];size=0
                async for chunk in response.content.iter_chunked(65536):
                    size+=len(chunk)
                    if size>4*1024*1024:
                        raise CannotConnect
                    chunks.append(chunk)
                data=json.loads(b"".join(chunks))
        except (aiohttp.ClientError,asyncio.TimeoutError,ValueError,UnicodeDecodeError):
            raise CannotConnect from None
        return validate_payload(data)
