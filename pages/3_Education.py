import streamlit as st
import PIL
from PIL import Image 

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

page_icon = Image.open("images/bug.png")
st.set_page_config(
    page_title='Noelle Law',
    page_icon=page_icon,
    layout="wide", 
)
#local_css("style/style.css")
st.header("EDUCATION & COURSEWORK")
with st.container():
    st.subheader(" New York University Tandon School of Engineering ")
    st.write("*Doctoral Student, Mechanical Engineering and Urban Sciences*, Fall 2025")
    st.subheader("Stanford Online")
    st.write("*Fall 2024*")
    st.markdown("""
    **Coursework**: Transforming the Grid: AI, Renewables, Storage, EVs and Prosumers.
    """)
    st.subheader(" New York University Tandon School of Engineering | GPA: 3.93/4.0")
    st.write("*Master of Science, Summa Cum Laude, Computer Science*, May 2023")
    st.markdown("""
    **Selected Coursework**: Artificial Intelligence, Machine Learning, Deep Learning, Robot Localization & Navigation, Visualization for Machine Learning
    
     **[Graduate Thesis](https://drive.google.com/file/d/1wvMbF-VV6zKs7vAlBgRmfmL6-rq3Uz1W/view)**: Beyond the Closed Set: Vision-Language Models for Open-Vocabulary Semantic Segmentation of Autonomous Driving Datasets. 
     *Read more about my Thesis in the projects tab!*
    
    """)

with st.container():
    st.subheader("University of Virginia SEAS | GPA: 3.57/4.0")
    st.write("*Bachelor of Science with Distinction, Computer Engineering (Minor: Design Integration)*, May 2021")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(Image.open('images/undergrad.jpeg'))
    with text_column:
        st.markdown("""
        **Selected Coursework**: Autonomous Mobile Robots, Robotics for Software Engineers, Embedded Computing & Robotics, Data & Diversity.
        
        **Awards**: Louis T. Rader Chairperson Award for Best Capstone (2021), VA-NC Alliance Academic Achievement Award (Spring 2020) 

        **[Undergraduate Thesis](https://libraetd.lib.virginia.edu/public_view/3n203z86h)**: The Robotany: A Cybernetic Plant and the Impact of Autonomous Technology on the Workforce. 
        *Read more about the Robotany in the projects tab!*

        """)
