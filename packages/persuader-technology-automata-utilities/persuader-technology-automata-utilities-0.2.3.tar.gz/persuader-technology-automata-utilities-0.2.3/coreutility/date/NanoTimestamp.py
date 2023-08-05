import time
from datetime import datetime, timezone


class NanoTimestamp:

    @staticmethod
    def get_nanoseconds():
        return time.clock_gettime_ns(time.CLOCK_REALTIME)

    @staticmethod
    def as_datetime(nanoseconds):
        conventional_time = nanoseconds // 1000000000
        nano_intervals = nanoseconds % 1000000000
        microsecond_intervals = nano_intervals // 1000
        # good enough @ microsecond (does not yet handle nanosecond interval) see: RFC3339 Nano timestamp
        conventional_datetime = datetime.utcfromtimestamp(conventional_time).replace(microsecond=microsecond_intervals)
        return conventional_datetime

    @staticmethod
    def as_nanoseconds(datetime_value):
        utc_timestamp = datetime_value.replace(tzinfo=timezone.utc).timestamp()
        return int(utc_timestamp * 1000000) * 1000

    @staticmethod
    def as_shorted_nanoseconds(nanoseconds):
        return nanoseconds - (nanoseconds % 1000)

    @staticmethod
    def to_string(value):
        if type(value) == datetime:
            nano_datetime = value
            utc_datetime = nano_datetime.replace(tzinfo=timezone.utc)
            return utc_datetime.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        else:
            nanoseconds = value
            nanoseconds_len = len(str(nanoseconds))
            divisor = 1000000000 if nanoseconds_len > 16 else 1000000
            conventional_time = nanoseconds // divisor
            nano_intervals = nanoseconds % divisor
            conventional_datetime = datetime.utcfromtimestamp(conventional_time)
            return conventional_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f').replace('000000', str(nano_intervals) + 'Z')
