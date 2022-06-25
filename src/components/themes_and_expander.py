from components.shared_component import number_input, selectbox, radio_input
from streamlit import session_state, expander

themes = ['darkgrid', 'dark', 'white', 'whitegrid']     

def set_theme(expander_key:str='toggle_expander_key', 
            label:str='set_theme', 
            selbox_label:str='theme', 
            selbox_options:list=themes
    ):
    """_summary_

    Args:
        expander_key (str, optional): _description_. Defaults to 'toggle_expander_key'.
        label (str, optional): _description_. Defaults to 'set_theme'.
        selbox_label (str, optional): _description_. Defaults to 'theme'.
        selbox_options (list, optional): _description_. Defaults to theme.
    """
    toggle_expander=session_state[expander_key]
    if toggle_expander:
        with expander(label):
            selectbox(label=selbox_label, 
                    options=selbox_options)
            return 
        selectbox(label=selbox_label, options=selbox_options)

def toggle_expander(expander_key:str='toggle_expander_key', 
                    expander_label:str='expander and chunk size',
                    radio_label:str='toggle expander',
                    chunk_size_label:str='chunk_size',
                    chunk_size_key:str='chunk_size_key'
    ):
    """_summary_

    Args:
        expander_key (str, optional): _description_. Defaults to 'toggle_expander_key'.
        expander_label (str, optional): _description_. Defaults to 'expander and chunk size'.
        radio_label (str, optional): _description_. Defaults to 'toggle expander'.
        chunk_size_label (str, optional): _description_. Defaults to 'chunk_size'.
        chunk_size_key (str, optional): _description_. Defaults to 'chunk_size_key'.
    """
    toggle_expander_key = session_state[expander_key]
    def _toggle_expander():
        radio_input(label=radio_label, 
                    options=(True, False), 
                    index=0, 
                    key=expander_key
        )
        if toggle_expander_key:
            number_input(label=chunk_size_label, 
                        min_value=1, 
                        max_value=5, 
                        step=1, 
                        value=3,
                        key=chunk_size_key
            ) 
    with expander(expander_label):
            _toggle_expander()



