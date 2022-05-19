import datetime as dt


class Utils:

    @classmethod
    def CovertToTime(cls, string_date):
        d = dt.datetime.strptime(string_date, "%Y-%m-%d")
        return d
