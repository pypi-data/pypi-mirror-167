"""Schema for Pykson."""

# https://elvia.portal.azure-api.net/docs/services/metervalueapi/operations/get-api-v2-maxhours?
# pylint: disable=invalid-name

from __future__ import annotations


def kv(key: str, map: dict) -> any | None:
    value = None if key not in map else map[key]
#    if (value is None):
#        print("Could not find", key, "in", map)
    return value

class maxHour():
    """Schema object."""

    startTime: str
    endTime: str
    value: float
    uom: str
    noOfMonthsBack: int
    production: bool
    verified: bool

    def __init__(self, map: dict) -> None:
        self.startTime = kv("startTime", map)
        self.endTime = kv("endTime", map)
        self.value = kv("value", map)
        self.uom = kv("uom", map)
        self.noOfMonthsBack = kv("noOfMonthsBack", map)
        self.production = kv("production", map)
        self.verified = kv("verified", map)
        


    def __str__(self) -> str:
        """Override default str in order to get data as a string."""
        return "startTime: {startTime}, endTime: {endTime}, value: {value}".format(
            startTime=self.startTime, endTime=self.endTime, value=str(self.value)
        )


# pylint: disable=invalid-name
class maxHourAggregate():
    """Schema object."""

    averageValue: float
    maxHours: list[maxHour] = []
    uom: str
    noOfMonthsBack: int
    
    def __init__(self, map: dict) -> None:
        self.averageValue = kv("averageValue", map)
        self.uom = kv("uom", map)
        self.noOfMonthsBack = kv("noOfMonthsBack", map)        
        self.maxHours = [maxHour(item) for item in map["maxHours"]]
        
        
        

    def __str__(self) -> str:
        """Override default str in order to get data as a string."""
        return f"Average {self.averageValue}Kwh, MaxHours {self.maxHours}"


# pylint: disable=invalid-name
class contractV2():
    """Schema object."""

    startDate: str
    endDate: str
    
    def __init__(self, map: dict) -> None:
        self.startDate = kv("startDate", map)
        self.endDate = kv("endDate", map)


# pylint: disable=invalid-name
class meteringPointV2():
    """Schema object."""


    meteringPointId: str
    maxHoursCalculatedTime: str
    maxHoursFromTime: str
    maxHoursToTime: str
    customerContract: contractV2
    maxHoursAggregate: list[maxHourAggregate]
    
    def __init__(self, map: dict) -> None:
        self.meteringPointId = kv("meteringPointId", map)
        self.maxHoursCalculatedTime = kv("maxHoursCalculatedTime", map)
        self.maxHoursFromTime = kv("maxHoursFromTime", map)
        self.maxHoursToTime = kv("maxHoursToTime", map)
        self.customerContract = kv("customerContract", map)
        self.maxHoursAggregate = [maxHourAggregate(item) for item in map["maxHoursAggregate"]]


class MaxHours():
    """Schema object."""
    meteringpoints: list[meteringPointV2]
    
    def __init__(self, map: dict) -> None:
        self.meteringpoints = [meteringPointV2(item) for item in map["meteringpoints"]]



# https://elvia.portal.azure-api.net/docs/services/metervalueapi/operations/get-api-v1-metervalues?


# pylint: disable=invalid-name
class timeSerie():
    """Schema object."""

    startTime: str
    endTime: str
    value: float
    uom: str
    production: bool = False
    verified: bool = False
    
    def __init__(self, map: dict) -> None:
        self.startTime = kv("startTime", map)
        self.endTime = kv("endTime", map)
        self.value = kv("value", map)
        self.uom = kv("uom", map)
        self.production = kv("production", map)
        self.verified = kv("verified", map)
        


# pylint: disable=invalid-name
class MeterValue():
    """Schema object."""
    fromHour: str
    toHour: str
    resolutionMinutes: int
    timeSeries: list[timeSerie]
    
    def __init__(self, map: dict) -> None:
        self.fromHour = kv("fromHour", map)
        self.toHour = kv("toHour", map)
        self.resolutionMinutes = kv("resolutionMinutes", map)
        self.timeSeries = [timeSerie(item) for item in map["timeSeries"]]
        

# pylint: disable=invalid-name
class contractV1():
    """Schema object."""
    startTime: str
    endTime: str
    
    def __init__(self, map: dict) -> None:
        self.startTime = kv("startTime", map)
        self.endTime = kv("endTime", map)

# pylint: disable=invalid-name
class meteringPointV1():
    """Schema object."""
    meteringPointId: str
    meterValue: MeterValue
    customerContract: contractV1
    
    def __init__(self, map: dict) -> None:
        self.meteringPointId = kv("meteringPointId", map)
        self.meterValue = MeterValue(kv("metervalue", map))
        self.customerContract = contractV1(kv("customerContract", map))


class MeterValues():
    """Schema object."""

    meteringpoints: list[meteringPointV1]
    
    def __init__(self, map: dict) -> None:
        self.meteringpoints = [meteringPointV1(item) for item in map["meteringpoints"]]