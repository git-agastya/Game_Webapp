import streamlit as st

st.title("Trending Game This Week!")
trending_games=[
    {"name":"Fortnite","votes":120},
    {"name":"Roblox","votes":100},
    {"name":"Minecrat","votes":90},
    {"name":"Among Us","votes":85}
]
for game in trending_games:
    st.write(f"**{game['name']}** - {game['votes']} votes")
    st.progress(game['votes'] / max([g['votes'] for g in trending_games]))
st.subheader("Suggest a Game")
suggestion=st.text_input("Type your games suggestion:")
if suggestion:
    st.success(f"Thanks! We will consider adding **{suggestion}** to the list.")
    

st.subheader("Upwote your favirote game!")
upvote_game = st.selectbox("Which game would you like to upvote?", [game['name'] for game in trending_games])

# Action button to upvote
if st.button("Like"):
    st.success(f"Thank you for upvoting **{upvote_game}**." )