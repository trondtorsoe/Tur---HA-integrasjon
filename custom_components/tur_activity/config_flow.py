"""Paste a dedicated key; no broker credentials or server address required."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers import selector
from .api import TurApi,InvalidAuth,CannotConnect,validate_key
from .const import DOMAIN,CONF_KEY

SCHEMA=vol.Schema({vol.Required(CONF_KEY):selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.PASSWORD))})

class TurConfigFlow(config_entries.ConfigFlow,domain=DOMAIN):
    VERSION=1
    async def _validate(self,user_input):
        key=validate_key(user_input[CONF_KEY])
        data=await TurApi(async_get_clientsession(self.hass),key).fetch()
        return key,data['access_id']

    async def async_step_user(self,user_input=None):
        errors={}
        if user_input is not None:
            try:
                key,ident=await self._validate(user_input)
            except InvalidAuth:
                errors['base']='invalid_auth'
            except CannotConnect:
                errors['base']='cannot_connect'
            else:
                await self.async_set_unique_id(ident)
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title='Tur',data={CONF_KEY:key})
        return self.async_show_form(step_id='user',data_schema=SCHEMA,errors=errors)

    async def async_step_reauth(self,entry_data):
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(self,user_input=None):
        return await self._replace(user_input,'reauth_confirm',self._get_reauth_entry())

    async def async_step_reconfigure(self,user_input=None):
        return await self._replace(user_input,'reconfigure',self._get_reconfigure_entry())

    async def _replace(self,user_input,step,entry):
        errors={}
        if user_input is not None:
            try:
                key,ident=await self._validate(user_input)
            except InvalidAuth:
                errors['base']='invalid_auth'
            except CannotConnect:
                errors['base']='cannot_connect'
            else:
                await self.async_set_unique_id(ident)
                self._abort_if_unique_id_configured() if entry.unique_id!=ident else None
                return self.async_update_reload_and_abort(entry,data_updates={CONF_KEY:key},unique_id=ident,reason='reauth_successful' if step=='reauth_confirm' else 'reconfigure_successful')
        return self.async_show_form(step_id=step,data_schema=SCHEMA,errors=errors)
