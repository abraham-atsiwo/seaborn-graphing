
from components.components_parameters import regression_widgets as widget_plot_type_parameters
from plot_categories.helpers import generate_components
from data_and_constants.datasets import default_data_plot_categories as default_df
from matplotlib.pyplot import subplots
from seaborn import regplot, residplot, lmplot, color_palette
from streamlit import session_state, pyplot

                                
categorical_pars = {'type_key': 'x_key', 
        'data_type_to_check':'category', 
        'initial_list':[],
        'df_key':'df_key'
}

order_dict = {'row_order':'row_key', 
              'col_order':'col_key', 
              'hue_order': 'hue_key', 
              'size_order': 'size_key', 
              'style_order':'style_key'
}

widget_keys = list(widget_plot_type_parameters.keys())
multiselect_labels_with_categorical = ['hue_order', 'row_order', 'col_order', 'size_order', 'style_order']  
                                                #values can be inferred to order_dict by
                                                #values populated by categorical variable or numeric with less uniques values
select_labels_with_colnames = ['hue', 'row', 'col', 'size', 'style', 'units', 'x_partial', 'y_partial'] 
                                                #select boxes with values set to column names
mixed_select_with_options = ['ci', 'x_ci'] #provides options for the user to enter values. Used with select boxes
multiselect_with_colnames = ['x_vars', 'y_vars', 'vars']
multiselect_labels_with_categorical = [] 
order_keys = [val + '_key' for val in multiselect_labels_with_categorical]

generate_multiple_input_kwargs = {
    'labels':[], 
    'toggle_expander_key':'toggle_expander_key', 
    'categorical_function_kwargs':categorical_pars,
    'multiselect_labels_with_categorical':multiselect_labels_with_categorical,
    'select_labels_with_colnames':select_labels_with_colnames,
    'mixed_select_with_options':mixed_select_with_options,
    'multiselect_with_colnames':multiselect_with_colnames,
    'widget_plot_type_parameters':widget_plot_type_parameters,
    'order_dict': order_dict
}

def validate_parameter(order_keys=order_keys, col_wrap_key='col_wrap_key'):
    def order_parameters(key_label):
        if key_label[:-4] in session_state['parameters_key'].keys():
            if key_label in session_state:
                if len(session_state[key_label]) == 0:
                    session_state['parameters_key'][key_label[:-4]] = None
                else:
                    return 

    def col_wrap():
        if 'col_wrap_key' in session_state:
            if session_state[col_wrap_key] == 0:
                session_state['parameters_key']['col_wrap'] = None
            else:
                return 
    
    def ci():
        if 'ci_key' in session_state:
            if session_state['ci_key'] == 'float':
                if 'enter_ci_key' in session_state:
                    session_state['parameters_key']['ci'] = session_state['enter_ci_key']
                else:
                    session_state['parameters_key']['ci'] = session_state['ci_key'] 

    def palette():
        if 'palette_key' in session_state:
            session_state['parameters_key']['palette'] = color_palette(session_state['palette_key'])

    result = list(map(order_parameters, order_keys))
    return result, col_wrap(), ci(), palette()


in_list_kwargs={'category_type': 'boxenplot', 'chunk_size_key': 'chunk_size_key', 
                'widget_keys': widget_keys, 'model_parameters': 'model_parameters'
}

def regression_parameters(in_list_kwargs = in_list_kwargs, 
                        validate_parameter_func = validate_parameter,
                        generate_multiple_input_kwargs=generate_multiple_input_kwargs
    ):
    generate_components(in_list_kwargs, validate_parameter_func, generate_multiple_input_kwargs)

def lm_plot(pars):
    figure = lmplot(**pars)

    
def reg_plot(pars):
    fig, ax = subplots()
    regplot(**pars, ax=ax)
    pyplot(fig)
    
def resid_plot(pars):
    fig, ax = subplots()
    residplot(**pars, ax=ax)
    pyplot(fig)



    

