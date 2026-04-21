import csv
import operator
from pathlib import Path
from datetime import datetime
import os

print(os.listdir())

file = "list_of_peaks.csv"

data = open(file, "rt")

data.close()

print("hello")