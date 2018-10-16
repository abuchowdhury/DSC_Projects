# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 04:20:00 2018

@author: achow
"""

from bokeh.layouts import column

import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/literacy_birth_rate.csv')

data.columns
import numpy as np

# =============================================================================
# fertility=data.fertility
# female_literacy=data.female_literacy
# =============================================================================
# Convert df to a ColumnDataSource: source
source = ColumnDataSource(data)

#EUR=(data.Continent=='EUR')
# Filter DataFrame
ASI=data[data['Continent'].isin(['ASI'])]
EUR=data[data['Continent'].isin(['EUR'])]
LAT=data[data['Continent'].isin(['LAT'])]
AF=data[data['Continent'].isin(['AF'])]
NAM=data[data['Continent'].isin(['NAM'])]
OCE=data[data['Continent'].isin(['OCE'])]


from bokeh.plotting import figure
PLOT_OPTS = dict(
        height=250, width=350, x_axis_type='log', x_range=(.25, 6.60), y_range=(10, 100)
)  #'''x_axis_type='log','''  y_axis_type='log',
# Import row from bokeh.layouts
from bokeh.layouts import row

# Create the first figure: p1
p1 = figure(title=str('Asia'), x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p2 = figure(title=str('Europe'), x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p3 = figure(title=str('Latin America'), x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p4 = figure(title=str('Africa'), x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p5 = figure(title=str('North America'), x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p6 = figure(title=str('Australia'), x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)', **PLOT_OPTS)


p1.circle('fertility', 'female_literacy', source=ASI)
p2.circle('fertility', 'female_literacy', source=EUR)
p3.circle('fertility', 'female_literacy', source=LAT)
p4.circle('fertility', 'female_literacy', source=AF)
p5.circle('fertility', 'female_literacy', source=NAM)
p6.circle('fertility', 'female_literacy', source=OCE)

# Import gridplot from bokeh.layouts
from bokeh.layouts import gridplot

# Create a list containing plots p1 and p2: row1
row1 = [p1,p2]

# Create a list containing plots p3 and p4: row2
row2 = [p3,p4]

# Create a list containing plots p5 and p46 row3
row3 = [p5,p6]

# Create a gridplot using row1 and row2: layout
layout = gridplot([row1,row2, row3])

# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/female_literacy_grid.html')
show(layout)

##########################

'''
Starting tabbed layouts
Tabbed layouts can be created in Pandas by placing plots or layouts in Panels.
In this exercise, you'll take the four fertility vs female literacy plots from the last exercise and make a Panel() for each.
No figure will be generated in this exercise. Instead, you will use these panels in the next exercise to build and display a tabbed layout.

Import Panel from bokeh.models.widgets.
Create a new panel tab1 with child p1 and a title of 'Latin America'.
Create a new panel tab2 with child p2 and a title of 'Africa'.
Create a new panel tab3 with child p3 and a title of 'Asia'.
Create a new panel tab4 with child p4 and a title of 'Europe'.
Click submit to check your work.
'''
# Import Panel from bokeh.models.widgets
from bokeh.models.widgets import Panel

# Create tab1 from plot p1: tab1
tab1 = Panel(child=p1, title='Asia')

# Create tab2 from plot p2: tab2
tab2 = Panel(child=p2, title='Europe')

# Create tab3 from plot p3: tab3
tab3 = Panel(child=p3, title='Latin America')

# Create tab4 from plot p4: tab4
tab4 = Panel(child=p4, title='Africa')

# Create tab5 from plot p5: tab5
tab5 = Panel(child=p5, title='North America')

# Create tab6 from plot p6: tab6
tab6 = Panel(child=p6, title='Australia')

'''
Displaying tabbed layouts
Tabbed layouts are collections of Panel objects. Using the figures and Panels from the previous two exercises, you'll create a tabbed layout to change the region in the fertility vs female literacy plots.
Your job is to create the layout using Tabs() and assign the tabs keyword argument to your list of Panels. The Panels have been created for you as tab1, tab2, tab3 and tab4.
After you've displayed the figure, explore the tabs you just added! The "Pan", "Box Zoom" and "Wheel Zoom" tools are also all available as before.
INSTRUCTIONS
100XP
Import Tabs from bokeh.models.widgets.
Create a Tabs layout called layout with tab1, tab2, tab3, and tab4.
Click 'Submit Answer' to output the file and show the figure.
'''
# Import Tabs from bokeh.models.widgets
from bokeh.models.widgets import Tabs

# Create a Tabs layout: layout
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])

# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/female_literacy_tabs_panel.html')
show(layout)