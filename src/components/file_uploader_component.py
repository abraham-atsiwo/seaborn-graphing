from streamlit import session_state, expander
from components.shared_component import file_uploader, selectbox
from components.helpers import toggle_disabled
from data_and_constants.constants import file_extensions
from data_and_constants.datasets import default_data_plot_categories as default_df

use_data = {'label': 'data_type', 
            'options': ['default data', 'upload file'],
} 
file_ext = {'label': 'file_extension', 
            'options': file_extensions,
            'disabled_func': toggle_disabled,
            'args': ('data_type_key', 'default_data')
}
file = {'label': 'upload_file', 
        'type': file_extensions, 
        'file_key': 'file_extension_key',
        'disabled_func': toggle_disabled,
        'args': ('data_type_key', 'default_data')
}

api_types = [selectbox, selectbox, file_uploader]
api_types_pars = [use_data, file_ext, file]


def file_uploader_data_type(api_types:list=api_types, 
                            api_types_pars:list[dict]=api_types_pars, 
                            toggle_expander_key='toggle_expander_key',
                            expander_label = 'data options'
    ):
    """_summary_

    Args:
        api_types (list, optional): _description_. Defaults to api_types.
        api_types_pars (list[dict], optional): _description_. Defaults to api_types_pars.
        toggle_expander_key (str, optional): _description_. Defaults to 'toggle_expander_key'.
        expander_label (str, optional): _description_. Defaults to 'data options'.
    """
    toggle_expander = session_state[toggle_expander_key]
    if toggle_expander:
        with expander(expander_label):
            for j in range(len(api_types)):
                api_types[j](**api_types_pars[j])
    else:
        for j in range(len(api_types)):
            api_types[j](**api_types_pars[j])
    

    
    
    
  
    

