import csv
import numpy as np
import os
import threading
import pandas as pd

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

def show_expense():
    start_date = input("Enter the start date: ")
    end_date = input("Enter the end date: ")
    df = pd.read_csv("D:/Python Projects/Personal Expense Tracker/expense_tracker.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    a = df[(df['Date']>=start_date) & (df['Date']<=end_date)]
    print(a)

