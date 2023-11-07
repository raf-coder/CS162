#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:02:24 2023

@author: rafmesta
"""
file_content = '''
47, 30
54, 32
58, 34
64, 37
72, 42
80, 48
88, 51
88, 50
81, 44
68, 37
53, 34
46, 31
'''

file_path = "data.txt"

with open(file_path, 'w') as file:
    file.write(file_content)

import matplotlib.pyplot as plt

high = []
low = []

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


with open(file_path, 'r') as e:
    for line in e:
        values = line.split(',')
        if len(values) == 2:
                # Extract high and low temperatures
                high_temp = float(values[0])
                low_temp = float(values[1])
                high.append(high_temp)
                low.append(low_temp)

# plot high temperatures
plt.plot(months, high, color='red', label='High', linestyle='solid')

# plot low temperatures
plt.plot(months, low, color='blue', label='Low', linestyle='solid')

# plot title
plt.title("Medford Oregon City Temperatures: Averages by Month")

# Set the labels for the axes
plt.xlabel("Month")
plt.ylabel("Temperature, in Fahrenheit degrees")

# Display the legend in the left upper corner
plt.legend(loc='upper left')

# Show the plot
plt.show()