from datetime import datetime


def get_datetime_from_pb_ts(timestamp):
    return datetime.fromtimestamp(timestamp.seconds + timestamp.nanos / 1e9)
