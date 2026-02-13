import streamlit as st
import time

# Page Setup
st.set_page_config(page_title="For My Valentine ❤️", page_icon="❤️")

# Styling to make it look nice
st.markdown("""
<style>
    .stApp {
        background-color: #ffe6e6;
    }
    h1 {
        color: #d6336c;
        text-align: center;
        font-family: 'Brush Script MT', cursive;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        width: 100%;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# --- CONTENT START ---

st.title("❤️ Happy Valentine's Day Babu! ❤️")
st.write("### To my favorite person in the world...")

# Photo Section
# To use your own photo: 
# 1. Upload your photo to a site like imgur.com 
# 2. Right click the image and select "Copy Image Address"
# 3. Paste that link below inside the quotes.
st.image("us.jpg", caption="My favorite person ❤️") # CHANGE THIS
st.image(image_url, use_container_width=True)

st.divider()

# Interactive Section
st.header("💌 Why I Love You")

if st.button("Reason #1"):
    st.success("You have the cutest laugh I've ever heard.") # CHANGE THIS

if st.button("Reason #2"):
    st.warning("You support my dreams like no one else.") # CHANGE THIS

if st.button("Reason #3"):
    st.error("You make the bad days better just by being there.") # CHANGE THIS

st.divider()

# The Big Question
st.subheader("I have one question...")
if st.button("Will you be my Valentine? 🌹"):
    st.balloons()

    st.markdown("## 💖 YAY! I love you! 💖")


