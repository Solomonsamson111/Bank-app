import streamlit as st
from savings_account import SavingsAccount
st.set_page_config(page_title="Bank app",layout="centered")
savings = SavingsAccount(20000)

with st.form("savings_form"):
    amount = st.number_input("Enter Amount", min_value=1000)
    operations = st.selectbox("Deposit or Withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("submit")

    if submit and operations == 'withdraw':
        with st.spinner("processing...."):
         savings.deposit(amount)
        print(savings.balance )
