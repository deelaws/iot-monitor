import enum

class SensorType(enum.Enum):
    RAIN = "rain"
    SMOKE = "smoke"
    DISTANCE = "distance"
    TEMPERATURE = "temperature"

    @staticmethod
    def get_type_from_string(mtype):
        if "rain" == mtype:
            return SensorType.RAIN
        elif "smoke" == mtype:
            return SensorType.SMOKE
        elif "distance" == mtype:
            return SensorType.DISTANCE
        elif "temperature" == mtype:
            return SensorType.TEMPERATURE
        else:
            return None
        