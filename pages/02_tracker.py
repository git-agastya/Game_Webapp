import streamlit as st

if 'games' not in st.session_state:
    st.session_state.games=[]

st.title("My Game Tracker")
st.write("Keep track of all games you play right here!")

game=st.text_input("Enter a game you played:")
rating=st.slider("Rate it on a scale from 1=bad to 5=awsome:",1,5)

if st.button("Add to Tracker"):
    st.session_state.games.append({"name":game,"rating":rating})
    st.success(f"Added {game} with rating {rating}")

if st.session_state.games:
    st.subheader("Your Game List")
    for i,g in enumerate(st.session_state.games, 1):
        st.write(f"{i}. **{g['name']}** - {g['rating']}/5")
