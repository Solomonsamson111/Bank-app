import streamlit as st
from savings_account import SavingsAccount
st.set_page_config(page_title="Bank app",layout="centered")
savings = SavingsAccount(25000)

with st.form("savings_form"):
    amount = st.number_input("Enter Amount", min_value=1000)
    operations = st.selectbox("Deposit or Withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("submit")

    if submit and operations == 'withdraw':
        with st.spinner("processing...."):
         savings.deposit(amount)
        print(savings.balance )

from account import account
st.set_page_config()
current = CurrentAccount(25000)

with st.form("current_form"):
    amount = st.number_input("Enter Amount", min_value=1000)
    operations = st.selectbox("Deposit or Withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("submit")

    if submit and operations == 'withdraw':
        with st.spinner("processing...."):
         current.deposit(amount)
        print(current.balance )
