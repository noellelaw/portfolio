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
st.header("PROJECTS & PAPERS")

with st.container():
    st.subheader("The Ink Splotch Effect: A Case Study on ChatGPT as a Co-Creative Game Designer | [arXiv](https://arxiv.org/abs/2403.02454)")
    st.write("Asad Anjum, Yuting Li, **Noelle Law**, M Charity, Julian Togelius | *FDG 2024*")
    st.markdown("""
    **Abstract**:
    This paper studies how large language models (LLMs) can act as effective, high-level creative collaborators and "muses" for game design. We model the design of this study after the exercises artists use by looking at amorphous ink splotches for creative inspiration. Our goal is to determine whether AI-assistance can improve, hinder, or provide an alternative quality to games when compared to the creative intents implemented by human designers. The capabilities of LLMs as game designers are stress tested by placing it at the forefront of the decision making process. Three prototype games are designed across 3 different genres: (1) a minimalist base game, (2) a game with features and game feel elements added by a human game designer, and (3) a game with features and feel elements directly implemented from prompted outputs of the LLM, ChatGPT. A user study was conducted and participants were asked to blindly evaluate the quality and their preference of these games. We discuss both the development process of communicating creative intent to an AI chatbot and the synthesized open feedback of the participants. We use this data to determine both the benefits and shortcomings of AI in a more design-centric role.
    
    `AI/ML` `Data Science` `Python`
    """)
with st.container():
    st.subheader("Beyond the Closed Set: Vision-Language Models for Open-Vocabulary Semantic Segmentation of Autonomous Driving Datasets")
    st.write("*September 2022 to May 2023*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.image('images/cseg.png')
    with text_column:
        st.markdown("""
        """)
        st.markdown("""
        - Pursued a master’s thesis in the Data, Intelligence, and Computational Engineering lab under Prof. Chinmay Hegde with a focus on vision-language (VL) models for open-vocabulary semantic segmentation of autonomous driving datasets. A meta-analysis was performed to identify impact of training dataset, common model bottlenecks, and model-accuracy-throughput trade-ff when applied in a zero-shot setting. 
        - Implemented a new visualization technique, called Triangles, to more efficiently analyze model results.
        - Designed a context-aware region-classification architecture for open-vocabulary segmentation based on issues identified in the meta-analysis. 
        - Explored inherent capabilities of denoising diffusion probablistic models to generate semantically meaningful regions.

        View my defense slides [here](https://drive.google.com/file/d/1dKxKcTDBrLPkzgfXg1NFeKDd5ijQPanQ/view?usp=sharing) and read the full report [here](https://drive.google.com/file/d/1wvMbF-VV6zKs7vAlBgRmfmL6-rq3Uz1W/view?usp=sharing)!
        `AI/ML` `Data Science & Visualization` `Python` `PyTorch` `JavaScript D3` `High-Performance Computing`
        """)
with st.container():
    st.subheader("Fast, Safe, and Proactive Runtime Planning and Control of Autonomous Ground Vehiclesin Changing Environments | [IEEE Xplore](https://ieeexplore.ieee.org/document/9483719) ")
    st.write("Grace Glaubit, Katie Kleeman, **Noelle Law**, Jeremiah Thomas, Shijie Gao, Rahul Peddi, Esen Yel, Nicola Bezzo | *SIEDS 2021*")
    st.write("*First 4 authors contributed equally to the paper.*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.image('images/amr.png')
    with text_column:
        st.markdown("""
            **Abstract**:
            Autonomous ground vehicles (UGVs) traversing paths in complex environments may have to adapt to changing terrain characteristics, 
            including different friction, inclines, and obstacle configurations. In order to maintain safety, vehicles must make adjustments 
            guided by runtime predictions of future velocities. To this end, we present a neural network-based framework for the proactive 
            planning and control of an autonomous mobile robot navigating through different terrains. Using our approach, the mobile robot 
            continually monitors the environment and the planned path ahead to accurately adjust its speed for successful navigation toward 
            a desired goal. The target speed is selected by optimizing two criteria: (1) minimizing the rate of change between predicted and 
            current vehicle speed and (2) maximizing the speed while staying within a safe distance from the desired path. Additionally, we 
            introduce random noise into the network to model sensor uncertainty and reduce the risk of predicting unsafe speeds. We extensively 
            tested and validated our framework on realistic simulations in Gazebo/ROS with a UGV navigating cluttered environments with different 
            terrain frictions and slopes.

            [Read the PDF here!](https://drive.google.com/file/d/1mPT_006Lz3W7w54uKtE_jplliXu_FtIa/view?usp=sharing) 

            `Python` `Matlab` `ROS` `Gazebo Simulation Software`
        """)
with st.container():
    st.subheader("The Robotany:A Cybernetic Plant ")
    st.write("*September to December 2020*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.video('https://www.youtube.com/watch?v=Wlms5b5Qncw')
    with text_column:
        st.markdown("""
        Zachary Hicks, Jason Ashley, Eleanor Ozer and I undertook the "Robotany" that integrates embedded systems interfacing, house plant physiology, 
        robotics and machine vision, and earned the Louis T. Rader Chairperson's Award for Best Capstone. The a cybernetic plant to track moisture levels, monitor growth, 
        and move based on its lighting needs.

        My primary role was as follows: 
        - Implemented a control algorithm in C using an ISR task scheduler to integrate light sensors, bump switches, cliff sensors, and the plant’s bioelectrochemical signals. 
        - Designed a computer vision algorithm with TensorFlow, OpenCV, and Python to isolate the plant from a user background, remove glare, and determine the growth levels of the plant for electrode placement and harvesting. 
        - Transmitted plant data via a WiFi module to be displayed on a user application. 
        """)
    st.markdown("""
        This work was completed in 12-weeks in a primarily virtual environment due to COVID-19. This required clear and effective communication so that 
        the 2-week integration period was successful. 

        [Read the full report here!](https://drive.google.com/file/d/1AoFtYZdHnXTRDDR_TJbMlkY0U8Tck1EZ/view) 

        `Embedded C` `Sensors & Actuators` `Control & Motion Planning` ` TI-RSLK MAX Robot` `MSP432 Microcontroller` `TensorFlow` `OpenCV` 
    """)
with st.container():
    st.subheader("TI-RSLK MAX Robot and Pololu Robotic Arm")
    st.write("*Spring 2020*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.image('images/robot_arm.jpeg')
    with text_column:
        st.markdown("""
        """)
        st.markdown("""
        - Developed a robot capable of navigating an environment through the integration of wall following, speed control and obstacle adjustment algorithms.
        - Programmed an attachable triple-joint robotic arm programmed to translate user input into movement, including the ability to pick up a light-weight object.

        `Embedded C` `Control` `Python` `Sensors & Actuators`
        """)
with st.container():
    st.subheader("Autonomous, Environmentally-Aware Greenhouse")
    st.write("*Spring 2019*")
    st.markdown("""
    - A cyber-physical greenhouse with a heating, cooling, and automated watering system that can be controlled using a MySQL relational database and an EC2 client.
    - Project strengthened ability to design and implement creative solutions under constraints (yes, the cooling system was a bike spoke and a servo motor that was able to lift the greenhouse roof.)

    `PHP Scripting` `HTML & Webpage Design` `C++` `Arduino` `AWS` `Tableau` `MySQL`
    """)
with st.container():
    st.subheader("PCB Audio Visualizer")
    st.write("*Spring 2019*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.video('https://youtu.be/xkFwRU_dNgc')
    with text_column:
        st.markdown("""
        A printed circuit board (PCB) that can filter a variety of signals and display the distribution of bass and treble through LED drivers, high / low pass filters, peak detectors, and a summing circuit.

        `PCB Design` `Signal Analysis` `Virtual Bench` `NI Multisim`
        """)
