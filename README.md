## Language
Python 3.6 (also tested and functioning using 2.7)

## Approach
A structured numpy array called data is created which contains the data from the CSV file, and has field names taken from the header. The main program logic is contained in a for loop over the requests in this numpy array, which starts at line 65 of sessionization.py. An empty list called open_sessions exists at the start of the loop. On each loop, every session of open_sessions is checked to see if the session should be closed (in which case the session is written to disk and removed from open_sessions), if the ip address matches an open session (in which case the session is updated), or if the ip address doesn't match an open session (in which case a session is created and added to open_sessions). After the main for loop is complete, all remaining open sessions are written to disk.  

## Dependencies
Numpy 1.14+

dateutil 2.7.3+

### Builtin
datetime

argparse 

## Run Instructions
Tested running with a fresh Anaconda python environment, followed by 
```
conda install numpy
conda install dateutil
```
Then to actually run:

```
cd edgar-analytics
./run.sh
```

To run test suite
```
cd insight-testsuite
./run_tests.sh
```
