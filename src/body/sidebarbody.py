from streamlit import session_state
from components.axis_component import axis 
from components.themes import set_theme
from plot_categories.export_user_interface import display_components_to_screen
from plot_categories.title_xlab_ylab import title_xlab_ylab


def display_screen(plot_type_categories_key='plot_type_categories_key'):
    screen_type = session_state[plot_type_categories_key]
    display_components_to_screen[screen_type]()

def sidebarbody_index():
    axis()
    set_theme()
    display_screen()
    # title_xlab_ylab()
