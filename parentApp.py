import pickle
import streamlit as st
import pandas as pd

page=st.sidebar.radio(" ",("New User","Exisisting User"))
st.title("Parent's Portal")
if (page=="New User"):
    st.title("Parent's Registration page")
    num=st.text_input("Enter your Mobile Number with country Code")
    resp=st.button("Register")
    if (resp):
        with open("receiver.pkl","wb") as f:
            pickle.dump(num,f)
        st.success("Registration successfull")

elif (page=="Exisisting User"):
    #st.Title("Parent's Registration page")
    st.write("Check site history")
    resp=st.button("Check")
    history=""
    if (resp):
        df=pd.read_csv("Data/Visited Sites.csv")
        st.dataframe(df)