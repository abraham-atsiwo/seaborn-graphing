from streamlit import set_page_config, write, sidebar, columns, subheader, balloons, container, button, download_button, pyplot, markdown
from sidebar.sidebar_main import sidebar_index
from body.sidebarbody import sidebarbody_index
from body.mainbody import mainbody_index
from css.style import index as css_main



set_page_config(page_title="Interactive Web Graphing", 
                   page_icon=None, 
                   layout="wide", 
                   initial_sidebar_state="auto", 
                   menu_items=None)

sidebarbody, mainbody = columns([1, 3])


# .element-container
def main():
    css_main()
    with sidebar:
        sidebar_index()
    with sidebarbody:
        sidebarbody_index()
    with mainbody:
        subheader('Web visualization based on the seaborn api.')
        mainbody_index()
        balloons()

        


if __name__  == '__main__':
    main()
    







