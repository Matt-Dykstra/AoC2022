#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

input=pd.read_csv("Day1.csv", skip_blank_lines=False)
calories=np.array(input['Calories'])

a=0
totals = []

for x in calories:
    if str(x) != 'nan':
        a+=x
    else:
        totals.append(a)
        a=0

print(max(totals))

print(sum(sorted(totals, reverse=True)[:3]))




