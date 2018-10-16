# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 22:58:07 2018

@author: achow
"""

import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/gapminder.csv', thousands=',', index_col='Year')

import numpy as np

from bokeh.io import curdoc
from bokeh.models import (
    LinearInterpolator,
    CategoricalColorMapper,
    ColumnDataSource,
    NumeralTickFormatter,
    HoverTool,
)
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
PLOT_OPTS = dict(
        height=800, width=1200,  x_axis_type='log',
        x_range=(100, 100000), y_range=(0, 100),
)
source = ColumnDataSource(dict(
    x=data.loc[1800].income,
    y=data.loc[1800].life,
    country=data.loc[1800].Country,
    population=data.loc[1800].population,
    region=data.loc[1800].region
))

size_mapper = LinearInterpolator(
    x=[data.population.min(), data.population.max()],
    y=[8, 65]
)
color_mapper = CategoricalColorMapper(
    factors=list(data.region.unique()),
    palette=Spectral6,
)

# =============================================================================
# p.add_tools(HoverTool(show_arrow=False, line_policy='next', tooltips=[
#     ('MZ', '@MZ_tip'),
#     ('Rel Intensity', '@Intensity_tip')
# ]))
# =============================================================================



p = figure(
    title=str('Gapminder data used to display "Income vs. Life Expectancy" for each country from 1800-2015. Circles ~ Population size     @AbuSChowdhury'), toolbar_location='above', 
    tools=[HoverTool(show_arrow=False, line_policy='next', tooltips=[
    ('Country    : ', '@country'),
    ('Population : ', '@population'),
    ('Region     : ', '@region'),
    ('Income : ', '@x'),
    ('Life Expectancy     : ', '@y')
        ])],
    **PLOT_OPTS)

p.xaxis[0].axis_label = 'Per Capital Income'
p.yaxis[0].axis_label = 'Life Expectancy'

p.circle(
    x='x', y='y',
    size={'field': 'population', 'transform': size_mapper},
    color={'field': 'region', 'transform': color_mapper},
    alpha=0.6,
    source=source,
    legend='region'
    
)
p.xaxis[0].formatter = NumeralTickFormatter(format="$0,")
p.legend.border_line_color = None
p.legend.location = (0, 50)
p.right.append(p.legend[0])

source.column_names
from bokeh.models import Slider
from bokeh.layouts import widgetbox

def update(attr, old, new):
    # new = year
    year = new
    new_data = dict(
        x=data.loc[year].income,
        y=data.loc[year].life,
        country=data.loc[year].Country,
        region=data.loc[year].region,
        population=data.loc[year].population
    )
    source.data = new_data
    p.title.text = str(year)

#year=data.index
slider = Slider(start=1800, end=2015, step=1, value=1800, title='Year')
slider.on_change('value', update)


from bokeh.layouts import column
layout = column(p, slider)
curdoc().add_root(layout)


