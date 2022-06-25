from components.shared_component import selectbox
from streamlit import session_state, expander

theme = ['darkgrid', 'dark', 'white', 'whitegrid']     

def set_theme(toggle_expander_key:str='toggle_expander_key', 
            theme_name:str='set_theme'
    ):
    """_summary_

    Args:
        toggle_expander_key (str, optional): _description_. Defaults to 'toggle_expander_key'.
        theme_name (str, optional): _description_. Defaults to 'set_theme'.
    """
    toggle_expander = session_state[toggle_expander_key]
    if toggle_expander:
        with expander(theme_name):
            selectbox(label='theme', options=theme)
        return 
    selectbox(label='theme', options=theme)
