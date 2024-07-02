import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constant import *
from PIL import Image
import json
import base64

page_icon = Image.open("images/bug.png")
st.set_page_config(
    page_title='Noelle Law',
    page_icon=page_icon,
    layout="wide",
)


linkedin_url = "https://www.linkedin.com/in/noelle-law/"
email_url = "mailto:noelle.t.law@gmail.com"
github_url = "https://github.com/noellelaw"

# -----------------  loading assets  ----------------- #
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
    <a href="{url}" target="_blank" style="margin-right: 20px;">
        <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
    </a>
    '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src = {
            "linkedin": "https://img.icons8.com/ios/50/linkedin.png",
            "github": "https://img.icons8.com/ios/50/github--v1.png",
            "email": "https://img.icons8.com/ios/50/new-post--v1.png"
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

    return icons_html

local_css("style/style.css")

# loading assets
lottie_gif = load_lottiefile("animations/robot.json")#load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
ros_lottie = load_lottiefile("animations/ros.json")
python_lottie = load_lottiefile("animations/python.json") #load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
embedded_lottie = load_lottiefile("animations/embeddedc.json")#load_lottieurl("https://lottie.host/3560055d-364f-4708-839d-157bc309c81f/A38ihrt7zF.json")
ml_lottie = load_lottiefile("animations/ai.json")#load_lottieurl("https://lottie.host/510f1a12-18cb-47ee-a6dc-a73d71d987dd/1JdgFuRHoQ.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
sim_lottie = load_lottiefile("animations/sim.json") #load_lottieurl("https://lottie.host/2a2a6a04-1648-467a-a310-db095d900da8/PMcOUGSxP0.json")
datascience_lottie = load_lottiefile("animations/datascience.json")#load_lottieurl("https://lottie.host/c72ea3b4-5c71-4d05-bd95-85ddaf951204/f3AeCuQies.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")



# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:black;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2,col3 = st.columns([8,2,0.5])

    full_name = info['Full_Name']
    with col1:
        gradient('F0EBE3','F6F5F2','C7B7A3',f"Hi, I'm {full_name}!", info["Intro"])
        st.write("")

        st.write(info['About'])

    with col2:
        st.image("images/profile_2.png", )
    with col3:
        st.markdown(
            social_icons(30, 30, LinkedIn=linkedin_url,  Email=email_url, GitHub=github_url, ),
            unsafe_allow_html=True)
    #st_lottie(lottie_gif, height=280, key="data")


# ----------------- sidebar -------------------------- #
#st.sidebar.image("images/profile.png", use_column_width=True)
        

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Highlighted Skills')
    st.write('*Take a peek at other tabs to see my full skillset.*')
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1, 0.5, 1, 0.5, 1, 0.5, 1, 0.5])
    with col1:
        st_lottie(python_lottie, key="python",  speed=1)
        st.markdown(f"<p style=color:#4D4545;'>Python</p>", 
                unsafe_allow_html=True)
    with col3:
        st_lottie(ml_lottie,key="ml", speed=1)
        st.write(f"<p style=color:#4D4545;'>AI / ML / CV</p>", 
                unsafe_allow_html=True)
        st_lottie(datascience_lottie,key="ds",  speed=1)
        st.markdown(f"<p style=color:#4D4545;'>Data Science</p>", 
                unsafe_allow_html=True)
    with col5:
        st_lottie(sim_lottie,key="simulation", speed=1)
        st.write(f"<p style=color:#4D4545;'>Modelling & Sim</p>", 
                unsafe_allow_html=True)
        st_lottie(ros_lottie, key="ros",  speed=1)
        st.markdown(f"<p style=color:#4D4545;'>Robotics & ROS</p>", 
                unsafe_allow_html=True)
    with col7:
        st_lottie(embedded_lottie,key="embedded", speed=1)
        st.write(f"<p style=color:#4D4545;'>Embedded C / C++</p>", 
                unsafe_allow_html=True)


