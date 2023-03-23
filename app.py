from pathlib import Path
import streamlit as st
from PIL import Image,ImageDraw,ImageOps
import sys
sys.path.insert(1, "C:/Users/Praks12/anaconda3/Lib/site-packages/streamlit_option_menu")
from streamlit_option_menu import option_menu
import numpy as np

#---Path Settings---
current_dir = Path(__file__).parent #if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "Resume_Prakhar.pdf"
profile_pic = current_dir / "Profile_pic.png"
robo1_pic= current_dir / "r1.png"
robo2_pic= current_dir / "r2.png"
stock_pic= current_dir / "stock_market.jpg"
data_pic = current_dir / "data_pic.png"
subtitle_pic= current_dir / "vedio_subtitle.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Prakhar Gupta"
PAGE_ICON = ":wave:"
NAME = "Prakhar Gupta"
DESCRIPTION = """
Passionate about solving problems , building things and coming up with innovative ideas.
"""
EMAIL = "prakhargupta.2001@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/prakhar-gupta-43830a73/",
    "GitHub": "https://github.com/prak12g?tab=repositories",
    "Instagram": "https://www.instagram.com/prakhar.g2001/"
}
PROJECTS = {
    "☞ RoboCon 2022 - Created 2 robots to play the game Lagori for the Robotics Competition held by IIT Delhi. Tech : Raspberrypi , Arduino ": "https://drive.google.com/drive/folders/16xGjY5oiOvtP1F6ZtGaT-ZZJrx2BYRa5",
    "☞ Stock Market Prediction: Used LSTM machine learning model to predict Mahindra’s (MM) stock price. Tech: TensorFlow, Python, Keras, Pandas": "https://github.com/prak12g/Stock-Market-Prediction-Using-ML.git",
    "☞ Data Extraction and Text Analysis: Extracted textual data articles from the given URL and performed text analysis to compute variables. Used articles from Hindustan Times as the dataset": "https://github.com/prak12g/Data-Extraction-and-Textual-Analysis.git",
    "☞ Hindi Subtitles Generation: Generated a SRT file for a Hindi video clip using ML": "https://github.com/prak12g/Hindi-Subtitles-Generation-Using-WhisperAI.git",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

def get_rounded_image(image):
    profile_pic1 = Image.open(image)
    mask = Image.new('L',profile_pic1.size,0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0)+profile_pic1.size,fill=255)
    masked_img = ImageOps.fit(profile_pic1, mask.size, centering=(0.5, 0.5))
    masked_img.putalpha(mask)
    return masked_img


selected = option_menu(
    menu_title = None,
    options = ["Home","Projects"],
    icons=["house","book"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
if selected == "Home":
# --- LOAD CSS, PDF & PROFIL PIC ---
    profile_pic1 = get_rounded_image(profile_pic)
   # mask = Image.new('L',profile_pic1.size,0)
   # draw = ImageDraw.Draw(mask)
   # draw.ellipse((0,0)+profile_pic1.size,fill=255)
    #masked_img = ImageOps.fit(profile_pic1, mask.size, centering=(0.5, 0.5))
    #masked_img.putalpha(mask)

# --- HERO SECTION ---
    col1, col2 = st.columns(2)
    with col1:
        st.image(profile_pic1,width = 238)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

 #--- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

# --- SKILLS ---
    st.write('\n')
    #st.subheader("<div style='text-align: center;'>This is a subheader aligned to center</div>",unsafe_allow_html=True)
    st.subheader("Skills Summary")
    st.write("---")
    st.write(
    """
- 👩‍💻 Languages: Python, C++ , JAVA , HTML , Kotlin, MySQL , Arduino
- 📊 Frameworks/Libraries: Scikit, OpenCV , Pytorch , Streamlit , Pandas, Keras , Matplotlib
- 📚 Platforms: Linux, Windows, Raspberry Pi
- 🗄️ Soft Skills: Leadership, Public Speaking, Problem Solving , Teamwork
"""
)
# --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Work Experiences")
    st.write("---")

# --- JOB 1
    st.write("🚧", "**Club Head - (Co-Founder) | Roboverse (Robotics Club)**")
    st.write("08/2022 - Present")
    st.write(
    """
- ► Lakshmanrekha: Organised the Line Following Robot Competition for 1st - 3rd Year students
- ► Workhop Orientation: Organised and conducted 3 sessions on ’Introduction to Robotics’ and its programming. Furthermore, conducted sessions on different types of sensors and the science behind them, along with the application and uses
""" 
    )

# --- JOB 2
    st.write('\n')
    st.write("🚧", "**Robotics Researcher | Deepfield Robotics**")
    st.write("08/2021 - 08/2022")
    st.write(
    """
- ► Matlab: Created the Control Loop in simulink
- ► OpenCv: Developed a vision-based targeting system for laser weeding for mobile robots using a visual servoing approach for continuous laser weeding
- ► Electronics: Created a test-bed combining circuits and hardware; coordinated with team members and communicated with the client in Germany
"""
    )

# --- JOB 3
    st.write('\n')
    st.write("🚧", "**Biodiesel Researcher Intern | Neutral Fuels**")
    st.write("07/2017")
    st.write(
    """
    - ► Experiment Conducted: Used ’Anion Exchanged Resin’ to help reduce the ’Free Fatty Acid’ (FFA%) in bio-diesel and presented my findings to the company executives
"""
    )
if selected =="Projects":
# --- Projects & Accomplishments ---
    st.write('\n')
    st.header(f"[{'RoboCon 2022'}]({'https://drive.google.com/drive/folders/16xGjY5oiOvtP1F6ZtGaT-ZZJrx2BYRa5'})")
    c1,c2 = st.columns(2,gap="small")
    with c1:
        st.image(get_rounded_image(robo2_pic),width = 280)
    with c2:
        for i in range(6):
            st.write('\n')
        st.write("<div style='text-align: center;'>Created 2 robots to play the game Lagori for the Robotics Competition held by IIT Delhi.</div>", unsafe_allow_html=True)
        st.write('\n')
        st.write("<div style='text-align: center;'>Tech : Raspberrypi , Arduino. </div>", unsafe_allow_html=True)
    st.write('\n')
    st.write("---")
    st.header(f"[{'Stock Market Prediction'}]({'https://github.com/prak12g/Stock-Market-Prediction-Using-ML.git'})")
    c1,c2 = st.columns(2)
    with c1:
        stock_pic = Image.open(stock_pic)
        resized_im = stock_pic.resize((round(stock_pic.size[0]*1), round(stock_pic.size[1]*1.3)))
        st.image(resized_im,width = 320)
    with c2:
        for i in range(2):
            st.write('\n')
        st.write("<div style='text-align: center;'>Used LSTM machine learning model to predict Mahindra’s (MM) stock price.</div>", unsafe_allow_html=True)
        st.write('\n')
        st.write("<div style='text-align: center;'>Library Used: TensorFlow , Python , Keras , Pandas </div>", unsafe_allow_html=True)
    st.write('\n')
    st.write("---")
    st.header(f"[{'Data Extraction and Text Analysis'}]({'https://github.com/prak12g/Data-Extraction-and-Textual-Analysis.git'})")
    c1,c2 = st.columns(2)
    with c1:
        data_pic = Image.open(data_pic)
        st.image(data_pic,width = 320)
       # resized_im = stock_pic.resize((round(stock_pic.size[0]*1), round(stock_pic.size[1]*1.3)))
    with c2:
        for i in range(4):
            st.write('\n')
        st.write("<div style='text-align: center;'>Extracted textual data articles from the given URL and performed text analysis to compute variables. Used articles from Hindustan Times as the dataset.</div>", unsafe_allow_html=True)
        st.write('\n')
        st.write("<div style='text-align: center;'>Library Used: BeautifulSoup , nltk, csv , Pandas , requests </div>", unsafe_allow_html=True)
    st.write('\n')
    st.write("---")
    st.header(f"[{'Hindi Subtitles Generation'}]({'https://github.com/prak12g/Hindi-Subtitles-Generation-Using-WhisperAI.git'})")
    c1,c2 = st.columns(2)
    with c1:
        subtitle_pic = Image.open(subtitle_pic)
        resized_im = subtitle_pic.resize((round(subtitle_pic.size[0]*1), round(subtitle_pic.size[1]*1.5)))
        st.image(resized_im,width=320)
    with c2:
        for i in range(3):
            st.write('\n')
        st.write("<div style='text-align: center;'> Generated a SRT file for a Hindi video clip using ML </div>", unsafe_allow_html=True)
        st.write('\n')
        st.write("<div style='text-align: center;'>Library Used: Whisper , OS , Subprocess </div>", unsafe_allow_html=True)
    st.write('\n')

    
