"""Tur activity sharing for Home Assistant."""
from homeassistant.const import Platform
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .api import TurApi
from .const import DOMAIN, CONF_KEY
from .coordinator import TurCoordinator

async def async_setup_entry(hass,entry):
    coordinator=TurCoordinator(hass,entry,TurApi(async_get_clientsession(hass),entry.data[CONF_KEY]))
    await coordinator.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN,{})[entry.entry_id]=coordinator
    await hass.config_entries.async_forward_entry_setups(entry,[Platform.SENSOR])
    entry.async_on_unload(entry.add_update_listener(_options_updated))
    return True

async def _options_updated(hass,entry):
    await hass.config_entries.async_reload(entry.entry_id)

async def async_unload_entry(hass,entry):
    if await hass.config_entries.async_unload_platforms(entry,[Platform.SENSOR]):
        hass.data[DOMAIN].pop(entry.entry_id,None)
        return True
    return False
