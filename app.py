import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"
API_KEY = "saurabh_123"

st.set_page_config(page_title="Expense Tracker App")

st.header("Add Expenses")

with st.form("Expense_form"):
    date = st.text_input("Date in DD-MM_YYYY: ")
    name = st.text_input("Name")
    quantity = st.number_input("Quantity",min_value=1)
    price = st.number_input("Price of each item",min_value=0.0)
    submit = st.form_submit_button("Add Expense")

    if submit:
        payload = {
            "date":date,
            "name":name,
            "quantity":quantity,
            "price":price
        }
        headers = {"x_api_key":API_KEY}
        response = requests.post(url = f"{API_URL}/add_expense",json=payload,headers=headers)

        if response.status_code == 200:
            st.success("Expense Added Successfully")
        else:
            st.error(f"Error:{response.json()}")

st.title("Fetch Data")
if st.button('Fetch Data'):
    headers = {'x_api_key':API_KEY}
    response = requests.get(f"{API_URL}/show_data",headers=headers)

    if response.status_code == 200:
        data = response.json()
        st.dataframe(data)
    else:
        st.error(f"Error in fetching the data: {response.json()}")
