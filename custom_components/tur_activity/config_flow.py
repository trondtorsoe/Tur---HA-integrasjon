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
    @staticmethod
    def async_get_options_flow(config_entry):
        return TurOptionsFlow()

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

class TurOptionsFlow(config_entries.OptionsFlow):
    """Local display aliases; never transmit group names to the Tur server."""
    async def async_step_init(self,user_input=None):
        aliases=dict(self.config_entry.options.get('group_names',{}))
        coordinator=self.hass.data.get(DOMAIN,{}).get(self.config_entry.entry_id)
        groups=(coordinator.data if coordinator and coordinator.data else {}).get('leadership',{}).get('groups',[])
        available={g['group'] for g in groups}
        if not available:
            return self.async_abort(reason='no_groups')
        errors={}
        if user_input is not None:
            gid=user_input.get('group');name=user_input.get('name','').strip()
            if gid not in available or len(name)>80 or any(ord(c)<32 for c in name):
                errors['base']='invalid_name'
            else:
                if name:aliases[gid]=name
                else:aliases.pop(gid,None)
                return self.async_create_entry(title='',data={**self.config_entry.options,'group_names':aliases})
        names={g['group']:g.get('name') or 'Group' for g in groups}
        choices=[selector.SelectOptionDict(value=gid,label=f"{aliases.get(gid,names[gid])} · {gid[:8]}") for gid in sorted(available)]
        schema=vol.Schema({vol.Required('group'):selector.SelectSelector(selector.SelectSelectorConfig(options=choices,mode=selector.SelectSelectorMode.DROPDOWN)),vol.Optional('name',default=''):selector.TextSelector()})
        return self.async_show_form(step_id='init',data_schema=schema,errors=errors)
