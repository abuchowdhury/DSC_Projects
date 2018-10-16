



# Import figure from bokeh.plotting
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.palettes import Spectral6

# Import the ColumnDataSource class from bokeh.plotting


from bokeh.io import curdoc
from bokeh.models import (
    LinearInterpolator,
    CategoricalColorMapper,
    HoverTool,
    ColumnDataSource,
    Select
)
from bokeh.palettes import Spectral6

# =============================================================================



import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/literacy_birth_rate.csv')




source = ColumnDataSource(data)


PLOT_OPTS = dict(
        
        
)
source = ColumnDataSource(dict(
    x=data.fertility,
    y=data.female_literacy,
    Country=data.Country,
    Continent=data.Continent,
    population=data.population
    
))

size_mapper = LinearInterpolator(
    x=[data.population.min(), data.population.max()],
    y=[8, 65]
)
color_mapper = CategoricalColorMapper(
    factors=list(data.Continent.unique()),
    palette=Spectral6,
)


# Create ColumnDataSource: source
source = ColumnDataSource(data={
            'x' : data.fertility,
            'y' : data.female_literacy,
       'Country': data.Country,
    'Continent' : data.Continent,
   'population' : data.population
})

# Create a new plot: plot
plot = figure(
    title=str('Gapminder data used to display "Income vs. Life Expectancy" for each country from 1800-2015. Circles ~ Population size     @AbuSChowdhury'), 
    plot_width=700, plot_height=700,
    toolbar_location='above', 
    tools=[HoverTool(show_arrow=False, line_policy='next', tooltips=[
    ('Continent    : ', '@Continent'),
    ('Country    : ', '@Country'),
    ('Female Literacy : ', '@female_literacy'),
    ('Fertility     : ', '@fertility'),
    ('Population : ', '@population')
        ])],
    **PLOT_OPTS)

# Add circles to the plot
plot.circle('x', 'y', size={'field': 'population', 'transform': size_mapper},
    color={'field': 'region', 'transform': color_mapper},
    alpha=0.6,
    source=source,
    legend='Continent')

# Define a callback function: update_plot
def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy': 
        source.data = {
            'x' : data.fertility,
            'y' : data.female_literacy,
       'Country': data.Country,
    'Continent' : data.Continent,
   'population' : data.population
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : data.fertility,
            'y' : data.population
        }

# Create a dropdown Select widget: select    
select = Select(title="distribution", options=['female_literacy', 'population'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)