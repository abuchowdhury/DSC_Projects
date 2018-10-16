# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 04:16:51 2018

@author: achowdhury
"""
'''
Beginning with just a plot
Let's get started on the Gapminder app. Your job is to make the ColumnDataSource object, prepare the plot, and add circles for Life expectancy vs Fertility. You'll also set x and y ranges for the axes.
As in the previous chapter, the DataCamp environment executes the bokeh serve command to run the app for you. When you hit 'Submit Answer', you'll see in the IPython Shell that bokeh serve script.py gets called to run the app. This is something to keep in mind when you are creating your own interactive visualizations outside of the DataCamp environment.

Make a ColumnDataSource object called source with 'x', 'y', 'country', 'pop' and 'region' keys. The Pandas selections are provided for you.
Save the minimum and maximum values of the life expectancy column data.life as ymin and ymax. As a guide, you can refer to the way we saved the minimum and maximum values of the fertility column data.fertility as xmin and xmax.
Create a plot called plot() by specifying the title, setting plot_height to 400, plot_width to 700, and adding the x_range and y_range parameters.
Add circle glyphs to the plot. Specify an fill_alpha of 0.8 and source=source.
'''



# Import the necessary modules
from bokeh.io import curdoc
#from bokeh.models import ColumnDataSource, LinearInterpolator
from bokeh.plotting import figure
#from bokeh.models import CategoricalColorMapper, LinearInterpolator
from bokeh.palettes import Spectral6
from bokeh.models import (
    LinearInterpolator,
    CategoricalColorMapper,
    ColumnDataSource,
    NumeralTickFormatter,
    Select,
    HoverTool,
)

from bokeh.layouts import widgetbox, row
from bokeh.models import Slider


import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/gapminder_tidy.csv', thousands=',', index_col='Year')


# =============================================================================
# =============================================================================
# PLOT_OPTS = dict(
#          height=800, width=1200,  x_axis_type='log',
#          x_range=(100, 100000), y_range=(0, 100),
# )
# # =============================================================================
# =============================================================================

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'fertility'       : data.loc[1970].fertility,
    'life'       : data.loc[1970].life,
    'country'      : data.loc[1970].Country,
    'pop'      : (data.loc[1970].population / 20000000) + 2,
    'region'      : data.loc[1970].region,
    'child_mortality'  : data.loc[1970].child_mortality,
    'gdp'     : data.loc[1970].gdp
})

#
# 
# Save the minimum and maximum values of the fertility column: xmin, xmax
#xmin, xmax = min(data.fertility), max(data.fertility)

# Save the minimum and maximum values of the life expectancy column: ymin, ymax
#ymin, ymax = min(data.life), max(data.life)

# Create the figure: plot
# =============================================================================
# plot = figure(title=('\nExploratoty data analysis on the Gapminder app. \n  Hover on each Glyps to display more information \n\nData set: 1973-2013                                                :- @AbuSChowdhury'), 
#               plot_height=700, plot_width=1000, x_range=(xmin, xmax), y_range=(ymin, ymax))
# 
# =============================================================================

plot = figure(title='Gapminder Data for 1970-2013             :- @AbuSChowdhury', plot_height=600, plot_width=800)



# =============================================================================
# p = figure(
#     title=str('Gapminder data used to display "Income vs. Life Expectancy" for each country from 1800-2015. Circles ~ Population size     @AbuSChowdhury'), toolbar_location='above', 
#     tools=[HoverTool(show_arrow=False, line_policy='next', tooltips=[
#     ('Country    : ', '@country'),
#     ('Population : ', '@population'),
#     ('Region     : ', '@region'),
#     ('Income : ', '@x'),
#     ('Life Expectancy     : ', '@y')
#         ])],
#     **PLOT_OPTS)
# =============================================================================
# Add circle glyphs to the plot
#plot.circle(x='x', y='y', fill_alpha=0.8, source=source)



'''
Enhancing the plot with some shading
Now that you have the base plot ready, you can enhance it by coloring each circle glyph by continent.
Your job is to make a list of the unique regions from the data frame, prepare a ColorMapper, and add it to the circle glyph.

Make a list of the unique values from the region column. You can use the unique() and tolist() methods on data.region to do this.
Import CategoricalColorMapper from bokeh.models and the Spectral6 palette from bokeh.palettes.
Use the CategoricalColorMapper() function to make a color mapper called color_mapper with factors=regions_list and palette=Spectral6.
Add the color mapper to the circle glyph as a dictionary with dict(field='region', transform=color_mapper) as the argument passed to the color parameter of plot.circle(). Also set the legend parameter to be the 'region'.
Set the legend.location attribute of plot to 'top_right'.
'''
# Make a list of the unique values from the region column: regions_list
regions_list = data.region.unique().tolist()


# Size Mapper

size_mapper = LinearInterpolator(
    x=[data.gdp.min(), data.gdp.max()],
    y=[8, 65]
)

# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)


plot.circle(x='x', y='y', size={'field': 'gdp', 'transform': size_mapper}, color={'field': 'region', 'transform': color_mapper}, alpha=0.6, source=source, legend='region')



# Set the legend.location attribute of the plot to 'top_right'
plot.legend.location = 'bottom_left'

# Import the necessary modules
# =============================================================================
# from bokeh.layouts import widgetbox, row
# from bokeh.models import Slider
# =============================================================================
'''
# Define the callback function: update_plot
def update_plot(attr, old, new):
    # set the `yr` name to `slider.value` and `source.data = new_data`
    yr = slider.value
    new_data = {
        'x'       : data.loc[yr].fertility,
        'y'       : data.loc[yr].life,
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
        'child_mortality'  : data.loc[yr].child_mortality,
        'gdp'     : data.loc[yr].gdp
    }
    source.data = new_data
    
'''




# Import HoverTool from bokeh.models
# =============================================================================
# #from bokeh.models import HoverTool
# =============================================================================

#  # Create a HoverTool: hover
hover = HoverTool(tooltips=[('Country    : ', '@country'),
      ('Region     : ', '@region'),
      ('Population : ', '@pop'),
      ('GDP     : ', '@gdp'),
      ('Fertility : ', '@x'),
      ('Life Expectancy     : ', '@y'),
      ('Child_mortality     : ', '@child_mortality')])
  
  # Add the HoverTool to the plot
plot.add_tools(hover)
    
# Define the callback: update_plot
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = x_select.value
    y = y_select.value
    # Label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    # Set new_data
    new_data = {
        'x'       : data.loc[yr][x],
        'y'       : data.loc[yr][y],
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes
    plot.x_range.start = min(data[x])
    plot.x_range.end = max(data[x])
    plot.y_range.start = min(data[y])
    plot.y_range.end = max(data[y])

    # Add title to plot
    plot.title.text = 'Gapminder data for %d' % yr
    
slider = Slider(start=1970, end=2013, step=1, value=1970, title='Year')
slider.on_change('value', update_plot)

# Attach the callback to the 'value' property of slider
#slider.on_change('value',update_plot)



# Create a dropdown Select widget for the x data: x_select
x_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='fertility',
    title='x-axis data'
)

# Attach the update_plot callback to the 'value' property of x_select
x_select.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='life',
    title='y-axis data'
)

# Attach the update_plot callback to the 'value' property of y_select
y_select.on_change('value', update_plot)

'''
Adding a hover tool
In this exercise, you'll practice adding a hover tool to drill down into data column values and display more detailed information about each scatter point.
After you're done, experiment with the hover tool and see how it displays the name of the country when your mouse hovers over a point!
The figure and slider have been created for you and are available in the workspace as plot and slider.


Adding dropdowns to the app
As a final step in enhancing your application, in this exercise you'll add dropdowns for interactively selecting different data features. In combination with the hover tool you added in the previous exercise, as well as the slider to change the year, you'll have a powerful app that allows you to interactively and quickly extract some great insights from the dataset!
All necessary modules have been imported, and the previous code you wrote is taken care off. In the provided sample code, the dropdown for selecting features on the x-axis has been added for you. Using this as a reference, your job in this final exercise is to add a dropdown menu for selecting features on the y-axis.
Take a moment, after you are done, to enjoy exploring the visualization by experimenting with the hover tools, sliders, and dropdown menus that you have learned how to implement in this course.

'''


# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select), plot)
curdoc().add_root(layout)
curdoc().title = 'Gapminder Data for 1970-2013  Fertility vs. Life Expectancy :- @AbuSChowdhury'

