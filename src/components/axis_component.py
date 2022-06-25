import streamlit as st
from streamlit import expander, session_state
from components.help_docs import helps
from components.shared_component import selectbox, generate_multiple_input, radio_input

one_axis_plot = ['ecdfplot', 'countplot', 'histplot', 'kdeplot'] #figures that can be plotted on one axis only (x-axis or y-axis)
one_and_both_axis_plot = ['histplot', 'kdeplot'] #figures that can be plotted on both axis(x/y or x and y)
def disable_axis_for_one_dimensional_figure(axis_type_key:str, 
                                            axis_type_value:str,
                                            plot_type_categories_key = 'plot_type_categories_key'
    )->bool:
    """_summary_

    Args:
        axis_type_key (str): _description_
        axis_type_value (str): _description_
        plot_type_categories_key (str, optional): _description_. Defaults to 'plot_type_categories_key'.

    Returns:
        bool: _description_
    """
    if st.session_state[plot_type_categories_key] in one_axis_plot:
        val = st.session_state[axis_type_key]
        if st.session_state.axis_type_key == axis_type_value:
            return True
    return False

x_axis = {'label': 'x', 
        'options': [],
        'help': helps['x'],
        'disabled_func': disable_axis_for_one_dimensional_figure, 
            'args': ('axis_type_key', 'y', 'plot_type_categories_key'),    
            }
y_axis = {'label': 'y', 
            'options':[], 
            'help': helps['y'],
            'disabled_func': disable_axis_for_one_dimensional_figure, 
            'args': ('axis_type_key', 'x'),
            'kwargs': { 'index': 1}         
            }



axis_types = [selectbox, selectbox]
axis_types_pars = [x_axis, y_axis]

def axis(api_types=axis_types, 
        api_types_pars=axis_types_pars, 
        df_col_key = 'df_col_key',
        expander_label = 'axis',
        radio_input_label = 'axis type',
        radio_values = ('both', 'x', 'y'),
        plot_type_categories_key = 'plot_type_categories_key',
        options_name = 'options',
        toggle_expander_key='toggle_expander_key'
    ):
    """_summary_

    Args:
        api_types (_type_, optional): _description_. Defaults to axis_types.
        api_types_pars (_type_, optional): _description_. Defaults to axis_types_pars.
        df_col_key (str, optional): _description_. Defaults to 'df_col_key'.
        expander_label (str, optional): _description_. Defaults to 'axis'.
        radio_input_label (str, optional): _description_. Defaults to 'axis type'.
        radio_values (tuple, optional): _description_. Defaults to ('both', 'x', 'y').
        plot_type_categories_key (str, optional): _description_. Defaults to 'plot_type_categories_key'.
        options_name (str, optional): _description_. Defaults to 'options'.
        toggle_expander_key (str, optional): _description_. Defaults to 'toggle_expander_key'.
    """
    toggle_expander = session_state[toggle_expander_key]
    axis_types_pars[0][options_name] = session_state[df_col_key]
    axis_types_pars[1][options_name] = session_state[df_col_key]
    if toggle_expander:
        with expander(expander_label):
            if session_state[plot_type_categories_key] in one_axis_plot:
                opt_values = radio_values
                if session_state[plot_type_categories_key] in one_and_both_axis_plot:
                    opt_values = radio_values
                elif session_state[plot_type_categories_key] in one_axis_plot:
                    opt_values = radio_values[1:]
                radio_input(label=radio_input_label, options=opt_values, index=1)
            generate_multiple_input(api_types, api_types_pars)
    else:
        generate_multiple_input(api_types, api_types_pars)

    

    