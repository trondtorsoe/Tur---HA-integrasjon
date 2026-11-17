"""Daily figures and own per-group leadership, with explicit missing-data handling."""
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
from homeassistant.components.sensor import SensorEntity,SensorDeviceClass,SensorStateClass
from homeassistant.const import UnitOfLength,UnitOfTime,PERCENTAGE
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.core import callback
from .const import DOMAIN,FIELDS,VERSION

SPECS={
 'steps':(None,'mdi:shoe-print',None),
 'distance_km':(UnitOfLength.KILOMETERS,'mdi:map-marker-distance',SensorDeviceClass.DISTANCE),
 'activity_minutes':(UnitOfTime.MINUTES,'mdi:timer-outline',SensorDeviceClass.DURATION),
 'ascent_m':(UnitOfLength.METERS,'mdi:elevation-rise',SensorDeviceClass.DISTANCE),
 'points':(None,'mdi:star-outline',None),
 'goal_percent':(PERCENTAGE,'mdi:bullseye-arrow',None),
}

def fresh(data):
    if data.get('stale') or data.get('updated') is None:
        return False
    try:
        now=datetime.now(timezone.utc)
        updated=datetime.fromtimestamp(data['updated']/1000,timezone.utc)
        return -300<=(now-updated).total_seconds()<=6*3600 and now.astimezone(ZoneInfo(data['timezone'])).date().isoformat()==data['date']
    except (ValueError,KeyError,TypeError,OverflowError):
        return False

async def async_setup_entry(hass,entry,async_add_entities):
    coordinator=hass.data[DOMAIN][entry.entry_id]
    async_add_entities([TurSensor(coordinator,entry,key) for key in (*FIELDS,'updated')])
    added=set()
    @callback
    def add_leadership():
        new=[]
        for group in coordinator.data.get('leadership',{}).get('groups',[]):
            gid=group['group']
            for result in group['results']:
                key=(gid,result['metric'],result['mode'],result['period_days'])
                if key not in added:
                    added.add(key);new.append(TurLeader(coordinator,entry,*key))
        if new:
            async_add_entities(new)
    add_leadership()
    entry.async_on_unload(coordinator.async_add_listener(add_leadership))

class TurBase(CoordinatorEntity,SensorEntity):
    _attr_has_entity_name=True
    def __init__(self,coordinator,entry):
        super().__init__(coordinator)
        self._attr_device_info=DeviceInfo(identifiers={(DOMAIN,entry.entry_id)},name='Tur',manufacturer='Tur',model='Activity Tracker (Beta)',sw_version=VERSION)

class TurSensor(TurBase):
    def __init__(self,coordinator,entry,key):
        super().__init__(coordinator,entry)
        self.key=key
        self._attr_unique_id=f'{entry.entry_id}_{key}'
        self._attr_translation_key=key
        if key=='updated':
            self._attr_device_class=SensorDeviceClass.TIMESTAMP
            self._attr_icon='mdi:clock-outline'
        else:
            self._attr_native_unit_of_measurement,self._attr_icon,self._attr_device_class=SPECS[key]
            self._attr_state_class=SensorStateClass.MEASUREMENT
    @property
    def available(self):
        if not super().available:
            return False
        data=self.coordinator.data
        if self.key=='updated':
            return data.get('updated') is not None
        return self.key in data['fields'] and fresh(data) and data['values'].get(self.key) is not None
    @property
    def native_value(self):
        data=self.coordinator.data
        if self.key=='updated':
            return datetime.fromtimestamp(data['updated']/1000,timezone.utc) if data.get('updated') else None
        return data['values'].get(self.key) if self.available else None
    @property
    def extra_state_attributes(self):
        return {'data_date':self.coordinator.data.get('date'),'data_timezone':self.coordinator.data.get('timezone')}

class TurLeader(TurBase):
    _attr_device_class=SensorDeviceClass.ENUM
    _attr_options=['leading','tied_lead','not_leading','insufficient_data']
    _attr_icon='mdi:podium'
    def __init__(self,coordinator,entry,gid,metric,mode,period):
        super().__init__(coordinator,entry)
        self.gid,self.metric,self.mode,self.period=gid,metric,mode,period
        self._attr_unique_id=f'{entry.entry_id}_{gid}_{metric}_{mode}_{period}'
        self._attr_translation_key=f'leadership_{metric}_{mode}_{period}'
        self._group_alias=entry.options.get('group_names',{}).get(gid)
    @property
    def translation_placeholders(self):
        if self._group_alias:
            return {'group':self._group_alias}
        for group in self.coordinator.data.get('leadership',{}).get('groups',[]):
            if group['group']==self.gid and group.get('name'):
                return {'group':group['name']}
        return {'group':self.gid[:8]}
    @callback
    def _handle_coordinator_update(self):
        self.__dict__.pop('name',None)
        super()._handle_coordinator_update()
    def result(self):
        for group in self.coordinator.data.get('leadership',{}).get('groups',[]):
            if group['group']==self.gid:
                return next((r for r in group['results'] if r['metric']==self.metric and r['mode']==self.mode and r['period_days']==self.period),None)
        return None
    @property
    def available(self):
        return super().available and 'leadership' in self.coordinator.data['fields'] and self.result() is not None
    @property
    def native_value(self):
        result=self.result()
        if not self.available:
            return None
        if not fresh(self.coordinator.data):
            return 'insufficient_data'
        return 'insufficient_data' if result['status']=='unknown' else result['status']
    @property
    def extra_state_attributes(self):
        return dict(group_id=self.gid,group_name=self.translation_placeholders['group'],period_days=self.period,metric=self.metric,comparison=self.mode,calculated=self.coordinator.data.get('leadership',{}).get('calculated'))
