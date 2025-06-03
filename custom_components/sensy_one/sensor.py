"""Sensor platform for Sensy One."""
from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
    SensorDeviceClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import SensyOneDataUpdateCoordinator
from .const import DOMAIN, SENSOR_PRESENCE, SENSOR_X, SENSOR_Y


@dataclass
class SensyOneSensorEntityDescription(SensorEntityDescription):
    """Class describing Sensy One sensor entity."""


SENSOR_DESCRIPTIONS = (
    SensyOneSensorEntityDescription(
        key=SENSOR_PRESENCE,
        name="Presence",
        device_class=SensorDeviceClass.POWER,  # not exact but placeholder
    ),
    SensyOneSensorEntityDescription(
        key=SENSOR_X,
        name="X Position",
    ),
    SensyOneSensorEntityDescription(
        key=SENSOR_Y,
        name="Y Position",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensors."""
    coordinator: SensyOneDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    entities: list[SensorEntity] = []

    for description in SENSOR_DESCRIPTIONS:
        entities.append(SensyOneSensor(coordinator, description))

    async_add_entities(entities)


class SensyOneSensor(CoordinatorEntity[SensyOneDataUpdateCoordinator], SensorEntity):
    """Representation of a Sensy One sensor entity."""

    entity_description: SensyOneSensorEntityDescription

    def __init__(
        self,
        coordinator: SensyOneDataUpdateCoordinator,
        description: SensyOneSensorEntityDescription,
    ) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_name = f"Sensy One {description.name}"

    @property
    def native_value(self):
        return self.coordinator.data.get(self.entity_description.key)
