import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Growth Mindset Challenge",page_icon=":hello:",layout="wide")



st.header("Set your learning goals")   
goal =st.text_input("what is your learning goal for today?")
if goal:
    st.write(f"Great you're working on:(goal)")

st.header("Reflect on your learning")
reflection = st.text_area("what did you learn today?")
if reflection:
    st.write("Thank you for reflecting: Keep up the good work.")

st.header("seek feedback")
feedback = st.text_area("what feedback have you receive recently?")
if feedback:
    st.write("use this feedback to improve and grow!")

st.header("Daily Motivation")
st.write("Here's a motivational quote to keep you going:")
st.write("> The only limit to our realization of tomorrow is our doubts of today.")

st.write("---")
st.write("Built with using streamlit")