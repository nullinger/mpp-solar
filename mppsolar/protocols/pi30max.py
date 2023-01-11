import logging

from .pi30 import pi30

log = logging.getLogger("pi30max")

QUERY_COMMANDS = {
    "QSID": {
        "name": "QSID",
        "description": "Device Serial Number inquiry",
        "help": " -- queries the device serial number (length greater than 14)",
        "type": "QUERY",
        "response": [["string", "Serial Number", ""]],
        "test_responses": [
            b"(1492932105105335005535\x94\x0e\r",
        ],
    },
    "QVFW3": {
        "name": "QVFW3",
        "description": "Remote CPU firmware version inquiry",
        "type": "QUERY",
        "response": [["string", "Remote CPU firmware version", ""]],
        "test_responses": [],
    },
    "VERFW": {
        "name": "VERFW",
        "description": "Bluetooth version inquiry",
        "type": "QUERY",
        "response": [["string", "Bluetooth version", ""]],
        "test_responses": [],
    },
    "QPIRI": {
        "name": "QPIRI",
        "description": "Current Settings inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            ["float", "AC Input Voltage", "V"],
            ["float", "AC Input Current", "A"],
            ["float", "AC Output Voltage", "V"],
            ["float", "AC Output Frequency", "Hz"],
            ["float", "AC Output Current", "A"],
            ["int", "AC Output Apparent Power", "VA"],
            ["int", "AC Output Active Power", "W"],
            ["float", "Battery Voltage", "V"],
            ["float", "Battery Recharge Voltage", "V"],
            ["float", "Battery Under Voltage", "V"],
            ["float", "Battery Bulk Charge Voltage", "V"],
            ["float", "Battery Float Charge Voltage", "V"],
            [
                "option",
                "Battery Type",
                [
                    "AGM",
                    "Flooded",
                    "User",
                    "TBD",
                    "Pylontech",
                    "WECO",
                    "Soltaro",
                    "LIb-protocol compatible",
                    "3rd party Lithium",
                ],
            ],
            ["int", "Max AC Charging Current", "A"],
            ["int", "Max Charging Current", "A"],
            ["option", "Input Voltage Range", ["Appliance", "UPS"]],
            [
                "option",
                "Output Source Priority",
                [
                    "Utility Solar Battery",
                    "Solar Utility Battery",
                    "Solar Battery Utility",
                ],
            ],
            [
                "option",
                "Charger Source Priority",
                [
                    "Utility first",
                    "Solar first",
                    "Solar + Utility",
                    "Only solar charging permitted",
                ],
            ],
            ["int", "Max Parallel Units", "units"],
            [
                "str_keyed",
                "Machine Type",
                {"00": "Grid tie", "01": "Off Grid", "10": "Hybrid"},
            ],
            ["option", "Topology", ["transformerless", "transformer"]],
            [
                "option",
                "Output Mode",
                [
                    "single machine output",
                    "parallel output",
                    "Phase 1 of 3 Phase output",
                    "Phase 2 of 3 Phase output",
                    "Phase 3 of 3 Phase output",
                    "Phase 1 of 2 phase output",
                    "Phase 2 of 2 phase output (120°)",
                    "Phase 2 of 2 phase output (180°)",
                    "unknown output",
                ],
            ],
            ["float", "Battery Redischarge Voltage", "V"],
            [
                "option",
                "PV OK Condition",
                [
                    "As long as one unit of inverters has connect PV, parallel system will consider PV OK",
                    "Only All of inverters have connect PV, parallel system will consider PV OK",
                ],
            ],
            [
                "option",
                "PV Power Balance",
                [
                    "PV input max current will be the max charged current",
                    "PV input max power will be the sum of the max charged power and loads power",
                ],
            ],
            ["int", "Max charging time for CV stage", "min"],
            [
                "option",
                "Operation Logic",
                ["Automatic mode", "On-line mode", "ECO mode"],
            ],
            ["int", "Max discharging current", "A"],
        ],
        "test_responses": [],
    },
    "QFLAG": {
        "name": "QFLAG",
        "description": "Flag Status inquiry",
        "help": " -- queries the enabled / disabled state of various Inverter settings (e.g. buzzer, overload, interrupt alarm)",
        "type": "QUERY",
        "response": [
            [
                "enflags",
                "Device Status",
                {
                    "a": {"name": "Buzzer", "state": "disabled"},
                    "b": {"name": "Overload Bypass", "state": "disabled"},
                    "d": {"name": "Solar Feed to Grid", "state": "disabled"},
                    "k": {"name": "LCD Reset to Default", "state": "disabled"},
                    "u": {"name": "Overload Restart", "state": "disabled"},
                    "v": {"name": "Over Temperature Restart", "state": "disabled"},
                    "x": {"name": "LCD Backlight", "state": "disabled"},
                    "y": {
                        "name": "Primary Source Interrupt Alarm",
                        "state": "disabled",
                    },
                    "z": {"name": "Record Fault Code", "state": "disabled"},
                },
            ]
        ],
        "test_responses": [],
    },
    "QPIGS": {
        "name": "QPIGS",
        "description": "General Status Parameters inquiry",
        "type": "QUERY",
        "response_type": "INDEXED",
        "response": [
            [1, "AC Input Voltage", "float", "V", {"icon": "mdi:power-plug"}],
            [2, "AC Input Frequency", "float", "Hz", {"icon": "mdi:current-ac"}],
            [3, "AC Output Voltage", "float", "V", {"icon": "mdi:power-plug"}],
            [4, "AC Output Frequency", "float", "Hz", {"icon": "mdi:current-ac"}],
            [5, "AC Output Apparent Power", "int", "VA", {"icon": "mdi:power-plug"}],
            [6, "AC Output Active Power", "int", "W", {"icon": "mdi:power-plug"}],
            [7, "AC Output Load", "int", "%", {"icon": "mdi:brightness-percent"}],
            [8, "BUS Voltage", "int", "V", {"icon": "mdi:details"}],
            [9, "Battery Voltage", "float", "V", {"icon": "mdi:battery-outline"}],
            [10, "Battery Charging Current", "int", "A", {"icon": "mdi:current-dc"}],
            [11, "Battery Capacity", "int", "%", {"icon": "mdi:battery-outline"}],
            [
                12,
                "Inverter Heat Sink Temperature",
                "int",
                "°C",
                {"icon": "mdi:details"},
            ],
            [13, "PV1 Input Current", "float", "A", {"icon": "mdi:solar-power"}],
            [14, "PV1 Input Voltage", "float", "V", {"icon": "mdi:solar-power"}],
            [
                15,
                "Battery Voltage from SCC",
                "float",
                "V",
                {"icon": "mdi:battery-outline"},
            ],
            [
                16,
                "Battery Discharge Current",
                "int",
                "A",
                {"icon": "mdi:battery-negative"},
            ],
            [
                17,
                "Device Status",
                "flags",
                [
                    "Is SBU Priority Version Added",
                    "Is Configuration Changed",
                    "Is SCC Firmware Updated",
                    "Is Load On",
                    "Is Battery Voltage to Steady While Charging",
                    "Is Charging On",
                    "Is SCC Charging On",
                    "Is AC Charging On",
                ],
            ],
            [18, "Battery Voltage Offset for Fans On", "int", "10mV"],
            [19, "EEPROM Version", "int", ""],
            [20, "PV1 Charging Power", "int", "W", {"icon": "mdi:solar-power"}],
            [
                21,
                "Device Status2",
                "flags",
                ["Is Charging to Float", "Is Switched On", "Is Dustproof Installed"],
            ],
            [22, "Solar Feed to Grid", "option", ["Disabled", "Enabled"]],
            [
                23,
                "Country",
                "keyed",
                {
                    "00": "India",
                    "01": "Germany",
                    "02": "South America",
                },
            ],
            [24, "Solar Feed to Grid Power", "int", "W"],
        ],
        "test_responses": [
            b"(227.2 50.0 230.3 50.0 0829 0751 010 447 54.50 020 083 0054 02.7 323.6 00.00 00000 00010110 00 00 00879 010\xf1\x8c\r",
        ],
    },
    "QPIGS2": {
        "name": "QPIGS2",
        "description": "General Status Parameters inquiry 2",
        "type": "QUERY",
        "response_type": "INDEXED",
        "response": [
            [1, "PV2 Input Current", "float", "A", {"icon": "mdi:solar-power"}],
            [2, "PV2 Input Voltage", "float", "V", {"icon": "mdi:solar-power"}],
            [3, "PV2 Charging Power", "int", "W", {"icon": "mdi:solar-power"}],
        ],
        "test_responses": [
            b"(03.1 327.3 01026 \xc9\x8b\r",
        ],
    },
    "QPGS": {
        "name": "QPGS",
        "description": "Parallel Information inquiry",
        "help": " -- example: QPGS0 queries the values of various metrics from instance 0 of parallel setup Inverters",
        "type": "QUERY",
        "response_type": "INDEXED",
        "response": [
            [1, "Parallel instance number", "option", ["Not valid", "valid"]],
            [2, "Serial number", "str", ""],
            [
                3,
                "Work mode",
                "keyed",
                {
                    "P": "Power On Mode",
                    "S": "Standby Mode",
                    "L": "Line Mode",
                    "B": "Battery Mode",
                    "F": "Fault Mode",
                    "H": "Power Saving Mode",
                    "D": "Shutdown Mode",
                },
            ],
            [
                4,
                "Fault code",
                "keyed",
                {
                    "00": "No fault",
                    "01": "Fan is locked",
                    "02": "Over temperature",
                    "03": "Battery voltage is too high",
                    "04": "Battery voltage is too low",
                    "05": "Output short circuited or Over temperature",
                    "06": "Output voltage is too high",
                    "07": "Over load time out",
                    "08": "Bus voltage is too high",
                    "09": "Bus soft start failed",
                    "10": "PV over current",
                    "11": "PV over voltage",
                    "12": "DC over current",
                    "13": "Battery discharge over current",
                    "51": "Over current inverter",
                    "52": "Bus voltage too low",
                    "53": "Inverter soft start failed",
                    "54": "Self-test failed",
                    "55": "Over DC voltage on output of inverter",
                    "56": "Battery connection is open",
                    "57": "Current sensor failed",
                    "58": "Output voltage is too low",
                    "60": "Power feedback protection",
                    "71": "Firmware version different",
                    "72": "Current sharing fault",
                    "80": "CAN communication failed",
                    "81": "Parallel host line lost",
                    "82": "Parallel synchronized signal lost",
                    "83": "Parallel battery voltage detect different",
                    "84": "AC input voltage or frequency detected different",
                    "85": "AC output current unbalanced",
                    "86": "AC output mode setting different",
                },
            ],
            [5, "Grid Voltage", "float", "V", {"icon": "mdi:power-plug"}],
            [6, "Grid Frequency", "float", "Hz", {"icon": "mdi:current-ac"}],
            [7, "AC Output Voltage", "float", "V", {"icon": "mdi:power-plug"}],
            [8, "AC Output Frequency", "float", "Hz", {"icon": "mdi:current-ac"}],
            [9, "AC Output Apparent Power", "int", "VA", {"icon": "mdi:power-plug"}],
            [10, "AC Output Active Power", "int", "W", {"icon": "mdi:power-plug"}],
            [11, "Load Percentage", "int", "%", {"icon": "mdi:brightness-percent"}],
            [12, "Battery Voltage", "float", "V", {"icon": "mdi:battery-outline"}],
            [13, "Battery Charging Current", "int", "A", {"icon": "mdi:current-dc"}],
            [14, "Battery Capacity", "int", "%", {"icon": "mdi:battery-outline"}],
            [15, "PV1 Input Voltage", "float", "V", {"icon": "mdi:solar-power"}],
            [
                16,
                "Total Charging Current",
                "int",
                "A",
                {"icon": "mdi:brightness-percent"},
            ],
            [
                17,
                "Total AC Output Apparent Power",
                "int",
                "VA",
                {"icon": "mdi:power-plug"},
            ],
            [18, "Total Output Active Power", "int", "W", {"icon": "mdi:power-plug"}],
            [
                19,
                "Total AC Output Percentage",
                "int",
                "%",
                {"icon": "mdi:brightness-percent"},
            ],
            [
                20,
                "Inverter Status",
                "flags",
                [
                    "Is SCC OK",
                    "Is AC Charging",
                    "Is SCC Charging",
                    "Is Battery Over Voltage",
                    "Is Battery Under Voltage",
                    "Is Line Lost",
                    "Is Load On",
                    "Is Configuration Changed",
                ],
            ],
            [
                21,
                "Output mode",
                "option",
                [
                    "single machine",
                    "parallel output",
                    "Phase 1 of 3 phase output",
                    "Phase 2 of 3 phase output",
                    "Phase 3 of 3 phase output",
                    "Phase 1 of 2 phase output",
                    "Phase 2 of 2 phase output (120°)",
                    "Phase 2 of 2 phase output (180°)",
                    "Unknown Output Mode",
                ],
            ],
            [
                22,
                "Charger source priority",
                "option",
                ["Utility first", "Solar first", "Solar + Utility", "Solar only"],
            ],
            [23, "Max Charger Current", "int", "A"],
            [24, "Max Charger Range", "int", "A"],
            [25, "Max AC Charger Current", "int", "A"],
            [26, "PV1 Input Current", "int", "A", {"icon": "mdi:solar-power"}],
            [
                27,
                "Battery Discharge Current",
                "int",
                "A",
                {"icon": "mdi:battery-negative"},
            ],
            [28, "PV2 Input Voltage", "float", "V", {"icon": "mdi:solar-power"}],
            [29, "PV2 Input Current", "int", "A", {"icon": "mdi:solar-power"}],
        ],
        "test_responses": [
            b"(0 92932105105315 B 00 000.0 00.00 230.0 50.00 0989 0907 012 53.2 009 090 349.8 009 00989 00907 011 10100110 0 1 100 120 030 02 000 275.3 02i]\r",
        ],
        "regex": "QPGS(\\d+)$",
    },
    "QMOD": {
        "name": "QMOD",
        "description": "Mode inquiry",
        "type": "QUERY",
        "response": [
            [
                "keyed",
                "Device Mode",
                {
                    "P": "Power on",
                    "S": "Standby",
                    "L": "Line",
                    "B": "Battery",
                    "F": "Fault",
                    "H": "Power Saving",
                    "D": "Shutdown",
                },
            ]
        ],
        "test_responses": [
            b"(S\x64\x39\r",
            b"(B\xe7\xc9\r",
        ],
    },
    "QPIWS": {
        "name": "QPIWS",
        "description": "Warning status inquiry",
        "type": "QUERY",
        "response": [
            [
                "stat_flags",
                "Warning",
                [
                    "PV loss warning",
                    "Inverter fault",
                    "Bus over fault",
                    "Bus under fault",
                    "Bus soft fail fault",
                    "Line fail warning",
                    "OPV short warning",
                    "Inverter voltage too low fault",
                    "Inverter voltage too high fault",
                    "Over temperature fault",
                    "Fan locked fault",
                    "Battery voltage to high fault",
                    "Battery low alarm warning",
                    "Reserved",
                    "Battery under shutdown warning",
                    "Battery derating warning",
                    "Overload fault",
                    "EEPROM fault",
                    "Inverter over current fault",
                    "Inverter soft fail fault",
                    "Self test fail fault",
                    "OP DC voltage over fault",
                    "Bat open fault",
                    "Current sensor fail fault",
                    "Battery short fault",
                    "Power limit warning",
                    "PV voltage high warning",
                    "MPPT overload fault",
                    "MPPT overload warning",
                    "Battery too low to charge warning",
                    "",
                    "Battery weak",
                    "Battery weak",
                    "Battery weak",
                    "",
                    "Battery equalisation warning",
                ],
            ]
        ],
        "test_responses": [
            b"(00000100000000001000000000000000\x56\xA6\r",
            b"(000000000000000000000000000000000000<\x8e\r",
        ],
    },
    "QDI": {
        "name": "QDI",
        "description": "Default Settings inquiry",
        "type": "QUERY",
        "response": [
            ["float", "AC Output Voltage", "V"],
            ["float", "AC Output Frequency", "Hz"],
            ["int", "Max AC Charging Current", "A"],
            ["float", "Battery Under Voltage", "V"],
            ["float", "Battery Float Charge Voltage", "V"],
            ["float", "Battery Bulk Charge Voltage", "V"],
            ["float", "Battery Recharge Voltage", "V"],
            ["int", "Max Charging Current", "A"],
            ["option", "Input Voltage Range", ["Appliance", "UPS"]],
            [
                "option",
                "Output Source Priority",
                ["Utility first", "Solar first", "SBU first"],
            ],
            [
                "option",
                "Charger Source Priority",
                [
                    "Utility first",
                    "Solar first",
                    "Solar + Utility",
                    "Only solar charging permitted",
                ],
            ],
            [
                "option",
                "Battery Type",
                [
                    "AGM",
                    "Flooded",
                    "User",
                    "TBD",
                    "Pylontech",
                    "WECO",
                    "Soltaro",
                    "LIb-protocol compatible",
                    "3rd party Lithium",
                ],
            ],
            ["option", "Buzzer", ["enabled", "disabled"]],
            ["option", "Power saving", ["disabled", "enabled"]],
            ["option", "Overload restart", ["disabled", "enabled"]],
            ["option", "Over temperature restart", ["disabled", "enabled"]],
            ["option", "LCD Backlight", ["disabled", "enabled"]],
            ["option", "Primary source interrupt alarm", ["disabled", "enabled"]],
            ["option", "Record fault code", ["disabled", "enabled"]],
            ["option", "Overload bypass", ["disabled", "enabled"]],
            ["option", "LCD reset to default", ["disabled", "enabled"]],
            [
                "option",
                "Output mode",
                [
                    "single machine",
                    "parallel output",
                    "Phase 1 of 3 phase output",
                    "Phase 2 of 3 phase output",
                    "Phase 3 of 3 phase output",
                    "Phase 1 of 2 phase output",
                    "Phase 2 of 2 phase output (120°)",
                    "Phase 2 of 2 phase output (180°)",
                    "Unknown Output Mode",
                ],
            ],
            ["float", "Battery Redischarge Voltage", "V"],
            [
                "option",
                "PV OK condition",
                [
                    "As long as one unit of inverters has connect PV, parallel system will consider PV OK",
                    "Only All of inverters have connect PV, parallel system will consider PV OK",
                ],
            ],
            [
                "option",
                "PV Power Balance",
                [
                    "PV input max current will be the max charged current",
                    "PV input max power will be the sum of the max charged power and loads power",
                ],
            ],
            ["int", "Max Charging Time at CV", "min"],
            ["int", "Max Discharging current", "A"],
        ],
        "test_responses": [
            b"(230.0 50.0 0030 44.0 54.0 56.4 46.0 60 0 0 2 0 0 0 0 0 1 1 1 0 1 0 54.0 0 1 224\xeb\xbc\r",
        ],
    },
    "QOPPT": {
        "name": "QOPPT",
        "description": "Device Output Source Priority Time Order Inquiry",
        "type": "QUERY",
        "response": [["bytes.decode", "Device Output Source Priority Time Order", ""]],
        "test_responses": [
            b"(2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 0 2 1>>\r",
        ],
    },
    "QCHPT": {
        "name": "QCHPT",
        "description": "Device Charger Source Priority Time Order Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            [
                "option",
                "Charger Source Priority 00 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 01 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 02 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 03 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 04 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 05 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 06 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 07 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 08 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 09 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 10 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 11 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 12 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 13 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 14 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 15 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 16 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 17 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 18 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 19 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 20 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 21 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 22 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Charger Source Priority 23 hours",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Device Charger Source Priority",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Selection of Charger Source Priority Order 1",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Selection of Charger Source Priority Order 2",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
            [
                "option",
                "Selection of Charger Source Priority Order 3",
                ["undefined", "Solar first", "Solar + Utility", "Only Solar"],
            ],
        ],
        "test_responses": [
            b"(3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 0 0 0\xd0\x8b\r",
        ],
    },
    "QT": {
        "name": "QT",
        "description": "Device Time Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [["bytes.decode", "Device Time", ""]],
        "test_responses": [
            b"(20210726122606JF\r",
        ],
    },
    "QBEQI": {
        "name": "QBEQI",
        "description": "Battery Equalization Status Parameters Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            ["option", "Equalization Enabled", ["Disabled", "Enabled"]],
            ["int", "Equalization Time", "min"],
            ["int", "Equalization Period", "day"],
            ["int", "Equalization Max Current", "A"],
            ["bytes.decode", "Reserved1", ""],
            ["float", "Equalization Voltage", "V"],
            ["bytes.decode", "Reserved2", ""],
            ["int", "Equalization Over Time", "min"],
            ["option", "Equalization Active", ["Inactive", "Active"]],
            ["int", "Equalization Elasped Time", "hour"],
        ],
        "test_responses": [
            b"(1 030 030 080 021 55.40 224 030 0 0234y?\r",
        ],
    },
    "QET": {
        "name": "QET",
        "description": "Total PV Generated Energy Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [["int", "Total PV Generated Energy", "Wh"]],
        "test_responses": [
            b"(00238800!J\r",
        ],
    },
    "QEY": {
        "name": "QEY",
        "description": "Yearly PV Generated Energy Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            ["int", "PV Generated Energy for Year", "Wh"],
            ["info:cv", "Year", ""],
        ],
        "test_responses": [
            b"(00238800!J\r",
        ],
        "regex": "QEY(\\d\\d\\d\\d)$",
    },
    "QEM": {
        "name": "QEM",
        "description": "Monthly PV Generated Energy Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            ["int", "PV Generated Energy for Month", "Wh"],
            ["info:cv[:4]", "Year", ""],
            ["info:calendar.month_name[int(cv[4:])]", "Month", ""],
        ],
        "test_responses": [
            b"(00238800!J\r",
        ],
        "regex": "QEM(\\d\\d\\d\\d\\d\\d)$",
    },
    "QED": {
        "name": "QED",
        "description": "Daily PV Generated Energy Inquiry",
        "help": " -- display daily generated energy, format is QEDyyyymmdd",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            ["int", "PV Generated Energy for Day", "Wh"],
            ["info:cv[:4]", "Year", ""],
            ["info:calendar.month_name[int(cv[4:6])]", "Month", ""],
            ["info:cv[6:]", "Day", ""],
        ],
        "test_responses": [
            b"(00238800!J\r",
        ],
        "regex": "QED(\\d\\d\\d\\d\\d\\d\\d\\d)$",
    },
    "QLT": {
        "name": "QLT",
        "description": "Total Output Load Energy Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [["int", "Total Output Load Energy", "Wh"]],
        "test_responses": [
            b"(00238800!J\r",
        ],
    },
    "QLY": {
        "name": "QLY",
        "description": "Yearly Output Load Energy Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            ["int", "Output Load Energy for Year", "Wh"],
            ["info:cv", "Year", ""],
        ],
        "test_responses": [
            b"(00238800!J\r",
        ],
        "regex": "QLY(\\d\\d\\d\\d)$",
    },
    "QLM": {
        "name": "QLM",
        "description": "Monthly Output Load Energy Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            ["int", "Output Load Energy for Month", "Wh"],
            ["info:cv[:4]", "Year", ""],
            ["info:calendar.month_name[int(cv[4:])]", "Month", ""],
        ],
        "test_responses": [
            b"(00238800!J\r",
        ],
        "regex": "QLM(\\d\\d\\d\\d\\d\\d)$",
    },
    "QLD": {
        "name": "QLD",
        "description": "Daily Output Load Energy Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            ["int", "Output Load Energy for Day", "Wh"],
            ["info:cv[:4]", "Year", ""],
            ["info:calendar.month_name[int(cv[4:6])]", "Month", ""],
            ["info:cv[6:]", "Day", ""],
        ],
        "test_responses": [
            b"(00238800!J\r",
        ],
        "regex": "QLD(\\d\\d\\d\\d\\d\\d\\d\\d)$",
    },
    "QLED": {
        "name": "QLED",
        "description": "LED Status Parameters Inquiry",
        "type": "QUERY",
        "response_type": "SEQUENTIAL",
        "response": [
            ["option", "LED Enabled", ["Disabled", "Enabled"]],
            ["option", "LED Speed", ["Low", "Medium", "Fast"]],
            [
                "option",
                "LED Effect",
                ["Breathing", "Unknown", "Solid", "Right Scrolling"],
            ],
            ["int", "LED Brightness", ""],
            ["int", "LED Number of Colors", ""],
            ["bytes.decode", "RGB", ""],
        ],
        "test_responses": [
            b"(1 1 2 5 3 148000211255255255000255255\xdaj\r",
        ],
    },
}

SETTER_COMMANDS = {
    "PLEDE": {
        "name": "PLEDE",
        "description": "Enable/disable LED function",
        "help": " -- examples: PLEDE0 (disable LED), PLEDE1 (enable LED)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]
        ],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "PLEDE([01])$",
    },
    "PLEDS": {
        "name": "PLEDS",
        "description": "Set LED speed",
        "help": " -- examples: PLEDS0 (set LED speed low), PLEDS1 (set LED speed medium), PLEDS2 (set LED speed high)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]
        ],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "PLEDS([012])$",
    },
    "PLEDM": {
        "name": "PLEDM",
        "description": "Set LED effect",
        "help": " -- examples: PLEDM0 (set LED effect breathing), PLEDM2 (set LED effect solid), PLEDM3 (set LED right scrolling)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]
        ],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "PLEDM([0123])$",
    },
    "PLEDB": {
        "name": "PLEDB",
        "description": "Set LED brightness",
        "help": " -- examples: PLEDB1 (set LED brightness low), PLEDB5 (set LED brightness normal), PLEDB9 (set LED brightness high)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]
        ],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "PLEDB([123456789])$",
    },
    "PLEDT": {
        "name": "PLEDT",
        "description": "Set LED total number of colors",
        "help": " -- examples: PLEDT2 (set 2 LED colors), PLEDT3 (set 3 LED colors)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]
        ],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "PLEDT([123])$",
    },
    "PLEDC": {
        "name": "PLEDC",
        "description": "Set LED color",
        "help": " -- examples: PLEDCnRRRGGGBBB (n: 1 line mode, 2 AVR mode, 3 battery mode)",
        "type": "SETTER",
        "response": [
            ["ack", "Command execution", {"NAK": "Failed", "ACK": "Successful"}]
        ],
        "test_responses": [
            b"(NAK\x73\x73\r",
            b"(ACK\x39\x20\r",
        ],
        "regex": "PLEDC(\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d)$",
    },
}

COMMANDS_TO_REMOVE = ["Q1", "QID", "QVFW3"]


class pi30max(pi30):
    def __str__(self):
        return "PI30 protocol handler for LV6048MAX and similar inverters"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self._protocol_id = b"PI30MAX"
        # Add pi30max specific commands to pi30 commands
        self.COMMANDS.update(QUERY_COMMANDS)
        # Add pi30max specific setter commands
        self.COMMANDS.update(SETTER_COMMANDS)
        # remove and unwanted pi30 commands
        for item in COMMANDS_TO_REMOVE:
            if item in self.COMMANDS:
                self.COMMANDS.pop(item)
        self.STATUS_COMMANDS = ["QPIGS", "QPIGS2"]
        self.SETTINGS_COMMANDS = ["QPIRI", "QFLAG"]
        self.DEFAULT_COMMAND = "QPI"
        log.info(
            f"Using protocol {self._protocol_id} with {len(self.COMMANDS)} commands"
        )
