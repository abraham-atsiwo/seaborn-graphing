
from streamlit import session_state 

def data_types(df_key='df_key', type_key='hue_key'):
    df = session_state.df_key
    # data_types = {df_col[j]:df[df_col[j]].dtypes.name for j in range(len(df_col))}
    if type_key in session_state:
        if session_state[type_key] is not None:
            type_var = session_state[type_key]
            dtype = df[type_var].dtypes.name
            if dtype == 'category':
                return list(df[type_var].cat.categories)
    return None


def axis_parameters():
    par = session_state['parameters_key']
    model_pars = session_state['model_parameters']
    pars = {key:par[key] for key in model_pars}
    if session_state.plot_type_key in ['Relational', 'Distribution', 'Categorical']:
        pars['kind'] = session_state['plot_type_categories_key'][:-4]
    pars['data'] = session_state['df_key']

    pars['y'] = session_state['y_key']
    pars['x'] = session_state['x_key']
    if session_state['plot_type_categories_key'] in ['countplot', 'histplot', 'ecdfplot', 'kdeplot']:
        if session_state['axis_type_key'] == 'x':
            pars['y'] = None
            pars['x'] = session_state['x_key']
        elif session_state['axis_type_key'] == 'y':
            pars['x'] = None
            pars['y'] = session_state['y_key']

    return pars 