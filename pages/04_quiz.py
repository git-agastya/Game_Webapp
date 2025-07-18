import streamlit as st

import random

import pandas as pd

import os


st.title("🧠 Fun Quiz Time")

st.subheader("Test your game knowledge and have fun!")


csv_path = "game_app\data\quiz_scores.csv"


username = st.text_input("Enter your name to start the quiz 👇")


# Prevent quiz from starting without a name

if username.strip() == "":

    st.warning("Please enter your name to begin!")

    st.stop()


# Define quiz questions (original version)

original_questions = [

    {

        "question": "What is the blocky game where you build and mine?",

        "options": ["Fortnite", "Roblox", "Minecraft", "CandyCrush"],

        "answer": "Minecraft"

    },

    {

        "question": "Which game has imposters and crewmates?",

        "options": ["Fortnite", "Among Us", "Clash Royale", "Minecraft"],

        "answer": "Among Us"

    },

    {

        "question": "Which game lets you create and play millions of user-made games?",

        "options": ["Roblox", "PUBG", "Valorant", "Minecraft"],

        "answer": "Roblox"

    },

    {

        "question": "In which game do players build towers and battle cards?",

        "options": ["Valorant", "Clash Royale", "Among Us", "PUBG"],

        "answer": "Clash Royale"

    },

    {

        "question": "Which game is known for building and surviving on floating islands?",

        "options": ["Minecraft Skyblock", "Call of Duty", "GTA", "Temple Run"],

        "answer": "Minecraft Skyblock"

    }

]


# Use session_state to shuffle only once per user session

if "questions" not in st.session_state:

    st.session_state.questions = random.sample(original_questions, len(original_questions))


score = 0

user_answers = []


# Show questions

for i, q in enumerate(st.session_state.questions):

    user_answer = st.radio(f"Q{i+1}: {q['question']}", q["options"], key=f"q{i}")

    user_answers.append((q["question"], user_answer, q["answer"]))

    if user_answer == q["answer"]:

        score += 1


# Score submission

if st.button("Check my Score"):

    st.success(f"🎯 {username}, you scored {score} out of {len(st.session_state.questions)}!")


    if score == len(st.session_state.questions):

        st.balloons()

        st.markdown("🏅 Perfect Score! You're a Game Genius!")

    elif score >= 3:

        st.markdown("👍 Great job! You're almost there!")

    else:

        st.markdown("🤔 Good try! Want to play again?")


    # Show correct answers

    with st.expander("📘 See Correct Answers"):

        for i, (q, ua, ca) in enumerate(user_answers):

            st.write(f"Q{i+1}: {q}")

            st.write(f"✅ Correct: {ca} | 👤 Your Answer: {ua}")

            st.markdown("---")


    # Save to CSV

    new_entry = pd.DataFrame([[username, score]], columns=["Name", "Score"])

    if os.path.exists(csv_path):

        old_data = pd.read_csv(csv_path)

        updated_data = pd.concat([old_data, new_entry], ignore_index=True)

    else:

        updated_data = new_entry


    updated_data.to_csv(csv_path, index=False)


    # Show high score info

    highest_score = updated_data["Score"].max()

    top_players = updated_data[updated_data["Score"] == highest_score]["Name"].tolist()


    st.subheader("🏆 Leaderboard Champion")

    st.write(f"Highest Score: **{highest_score}**")

    st.write("Top Player(s):")

    for player in top_players:

        st.markdown(f"- 👑 {player}")
