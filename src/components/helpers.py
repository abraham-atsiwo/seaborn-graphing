import streamlit as st
import string

def toggle_disabled(key, value):
    if value is not None:
        value = str(value).strip()
        value = value.replace(" ", "_").lower()
    if key in st.session_state:
        key_val = st.session_state[key]
        if isinstance(key_val, list):
            if len(key_val) > 0:
                key_val = key_val[0]
        key_val = str(key_val)
        key_val = key_val.replace(" ", "_").lower()
        
        if (key_val == value):
            return True 
    return False


def key_help_generator(label=None, key=None, help=None):
    label = label.replace(' ', '_')
    if key is None:
        tmp_key = label.translate({ord(c): None for c in string.whitespace}).lower()
        key = tmp_key + '_key'
    if help is None:
        help = label
    return key, help




