"""
Week 7 Final Project
"""
#! /usr/bin/env python3

import re
import csv

error_data = dict()
usr_inf_err_data = dict()

regex = r".*: (\b[A-Z]+\b) ([A-Za-z ']+) .*\(([\w.]+)\)$"

with open('/home/student-02-eb878dcbeb88/syslog.log' ,'r') as log:
  log_file = log.readlines()
  for line in log_file:
    result = re.search(regex, line.strip())
    if result:
      result = result.groups()
    else:
     continue

    if result[0] == "ERROR":
      if result[1] not in error_data:
        error_data[result[1]] = 1
      else:
        error_data[result[1]] += 1

    if result[0] in ["ERROR","INFO"]:
      if result[2] not in usr_inf_err_data:
        if result[0] == "ERROR":
          usr_inf_err_data[result[2]] = [0,1]
        else:
          usr_inf_err_data[result[2]] = [1,0]
      else:
        if result[0] == "ERROR":
          usr_inf_err_data[result[2]][1] += 1
        else:
          usr_inf_err_data[result[2]][0] += 1

sorted_error_data =[["Error", "Count"]] + sorted(error_data.items(), key=lambda item: item[1], reverse=True)
sorted_usr_inf_err_data = [["Username", "INFO", "ERROR"]] +[[i[0],i[1][0],i[1][1]] for i in sorted(usr_inf_err_data.items(), key=lambda item: item[0])]
print(sorted_usr_inf_err_data)

with open('error_message.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerows(sorted_error_data)

with open('user_statistics.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerows(sorted_usr_inf_err_data)