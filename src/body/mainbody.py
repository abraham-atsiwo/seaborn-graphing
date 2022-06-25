from plot_categories.seaborn_plot_functions import plot_type_based_on_category as custom_plot_type_category
from streamlit import session_state, pyplot, subheader, expander, dataframe, spinner
from body.validate_parameters import validate_scatter_parameters
from seaborn import set_theme
import seaborn as sns
from matplotlib.pyplot import subplots
from body.helpers import axis_parameters


def plot_parameters():
    # pars = axis_parameters()
    if session_state['plot_type_key'] in ['Relational', 'Distribution', 'Categorical']:
       pars = validate_scatter_parameters()
    if session_state['plot_type_key'] in ['Jointplot']:
        pars = validate_scatter_parameters()
        pars['kind'] = session_state['plot_type_categories_key']
    if session_state['plot_type_key'] in ['Pairplot']:
        pars = validate_scatter_parameters()
        pars['kind'] = session_state['plot_type_categories_key'][:-8]
        del pars['x']; del pars['y']
    elif session_state['plot_type_key'] in ['Matrixplot']:
        pars = validate_scatter_parameters()
        del pars['x']; del pars['y']
    else:
        pars = validate_scatter_parameters()
    return pars

def get_data():
    df = session_state['df_key']
    # subheader('Description')
    with expander('Data'):
        dataframe(df.head())

def display_plot(plot_type_categories_key='plot_type_categories_key'):
    plot_type = session_state[plot_type_categories_key]
    pars = plot_parameters()
    if plot_type in ['regplot', 'residplot', 'heatmap']:
        fig, ax = subplots()
        ax = custom_plot_type_category[plot_type](**pars)
        pyplot(fig)
    else:
        fig = custom_plot_type_category[plot_type](**pars)
        pyplot(fig)
    return pars

def mainbody_index():
    set_theme(style=session_state['theme_key'])
    get_data()
    with spinner("Please wait: updating plot with new data..."):
        display_plot()
   
