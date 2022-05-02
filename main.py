import csv
import os
import time
from datetime import datetime
asterisks = '*' * 100
asterisks1 = '*' * 10
import ipaddress



# Function to ping IP addresses.
def run_ping(ip_address):
    ping_reply = os.system("ping -n 3 {}".format(ip_address))
    return ping_reply
# Function to save ping results. 
def saveResult(nodeName, NodeStatus):
    name = nodeName + ' on ' + datetime.now().strftime('%d-%m-%Y %H_%M_%S_%p')
    filename = "Result/%s.txt"% name # append a string to the end of the file name using %s
    if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError:
                    pass
    with open(filename, "x") as f:
        for items in NodeStatus:
            if len(NodeStatus) == 0:
                f.write('All Nodes are reachable')
            else:
                f.write(items + '\n')



"""Function that processes when file is uploaded.

Args:
    - file: The file that is uploaded.

Returns:
    - None
"""
def run(file):

    # This list holds the nodes that are not reachable. 
    statusList = []


    # open the csv files in read-only format.
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for i in range(len(row)):
                try:
                    ipaddress.ip_address(row[i])

                    # * If the IP address is valid, then ping it.
                    if run_ping(row[i]) == 0:
                        print(asterisks1 + '\n' + row[i] + ' is reachable' + '\n' + asterisks1)
                    else:
                        # * If the IP address is not reachable, then add it to the list.
                        stat = '{}'.format(row[i]) + ' is not reachable'
                        statusList.append(stat)
                        print(asterisks1 + '\n' + row[i] + ' is not reachable' + '\n' + asterisks1)
                except ValueError:
                    print(asterisks1 + '\n' + 'Invalid IP address' + '\n' + asterisks1)

    # * Save the results to a text file.
    saveResult('Ping result', statusList)
    statusList.clear()
    return statusList


