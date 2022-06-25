from components.shared_component import text_input
import streamlit as st

def title_xlab_ylab(expander=True):
    if expander:
        with st.expander("title, xlab, ylab"):
            text_input(label = 'title')
            text_input(label = 'xlabel')
            text_input(label = 'ylabel')
    else:
        text_input(label = 'title')
        text_input(label = 'xlabel')
        text_input(label = 'ylabel')