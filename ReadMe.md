# Simple logging module
To use, simple import the module. Call the 'log' function with two parameters: 'msg' and 'file_name'. The module will create a new CSV file with 'file_name' as the name, or will simply append to it if it already exists.

## Example:
Import the file, and call the function:
```py
import log_csv

log_csv.log(msg='test message', file_name='log.csv')
```
Output: 
```
Date,Time,Message
1-1-2000,00:00:00,test message
```