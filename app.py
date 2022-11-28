import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webage", page_icon=":tada:",
                   layout="wide")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

contact_form = """
        <form action="https://formsubmit.co/3b395cb5994b120cbd88920acb514e10" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button class="css-1x8cf1d edgvbvh10" type="submit">Send</button>
        </form>

        """


# --- LOAD ASSETS ---
lottie_an = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_b4hn3bqt.json")


# ---BODY---
with st.container():

    left_col, right_col = st.columns(2)
    with left_col:
        st.subheader("Hi, I am Katya Klimenkova :wave:")
        st.title("Looking for a specialist/assistant position in Minsk or remote")
        st.write("I'm passionate about finding ways to use Appscript and Python to be more efficient in my job")
        st.write("[My LinkedIn ->](https://www.linkedin.com/in/katya-klimenkova-628700224/)")

    with right_col:
        st_lottie(lottie_an, height=300, key="coding")

st.write("---")
with st.container():
    lc, cc,  rc = st.columns((3, 1, 3))
    with lc:
        st.header("About Me")
        st.write("#")
        st.write(
            """
            I'm an **easy-going** person, motivated 
            by **a friendly atmosphere** in a team, where one 
            can share their ideas and reach 
            agreements in a rational way. I'm always **eager to learn**
            new things and tools. 
            """
            )
        st.write(
            """
            I'm more of an **action-oriented** worker – an 
            implementer, so if you are looking for one, I'm 
            the best fit for your team.
            """
            )

        st.write("#")

        with open("KatyaKlimenkova_CV.pdf", 'rb') as f:
            pdf = f.read()

        st.download_button(
            "Download my CV",
            data=pdf,
            file_name="KatyaKlimenkova_CV.pdf",
            mime='application/octet-stream'
        )


    with rc:
        st.header("Contact Me")
        st.markdown(contact_form, unsafe_allow_html=True)
