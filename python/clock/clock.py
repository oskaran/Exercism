

class Clock:
    def __init__(self, hour, minute):
        hour += minute // 60
        self.hour = hour % 24
        self.minute = minute % 60

    def __repr__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        return (self.hour == other.hour) and (self.minute == other.minute)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

#what is the difference?

    # def __repr__(self):
    #     return f"Clock({self.hour}, {self.minute})"

    # def __str__(self):
    #     return f"{self.hour:02}:{self.minute:02}"