import streamlit as st

# 1. Page Config
st.set_page_config(page_title="For My Valentine ❤️", page_icon="💖")

# 2. Styling
st.markdown("""
    <style>
    .stApp { background-color: #9c6d6d; }
    .stButton>button {
        background-color: #9c6d6d;
        color: white;
        font-size: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Session State Management
if 'page' not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

def restart():
    st.session_state.page = 1

# --- PAGE 1: WELCOME ---
if st.session_state.page == 1:
    st.title("Happy Valentine's Day Babyy! 💖")
    st.write("### I have a surprise for you...")
    
    # Cute bear/heart image that WORKS
    st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?w=600", caption="For You")
    
    if st.button("Open My Gift 🎁"):
        next_page()

# --- PAGE 2: REASONS ---
elif st.session_state.page == 2:
    st.title("Why I Love You ✨")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1516575150278-77136aed6920?w=400", caption="Us <3")
    with col2:
        st.image("https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?w=400", caption="My Love")

    st.success("1. You make me laugh when I'm sad.")
    st.info("2. You give the best hugs.")
    st.warning("3. You are my home.")
    
    if st.button("Next ->"):
        next_page()

# --- PAGE 3: THE QUESTION ---
elif st.session_state.page == 3:
    st.title("Will you be my Valentine? 🥺")
    
    # Puppy eyes image
    st.image("https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=500")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! ❤️"):
            st.session_state.page = 4
            st.rerun()
    with col2:
        if st.button("No 💔"):
            st.error("Wrong answer! Try again 😈")

# --- PAGE 4: SUCCESS ---
elif st.session_state.page == 4:
    st.balloons()
    st.title("💖 I LOVE YOU BABU! 💖")
    st.image("https://images.unsplash.com/photo-1513201099705-a9746e1e201f?w=600", caption="YAY!")
    if st.button("Start Over"):
        restart()


