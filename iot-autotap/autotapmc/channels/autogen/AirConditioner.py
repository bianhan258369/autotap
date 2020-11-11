from model.Channel import Channel


class AirConditioner(Channel):
    power = 0

    def ap_powerIsTrue(self):
        return self.power == 1

    def action_powerSetTrue(self):
        self.power = 1

    def enable_powerSetTrue(self):
        return self.power != 1

    def action_powerSetFalse(self):
        self.power = 0

    def enable_powerSetFalse(self):
        return self.power != 0


    thermostat = 72.5

    def ap_thermostatLessThan70(self):
        return self.thermostat < 70

    def ap_thermostatGreaterThan70(self):
        return self.thermostat > 70

    def ap_thermostatLessThan75(self):
        return self.thermostat < 75

    def ap_thermostatGreaterThan75(self):
        return self.thermostat > 75

    def ap_thermostatLessThan80(self):
        return self.thermostat < 80

    def ap_thermostatGreaterThan80(self):
        return self.thermostat > 80

    def action_thermostatSetTo69(self):
        self.thermostat = float(69)

    def enable_thermostatSetTo69(self):
        return self.thermostat != 69

    def action_thermostatSetTo70(self):
        self.thermostat = float(70)

    def enable_thermostatSetTo70(self):
        return self.thermostat != 70

    def action_thermostatSetTo72_5(self):
        self.thermostat = float(72.5)

    def enable_thermostatSetTo72_5(self):
        return self.thermostat != 72.5

    def action_thermostatSetTo75(self):
        self.thermostat = float(75)

    def enable_thermostatSetTo75(self):
        return self.thermostat != 75

    def action_thermostatSetTo77_5(self):
        self.thermostat = float(77.5)

    def enable_thermostatSetTo77_5(self):
        return self.thermostat != 77.5

    def action_thermostatSetTo80(self):
        self.thermostat = float(80)

    def enable_thermostatSetTo80(self):
        return self.thermostat != 80

    def action_thermostatSetTo81(self):
        self.thermostat = float(81)

    def enable_thermostatSetTo81(self):
        return self.thermostat != 81


