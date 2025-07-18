import streamlit as st
st.sidebar.title("Game Fun App")
page=st.sidebar.selectbox("Select a Page",["Home","Game Tracker","Trending Games","Quiz","Feedback","Contact","About Me"])
# if page=="Home":
#     import pages.01_home
# elif page=="Game Tracker":
#     import pages.02_tracker
# elif page=="Trending Games":
#     import pages.03_trending
# elif page=="Quiz":
#     import pages.04_quiz
# elif page=="Feedback":
#     import pages.05_feedback
# elif page=="Contact":
#     import pages.06_contact
# elif page=="About Me":
#     import pages.07_aboutme"