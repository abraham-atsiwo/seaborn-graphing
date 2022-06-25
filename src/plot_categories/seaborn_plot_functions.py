from seaborn import relplot, displot, catplot, lmplot, regplot, residplot, jointplot, pairplot, heatmap, clustermap

plot_type_functions = {'Relational': relplot, 
                        'Distribution': displot, 
                        'Categorical': catplot, 
                        'lmplot': lmplot,
                        'regplot': regplot, 
                        'residplot': residplot
}

plot_type_based_on_category = {'scatterplot':relplot, 
                                'lineplot':relplot,
                                'histplot': displot,
                                'kdeplot': displot,
                                'ecdfplot': displot,
                                'stripplot': catplot,
                                'swarmplot': catplot,
                                'boxplot': catplot,
                                'violinplot': catplot,
                                'boxenplot': catplot,
                                'pointplot': catplot,
                                'barplot': catplot,
                                'countplot': catplot,
                                'lmplot': lmplot,
                                'regplot': regplot, 
                                'residplot': residplot,
                                'scatter': jointplot,
                                'kde': jointplot,
                                'hist': jointplot,
                                'hex': jointplot,
                                'reg': jointplot,
                                'resid': jointplot,
                                'scatterpairplot': pairplot, 
                                'histpairplot': pairplot, 
                                'kdepairplot': pairplot,
                                'regpairplot': pairplot,
                                'heatmap': heatmap, 
                                'clustermap': clustermap,
}



