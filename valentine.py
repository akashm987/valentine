import streamlit as st
import time

# 1. Page Config (Tab Title & Mobile Settings)
st.set_page_config(
    page_title="For My Valentine ❤️",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS (Make it pretty & Mobile Friendly)
st.markdown("""
    <style>
    /* Background Color */
    .stApp {
        background-color: #9c6d6d;
    }
    
    /* Center all images */
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    
    /* Make buttons look clickable and nice on mobile */
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        font-size: 18px;
        padding: 10px;
        width: 100%;
        border: 2px solid #ff4b4b;
    }
    
    /* Specific style for the YES button to make it pop */
    .big-button {
        font-size: 30px !important;
        background-color: #ff0000 !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Session State (This tracks which page we are on)
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0

# --- Functions to change pages ---
def next_page():
    st.session_state.page += 1

def restart():
    st.session_state.page = 1
    st.session_state.no_count = 0

def click_no():
    st.session_state.no_count += 1

# ================= PAGE 1: INTRO =================
if st.session_state.page == 1:
    st.title("Happy Valentine's Day Babyy! 😘🫂💖🧿")
    st.write("### I have a surprise for you...")
    
    # Cute bear gif
    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", width=300)
    
    st.write("") # Spacer
    if st.button("Open My Gift 🎁"):
        next_page()

# ================= PAGE 2: REASONS & PHOTOS =================
elif st.session_state.page == 2:
    st.title("Aanu Babyyyyy 😘😘😘😘😘")
    
    # Photo Gallery (You can add your own image links here)
    col1, col2 = st.columns(2)
    with col1:
        st.image("MyLove.jpg", caption="My Love") 
    with col2:
        st.image("us.jpg", caption="Us <3")

    st.divider()
    
    # Reasons List
    # st.subheader("3 Reasons why you are the best:")
    st.success(" Your smile lights up my entire world")
    st.info("You make even the boring days feel like an adventure")
    st.warning("I Love You Soo Much My Love 😘🫂❤️🧿")
    
    st.write("")
    if st.button("Next ->"):
        next_page()

# ================= PAGE 3: THE BIG QUESTION =================
elif st.session_state.page == 3:
    
    # If they clicked YES
    if st.session_state.get('yes_clicked'):
        st.balloons()
        st.title("I Love You My Cutie Pie 👀🫂❤️🧿")
        st.image("yay.jpg") # Happy bear
        st.write("You just made me the happiest person alive!")
        
        # Hearts animation
        st.markdown("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
        if st.button("Read it again?"):
            st.session_state.yes_clicked = False
            restart()
            
    # If they haven't answered yet
    else:
        st.title("Will you be my Valentine? 🥺")
        st.image("wilyoubemyvalentine.jpg", width=250) # Pleading face
        
        st.write("")
        
        # Logic for Growing Button
        # The 'Yes' button gets more exclamation marks and emojis every time 'No' is clicked
        yes_label = "YES! ❤️"
        if st.session_state.no_count > 0:
            yes_label = "YES" + "!" * st.session_state.no_count + " ❤️" * st.session_state.no_count
        
        # Columns for buttons
        col1, col2 = st.columns(2)
        
        with col1:
            # If they click YES
            if st.button(yes_label, key="yes_btn", use_container_width=True):
                st.session_state.yes_clicked = True
                st.rerun()
        
        with col2:
            # The NO button
            # It changes text or disappears if clicked too many times
            if st.session_state.no_count < 5:
                no_label = "No 💔"
                if st.session_state.no_count == 1: no_label = "Are you sure?"
                if st.session_state.no_count == 2: no_label = "Please?"
                if st.session_state.no_count == 3: no_label = "Don't do this!"
                if st.session_state.no_count == 4: no_label = "I'm gonna cry..."
                
                if st.button(no_label, key="no_btn", on_click=click_no, use_container_width=True):
                    pass # The page just reloads with a bigger YES button
            else:
                st.write("😈 No choice now!")

