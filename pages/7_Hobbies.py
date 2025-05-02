import streamlit as st
from PIL import Image
from constant import *
from io import BytesIO
import streamlit.components.v1 as components



page_icon = Image.open("images/bug.png")
st.set_page_config(
    page_title='Noelle Law',
    page_icon=page_icon,
    layout="wide", 
)
st.header("HOBBIES")

st.write("Art, running, reading, gardening, and really anything that gets me outdoors.")
with st.container():
    col1,col2, col3, col4 = st.columns([2,2,2,2])
    with col1: 
      st.image("images/painting_2.jpeg")
      st.image("images/polar_plunge_1.JPG")
      st.image("images/polar_plunge_2.jpeg")
      st.image("images/hiking7.JPG")
      st.image("images/soccer.jpeg")
      st.image("images/hiking6.jpeg")
    with col2: 
      st.image(("images/running2.jpeg"))
      st.image("images/sister.jpeg")
      st.image("images/painting_3.jpeg")
      st.image("images/hiking8.jpeg")
      st.image("images/hiking2.jpeg")
      st.image("images/hiking11.JPG")
    with col3: 
      st.image("images/painting_4.jpeg")
      st.image("images/poem.PNG")
      st.image("images/hiking3.jpeg")
      st.image("images/hiking5.jpeg")
      st.image("images/art3.jpeg")
    with col4: 
      st.image("images/plants.jpeg")
      st.image("images/brother.JPG")
      st.image("images/art5.png")
      st.image("images/art2.jpeg")
      st.image("images/art1.jpeg")
      st.image("images/painting.jpeg")