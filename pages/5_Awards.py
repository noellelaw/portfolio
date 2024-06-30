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
st.header("AWARDS & HONORS")
# Wat was your solution sir?
with st.container():
    st.subheader("City of Tomorrow High Achiever Award | [Ford Motor Company](https://corporate.ford.com/home.html)")
    st.write("*Received Summer 2022*")
    st.markdown("""
    A three week challenge in which 244 interns joined a forward thinking dialogue about the future of Ford and how it can build a better world. 
    Our team of 4 persons designed and submitted a solution in Future Mobility that received the high achiever award.
    """)

with st.container():
    st.subheader("Louis T. Radar Chairperson's Award for Best Capstone | [University of Virginia](https://engineering.virginia.edu/department/electrical-and-computer-engineering)")
    st.write("*Received May 2021*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.video('https://www.youtube.com/watch?v=Wlms5b5Qncw')
    with text_column:
        st.markdown("""
        Zachary Hicks, Jason Ashley, Eleanor Ozer and I undertook the "Robotany" that integrates embedded systems interfacing, house plant physiology, 
        robotics and machine vision, and earned the Louis T. Rader Chairperson's Award for Best Capstone. This cybernetic plant autonomously tracked moisture levels, monitored growth,
        and moved based on its lighting needs.

        My primary role was as follows: 
        - Implemented a control algorithm in C using an ISR task scheduler to integrate light sensors, bump switches, cliff sensors, and the plant’s bioelectrochemical signals. 
        - Designed a computer vision algorithm with TensorFlow, OpenCV, and Python to isolate the plant from a user background, remove glare, and determine the growth levels of the plant for electrode placement and harvesting. 
        - Transmitted plant data via a WiFi module to be displayed on a user application. 
        """)
    st.markdown("""
        This work was completed in 12-weeks in a primarily virtual environment due to COVID-19. This required clear and effective communication so that 
        the 2-week integration period was successful. 

        [Read the full report here!](https://drive.google.com/file/d/1AoFtYZdHnXTRDDR_TJbMlkY0U8Tck1EZ/view) 
    """)
# I dried up reading the last sentence
with st.container():
    st.subheader("VA-NC Academic Achievement Award | [VA-NC Alliance](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1712724&HistoricalAwards=false)")
    st.write("*Received Spring 2020*")
    st.markdown("""
        The VA-NC Alliance recognizes the academic success and leadership development of STEM students. The Academic Achievement Award aims to recognize academic excellence. It was an honor to receive this award.  
    """)
with st.container(): 
    st.subheader("Multiple Awards for High School Science Project, Listed Below")
    st.write("*Received Spring 2015*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.image('images/sciencefair.png')
    with text_column:
        st.markdown("""
            **Experiments in Caffeine: The Effect of Roasting on the Caffeine Concentration in Coffee and the Standardization of Caffeine Extraction via Anti-Solvent Crystallization**
                
            Awards received: 
            - Northern Virginia Regional Science Fair 2015, 1st Place (Chemistry)
            - [Virginia Junior Academy of Science Symposium 2015](https://vjas.org/index.html) Honorable Mention (Chemistry)
            - [Society of Women Engineers](https://swe.org/) 2015 STEM Fair Specialty Award Recipient 
            - [Washington Statistical Society](https://washstat.org/) 2015 STEM Fair Award Recipient 
            """)
with st.container(): 
    st.subheader("Presidential Service Award, Gold | [AmeriCorps](https://presidentialserviceawards.gov/about)")
    st.write("*Received 2014, 2013, 2012, 2011*")
    st.markdown("""
            Completed 100+ hours of community service each year with specific focus on the following organizations:
            - [Rady Children's Ronald McDonald House](https://rmhc.org/)
            - [Father Joe's Villages](https://my.neighbor.org/)
            - [Serving Seniors](https://servingseniors.org/)
            - [Therapeutic Recreation Services, San Diego Parks and Recreation](https://www.sandiego.gov/park-and-recreation/activities/trs)
        """)


