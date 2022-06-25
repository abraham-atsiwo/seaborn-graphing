import streamlit as st 
import seaborn as sns
from inspect import isfunction
from components.helpers import key_help_generator
from data_and_constants.constants import file_extensions_func
# from plot_categories.seaborn_plot_functions import  plot_type_based_on_category



def selectbox(label, options, key=None, help=None, disabled_func=None, args=None, kwargs={}):
    disabled = False
    if isfunction(disabled_func):
        disabled = disabled_func(*args)
    key, help = key_help_generator(label, key, help)
    st.selectbox(label=label, options=options, key=key, help=help, disabled=disabled, **kwargs)

def text_input(label, value=None, key=None, help=None, disabled_func=None, args=None, kwargs={}):
    disabled = False
    if isfunction(disabled_func):
        disabled = disabled_func(*args)
    key, help = key_help_generator(label, key, help)
    st.text_input(label, value, key=key, help=help, disabled=disabled, **kwargs)

def number_input(label, min_value, max_value, value, step, key=None, help=None, disabled_func=None, args=None, kwargs={}):
    disabled = False
    if isfunction(disabled_func):
        disabled = disabled_func(*args)
    key, help = key_help_generator(label, key, help)
    st.number_input(label, min_value, max_value, value, step, key=key, help=help, disabled=disabled, **kwargs)

def radio_input(label, options, index, key=None, help=None, disabled_func=None, args=None, kwargs={}):
    disabled = False
    if isfunction(disabled_func):
        disabled = disabled_func(*args)
    key, help = key_help_generator(label, key, help)
    st.radio(label, options, index, key=key, help=help, disabled=disabled, **kwargs)

def multiselect(label, options, default=[], key=None, help=None, disabled_func=None, args=None, kwargs={}):
    disabled = False
    if isfunction(disabled_func):
        disabled = disabled_func(*args)
    key, help = key_help_generator(label, key, help)
    st.multiselect(label, options, default, key=key, help=help, disabled=disabled, **kwargs)

def color_picker(label, value=None, key=None, help=None, disabled_func=None, args=None, kwargs={}):
    disabled = False
    if isfunction(disabled_func):
        disabled = disabled_func(*args)
    key, help = key_help_generator(label, key, help)
    st.color_picker(label, value, key=key, help=help, disabled=disabled, **kwargs)


def file_uploader(label, type, key=None, help=None, default_df=None,
                  df_key=None, file_key=None, disabled_func=None, args=None, kwargs={}):   
    def func_uploaded_data(key_ext):
        file_ext = st.session_state[key_ext]
        for key, value in file_extensions_func.items():
            if file_ext == key:
                return value

    if default_df is not None:
        df = default_df['scatterplot']
    else:
        df = sns.load_dataset('tips')
    if df_key is None:
        df_key = 'df_key'
    df_col_key = df_key[:-3] + 'col_key'
    disabled = False
    if isfunction(disabled_func):
        disabled = disabled_func(*args)
    key, help = key_help_generator(label, key, help)
    if df_key not in st.session_state:
        st.session_state[df_key] = None
        st.session_state[df_col_key] = None
    file = st.file_uploader(label, type, key=key, help=help, disabled=disabled, **kwargs)
    if file:
        df = func_uploaded_data(file_key)(file)
    st.session_state[df_key] = df
    st.session_state[df_col_key] = df.columns 
    

def generate_multiple_input(api_types=[], pars_api_types=[{}]):
    n = len(api_types)
    for j in range(n):
        func = api_types[j]
        if isfunction(func):
            pars = pars_api_types[j]        
            func(**pars)
            lbl = pars['label']
            st.session_state['parameters_key'][lbl] = st.session_state[lbl+'_key']
            








