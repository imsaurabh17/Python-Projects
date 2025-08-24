import csv
import numpy as np
import os
import threading

file_lock = threading.Lock()

if not os.path.exists("expense_tracker.csv"):
    with file_lock:
        with open("expense_tracker.csv","w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(['Date',"Item_Name","Quantity of Item","Price of Each Unit","Total Amount"])
            f.flush()
            os.fsync(f.fileno())
            print("File created")
else:
    print("File already exists")

def add_expense(date,name,quantity,price):
    amount = quantity*price
    with file_lock:
        with open("expense_tracker.csv","a",newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date,name,quantity,price,amount])
            f.flush()
            os.fsync(f.fileno())
        print("Details added")