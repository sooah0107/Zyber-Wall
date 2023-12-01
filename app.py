import streamlit as st
from sendAlert import send
from Tester import checkLink
import csv
import webbrowser
import time

from datetime import datetime
now = datetime.now()


st.title("Prototype")
link=st.text_input("Enter the destination link")
srch=st.button("Search")
status=""
if(srch):
    res=checkLink(link)
    if res!=1: #i.e. 1 -> Not Allowed
        st.success(str(res) +": Content is to be Allowed" )
        time.sleep(0.5)
        webbrowser.open_new(link)
    else:
        st.error(str(res) +": Content has been blocked")
        st.info("Do you want to take permission?")


prmsn=st.button("Ask Permission")
print(prmsn)
if(prmsn):
    print("Clicked")
    status=send(link)   #status 1 means allow
    print("Envoked send")
    if status==1:
        webbrowser.open_new(link)
    else:
        st.error("Permission declined")
'''else:
    st.error("Permission declined")'''

data=[now.strftime("%H:%M:%S"),link]

with open("Data/Visited Sites.csv","a") as f:
    w=csv.writer(f)
    w.writerow(data)   


        