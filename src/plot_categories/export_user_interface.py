from plot_categories.relational_api import relational_parameters 
from plot_categories.distribution_api import distribution_parameters
from plot_categories.categorical_api import categorical_parameters
from plot_categories.regression_api import regression_parameters
from plot_categories.jointplot_api import jointplot_parameters
from plot_categories.pairplot_api import pairplot_parameters
from plot_categories.matrix_api import matrixplot_parameters


display_components_to_screen = {
    'scatterplot': relational_parameters,
    'lineplot': relational_parameters,
    'histplot': distribution_parameters,
    'ecdfplot': distribution_parameters,
    'kdeplot': distribution_parameters,
    'stripplot': categorical_parameters,
    'swarmplot': categorical_parameters,
    'boxplot': categorical_parameters,
    'violinplot': categorical_parameters,
    'boxenplot': categorical_parameters,
    'pointplot': categorical_parameters,
    'barplot': categorical_parameters,
    'countplot': categorical_parameters,
    'lmplot': regression_parameters,
    'residplot': regression_parameters,
    'regplot': regression_parameters,
    'scatter': jointplot_parameters,
    'kde': jointplot_parameters,
    'hist': jointplot_parameters,
    'hex': jointplot_parameters,
    'reg': jointplot_parameters,
    'resid': jointplot_parameters,
    'scatterpairplot': pairplot_parameters, 
    'histpairplot': pairplot_parameters, 
    'kdepairplot': pairplot_parameters,
    'regpairplot': pairplot_parameters,
    'heatmap': matrixplot_parameters,
    'clustermap': matrixplot_parameters
}
