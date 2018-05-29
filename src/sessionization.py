import numpy as np
import numpy.lib.recfunctions
import datetime
import dateutil
import dateutil.parser
from argparse import ArgumentParser  # To read command line arguments

parser = ArgumentParser(description="Take EDGAR Logs and output session times")
parser.add_argument('input_filename')  # input
parser.add_argument('inactivity_period')  # inactivity period
parser.add_argument('output_filename')  # output file

args = parser.parse_args()

# Originally I used CSV library to parse CSV myself,
# but better to do everything within numpy. np.recfromcsv makes structured array
data = np.recfromcsv(args.input_filename)

# np.lib.recfunctions.append_fields(data, 'datetime_object', data=datetime_array)

# Sort in place by user for convenience, faster than looping through each time
# to find same user
# Default np sort as of numpy 1.12  is now introsort, which starts as quicksort
# (O(n^2) but switches to heapsort (O(n*log(n)))
# when it does not progress fast enough, good for large data
data.sort(order=['ip', 'date', 'time'])

with open(args.inactivity_period, 'r') as f:
    f = list(f)
    if len(f) > 1:
        print("oh no")
    # TODO: check that inactivity period is formatted as int in file
    inactivity_period = int(f[0])
    if inactivity_period < 1 or inactivity_period > 86400:
        print("oh no")
inactivity_period = datetime.timedelta(seconds=inactivity_period)
# print(inactivity_period)

# data[0].date

# print(data[data.zone==0])

# sessions = np.empty([1], dtype=[('ip', str), ('firstrequest', str),
#                             ('lastrequest', str), ('duration', int),
#                             ('count', int)])
#
# print(sessions)

def date_time_to_datetime(request):
    '''
    Takes line of np array with date and time fields,
    returns single string ISO Format date and time
    '''
    return dateutil.parser.parse(request.date.decode('utf-8') + ' ' +
            request.time.decode('utf-8'))


def write_session(output_filename, ip, starttime, endtime, duration, count):
    '''
        Write session to file
    '''
    starttime = starttime.strftime('%Y-%m-%d %H:%M:%S')
    endtime = endtime.strftime('%Y-%m-%d %H:%M:%S')
    duration = str(int(duration.total_seconds()))
    count = str(count)
    with open(output_filename, 'a+') as f:
        f.write(ip + ',' + starttime + ',' + endtime + ',' + duration +
            ',' + count + '\n')
    print('wrote session', ip, starttime, endtime, duration, count)
    return True

# Initialise with first request in dataset - that way
# I don't have to check every loop whether it's the first request
first_request = data[0]
# concatenate datetime into single isoformat string that dateutil can parse
# init_time = dateutil.parser.parse(first_request.date.decode('utf-8') + ' ' +
#         first_request.time.decode('utf-8'))
init_time = date_time_to_datetime(first_request)
last_time = init_time
ip = first_request.ip.decode('utf-8')
count = 0
for request in data:
    count += 1
    request_ip = request.ip.decode('utf-8')
    request_time = dateutil.parser.parse(request.date.decode('utf-8') + ' ' +
                    request.time.decode('utf-8'))
    if (request_time - last_time > inactivity_period) or (request_ip != ip):
        duration = last_time - init_time
        write_session(args.output_filename, ip, init_time, last_time, duration, count)
        count = 0
        init_time = request_time
        ip = request_ip
    last_time = request_time



#
#     if request.ip == ip:
#     if
#     if (record_time > latest_time) and record_time:
#         latest_time = record_time
# session_time = latest_time - init_time
