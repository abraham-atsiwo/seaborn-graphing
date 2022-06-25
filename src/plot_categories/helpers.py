from inspect import isfunction
from streamlit import session_state, expander
from inspect import signature  
from itertools import islice
from components.components_parameters import  get_columns
from plot_categories.seaborn_plot_functions import plot_type_based_on_category
from components.components_parameters import widget_plot_type_parameters
from components.shared_component import text_input

# order_dict = {'row_order':'row_key', 
#               'col_order':'col_key', 
#               'hue_order': 'hue_key', 
#               'size_order': 'size_key', 
#               'style_order':'style_key'
# }

# widget_keys = list(widget_plot_type_parameters.keys())
# multiselect_labels_with_categorical = ['hue_order', 'row_order', 'col_order', 'size_order', 'style_order']  
#                                                 #values can be inferred to order_dict by
#                                                 #values populated by categorical variable or numeric with less uniques values
# select_labels_with_colnames = ['hue', 'row', 'col', 'size', 'style', 'units', 'x_partial', 'y_partial'] 
#                                                 #select boxes with values set to column names
# mixed_select_with_options = ['ci', 'x_ci'] #provides options for the user to enter values. Used with select boxes
# multiselect_with_colnames = ['x_vars', 'y_vars', 'vars']


def plot_function_signature(func:callable, exception_pars:str=['kwargs'])->list:
    """_summary_
        returns a list containing parameters to a specified function
    Args:
        func (callable): _description_
        exception_pars (str, optional): _description_. Defaults to ['kwargs'].

    Returns:
        list: _description_
    """
    args_list = list(signature(func).parameters.keys())
    for par in exception_pars:
        if par in args_list:
            args_list.remove(par)
    return args_list

def toggled_input_base_on_label(label:str, plot_type_func:callable)->bool:
    args_list = plot_function_signature(plot_type_func)
    label = label.replace(' ', '_').lower()
    if label not in args_list:
        return True 
    return False


def intersection(lst1:list, lst2:list)->list:
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3

def categorical_variable_levels(df_key:str, 
                                type_key:str, 
                                data_type_to_check:list,
                                initial_list:list,
    )->list:
    """_summary_
        levels of a categorical variable or a numeric varialbe with levels less than a given threshold: less than 10 in this case.
    Args:
        df_key (_type_, optional): _description_. Defaults to str.
        type_key (_type_, optional): _description_. Defaults to str.
        data_type_to_check (list, optional): _description_. Defaults to ['category', 'object'].
        initial_list (list, optional): _description_. Defaults to [].

    Returns:
        list: _description_
    """
    df = session_state[df_key]
    if type_key in session_state:
        if session_state[type_key] is not None:
            type_var = session_state[type_key]
            dtype = df[type_var].dtypes.name #Get unique values for a categorical variable
            if dtype is not None:
                if dtype in data_type_to_check:
                    initial_list = list(df[type_var].unique())
                    if None in initial_list:
                        initial_list.remove(None)
                    return initial_list
                else:
                    # Get unique values for numeric value and 
                    tmp_list = set(df[type_var])
                    if len(tmp_list) <= 10: 
                        return tmp_list 
    return initial_list


def plot_parameters_in_list(category_type:str, 
                            chunk_size_key:str, 
                            widget_keys:dict, 
                            model_parameters:str
    )->list[list]:
    """_summary_
        parameters of a function in a given given splitted into chunks of chunksize
    Args:
        category_type (str): _description_
        chunk_size_key (str, optional): _description_. Defaults to 'chunk_size_key'.
        widget_keys (dict, optional): _description_. Defaults to widget_keys.
        model_parameters (str, optional): _description_. Defaults to 'model_parameters'.

    Returns:
        list[list]: _description_
    """
    chunk_size = session_state[chunk_size_key]
    plot_type = plot_type_based_on_category[category_type]  #plot category type
    pars = plot_function_signature(plot_type) #signature from function
    func_pars_in_widgets = intersection(widget_keys, pars) #parameters in list
    session_state[model_parameters] = func_pars_in_widgets #set model parameters in session
    n = len(func_pars_in_widgets)
    chunk_size = int(session_state.chunk_size_key)
    if chunk_size < n:
        m = n // chunk_size
        split_list = [chunk_size]*int(m)
        split_list.extend([n-len(split_list)])
        temp = iter(func_pars_in_widgets)
        chunked_list = [list(islice(temp, 0, ele)) for ele in split_list] #split list into chunks
    else: 
        chunked_list = [func_pars_in_widgets]
    return chunked_list


def component_select(lbl:str, widget_plot_type_parameters:dict):
    label_details = widget_plot_type_parameters.get(lbl)
    parameters = label_details['pars']
    input_type = label_details['input_type']
    parameters['options'] = get_columns()
    input_type(**parameters)

def component_multiselect_with_colnames(lbl:str, widget_plot_type_parameters:dict):
    label_details = widget_plot_type_parameters.get(lbl)
    parameters = label_details['pars']
    input_type = label_details['input_type']
    options = get_columns()[1:]
    parameters['options'] = options
    parameters['default'] =  options[:4] if len(options) > 4 else options
    input_type(**parameters)

def component_multiselect(lbl:str, categorical_function_kwargs:dict, widget_plot_type_parameters:dict, order_dict:dict):
    key = order_dict[lbl]
    categorical_function_kwargs['type_key'] = key
    label_details = widget_plot_type_parameters.get(lbl)
    parameters = label_details['pars']
    input_type = label_details['input_type']
    options = categorical_variable_levels(**categorical_function_kwargs)
    parameters['options'] = options
    parameters['default'] = options
    input_type(**parameters)
 
def component_others(lbl:list, widget_plot_type_parameters:dict):
    label_details = widget_plot_type_parameters.get(lbl)
    parameters = label_details['pars']
    input_type = label_details['input_type']
    input_type(**parameters)
    label = parameters['label']
    if label in ['hue_norm', 'sizes', 'size_norm']:
        tmp_label = 'hue' if label == 'hue_norm' else 'size'
        if session_state[tmp_label+'_key'] is not None:
            if session_state[label+'_key'] == 'enter tuple':
                if session_state['dtypes_key'][session_state[tmp_label+'_key']] not in ['object', 'category']:
                    text_input(label=label+'_low', value = 0)
                    text_input(label=label+'_high', value = 20)
    
     
def component_mixed_input(lbl:list, widget_plot_type_parameters:dict):
    label_details = widget_plot_type_parameters.get(lbl)
    parameters = label_details['pars']
    input_type = label_details['input_type']
    lbl_key = parameters['key']
    value_to_trigger_widget = label_details['mixed_pars']['value_to_trigger_another_widget']
    input_type(**parameters)
    if session_state[lbl_key] == value_to_trigger_widget:
        mixed_input = label_details['mixed_pars']
        pars = mixed_input['pars']
        input_val = mixed_input['input_type']
        input_val(**pars)


def generate_multiple_input(labels:list, 
                            toggle_expander_key:str, 
                            categorical_function_kwargs:dict = {},
                            multiselect_labels_with_categorical:list = [],
                            select_labels_with_colnames:list = [],
                            mixed_select_with_options:list = [],
                            multiselect_with_colnames:list = [],
                            widget_plot_type_parameters:dict = {},
                            order_dict:dict = {}
    ):
    toggle_expander = session_state[toggle_expander_key]
    def display():
        for lbl in labels:
            if lbl in multiselect_labels_with_categorical:
                component_multiselect(lbl, categorical_function_kwargs, widget_plot_type_parameters, order_dict)
                # lbl_name = lbl.replace(' ', '_')
            elif lbl in select_labels_with_colnames:
                component_select(lbl, widget_plot_type_parameters)
            elif lbl in mixed_select_with_options: 
                component_mixed_input(lbl, widget_plot_type_parameters)
            elif lbl in multiselect_with_colnames:
                component_multiselect_with_colnames(lbl, widget_plot_type_parameters)
            else:
                component_others(lbl, widget_plot_type_parameters)
            session_state['parameters_key'][lbl] = session_state[lbl+'_key']

    if len(labels) > 0: 
        if toggle_expander:
            with expander(', '.join(labels)):
               display()
        else:
            display()     

def generate_components(in_list_kwargs:dict, 
                        validate_parameter_func:callable,
                        generate_multiple_input_kwargs:dict={}
    ):
    in_list_kwargs['category_type'] = session_state['plot_type_categories_key']
    chunked_list = plot_parameters_in_list(**in_list_kwargs)
    for label_list in chunked_list:
       generate_multiple_input_kwargs['labels'] = label_list
       generate_multiple_input(**generate_multiple_input_kwargs)
    if isfunction(validate_parameter_func):
        validate_parameter_func()