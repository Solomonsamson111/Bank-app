import streamlit as st

st.set_page_config(page_title="Bank App", layout="centered")
st.title("current account")




if 'balance' not in st.session_state:
    st.session_state.balance = 25000


st.write(f"current balance: ${st.session_state.balance:.2f}")

st.subheader("Deposit")
deposit_amount = (
    st.number_input("Enter amount to deposit", min_value=0.0,format="%.2f"))
if st.button("Deposit"):
    st.session_state.balance += deposit_amount
    st.success(f"Deposited ${deposit_amount:.2f}")


st.subheader("Withdraw Money")
Withdraw_amount = (
    st.number_input("Enter amount to withdraw", min_value=0.0,format="%.2f"))
if st.button("Withdraw"):
    if Withdraw_amount> st.session_state.balance:
        st.error("insufficient funds!")
    else:
        st.session_state.balance -= Withdraw_amount
        st.success(f"withdrew ${Withdraw_amount:.2f}")
