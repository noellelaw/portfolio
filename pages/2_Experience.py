import streamlit as st
import PIL
from PIL import Image 


page_icon = Image.open("images/bug.png")
st.set_page_config(
    page_title='Noelle Law',
    page_icon=page_icon,
    layout="wide", 
)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
#local_css("style/style.css")
st.header("EXPERIENCE")

with st.container():
    st.subheader("Machine Learning & Perception Engineer | [JHU Applied Physics Lab](https://www.jhuapl.edu/about)")
    st.write("*August 2023 to Present*")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(Image.open('images/jhu.jpeg'))
    with text_column:
        st.markdown("""
        - Design and develop algorithms for more interpretable and trustworthy machine learning systems, with focus on vision (multispectral) and language modalities. 
        - Principal Investigator for Conformal Autoregressive Generation for Large Language Models, in which a multi-hypothesis-based approach is leveraged to better quantify model uncertainty. 
        - Redesigned data preprocessing pipeline, improving speed by 92% and allowing for quicker downstream model development. 
        - Selected for the [BLAST annual innovation challenge](https://www.jhuapl.edu/culture/innovation) to develop a rapid-prototype solution for a given problem during summer 2024.   
        `Python` `Pytorch` `AI/ML/CV` `Data Science` `Simulation` `Experimental Design` `Docker` `Git`
        """)
with st.container():
    st.subheader("Research Assistant | [NYU DICE Lab](https://chinmayhegde.github.io/lab/)")
    st.write("*September 2022 to June 2023*")
    # I'd add a quick line about how Triangles more efficiently analyzed
    st.markdown("""
    - Pursued a master’s thesis in the Data, Intelligence, and Computational Engineering lab under Prof. Chinmay Hegde with a focus on vision-language (VL) models for open-vocabulary semantic segmentation of autonomous driving datasets. A meta-analysis was performed to identify impact of training dataset, common model bottlenecks, and model-accuracy-throughput trade-off when applied in a zero-shot setting.
    - A new visualization technique, Triangles, was implemented to more efficiently analyze model results.
    - A context-aware region classification architecture was designed for open-vocabulary segmentation based on issues identified in the meta-analysis.
    - Exploration on the inherent capabilities of denoising diffusion probabilistic models to generate semantically meaningful regions.
    `Python` `Pytorch` `AI/ML/CV` `Data Science` `Javascript` `D3` `Experiment Design`
    """)
with st.container():
    st.subheader("Foundations of Robotics Teaching Assistant | [New York University](https://engineering.nyu.edu/faculty/giuseppe-loianno)")
    st.write("*September to December 2022*")
    st.markdown("""
    - Developed & graded homework assignments and provided active instruction to a graduate-level foundations of robotics (ROB-GY 6003) course comprised of 80+ persons.
    `Matlab & Simulink` `Direct & Inverse Kinematics` `Sensors & Actuators` `Trajectory Generation & Path Planning` 
    """)
with st.container():
    st.subheader("Research & Advanced Engineering Intern | [Ford Motor Company, Greenfield Labs](https://corporate.ford.com/operations/locations/silicon-valley.html)")
    st.write("*May to August 2022*")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(Image.open('images/ford.png'))
    with text_column:
        st.markdown("""
        - Explored use of machine learning for robotic grasping operations through use of 6-DoF deep object pose estimation, in which a one-shot deep fully convolutional neural network was used as a part of a larger system.
        - Developed synthetic data pipeline and simulations of 3D depth cameras in ROS and NVIDIA Omniverse, including the development, training, and testing of datasets for 4 YCB objects for a Ford custom object.
        - Presented accomplishments to team of 30+ team, project, group members and leads.
        `NVIDIA Omniverse` ` Synthetic Data Generation` `Sim to Real` `Python` `Pytorch` `AI/ML/CV` `Data Science`
        """)
# These next two entries read almost identically, but fine for a website
with st.container():
    st.subheader("Embedded Computing & Robotics TA and Course Developer | [University of Virginia](https://engineering.virginia.edu/department/electrical-and-computer-engineering)")
    st.write("*January 2020 - May 2021*")
    image_column, text_column = st.columns((1,5))
    with image_column:
        #st.video("https://youtu.be/-G3QmFMvNKc", start_time=14)
        st.video("https://www.youtube.com/watch?v=tDim7dEgqYc")
    with text_column:
        st.markdown("""
        - Provided active instruction to 50+ students, including the development of labs, tutorials, and weekly quizzes to ensure learning goals were met.
        - Researched and redeveloped course curriculum throughout summer 2020.
        `Embedded C` `TI-RSLK MAX` `Sensors & Actuators` `Controllers` `Signal Processing` `MSP432`
        """)
with st.container():
    st.subheader("Computer Architecture Teaching Assistant | [University of Virginia](https://engineering.virginia.edu/department/electrical-and-computer-engineering)")
    st.write("*January 2021 to May 2021*")
    st.markdown("""
        - Provided active instruction to 50+ students for Computer Architecture and Design (ECE 4435), including hosting weekly office hours and grading assignments to ensure learning goals were met.
        - Researched and redeveloped course curriculum throughout summer 2020.
        `VHDL` `Simulation & Synthesis` 
    """)
with st.container():
    st.subheader("Software Engineering Intern | [ASML](https://www.asml.com/en)")
    st.write("*May 2020 to August 2020*")
    st.markdown("""
        - Created a hardware simulator for the embedded systems of the Extreme UV lithography light source using MATLAB, C, C++, and company-specific languages to enable more efficient feature development.
        - Tested simulator and communication interfaces using Python scripting, gtest, and gmock.
        - Contributed to all aspects of the build, test, and release cycle and presented accomplishments to 40+ team, project, and group members and leads.
        `Embedded C` `C++` `Matlab & Simulink` `Python` `gtest` `gmock` 
    """)
with st.container():
    st.subheader("Software Developer Intern | [ASML](https://www.asml.com/en)")
    st.write("*May 2019 to August 2019*")
    st.markdown("""
        - Implemented hardware stubs and an image generation library using Python, OpenCV and C++.
        - Presented accomplishments to 10+ team members and leads.
        `C++` `Python` `OpenCV` 
    """)
with st.container():
    st.subheader("Introduction to Engineering Teaching Assistant | [UVA](https://engineering.virginia.edu/)")
    st.write("*August 2018 to December 2019*")
    st.markdown("""
        - Introduction to engineering course in which I provided active instruction to 30+ students, including the development of a module for students to design and construct a solar panel.
        `Circuit design` `Matlab & Simulink` `Python` 
    """)
with st.container():
    st.subheader("General Physics for Engineers I, Workshop Teaching Assistant | [UVA](https://www.phys.virginia.edu/)")
    st.write("*May 2018 to December 2019*")
    st.markdown("""
        - Introduction to physics lab course for general group problem solving that teaches the application of physics to real life scenarios.
        - Provided active instruction and hosted weekly office hours to 24+ students. 
        `Data Acquisition & Analysis` `Classical Mechanics & Thermodynamics`
    """)
with st.container():
    st.subheader("Virginia Aerospace Science and Technology Scholar, Human Factors Team Lead | [Virginia Space Grant Consortium](https://vsgc.odu.edu/vasts/)")
    st.write("*September 2015 - July 2016*")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image("images/nasa_larc.jpeg")
    with text_column:
        st.markdown("""
        - Successfully completed and placed among top performers in coursework designed to inform scholars about NASA, space exploration, and key STEM skills. Course was worth two college credits. 
        - Selected for summer academy program hosted by NASA Langley Research Center, in which scholars worked in project teams to design a human mission to Mars. 
        - Interviewed and selected to be the Human Factors Team Lead during NASA Academy program. 
        - This is where I first met [ISAAC](https://www.nasa.gov/centers-and-facilities/langley/robot-isaac-will-help-nasa-langley-speed-toward-innovation/), and fell in love with robotics.

        """)