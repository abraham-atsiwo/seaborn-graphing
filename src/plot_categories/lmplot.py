from inspect import isfunction
from components.components_parameters import widget_plot_type_parameters
from plot_categories.helpers import plot_function_signature, plot_parameters_in_list, \
        categorical_variable_levels, component_select, plot_type_based_on_category, \
        component_multiselect, component_others, generate_multiple_input
from components.components_parameters import  get_columns
from data_and_constants.datasets import default_data_plot_categories as default_df
import streamlit as st
import seaborn as sns
from matplotlib.pyplot import subplots


order_dict = {'row_order':'row_key', 'col_order':'col_key', 'hue_order': 'hue_key', 
              'size_order': 'size_key', 'style_order':'style_key'}

widget_keys = list(widget_plot_type_parameters.keys())
                                
pars = {'type_key': 'x_key', 
        'data_type_to_check':'category', 
        'initial_list':[],
        'df_key':'df_key'
}

select_labels_with_colnames = ['hue', 'row', 'col', 'size', 'style', 'units', 'x_partial', 'y_partial']
multiselect_labels_with_categorical = ['hue_order', 'row_order', 'col_order']
order_keys = [val + '_key' for val in multiselect_labels_with_categorical]

def validate_parameter(order_keys=order_keys, col_wrap_key='col_wrap_key'):
    def order_parameters(key_label):
        if key_label in st.session_state:
            if len(st.session_state[key_label]) == 0:
                st.session_state['parameters_key'][key_label[:-4]] = None
            else:
                return 

    def col_wrap():
        if st.session_state[col_wrap_key] == 0:
            st.session_state['parameters_key']['col_wrap'] = None
        else:
            return 
    
    def ci():
        if 'ci_key' in st.session_state:
            if st.session_state['ci_key'] == 'float':
                if 'enter_ci_key' in st.session_state:
                    st.session_state['parameters_key']['ci'] = st.session_state['enter_ci_key']
                else:
                    st.session_state['parameters_key']['ci'] = st.session_state['ci_key'] 

    def palette():
        if 'palette_key' in st.session_state:
            st.session_state['parameters_key']['palette'] = sns.color_palette(st.session_state['palette_key'])

    result = list(map(order_parameters, order_keys))
    return result, col_wrap(), ci(), palette()


in_list_kwargs={'category_type': 'boxenplot', 'chunk_size': 3}
def lmplot_parameters(expander=True, 
                                in_list_kwargs = in_list_kwargs, 
                                categorical_function_kwargs=pars,
                                init_options = [], 
                                validate_parameter_func = validate_parameter
    ):
    in_list_kwargs['category_type'] = st.session_state['plot_type_categories_key']
    chunked_list = plot_parameters_in_list(expander=expander, **in_list_kwargs)
    for label_list in chunked_list:
       generate_multiple_input(label_list, expander, init_options, categorical_function_kwargs)
    if isfunction(validate_parameter_func):
        validate_parameter_func()


def lm_plot(pars):
    figure = sns.lmplot(**pars)
    st.pyplot(figure)
    #st.write(pars)



    

