from datetime import datetime, timezone


# todo: need to remove these methods (DELETE!!!)
def generate_timestamp():
    return datetime.now(timezone.utc)


def format_to_utc_timestamp(value):
    return datetime.fromisoformat(value)


def as_file_timestamp(timestamp=generate_timestamp()):
    utc_timestamp = timestamp.isoformat()
    return utc_timestamp.replace('-', '').replace('T', '_').replace(':', '').replace('.', '_').replace('+0000', '')


def as_file_date_stamp(timestamp=generate_timestamp()):
    return timestamp.strftime('%Y%m%d')


def get_utc_timestamp(timestamp=None):
    timestamp_to_use = generate_timestamp() if timestamp is None else timestamp
    return int(timestamp_to_use.timestamp() * 1000)
