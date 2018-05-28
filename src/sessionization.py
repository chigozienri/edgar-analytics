import numpy as np
# challenge says to try to avoid using pandas,
# but using for now as I am familiar with it.
# May change in a later version if I have time.
# import pandas as pd
# import csv
import datetime
import dateutil
from argparse import ArgumentParser  # To read command line arguments

parser = ArgumentParser(description="Take EDGAR Logs and output session times")
parser.add_argument('input_filename')  # input
parser.add_argument('inactivity_period')  # inactivity period
parser.add_argument('output_filename')  # output file

args = parser.parse_args()

data = np.recfromcsv(args.input_filename)  # Better to do everything within np
# Legacy: use csv library instead of np.recfromcsv
# with open(args.input_filename, 'r') as f:
#     csvdata = np.array(list(csv.reader(f)))
#
# header = csvdata[:1]
# data = csvdata[1:]

# print(header)
# print(data['ip'])

# ndtype = np.dtype([('ip', str), ('date', str), ('time', str),
#                    ('zone', float), ('cik', str), ('accession', str),
#                    ('extention', str), ('code', float), ('size', float),
#                    ('idx', float), ('norefer', float), ('noagent', float),
#                    ('find', float), ('crawler', float), ('browser', str)])

# prototypeheader = np.array(['ip', 'date', 'time', 'zone', 'cik', 'accession',
#                             'extention', 'code', 'size', 'idx', 'norefer',
#                             'noagent', 'find', 'crawler', 'browser'])
# # if header.all() != prototypeheader.all():
# #     print('oh no')
#
#
# # datatypelist = np.dtype([('ip', str)])
# print(datatypelist)
# data = data.transpose().astype(datatypelist)

# Sort in place by user for convenience, faster than looping through each time
# to find same user
# Default np sort as of numpy 1.12  is now introsort, which starts as quicksort
# (O(n^2) but switches to heapsort (O(n*log(n)))
# when it does not progress fast enough, good for large data
data.sort(order='ip')
print(data[data.ip==b'107.178.195.aag'])

with open(args.inactivity_period, 'r') as f:
    f = list(f)
    if len(f) > 1:
        print("oh no")
    # TODO: check that inactivity period is formatted as int between 1 and 86400
    inactivity_period = int(f[0])
    if inactivity_period < 1 or inactivity_period > 86400:
        print("oh no")
print(inactivity_period)
