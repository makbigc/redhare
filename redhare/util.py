import re
import datetime


def transform_data(record):
    '''Transform HTML tags to string'''
    non_digit = re.compile('\D')
    record_fixed = [0]*13

    if non_digit.search(record[0].string):
        record_fixed[8:] = [""]*5
    else:
        for i in [7, 8, 10, 11]:
            record_fixed[i+1] = record[i].string
        record_fixed[10] = '-'.join(record[9].strings)
        record_fixed[8:] = map(str, record_fixed[8:])

    # The third column of record contains the horse name and the horse code.
    # Hence, since the third index, the record_fixed is shifted to right for
    # one to match the record.
    record_fixed[2:4] = list(record[2].strings)
    record_fixed[:2] = [a.string for a in record[:2]]
    record_fixed[4:8] = [a.string for a in record[3:7]]

    record_fixed[:8] = map(str, record_fixed[:8])
    record_fixed[3] = record_fixed[3].strip("()")
    return record_fixed


def validate_date(ctx, param, value):
    try:
        if value is None:
            return value
        else:
            datetime.datetime.strptime(value, '%Y%m%d')
            return value
    except ValueError:
        raise ValueError('The date format should be YYYYMMDD')
