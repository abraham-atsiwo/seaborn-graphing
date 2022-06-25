from streamlit import session_state
from pandas import DataFrame
from components.file_uploader_component import file_uploader_data_type
from components.plot_type_category_component import plot_type_category
from data_and_constants.datasets import default_data_plot_categories as default_df
from utilities.session_initialization import set_initial_state_values, state_initialization
from components.themes_and_expander import set_theme, toggle_expander

init_pars = {'data_type_key': 'default_data', 
            'plot_type_categories_key': 'scatterplot'
}
update_data_pars = {'data_type_value': 'default data', 
                    'data_type_key': 'data_type_key',
                    'df_key': 'df_key', 
                    'df_col_key': 'df_col_key', 
                    'plot_type_categories_key': 'plot_type_categories_key', 
                    'df': default_df
}

def get_data(data_type_value:str, 
            data_type_key:str, 
            df_key:str, 
            df_col_key:str, 
            plot_type_categories_key:str, 
            df:DataFrame 
    ):
    """_summary_

    Args:
        data_type_value (str): _description_
        data_type_key (str): _description_
        df_key (str): _description_
        df_col_key (str): _description_
        plot_type_categories_key (str): _description_
        df (DataFrame): _description_
    """
    if session_state[data_type_key] == data_type_value:
        session_state[df_key] = df[session_state[plot_type_categories_key]]
        session_state[df_col_key] = df[session_state[plot_type_categories_key]].columns

def data_types(df_key:str='df_key', 
            dtypes_key:str='dtypes_key'
    ):
    """_summary_

    Args:
        df_key (str, optional): _description_. Defaults to 'df_key'.
        dtypes_key (str, optional): _description_. Defaults to 'dtypes_key'.
    """
    df = session_state.df_key
    df_col = df.columns
    data_types = {df_col[j]:df[df_col[j]].dtypes.name for j in range(len(df_col))}
    session_state.dtypes_key = data_types

def sidebar_index():
    set_initial_state_values(**state_initialization)
    toggle_expander()
    file_uploader_data_type()
    plot_type_category()
    get_data(**update_data_pars)
    data_types()

    
    




