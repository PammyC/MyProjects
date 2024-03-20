import streamlit as st
import tensorflow as tf
from streamlit_option_menu import option_menu
from tensorflow import image
st.set_page_config(page_title="My Resume",page_icon=":tada:",layout="wide")


im1 = tf.image("E:\StartUpWorld_Intern\MIT_logo.png")

st.write("---")



st.write("---")
#header section
st.title("Pramod Choukidar")
#st.subheader("streamlit option menu")
st.subheader("8788283992 || pramodchoukidar@gmail.com || (MH) INDIA")
st.markdown("https://linkedin.com/pramod-c-")

st.write("This section will have paragra[h and the] sentences")
st.write("place the hyperlinks here")
st.write("""""")

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
