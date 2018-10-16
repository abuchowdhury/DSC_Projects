# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:12:34 2018

@author: achow
"""

from bokeh.io import output_file, show
# Import figure from bokeh.plotting
from bokeh.plotting import figure
from bokeh.layouts import row
# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

#from bokeh.io import curdoc
from bokeh.models import (
    LinearInterpolator,
    CategoricalColorMapper,
    HoverTool
)

from bokeh.palettes import Spectral11

import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/literacy_birth_rate.csv')

data.columns
#import numpy as np

# Create ColumnDataSource: source
source = ColumnDataSource(data)

ASI=data[data['Continent'].isin(['ASI'])]
EUR=data[data['Continent'].isin(['EUR'])]
LAT=data[data['Continent'].isin(['LAT'])]
AF=data[data['Continent'].isin(['AF'])]
NAM=data[data['Continent'].isin(['NAM'])]
OCE=data[data['Continent'].isin(['OCE'])]

#ALL=data[data['Continent'].isin(['ASI', 'EUR', 'LAT', 'AF', 'NAM', 'OCE'])]

PLOT_OPTS1 = dict(
        height=700, width=600, x_axis_type='log', y_axis_type='log', x_range=(.5, 7.15), y_range=(10, 100)
) 

PLOT_OPTS2 = dict(
        height=700, width=600, x_axis_type='log', y_axis_type='log', x_range=(.5, 7.15), y_range=(10000, 1500000000)
)
# Create the first figure: p1
p1 = figure(title=str('Fertility vs. Female Literacy'), x_axis_label='fertility (children per woman)', y_axis_label='female literacy (% population)',
            toolbar_location='above', 
    tools=[HoverTool(show_arrow=False, line_policy='next', tooltips=[
    ('Continent     : ', '@Continent'),
    ('Country    : ', '@Country'),
    ('Population : ', '@population'),
      ('Female_literacy    : ', '@female_literacy'),
    ('Fertility : ', '@fertility')  
    ])], **PLOT_OPTS1)

size_mapper = LinearInterpolator(
    x=[data.population.min(), data.population.max()],
    y=[5, 35]
)
color_mapper = CategoricalColorMapper(
    factors=list(data.Continent.unique()),
    palette=Spectral11,
)

# Add the first circle glyph to the figure p
p1.circle('fertility', 'female_literacy', size={'field': 'population', 'transform': size_mapper},
    color={'field': 'Continent', 'transform': color_mapper},
    alpha=0.6,
    source=source,
    legend='Continent')

# =============================================================================
# p1.circle('fertility', 'female_literacy', source=EUR, size=7, alpha=.5, color='blue', legend='Europe')
# p1.circle('fertility', 'female_literacy', source=LAT, size=7, alpha=.5, color='black', legend='Latin America')
# p1.circle('fertility', 'female_literacy', source=AF, size=7, alpha=.5, color='purple', legend='Africa')
# p1.circle('fertility', 'female_literacy', source=NAM, size=7, alpha=.5, color='green', legend='North America')
# p1.circle('fertility', 'female_literacy', source=OCE, size=7, alpha=.5, color='brown', legend='Australia')
# 
# =============================================================================
# Create the second figure: p2
p2 = figure(title=str('Fertility vs. Population                                       - @AbuSChowdhury'), x_axis_label='fertility (children per woman)', y_axis_label='population (millions)',
            toolbar_location='above', 
    tools=[HoverTool(show_arrow=False, line_policy='next', tooltips=[
    ('Continent     : ', '@Continent'),
    ('Country    : ', '@Country'),
    ('Population : ', '@population'),
      ('Female_literacy    : ', '@female_literacy'),
    ('Fertility : ', '@fertility')  
    ])], **PLOT_OPTS2)

# Create row layout of figures p1 and p2: layout

p2.circle('fertility', 'population', size={'field': 'population', 'transform': size_mapper},
    color={'field': 'Continent', 'transform': color_mapper},
    alpha=0.6,
    source=source,
    legend='Continent')
# =============================================================================
# p2.circle('fertility', 'population', source=EUR, size=7, alpha=.5, color='blue', legend='Europe')
# p2.circle('fertility', 'population', source=LAT, size=7, alpha=.5, color='black', legend='Latin America')
# p2.circle('fertility', 'population', source=AF, size=7, alpha=.5, color='purple', legend='Africa')
# p2.circle('fertility', 'population', source=NAM, size=7, alpha=.5, color='green', legend='North America')
# p2.circle('fertility', 'population', source=OCE, size=7, alpha=.5, color='brown', legend='Australia')
# 
# =============================================================================
layout = row(p1,p2)

# Specify the name of the output_file and show the result

print('We have created a HoverTool object and display the country and additional info for each circle glyph in the figure. \n')

'''
Positioning and styling legends
Properties of the legend can be changed by using the legend member attribute of a Bokeh figure after the glyphs have been plotted.
In this exercise, you'll adjust the background color and legend location of the female literacy vs fertility plot from the previous exercise.
The figure object p has been created for you along with the circle glyphs.

Use p.legend.location to adjust the legend location to be on the 'bottom_left'.
Use p.legend.background_fill_color to set the background color of the legend to 'lightgray'.
'''
# Assign the legend to the bottom left: p.legend.location
p1.legend.location='bottom_left'
p2.legend.location='bottom_right'

# Fill the legend background with the color 'lightgray': p.legend.background_fill_color
p1.legend.background_fill_color='lightgray'
p2.legend.background_fill_color='lightgray'


'''
Adding a hover tooltip
Working with the HoverTool is easy for data stored in a ColumnDataSource.
In this exercise, you will create a HoverTool object and display the country for each circle glyph in the figure that you created in the last exercise. This is done by assigning the tooltips keyword argument to a list-of-tuples specifying the label and the column of values from the ColumnDataSource using the @ operator.
The figure object has been prepared for you as p.
After you have added the hover tooltip to the figure, be sure to interact with it by hovering your mouse over each point to see which country it represents.
INSTRUCTIONS
100XP
Import the HoverTool class from bokeh.models.
Use the HoverTool() function to create a HoverTool object called hover and set the tooltips argument to be [('Country','@Country')].
Use p.add_tools() with your HoverTool object to add it to the figure.
'''
# =============================================================================
# # Import HoverTool from bokeh.models
# 
# 
# # Create a HoverTool object: hover
# hover = HoverTool(tooltips=[('Country','@Country')])
# 
# # Add the HoverTool object to figure p
# p.add_tools(hover)
# 
# =============================================================================
# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/hover_fert_lit_groups.html')
show(layout)

# =============================================================================
# p = figure(
#     title=str(2010), toolbar_location='above', 
#     tools=[HoverTool(show_arrow=False, line_policy='next', tooltips=[
#     ('Continent     : ', '@Continent'),
#     ('Country    : ', '@country'),
#     ('Population : ', '@population'),
#       ('Female_literacy    : ', '@female_literacy'),
#     ('Fertility : ', '@fertility')  
#     ])],
#     **PLOT_OPTS1)
# =============================================================================

