from streamlit import session_state, expander, write
from components.shared_component import selectbox
from data_and_constants.datasets import default_data_plot_categories as default_df, plot_type_categories



def plt_type_category_on_change(parameters_key:str='parameters_key', 
                                col_wrap_key:str='col_wrap_key', 
                                col_wrap_label:str='col_wrap'
    ):
    """_summary_
        Set certain parameters to their default values.
    Args:
        parameters_key (str, optional): _description_. Defaults to 'parameters_key'.
        col_wrap_key (str, optional): _description_. Defaults to 'col_wrap_key'.
        col_wrap_label (str, optional): _description_. Defaults to 'col_wrap'.
    """
    from copy import copy
    session_state[col_wrap_key] = 0
    session_state[parameters_key][col_wrap_label] = 0
    pars = session_state['parameters_key']
    tmp_pars = copy(pars)
    for key, val in tmp_pars.items():
        if key+'_key' in session_state:
            if key in ['hue', 'row', 'col', 'size', 'style', 'hue_norm', 'size_norm']:
                pars[key] = None

    write(session_state['plot_type_key'])

plt_type = {'label': 'Plot type', 
            'options': list(plot_type_categories.keys()),
            # 'kwargs': {'on_change': plt_type_category_on_change, 
            #            'kwargs': {'parameters_key':'parameters_key'
            #         }
            # }
}

plt_type_cat = {'label': 'plot type categories', 
                'options': None,
                'kwargs': {'on_change': plt_type_category_on_change, 
                           'kwargs': {'parameters_key':'parameters_key'}
                }
}

def plot_type_category(plt_type=plt_type, 
                    plt_type_cat=plt_type_cat, 
                    toggle_expander_key='toggle_expander_key',
                    plot_type_key='plot_type_key',
                    expander_label='plot type and plot categories'
    ):
    """_summary_

    Args:
        plt_type (_type_, optional): _description_. Defaults to plt_type.
        plt_type_cat (_type_, optional): _description_. Defaults to plt_type_cat.
        toggle_expander_key (str, optional): _description_. Defaults to 'toggle_expander_key'.
        plot_type_key (str, optional): _description_. Defaults to 'plot_type_key'.
        expander_label (str, optional): _description_. Defaults to 'plot type and plot categories'.
    """
    toggle_expander = session_state[toggle_expander_key]
    if toggle_expander:
        with expander(expander_label):
            selectbox(**plt_type)
            plt_type_cat['options'] = plot_type_categories[session_state.plot_type_key]
            selectbox(**plt_type_cat)
    else:
        selectbox(**plt_type)
        plt_type_cat['options'] = plot_type_categories[session_state.plot_type_key]
        selectbox(**plt_type_cat)