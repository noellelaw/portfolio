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
st.header("VOLUNTEERING")
#local_css("style/style.css")
with st.container():
    st.subheader("Co-Instructor, Python for Girls II | [APL STEM Academy](https://secwww.jhuapl.edu/stem/stem-academy)")
    st.write("*January 2024 to Present*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.video("https://www.youtube.com/watch?v=ffMzq3NsB8U")
    with text_column:
        st.markdown("""
        APL STEM Academy provides an accessible, inclusive, and supportive place to learn. I am extremely passionate when it comes to STEM as a space for
        all, so it has been such a pleasure to volunteer at this organization.
        - Provided active instruction to 16 middle school students in a 12 week Python for Girls II course.
        - Included the development of lectures, games, and labs. 

        """)

# I'd recommend combining the first two bullets about spreading the word / answering questions. Maybe combine them and quickly say why that is so important to do
with st.container():
    st.subheader("Trash Talk (Waste Management) Volunteer | [JHUAPL](https://sustainability.jhu.edu/news/ask-the-green-guide-compost-on-campus/)")
    st.write("*December 2023 to Present*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.image('images/trashtalk.png')
    with text_column:
        st.markdown("""
        Composting has an incredible array of ecological, environmental and social impacts as it can create more resilient ecosystems through healthier soils.
        This creates an system that benefits food security, public health, and increased biodiversity. 

        As a Trash Talk (Waste Management) volunteer:
        - Stood at a waste management area during lunch and breakfast hours to inform persons where each item can be placed (trash, recycle, compost).
        - Answered any questions regarding who we partnered with for composting, the differences in a commercial recycling contact and its impact, and why it is so critical items are placed in the correct bins.
        - Helped increase communication when materials changed due to supply chain issues to ensure the correct items were placed in the correct bins.
        """)
with st.container():
    st.subheader("Computers4Kids Clubhouse Volunteer | [C4K](https://c4kclubhouse.org/our-mission/)")
    st.write("*Fall 2018 to Spring 2019*")
    st.markdown("""
    C4K aims to provide a free space and mentorship program for 6th-12th graders to explore their passions in science, technology, engineering, arts, and math (STEM).
    
    As a C4K volunteer:
    - Designed modules, such as introduction to digital signal processing (DSP), that would provide a friendly and digestible way to learn a new concept. Modules included active-learning projects. 
    - Assisted students with discovering new skills and helping them with projects.
    """)
with st.container():
    st.subheader("Club Dust Volunteer | [Club Dust](https://www.clubdust.org/)")
    st.write("*Winter 2013 to Present*")
    image1_column,  image2_column, text_column, = st.columns((2,2,1))
    with image1_column:
        st.image('images/clubdust.jpeg')
    with image2_column:
        st.image('images/club_dust.jpeg')
    st.markdown("""
    Club Dust aims to build houses and provide resources to extremely poor families in the border towns of Tijuana and Tecate, Mexico. They host two longer trips each year to build homes
    with smaller day trips interspersed. Award received Summer 2015 for willingness to assist wherever there were gaps in the workflow.
    
    As a volunteer:
    - Build, sand, and paint furniture.
    - Organize and deliver clothes, food, and shoes.
    """)
with st.container():
    st.subheader("Therapeutic Recreation Services Volunteer | [San Diego Parks and Recreation](https://www.sandiego.gov/park-and-recreation/activities/trs)")
    st.write("*Summer 2013 to Fall 2014*")
    st.markdown("""
    This program provides sports, recreation, leisure, and outreach services to people with physical, mental, and emotional disabilities.
    
    I primarily volunteered at the summer camp programs, where I would work with younger age groups to explore various activities such as surfing, volleyball, and other activities. During the year I would volunteer at dances and other activities. 
    """)
with st.container():
    st.subheader("Father Joe's Villages Volunteer | [Father Joe's Villages](https://my.neighbor.org/take-action/volunteer/)")
    st.write("*Summer 2012 to Fall 2013*")
    st.markdown("""
    As a volunteer, I would prepare and serve meals.
    """)
with st.container():
    st.subheader("Rady Children's Ronald McDonald House Volunteer | [Ronald McDonald House](https://rmhc.org/)")
    st.write("*Summer 2011 to Fall 2013*")
    st.markdown("""
    As a volunteer for the Ronald McDonald House, I would volunteer at various events, such as holiday carnivals and parties to help provide community and fun for children and families of seriously ill children who were receiving 
    medical care in Rady Children's Hospital. 
    """)
with st.container():
    st.subheader("Serving Seniors Volunteer | [Serving Seniors](https://servingseniors.org/get-involved/volunteer.html/title/nutrition-support)")
    st.write("*Summer 2011 to Spring 2023*")
    st.markdown("""
    As a volunteer, I would help provide nutrition support and spend time with seniors to help provide a sense of community.
    """)




