import streamlit as st
from components.shared_component import multiselect, number_input, radio_input, selectbox, color_picker, text_input

from components.helpers import toggle_disabled
from components.help_docs import helps
from data_and_constants.datasets import default_data_plot_categories as default_df


state_initialization = {'plot_type_key': 'Relational', 
                        'data_type_key': 'default data',
                        'plot_type_categories_key': 'scatterplot',
                        'df_col_key': default_df['scatterplot'].columns,
                        'parameters_key': {},
                        'row_key': None,
                        'col_key': None
                        }

def set_initial_values(**kwargs):
        for key, values in kwargs.items():
                if key not in st.session_state:
                        st.session_state[key] = values 

set_initial_values(**state_initialization)

def col_wrap_toggled_disabled(row_key, row_value_to_trigger_disable, col_wrap_key, col_value_to_trigger_disable):
        if row_key in st.session_state:
                row_value = st.session_state[row_key]
                col_value = st.session_state[col_wrap_key]
                if row_value != row_value_to_trigger_disable or col_value is col_value_to_trigger_disable:
                        return True
        return False

def row_on_change(row_key, col_wrap_key):
        if row_key in st.session_state and col_wrap_key in st.session_state:
                row_value = st.session_state[row_key]
                if row_value is not None:
                        st.session_state[col_wrap_key] = 0

def disable_hue_norm_sizes(key, val):
        if st.session_state[key] == val:
                return True 
        return False


def get_columns():
        options = [None]
        tmp = st.session_state.df_col_key
        options.extend(tmp)
        return options

df_col = get_columns() 

hue = {'pars' : {'label': 'hue', 
                'options': [],
                'help': helps['hue']
                },
        'input_type': selectbox       
}

row = {'pars' : {'label': 'row', 
                'options':[],
                'help': helps['row'],
                'kwargs': {'on_change': row_on_change, 
                         'kwargs': {'row_key':'row_key', 'col_wrap_key':'col_wrap_key'}
                        }
                },
        'input_type': selectbox       
}
col = {'pars' : {'label': 'col', 
                'options':[],
                'help': helps['col']
                },
        'input_type': selectbox       
}
size = {'pars' : {'label': 'size', 
                'options':[],
                'help': helps['size']
                },
        'input_type': selectbox       
}
style = {'pars' : {'label': 'style', 
                'options':[],
                'help': helps['style']
                },
        'input_type': selectbox,
        'input_type_name': 'selectbox'      
}


col_wrap = {'pars': 
               {'label': 'col wrap', 
                'min_value':0,
                'max_value': 10,
                'value': 0, 
                'step': 1,
                'help': helps['col_wrap'],
                'disabled_func': col_wrap_toggled_disabled,
                'args': ('row_key', None, 'col_key', None)
                },
             'input_type': number_input   
}

row_order = {'pars' : {'label': 'row_order', 
                'options':[],
                'help': helps['row_order']
                },
        'input_type': multiselect,
        'input_type_name': 'multiselect',
        'default':[]      
}


col_order = {'pars' : {'label': 'col_order', 
                'options':[],
                'help': helps['col_order'],
                },
        'input_type': multiselect,
        'input_type_name': 'multiselect',
}
hue_order = {'pars' : {'label': 'hue_order', 
                'options':[],
                'help': helps['hue_order']
                },
        'input_type': multiselect,
        'input_type_name': 'multiselect',
        'default':[]      
}
size_order = {'pars' : {'label': 'size_order', 
                'options':[],
                'help': helps['style_order']
                },
        'input_type': multiselect,
        'input_type_name': 'multiselect',
        'default':[None]      
}
sizes = {'pars' : {'label': 'sizes', 
                'options':[None, 'enter tuple'],
                'help': helps['sizes'],
                 'disabled_func': disable_hue_norm_sizes,
                'args': ('size_key', None)
                },
        'input_type': selectbox,

}
style_order = {'pars' : {'label': 'style_order', 
                'options':[],
                'help': helps['style_order']
                },
        'input_type': multiselect,
        'input_type_name': 'multiselect',    
}
disable_hue_norm_sizes
hue_norm = {'pars' : {'label': 'hue_norm', 
                # 'options':[None],
                'options':[None, 'enter tuple'],
                'help': helps['hue_norm'],
                'disabled_func': disable_hue_norm_sizes,
                'args': ('hue_key', None)
                },
        'input_type': selectbox,
        'input_type_name': 'multiselect',
}
size_norm = {'pars' : {'label': 'size_norm', 
                'options':[None, 'enter tuple'],
                'help': helps['size_norm'],
                'disabled_func': disable_hue_norm_sizes,
                'args': ('size_key', None)
                },
        'input_type': selectbox,
}


groups_par = {'hue': hue, #'col': col, 'row': row, 
              'hue_order': hue_order, 'col_order': col_order, 'row_order': row_order, 
              'col_wrap': col_wrap, 'size': size, 'style': style, 
              'size_order': size_order, 'style_order': style_order, 
              'hue_norm': hue_norm, 'sizes': sizes, 'size_norm': size_norm
}



"""Miscellaneous"""

dashes = {'pars' : {'label': 'dashes', 
                'options':(True, False),
                'help': helps['dashes'],
                'index':0
                },
        'input_type': radio_input    
}
markers = {'pars' : {'label': 'markers', 
                'options':(None, 'style_1', 'style_2', 'style_3', 'style_4'),
                'help': helps['markers'],
                'index':0
                },
        'input_type': radio_input    
}
legend = {'pars' : {'label': 'legend', 
                'options':('auto', 'brief', 'full', False),
                'help': helps['legend'],
                'index':0
                },
        'input_type': radio_input    
}

height = {'pars': 
               {'label': 'height', 
                'min_value':1,
                'max_value': 10,
                'value': 5, 
                'step': 1,
                'help': helps['height']
                },
             'input_type': number_input   
}
aspect = {'pars': 
               {'label': 'aspect', 
                'min_value':1,
                'max_value': 10,
                'value': 1, 
                'step': 1,
                'help': helps['aspect'],
                },
             'input_type': number_input   
}

units = {'pars' : {'label': 'units', 
                'options':[],
                'help': helps['units']
                },
        'input_type': selectbox,
        'input_type_name': 'selectbox'      
}



palette = {'pars' : {'label': 'palette', 
                'options':[None, 'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'],
                'help': helps['palette']
                },
        'input_type': selectbox,
        'input_type_name': 'selectbox'      
}


others_par = {'dashes':dashes, 'markers':markers, 'legend':legend, 'height':height, 'aspect':aspect, 'units':units, 'palette': palette}

relational_widgets = {**groups_par, **others_par}

""""Plot pertaining to categorical and distribution""" 
#Boolean variables

rug = {'pars' : {'label': 'rug', 
                'options':(True, False),
                'index': 1,
                'help': helps['rug']
                },
        'input_type': radio_input     
}

log_scale = {'pars' : {'label': 'log_scale', 
                'options':(True, False),
                'index': 1,
                'help': helps['log_scale']
                },
        'input_type': radio_input     
}

color = {'pars' : {'label': 'color', 
                'help': helps['color']
                },
        'input_type': color_picker    
}

orient = {'pars' : {'label': 'orient', 
                'options':('v', 'h'),
                'index': 0,
                'help': helps['orient']
                },
        'input_type': radio_input     
}


distribution_widgets = {**relational_widgets, 'rug': rug, 'color':color, 'log_scale':log_scale}

import numpy as np
estimator = {'pars' : {'label': 'estimator', 
                'options':(np.mean, np.median, np.average, np.var, np.std, np.nanmedian, np.nanmean, np.nanstd, np.nanvar),
                'help': helps['estimator']
                },
        'input_type': selectbox    
}

#used for confidence interval incase the user want to enter value
mixed_ci_pars = {'pars': 
                        {'label': 'enter ci', 
                        'min_value':0,
                        'max_value': 100,
                        'value': 95, 
                        'step': 5,
                        'help': helps['ci'],
                        'key': 'enter_ci_key'
                        },
             'input_type': number_input,
             'value_to_trigger_another_widget': 'float'   
}

ci = {'pars' : {'label': 'ci', 
                'options':(None, "sd", 'float'),
                'help': helps['ci'],
                'key': 'ci_key'
                },
        'input_type': selectbox, 
        'mixed_pars': mixed_ci_pars
}

n_boot = {'pars': 
                {'label': 'n_boot', 
                'min_value':1000,
                'max_value': 10000,
                'value': 1000, 
                'step': 100,
                'help': helps['n_boot']
                },
        'input_type': number_input
}
seed = {'pars': 
                {'label': 'seed', 
                'min_value':100,
                'max_value': 1000,
                'value': 100, 
                'step': 100,
                'help': helps['seed']
                },
             'input_type': number_input,
}
order = {'pars': 
                {'label': 'order', 
                'min_value':1,
                'max_value': 100,
                'value': 1, 
                'step': 1,
                'help': helps['order']
                },
             'input_type': number_input,
}



legend_out = {'pars' : {'label': 'legend_out', 
                'options':(True, False),
                'index': 0,
                'help': helps['legend_out']
                },
        'input_type': radio_input     
}
sharex = {'pars' : {'label': 'sharex', 
                'options':(True, False, 'col', 'row'),
                'index': 0,
                'help': helps['sharex']
                },
        'input_type': radio_input     
}
sharey = {'pars' : {'label': 'sharey', 
                'options':(True, False, 'col', 'row'),
                'index': 0,
                'help': helps['sharey']
                },
        'input_type': radio_input     
}
margin_titles = {'pars' : {'label': 'margin_titles', 
                'options':(True, False),
                'index': 1,
                'help': helps['margin_titles']
                },
        'input_type': radio_input     
}

categorical_widgets = {**distribution_widgets, 'orient': orient, 'estimator':estimator, 'ci': ci, #'seed': seed,
                        'n_boot': n_boot,  'legend_out': legend_out,  'sharex': sharex, 'sharey': sharey, 'margin_titles': margin_titles
}



#number input for


"""Regression Specific Parameters"""

#boolean options for 
x_estimator = {'pars' : {'label': 'x_estimator', 
                'options':(None, np.mean, np.median, np.average, np.var, np.std, np.nanmedian, np.nanmean, np.nanstd, np.nanvar),
                'help': helps['x_estimator']
                },
        'input_type': selectbox    
}

x_bins = {'pars': 
                {'label': 'x_bins', 
                'min_value':2,
                'max_value': 100,
                'value': 3, 
                'step': 1,
                'help': helps['x_bins']
                },
             'input_type': number_input,
}
#used for confidence interval incase the user want to enter value
mixed_x_ci_pars = {'pars': 
                        {'label': 'enter ci', 
                        'min_value':0.0,
                        'max_value': 1.0,
                        'value': 0.95, 
                        'step': 0.1,
                        'help': helps['x_ci'],
                        'key': 'enter_ci_key'
                        },
             'input_type': number_input,
             'value_to_trigger_another_widget': 'int'   
}

x_ci = {'pars' : {'label': 'x_ci', 
                'options':(None, "ci", "sd"),
                'help': helps['x_ci'],
                'key': 'x_ci_key'
                },
        'input_type': selectbox, 
        'mixed_pars': mixed_x_ci_pars
}

scatter = {'pars' : {'label': 'scatter', 
                'options':(True, False),
                'index': 0,
                'help': helps['scatter']
                },
        'input_type': radio_input     
}
fit_reg = {'pars' : {'label': 'fit_reg', 
                'options':(True, False),
                'index': 0,
                'help': helps['fit_reg']
                },
        'input_type': radio_input     
}

logistic = {'pars' : {'label': 'logistic', 
                'options':(True, False),
                'index': 1,
                'help': helps['logistic']
                },
        'input_type': radio_input     
}
lowess = {'pars' : {'label': 'lowess', 
                'options':(True, False),
                'index': 1,
                'help': helps['lowess']
                },
        'input_type': radio_input     
}
robust = {'pars' : {'label': 'robust', 
                'options':(True, False),
                'index': 1,
                'help': helps['robust']
                },
        'input_type': radio_input     
}
logx = {'pars' : {'label': 'logx', 
                'options':(True, False),
                'index': 1,
                'help': helps['logx']
                },
        'input_type': radio_input     
}

x_partial = {'pars' : {'label': 'x_partial', 
                'options':[],
                'help': helps['x_partial']
                },
        'input_type': selectbox    
}
y_partial = {'pars' : {'label': 'y_partial', 
                'options':[],
                'help': helps['y_partial']
                },
        'input_type': selectbox    
}

truncate = {'pars' : {'label': 'truncate', 
                'options':(True, False),
                'index': 0,
                'help': helps['truncate']
                },
        'input_type': radio_input     
}


x_jitter = {'pars': 
                {'label': 'x_jitter', 
                'min_value':0.0,
                'max_value': 1.0,
                'value': 0.0, 
                'step': 0.05,
                'help': helps['x_jitter'],
                },
             'input_type': number_input,
}
y_jitter = {'pars': 
                {'label': 'y_jitter', 
                'min_value':0.0,
                'max_value': 1.0,
                'value': 0.0, 
                'step': 0.05,
                'help': helps['y_jitter'],
                },
             'input_type': number_input,
}

dropna = {'pars' : {'label': 'dropna', 
                'options':(True, False),
                'index': 0,
                'help': helps['truncate']
                },
        'input_type': radio_input     
}


regression_widgets = {**relational_widgets, 'units':units, 'color':color, 'ci': ci, 'n_boot': n_boot, 'x_estimator': x_estimator,  
                      'x_ci': x_ci, 'scatter': scatter, 'fit_reg':fit_reg, 'logistic': logistic,
                      'lowess':lowess, 'robust': robust, 'logx': logx, 'x_partial': x_partial, 
                      'y_partial': y_partial, 'truncate': truncate, 
                      'x_jitter': x_jitter, 'y_jitter': y_jitter, 'dropna': dropna, #'x_bins':x_bins,
}


"""Joinplot parameters"""
ratio = {'pars': 
                {'label': 'ratio', 
                'min_value':1,
                'max_value': 10,
                'value': 1, 
                'step': 1,
                # 'help': helps['y_jitter'],
                },
             'input_type': number_input,
}
space = {'pars': 
                {'label': 'space', 
                'min_value':0,
                'max_value': 10,
                'value': 0, 
                'step': 1,
                # 'help': helps['y_jitter'],
                },
             'input_type': number_input,
}


marginal_ticks = {'pars' : {'label': 'marginal_ticks', 
                'options':(True, False),
                'index': 0,
                'help': helps['truncate']
                },
        'input_type': radio_input     
}

jointplot_widgets = {**relational_widgets, 'ratio' :ratio, 'space': space,'dropna': dropna,'marginal_ticks':marginal_ticks}



"""Pairplot Parameters"""
diag_kind = {'pars' : {'label': 'diag_kind', 
                'options':['auto', 'hist', 'kde', None],
                # 'help': helps['']
                },
        'input_type': selectbox    
}
x_vars = {'pars' : {'label': 'x_vars', 
                'options':[],
                # 'help': helps['']
                },
        'input_type': multiselect    
}
y_vars = {'pars' : {'label': 'y_vars', 
                'options':[],
                # 'help': helps['']
                },
        'input_type': multiselect   
}

corner = {'pars' : {'label': 'corner', 
                'options':(True, False),
                'index': 0,
        #      "   'help': helps['']"
                },
        'input_type': radio_input     
}

vars = {'pars' : {'label': 'vars', 
                'options':[],
                # 'help': helps['hue_order']
                },
        'input_type': multiselect,  
}

pairplot_widgets ={**relational_widgets, 'diag_kind':diag_kind, 'x_vars': x_vars,'y_vars':y_vars, 'corner':corner,'vars':vars}



"""Matrix plot parameters"""

vmin = {'pars': 
                {'label': 'vmin', 
                'min_value':0.0,
                'max_value': 100.0,
                'value': 5.0, 
                'step': 0.5,
                # 'help': helps['y_jitter'],
                },
             'input_type': number_input,
}
vmax = {'pars': 
                {'label': 'vmax', 
                'min_value':0.0,
                'max_value': 100.0,
                'value': 15.0, 
                'step': 0.5,
                # 'help': helps['y_jitter'],
                },
             'input_type': number_input,
}
center = {'pars': 
                {'label': 'center', 
                'min_value':0.0,
                'max_value': 100.0,
                'value': 15.0, 
                'step': 0.5,
                # 'help': helps['y_jitter'],
                },
             'input_type': number_input,
}
linewidths = {'pars': 
                {'label': 'linewidths', 
                'min_value':0.0,
                'max_value': 100.0,
                'value': 1.0, 
                'step': 0.5,
                # 'help': helps['y_jitter'],
                },
             'input_type': number_input,
}

annot = {'pars' : {'label': 'annot', 
                'options':(True, False),
                'index': 1,
                # 'help': helps['truncate']
                },
        'input_type': radio_input     
}
cbar = {'pars' : {'label': 'cbar', 
                'options':(True, False),
                'index': 1,
                # 'help': helps['truncate']
                },
        'input_type': radio_input     
}
square = {'pars' : {'label': 'square', 
                'options':(True, False),
                'index': 1,
                # 'help': helps['truncate']
                },
        'input_type': radio_input     
}
xticklabels = {'pars' : {'label': 'xticklabels', 
                'options':(True, False),
                'index': 1,
                # 'help': helps['truncate']
                },
        'input_type': radio_input     
}
yticklabels = {'pars' : {'label': 'yticklabels', 
                'options':(True, False),
                'index': 1,
                # 'help': helps['truncate']
                },
        'input_type': radio_input     
}
mask = {'pars' : {'label': 'mask', 
                'options':(True, False),
                'index': 1,
                # 'help': helps['truncate']
                },
        'input_type': radio_input     
}

heatmap_widgets = {'linewidths':linewidths, 'vmin':vmin, 'vmax':vmax, 'center': center,
                'annot':annot, 'cbar':cbar,  'xticklabels':xticklabels, 'yticklabels':yticklabels, 
                'mask': mask, 'square':square, 
}
# 'vmin':vmin, 'vmax':vmax, 'center': center, 


z_score = {'pars': 
                {'label': 'z_score', 
                'min_value':0,
                'max_value': 100,
                'value': 1, 
                'step': 1,
                # 'help': helps['y_jitter'],
                },
             'input_type': number_input,
}
standard_scale = {'pars': 
                {'label': 'standard_scale', 
                'min_value':0,
                'max_value': 100,
                'value': 0, 
                'step': 1,
                # 'help': helps['y_jitter'],
                },
             'input_type': number_input,
}

row_cluster = {'pars' : {'label': 'row_cluster', 
                'options':(True, False),
                'index': 0,
                # 'help': helps['truncate']
                },
        'input_type': radio_input     
}
col_cluster = {'pars' : {'label': 'col_cluster', 
                'options':(True, False),
                'index': 0,
                # 'help': helps['truncate']
                },
        'input_type': radio_input     
}


cluster_widgets = {'z_score' :z_score, 'row_cluster': row_cluster,'col_cluster':col_cluster}
# 'standard_scale': standard_scale,
matrix_widgets = {**relational_widgets, **heatmap_widgets, **cluster_widgets}

widget_plot_type_parameters = {**matrix_widgets, **groups_par, **others_par, **categorical_widgets, 
                                **regression_widgets, **jointplot_widgets, **pairplot_widgets
}
