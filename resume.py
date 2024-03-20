import streamlit as st
from streamlit_option_menu import option_menu
from streamlit import image
from PIL import Image




st.set_page_config(page_title="My Resume",page_icon=":wave:",layout="wide")


#im1 = st.image(C:\Users\hp\OneDrive\Documents\Downloads\FullSizeRender.jpg)

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu(menu_title = "Skill", options=["Manual Testing", "SQL", "Python"], icons=["", "database", ""], menu_icon="cast", default_index=0)

if selected == "Intro":
        st.write(f"Welcome to my resume web page :wave: {selected}")
if selected == "Project":
        st.title(f"You have Selected {selected}")
if selected == "Contact":
        st.title(f"You have Selected {selected}")


st.write("---")
#header section
st.title("Pramod Choukidar")
#st.subheader("")
st.markdown("8788283992 || pramodchoukidar@gmail.com || pramod.choukidar@mit.asia || (MH) INDIA")



st.write('''Dedicated and results-driven PG degree holder in Master of Computer Applications (MCA),
          certified in Software Testing,
          eager to leverage expertise and skills in testing methodologies to contribute to your esteemed organization.
          With a keen eye for detail and a commitment to excellence,
          I am adept at identifying and rectifying software defects,
          ensuring the delivery of high-quality products.
          My proactive approach as a smart worker,
          coupled with a strong work ethic as a hard worker,
          enables me to effectively streamline processes,
          reducing both time and costs for the company.
          I am enthusiastic about joining a dynamic team where I can apply my quality assurance skills to drive success and achieve mutual growth,
          while also seeking opportunities for personal and professional development.''')
st.write("""
●Knowledge of Software testing principles, SDLC, Levels of Testing, Types of Testing.
         
●Knowledge of Writing Test Documents, Review and Executing Test Documents, Defect Tracking Tool.
         
●Good knowledge of writing SQL queries practiced extensively on SQL Server Express Edition Database. 
         
●Knowledge on Creating Selenium Test Cases using Element Locators and WebDriver methods.
         
●Expertise in Python Programming Fundamentals, and Database Fundamentals. 
         
●Should have good coordination with the team. 
         
●Ability to write test scenarios, test cases, prepare test suits, run, and generate test reports. 
         
●Having understanding of programming concepts packages, module, library, oops etc.
         """)

st.write("---")
#what i do

with st.container():
    st.write("This have an container part")



st.write("---")

#Highlights

with st.container():
    left_column, center_column, right_column = st.columns(3)
with left_column:
    st.write("This have an container part")
with right_column:
    st.write("this is right place :smile:")

with center_column:
    st.write("This is centre of :wave:")

st.write("---")

#Copyrights / mail
with st.container():
    left_column, center_column, right_column = st.columns(3)
with left_column:
    st.write("")
with right_column:
    st.write("")
with center_column:
    st.markdown("https://linkedin.com/pramod-c-")

