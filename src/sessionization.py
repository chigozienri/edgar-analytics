import numpy as np
import pandas as pd  # challenge says to try to avoid using pandas, but using for now as I am familiar with it. May change in a later version if I have time.
import csv
from argparse import ArgumentParser  # To read command line arguments

parser = ArgumentParser(description="Take EDGAR Logs and output session times")
parser.add_argument('input_filename')  # input
parser.add_argument('inactivity_period')  # inactivity period
parser.add_argument('output_filename')  # output file

args = parser.parse_args()

# data = np.genfromtxt(args.input_filename) This didn't work, to fix later. For now, just use csv library
with open(args.input_filename, 'r') as f:
    csvdata = np.array(list(csv.reader(f)))

header = csvdata[:1]
data = csvdata[1:]

print(header)
print(data)
