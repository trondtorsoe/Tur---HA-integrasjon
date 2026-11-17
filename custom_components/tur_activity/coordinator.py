"""One coordinated request for all Tur sensors."""
from datetime import timedelta
import logging
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .api import InvalidAuth, CannotConnect
from .const import DOMAIN
_LOGGER=logging.getLogger(__name__)

class TurCoordinator(DataUpdateCoordinator):
    def __init__(self,hass,entry,api):
        super().__init__(hass,_LOGGER,name=DOMAIN,config_entry=entry,update_interval=timedelta(minutes=5))
        self.api=api
    async def _async_update_data(self):
        try:
            return await self.api.fetch()
        except InvalidAuth:
            raise ConfigEntryAuthFailed('Tur sharing key is invalid or revoked') from None
        except CannotConnect:
            raise UpdateFailed('Cannot retrieve Tur activity data') from None
