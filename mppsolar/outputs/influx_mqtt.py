import logging
import paho.mqtt.publish as publish

from .mqtt import mqtt

log = logging.getLogger("MPP-Solar")


class influx_mqtt(mqtt):
    def __init__(self, *args, **kwargs) -> None:
        log.debug(f"processor.influx_mqtt __init__ kwargs {kwargs}")

    def build_msgs(self, data, tag):
        # Build array of Influx Line Protocol messages
        msgs = []
        # Remove command and _command_description
        cmd = data.pop("_command", None)
        data.pop("_command_description", None)
        if tag is None:
            tag = cmd
        # Loop through responses
        for key in data:
            value = data[key][0]
            unit = data[key][1]
            # Message format is: tag, tag,setting=total_ac_output_apparent_power value=1577.0,unit="VA"
            if not unit:
                unit = ""
            msg = {
                "topic": "mpp-solar",
                "payload": f"{tag},setting={key} value={value},unit={unit}",
            }
            msgs.append(msg)
        return msgs
