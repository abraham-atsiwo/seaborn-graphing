
from streamlit import session_state
from data_and_constants.datasets import default_data_plot_categories as default_df
  
state_initialization = {'plot_type_key': 'Relational', 
                        'data_type_key': 'default data',
                        'plot_type_categories_key': 'scatterplot',
                        'df_col_key': default_df['scatterplot'].columns,
                        'parameters_key': {},
                        'axis_type_key': 'x',
                        'dtypes_key': None,
                        'col_key': default_df['scatterplot'].columns,
                        'chunk_size_key': 3,
                        'model_parameters': {},
                        'hue_key': None,
                        'toggle_expander_key': True,
}

def set_initial_state_values(**kwargs):
    for key, values in kwargs.items():
        if key not in session_state:
            session_state[key] = values


