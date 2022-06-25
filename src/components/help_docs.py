
helps = {
        'x': 'Variables that specify positions on the x axes.',
        'y': 'Variables that specify positions on the y axes.',
        'hue': 'Grouping variable that will produce elements with different colors. \
                Can be either categorical or numeric, although color mapping will behave differently in latter case.',
        'size': 'Grouping variable that will produce elements with different sizes. Can be either categorical or numeric, \
                although size mapping will behave differently in latter case.',
        'style': 'Grouping variable that will produce elements with different styles. \
                Can have a numeric dtype but will always be treated as categorical.',
        'row': 'Variables that define subsets to plot on different facets.',
        'col': 'Variables that define subsets to plot on different facets.', 
        'col_wrap': '“Wrap” the column variable at this width, so that the column facets span multiple rows. Incompatible with a row facet.', 
        'row_order': 'Order to organize the rows and/or columns of the grid in, otherwise the orders are inferred from the data objects.',
        'col_order': 'Order to organize the rows and/or columns of the grid in, otherwise the orders are inferred from the data objects.',
        'palette': 'Method for choosing the colors to use when mapping the hue semantic. String values are passed to color_palette(). \
                        List or dict values imply categorical mapping, while a colormap object implies numeric mapping.',
        'hue_order': 'Specify the order of processing and plotting for categorical levels of the hue semantic.',
        'hue_norm': 'Either a pair of values that set the normalization range in data units or an object that will \
                        map from data units into a [0, 1] interval. Usage implies numeric mapping.',
        'sizes': 'An object that determines how sizes are chosen when size is used. It can always be a list of size values or a dict mapping \
                levels of the size variable to sizes. When size is numeric, it can also be a tuple specifying the \
                minimum and maximum size to use such that other values are normalized within this range.', 
        'size_order': 'Specified order for appearance of the size variable levels, otherwise they are determined \
                        from the data. Not relevant when the size variable is numeric.',
        'size_norm': 'Normalization in data units for scaling plot objects when the size variable is numeric.',
        'style_order': 'Specified order for appearance of the style variable levels otherwise they are determined from the data. Not relevant when the style variable is numeric.',
        'dashes': 'Object determining how to draw the lines for different levels of the style variable. Setting to True will use default dash codes, or you can pass a list of dash \
                        codes or a dictionary mapping levels of the style variable to dash codes. Setting to False will use solid lines for all subsets. Dashes are specified as in matplotlib: \
                        a tuple of (segment, gap) lengths, or an empty string to draw a solid line.',
        'markers': 'Object determining how to draw the markers for different levels of the style variable. Setting to True will use default markers, or you can pass a list of markers or \
                        a dictionary mapping levels of the style variable to markers. Setting to False will draw marker-less lines. Markers are specified as in matplotlib.',
        'legend': 'How to draw the legend. If “brief”, numeric hue and size variables will be represented with a sample of evenly spaced values. If “full”, every group will get an entry in the \
                        legend. If “auto”, choose between brief or full representation based on number of levels. If False, no legend data is added and no legend is drawn.', 
        'height': 'Height (in inches) of each facet. See also: aspect.', 
        'aspect': 'Aspect ratio of each facet, so that aspect * height gives the width of each facet in inches.', 
        'units': 'Grouping variable identifying sampling units. When used, a separate line will be drawn for each unit with appropriate semantics, but no legend entry will be added. \
                        Useful for showing distribution of experimental replicates when exact identities are not needed.',
        'rug': 'f True, show each observation with marginal ticks (as in rugplot()).',
        'log_scale': 'Set axis scale(s) to log. A single value sets the data axis for univariate distributions and both axes for bivariate distributions. A pair of values sets each axis independently.  \
                                Numeric values are interpreted as the desired base (default 10). If False, defer to the existing Axes scale.' ,
        'color': 'Single color specification for when hue mapping is not used. Otherwise, the plot will try to hook into the matplotlib property cycle.', 
        'orient': 'Orientation of the plot (vertical or horizontal). This is usually inferred based on the type of the input variables, but it can be used to \
                resolve ambiguity when both x and y are numeric or when plotting wide-form data.',
        'estimator': 'callable that maps vector -> scalar, optional', 
        'ci': 'Size of confidence intervals to draw around estimated values. If “sd”, skip bootstrapping and draw the standard deviation of the observations. \
                If None, no bootstrapping will be performed, and error bars will not be drawn.'  , 
        'n_boot': 'Number of bootstrap iterations to use when computing confidence intervals.'   , 
        'seed': 'Seed or random number generator for reproducible bootstrapping.' ,
        'order': 'Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.' ,
        'sharex': 'If true, the facets will share y axes across columns and/or x axes across rows.' ,
        'sharey': 'If true, the facets will share y axes across columns and/or x axes across rows.' ,
        'legend_out': 'If True, the figure size will be extended, and the legend will be drawn outside the plot on the center right.',
        'margin_titles': 'If True, the titles for the row variable are drawn to the right of the last column. This option is experimental and may not work in all cases.' ,
        'x_estimator': 'Apply this function to each unique value of x and plot the resulting estimate. This is useful when x is a discrete variable. If x_ci is given, this estimate will be bootstrapped and a confidence interval will be drawn.',
        'x_bins': 'Bin the x variable into discrete bins and then estimate the central tendency and a confidence interval. This binning only influences how the scatterplot is drawn; the regression is still fit to the original data. This parameter \
                        is interpreted either as the number of evenly-sized (not necessary spaced) bins or the positions of the bin centers. When this parameter is used, it implies that the default of x_estimator is numpy.mean.',
        'scatter': 'If True, draw a scatterplot with the underlying observations (or the x_estimator values).' ,
        'fit_reg': 'If True, estimate and plot a regression model relating the x and y variables.'    ,
        'logistic': 'If True, assume that y is a binary variable and use statsmodels to estimate a logistic regression model. Note that this is substantially more computationally intensive than linear regression, so you may wish to decrease the number of bootstrap resamples (n_boot) or set ci to None.' , 
        'lowess' : 'If True, use statsmodels to estimate a nonparametric lowess model (locally weighted linear regression). Note that confidence intervals cannot currently be drawn for this kind of model.' ,
        'robust': 'If True, use statsmodels to estimate a robust regression. This will de-weight outliers. Note that this is substantially more computationally intensive than standard linear regression, so you may wish to decrease the number of bootstrap resamples (n_boot) or set ci to None.',
        'logx': 'If True, estimate a linear regression of the form y ~ log(x), but plot the scatterplot and regression model in the input space. Note that x must be positive for this to work.' ,
        'x_partial': 'Confounding variables to regress out of the x or y variables before plotting.', 
        'y_partial': 'Confounding variables to regress out of the x or y variables before plotting.',
        'x_ci': 'Size of the confidence interval used when plotting a central tendency for discrete values of x. If "ci", defer to the value of the ci parameter. If "sd", skip bootstrapping and show the standard deviation of the observations in each bin.',
        'truncate': 'If True, the regression line is bounded by the data limits. If False, it extends to the x axis limits.',
        'x_jitter': 'Add uniform random noise of this size to either the x or y variables. The noise is added to a copy of the data after fitting the regression, and only influences the look of the scatterplot. This can be helpful when plotting variables that take discrete values.',
        'y_jitter': 'Add uniform random noise of this size to either the x or y variables. The noise is added to a copy of the data after fitting the regression, and only influences the look of the scatterplot. This can be helpful when plotting variables that take discrete values.',
        

}