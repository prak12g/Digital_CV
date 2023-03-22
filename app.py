from pathlib import Path

import streamlit as st
from PIL import Image

#---Path Settings---
current_dir = Path(__file__).parent #if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "Resume_Prakhar.pdf"
profile_pic = current_dir / "Profile_Pic.jpg"

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
}
PROJECTS = {
    "🏆 RoboCon 2022 - Created 2 robots to play the game Lagori for the Robotics Competition held by IIT Delhi. Tech : Raspberrypi , Arduino ": "https://drive.google.com/drive/folders/16xGjY5oiOvtP1F6ZtGaT-ZZJrx2BYRa5",
    "🏆 Stock Market Prediction: Used LSTM machine learning model to predict Mahindra’s (MM) stock price. Tech: TensorFlow, Python, Keras, Pandas": "https://github.com/prak12g/Stock-Market-Prediction-Using-ML.git",
    "🏆 Data Extraction and Text Analysis: Extracted textual data articles from the given URL and performed text analysis to compute variables. Used articles from Hindustan Times as the dataset": "https://github.com/prak12g/Data-Extraction-and-Textual-Analysis.git",
    "🏆 Hindi Subtitles Generation: Generated a SRT file for a Hindi video clip using ML": "https://github.com/prak12g/Hindi-Subtitles-Generation-Using-WhisperAI.git",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

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

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- SKILLS ---
st.write('\n')
st.subheader("Skills Summary")
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

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")