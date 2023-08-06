
# pymonitor

more info including examples can be found here <br>
[https://github.com/noahgrad/pymonitor/](https://github.com/noahgrad/pymonitor/)

## Why?
Lets say you have a lot of etls that runs in different platforms (airflow, kubernetes etc)  and writes data to different places  (mysql, snowflake, s3 etc) so how do you monitor them? how do you check that each of etls end up correctly and the data reached its destination?
pymonitor come to help discover that the data didn't reach its destination ASAP.

## The idea
The idea is to do the same thing pytest is doing for testing just for monitoring. 
Run pymonitor.py script on a specific directory it will run all monitoring files - files with specific name and will try to run their monitor method - method with specific name. <br>
Lets say we have a directory of etls each etl in its own subdirectory in this case we will add a monitor file to each of the subdirectories. Each monitor file will monitor just its etl. <br> 
By the end of running the script we will get a covergae of monitor for all the etls that implemented a monitor method in a monitor file (the same as in pytest)

## Usage example
python src/pymonitoring/pymonitor.py --dir etls --end_ts 1663064624 --filename "Example*.py" <br>
Will try to find all the Example*.py file name in directory etls and run their monitor method. <br>
or  <br>
**pip intsall pymonitor-foretls** <br>
from pymonitoring.pymonitor import monitor
monitor("examples", 1663064624,"Example*.py")


## The pymonitor.py script or monitor method 
Need to get: <br>
**end_ts**  - the timestamp untill it we want to monitor. <br>
**dir**         - the directory to run on <br>
Can get: <br>
**filename** - seach for files with this name in the given directory default is 'monitor.py' <br>
**methodname** - execute this method with the end_ts paramter default is 'monitor' <br>
Get all files name  filename in dir  <br>
for each file:  <br>
 execute the method methodname with the end_ts <br>

## The PyMonitoring class
Contains some static methods to help you peform some monitoring currenty we have: <br>
**send_slack_monitoring_massage** - Send message to the slack channel <br>
**check_table_in_sf** - Check if there is data in the specified table between the start ts and end ts in the given time_field_name  <br>
if there is data return True else can send slack notification and return False <br>
**check_query_in_sf** - Send query to snowflake and return the query result.  <br>
send slack message if there is no data <br>

More method should come

## The examples directory
Contains 2 example of how to write and use the PyMonitoring class.


