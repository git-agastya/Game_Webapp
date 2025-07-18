
import streamlit as st
st.title("About Games 🎮")

st.write(
    "Games are fun, exciting, and a great way to learn new things! There are so many types of games like sports games, board games, video games, and outdoor games. "
    "They help you improve your skills, stay active, and most importantly, have fun with friends!"
)
# List of game categories
game_categories = {
    "Sports Games": "Football, Basketball, Tennis, Baseball",
    "Board Games": "Monopoly, Chess, Scrabble, Clue",
    "Video Games": "Minecraft, Fortnite, Mario Kart, Roblox",
    "Outdoor Games": "Hide and Seek, Tag, Kickball, Jump Rope"
}
for category, games in game_categories.items():
    st.subheader(category)
    st.write(games)