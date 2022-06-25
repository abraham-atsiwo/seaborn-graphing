from streamlit import session_state 
from body.helpers import axis_parameters 

def validate_scatter_parameters():
    pars = axis_parameters()
    markers_style_scatter = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
    if 'style_key' in session_state:
        if session_state['style_key'] is not None:
            if 'style_order_key' in session_state:
                if session_state['markers_key'] is not None:
                    n = len(session_state['style_order_key'])
                    marker_option = session_state['markers_key']
                    from random import sample
                    pars['markers'] = sample(markers_style_scatter, n)

    if 'hue_norm' in list(pars.keys()):
        if session_state['hue_key'] is not None:
            if 'hue_norm_low_key' in session_state:
                if session_state['hue_norm_key'] is not None:
                    if session_state['dtypes_key'][session_state['hue_key']] not in ['object', 'category']:
                        pars['hue_norm'] = (int(session_state['hue_norm_low_key']), int(session_state['hue_norm_high_key']))
                    else:
                        pars['hue_norm'] = None
                else:
                    pars['hue_norm'] = None
            else:
                pars['hue_norm'] = None


    if 'size' in list(pars.keys()):
        if session_state['size_key'] is not None:
            if 'sizes_low_key' in session_state:
                if session_state['sizes_key'] is not None:
                    if session_state['dtypes_key'][session_state['size_key']] not in ['object', 'category']:
                        pars['sizes'] = (int(session_state['sizes_low_key']), int(session_state['sizes_high_key']))
                    else:
                        pars['sizes'] = None
                else:
                    pars['hue_norm'] = None
            else:
                pars['hue_norm'] = None

    if 'size' in list(pars.keys()):
        if session_state['size_key'] is not None:
            if 'size_norm_low_key' in session_state:
                if session_state['size_norm_key'] is not None:
                    if session_state['dtypes_key'][session_state['size_key']] not in ['object', 'category']:
                        pars['size_norm'] = (int(session_state['size_norm_low_key']), int(session_state['size_norm_high_key']))
                    else:
                        pars['size_norm'] = None
                else:
                    pars['size_norm'] = None
            else:
                pars['size_norm'] = None
    return pars