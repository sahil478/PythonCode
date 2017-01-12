import time
import string
import datetime
import os
import sys
import commands


from influxdb import InfluxDBClient

x = float(commands.getoutput("ps aux|awk 'NR>0 {s+=$3};END{print s}'"))
print(x)
print(str(datetime.datetime.now()))
print("\n")
json_body = [
    {
        "measurement": 'cpu_load_short',
        
        "time": str(datetime.datetime.now()),
        "fields": {
            "CPU": x,
        }
    }
]

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example12')

client.create_database('example12')

client.write_points(json_body)

result = client.query('select CPU from cpu_load_short;')

print("Result: {0}".format(result))
    
	   

    
