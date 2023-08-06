class GameUnitError(Exception):
    def __init__(self, message='', code=1000):
        super().__init__(message)
        self.padding = '~' * 50 + '\n'
        self.error_message = 'Unspecified Error!'


class HealthMeterException(GameUnitError):
    def __init__(self, message=''):
        super().__init__(message)
        self.error_message = (self.padding +
                              "ERROR: Health Meter Problem" +
                              '\n' + self.padding)


class HutError(GameUnitError):
    def __init__(self, code):
        self.error_message = ''
        self.error_dict = {
            000: "ERROR-000: Unspecified Error",
            101: "ERROR-101: Health Meter Problem",
            102: "ERROR-102: Attack issue! Ignored",
        }
        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n' + '~' * 50

