import streamlit as st
tab1,tab2,tab3=st.tabs(["About","Hobbies","Contact"])
with tab1:
    col1,col2=st.columns([0.3,0.7])
    with col1:
        st.image(r"\pages\light_fruit.webp",width=200)
        st.subheader("Agastya has a light fruit.💫")
    with col2:
        st.write("Agastya is a really good ggrinder in the Roblox game, Blox Fruits. He loves the game and has a pretty good status " \
        "and would like to help any of you who would like to grind like him too.")
with tab2:
    st.write("I love to do coding, playing piano, playing tennis, and of course playing video games. I also like physical stuff.")
with tab3:
    st.write("email: email2agastya@gmail.com")
    st.write("roblox profile: rip_Jax")
