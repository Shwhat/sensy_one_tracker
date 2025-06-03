# sensy_one_tracker
Live tracking on 2d map using mmwave sensors

## Home Assistant Integration

This repository provides a custom integration for Home Assistant to connect with the Sensy-One mmWave sensor. The integration retrieves position and presence information from the sensor over HTTP and exposes them as `sensor` entities within Home Assistant.

### Installation

1. Copy the `custom_components/sensy_one` directory to the `custom_components` folder of your Home Assistant configuration.
2. Restart Home Assistant.
3. Add the integration via the Home Assistant UI by navigating to **Settings > Devices & Services** and clicking **Add Integration**. Search for **Sensy One** and follow the prompts.

### Configuration

The integration requires the host address of the sensor. The default update interval is 5 seconds. Each instance creates the following sensors:

- `sensor.sensy_one_presence` – Boolean indicator of presence detection.
- `sensor.sensy_one_x` – X coordinate of the tracked object.
- `sensor.sensy_one_y` – Y coordinate of the tracked object.

### Development

All code is released under the GPLv3 license. Contributions are welcome.
