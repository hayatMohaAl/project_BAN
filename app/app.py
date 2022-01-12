import streamlit as st

import utils
import templates

# Set up page.
st.set_page_config(page_title="Ban is the new no", page_icon="🐙")
utils.local_css("static/local_styles.css")

if "show_all_repos" not in st.session_state:
    st.session_state["show_all_repos"] = False

def show_more():
    st.session_state["show_all_repos"] = True

def show_less():
    st.session_state["show_all_repos"] = False

if "preview_shown" not in st.session_state:
    st.session_state["preview_shown"] = False

# Create all streamlit components.
st.write("")
st.write(
    '<img width=100 src="https://emojipedia-us.s3.amazonaws.com/source/skype/289/squid_1f991.png" style="margin-left: 5px; filter: hue-rotate(230deg) brightness(1.1);">',
    unsafe_allow_html=True,
)
st.title("How to moderate the tweets with our solution")
st.write(
    """
    [![Follow](https://img.shields.io/twitter/follow/LeWagonNice?style=social)](https://twitter.com/LeWagonNice)
    """
)
st.write("")
tweet = st.text_input("Add a new tweet here :")
if not tweet :
    st.button("Let's check")
    # This button doesn't do anything, the page updates anyway when clicked.
    # But it reassures the user that it's just a preview and we don't tweet immediately.

progress_text = st.empty()
progress_bar = st.empty()
error_box = st.container()
tweet_box = st.empty()
checkboxes_external = st.container()
tweet_button = st.empty()

#Test de formulaire

with st.form("my_form"):
    st.write("Inside the form")
    tweet = st.text_input("Add a new tweet here :")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

# Code pour prédire si un tweet est à bannir ou non. Si oui message d'erreur si ok message de validation.

#new_input =
#new_output = model.predict(new_input)
#if new_output = 1 ... else ...

# Show tweets from Twitter bot (@gh2021_bot). The content of the iframe is hosted in
# a small Github pages site from this repo: https://github.com/jrieke/year-on-github-tweet-wall
st.write("---")
st.markdown(
    """
    <div style="display: flex; width: 100%; height: 100%; flex-direction: column; overflow: hidden;">
        <iframe height="1000" style="margin-left: -15px;" src="https://twitter.com/search?q=meetoo&src=typed_query"></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

fineprint = st.empty()
