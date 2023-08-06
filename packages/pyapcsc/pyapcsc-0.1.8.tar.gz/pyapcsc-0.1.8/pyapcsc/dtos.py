""" Access classes for parsing json results from the API. """


class DeviceStatus:
    """ Device status. """

    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def plugin_status(self) -> str:
        return self._raw.get("pluginStatus")

    @property
    def ups_operating_mode(self) -> str:
        return self._raw.get("upsOperatingMode")

    @property
    def ups_firmware_status(self) -> str:
        return self._raw.get("upsFWStatus")

    @property
    def reduced_reporting_enabled(self) -> bool:
        return self._raw.get("reducedReportingEnabled")

    @property
    def monitoring_enabled(self) -> str:
        return self._raw.get("monitoringEnabled")


class Gateway:
    """ APC Device Informtion. """

    def __init__(self, raw: dict):
        self._raw = raw
        self._status = DeviceStatus(raw["status"])

    @property
    def model(self) -> str:
        return self._raw.get("model")

    @property
    def part_number(self) -> str:
        return self._raw.get("partNumber")

    @property
    def serial_number(self) -> str:
        return self._raw.get("serialNumber")

    @property
    def name(self) -> str:
        return self._raw.get("name")

    @property
    def description(self) -> str:
        return self._raw.get("description")

    @property
    def status(self) -> DeviceStatus:
        return self._status


class OutputDetails:
    """ Output details. """

    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def load_apparent_percentage(self) -> int:
        return self._raw.get("loadApparentPercentage")

    @property
    def load_real_percentage(self) -> int:
        return self._raw.get("loadRealPercentage")

    @property
    def current(self) -> int:
        return self._raw.get("current")

    @property
    def energy(self) -> int:
        return self._raw.get("energy")

    @property
    def voltage(self) -> int:
        return self._raw.get("voltage")

    @property
    def frequency(self) -> int:
        return self._raw.get("frequency")

    @property
    def low_transfer_voltage(self) -> int:
        return self._raw.get("lowTransferVoltage")

    @property
    def high_transfer_voltage(self) -> int:
        return self._raw.get("highTransferVoltage")

    @property
    def sensitivity_setting(self) -> int:
        return self._raw.get("sensitivitySetting")


class InputDetails:
    """ Detail information about the gateway. """

    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def voltage(self) -> int:
        return self._raw.get("voltage")

    @property
    def current(self) -> int:
        return self._raw.get("current")

    @property
    def frequency(self) -> int:
        return self._raw.get("frequency")


class BatteryDetails:
    """ Details about the battery. """

    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def charge_state_percentage(self) -> int:
        return self._raw.get("chargeStatePercentage")

    @property
    def runtime_remaining(self) -> int:
        return self._raw.get("runtimeRemaining")

    @property
    def temperature(self) -> int:
        return self._raw.get("temperature")

    @property
    def voltage(self) -> int:
        return self._raw.get("voltage")

    @property
    def selfTestResult(self) -> str:
        return self._raw.get("selfTestResult")

    @property
    def install_date(self) -> str:
        return self._raw.get("installDate")

    @property
    def replace_date(self) -> str:
        return self._raw.get("replaceDate")


class GatewayDetails:
    """ Detail information about the gateway. """

    def __init__(self, raw: dict):
        self._raw = raw
        self._output = OutputDetails(raw["output"])
        self._input = InputDetails(raw["input"])
        self._battery = BatteryDetails(raw["battery"])

    @property
    def output(self) -> OutputDetails:
        return self._output

    @property
    def input(self) -> InputDetails:
        return self._input

    @property
    def battery(self) -> BatteryDetails:
        return self._battery
