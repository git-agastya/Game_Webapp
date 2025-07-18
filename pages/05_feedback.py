import streamlit as st
import os
import pandas as pd

folder_path="data"
file_path=r"game_app\data\feedback.csv"



if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not os.path.exists(file_path):
    dataframe=pd.DataFrame(columns=["Name","Feedback","Rating"])
    dataframe.to_csv(file_path,index=False)

def clear():
    st.session_state.name=""
    st.session_state.fb=""

name=st.text_input("Enter your name",key="name")
feedback=st.text_area("Please provide your valueable feedback",key="fb")
rating=st.slider("Please rate on a scale of 1-5",min_value=1,max_value=5,step=1,value=1)

emoji_holder=st.empty()
if rating==1:
    emoji_holder.subheader("We will definitly improve"+":weary:")
if rating==2:
    emoji_holder.subheader("We will definitly improve your experience"+":disappointed_relieved:")
if rating==3:
    emoji_holder.subheader("Thanks"+":persevere:")
if rating==4:
    emoji_holder.subheader("Oh you are loving it!!!"+":smiley_cat:")
if rating==5:
    emoji_holder.subheader("Thank you so much for your love"+":heart_eyes_cat:")


col1,col2=st.columns([0.2,0.8])
with col1:
    submit=st.button("Submit :smile:")
with col2:
    clear=st.button("Clear :scissors:",on_click=clear)

def insert(file_path):
    df=pd.read_csv(file_path)
    length=len(df)
    df.loc[length]=[name,feedback,rating]
    df.to_csv(file_path,index=False)

def view(file_path):
    df=pd.read_csv(file_path)
    st.dataframe(df)

if submit:
    insert(file_path)
    st.success("Thank you for your valuable feedback")


st.subheader("Past feedbacks")
view(file_path)
