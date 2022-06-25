from seaborn import load_dataset

# default_data = {'Relational':sns.load_dataset("tips"), 
#                 'Distribution':sns.load_dataset("penguins"), 
#                 'Categorical':sns.load_dataset("exercise"),
#                 'Regression':sns.load_dataset("tips")
# }

# theme_styles = ['darkgrid', 'whitegrid', 'white', 'dark']


# default_plot_category = {'Relational':'scatterplot', 
#                         'Distribution':'histplot', 
#                         'Categorical':'stripplot', 
#                         'Regression':'lmplot'
# }

set_column_order = {'fmri':['timepoint', 'signal', 'subject', 'event', 'region'], 
                    'tips':['day', 'total_bill', 'tip', 'sex', 'smoker', 'size', 'time'],
                    'penguins':['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'species', 'island', 'body_mass_g', 'sex']
                    }

#plot specifics 
iris = load_dataset("iris")
species = iris.pop("species")
default_data_plot_categories = {'scatterplot':load_dataset('tips'), 
                                'lineplot':load_dataset("fmri")[set_column_order['fmri']],  
                                'histplot': load_dataset("penguins"),
                                'kdeplot': load_dataset("tips"),
                                'ecdfplot': load_dataset("penguins"),
                                'stripplot': load_dataset("tips")[set_column_order['tips']],
                                'swarmplot': load_dataset("tips")[set_column_order['tips']],
                                'boxplot': load_dataset("tips")[set_column_order['tips']],
                                'violinplot': load_dataset("tips")[set_column_order['tips']],
                                'boxenplot': load_dataset("tips")[set_column_order['tips']],
                                'pointplot': load_dataset("tips")[set_column_order['tips']],
                                'barplot': load_dataset("tips")[set_column_order['tips']],
                                'countplot': load_dataset("titanic"),
                                'lmplot': load_dataset("tips"),
                                'regplot': load_dataset("tips"),
                                'residplot': load_dataset("tips"),
                                'scatter': load_dataset("penguins")[set_column_order['penguins']],
                                'kde': load_dataset("penguins")[set_column_order['penguins']],
                                'hist': load_dataset("penguins")[set_column_order['penguins']],
                                'hex': load_dataset("penguins")[set_column_order['penguins']],
                                'reg': load_dataset("penguins")[set_column_order['penguins']],
                                'resid': load_dataset("penguins")[set_column_order['penguins']],
                                'histpairplot': load_dataset("penguins"),
                                'kdepairplot': load_dataset("penguins"),
                                'scatterpairplot': load_dataset("penguins"),
                                'regpairplot': load_dataset("penguins"),
                                'heatmap': iris,
                                'clustermap': iris
}


Relational = ['scatterplot', 'lineplot']
Distribution = ['histplot', 'kdeplot', 'ecdfplot']
Categorical = ['stripplot', 'swarmplot', 'boxplot', 'violinplot', 'boxenplot', 'pointplot', 'barplot', 'countplot']
# Regression = ['regplot', 'residplot']
Jointplot = ['scatter', 'kde', 'hist', 'hex', 'reg', 'resid']
Pairplot = ['scatterpairplot', 'kdepairplot', 'histpairplot', 'regpairplot']
Matrixplot = ['clustermap', 'heatmap']
Regression = ['lmplot', 'regplot', 'residplot']

plot_type_categories = {
                        'Relational':Relational, 
                        'Distribution':Distribution, 
                        'Categorical':Categorical, 
                        'Jointplot': Jointplot,
                        'Pairplot': Pairplot,
                        'Matrixplot': Matrixplot,
                        'Regression':Regression,
}
