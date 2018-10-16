# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:31:38 2018

@author: achowdhury
"""
# Chap 1
'''
A simple scatter plot
In this example, you're going to make a scatter plot of female literacy vs fertility using data from the European Environmental Agency. This dataset highlights that countries with low female literacy have high birthrates. The x-axis data has been loaded for you as fertility and the y-axis data has been loaded as female_literacy.
Your job is to create a figure, assign x-axis and y-axis labels, and plot female_literacy vs fertility using the circle glyph.
After you have created the figure, in this exercise and the ones to follow, play around with it! Explore the different options available to you on the tab to the right, such as "Pan", "Box Zoom", and "Wheel Zoom". You can click on the question mark sign for more details on any of these tools.
Note: You may have to scroll down to view the lower portion of the figure.

Import the figure function from bokeh.plotting, and the output_file and show functions from bokeh.io.
Create the figure p with figure(). It has two parameters: x_axis_label and y_axis_label.
Add a circle glyph to the figure p using the function p.circle() where the inputs are, in order, the x-axis data and y-axis data.
Use the output_file() function to specify the name 'fert_lit.html' for the output file.
Create and display the output file using show() and passing in the figure p.
'''
import pandas as pd
data = pd.read_csv('C:/scripts/literacy_birth_rate.csv')

data.columns
import numpy as np

fertility=data.fertility
female_literacy=data.female_literacy

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label ='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility, female_literacy)

# Call the output_file() function and specify the name of the file
output_file('c:/scripts/fert_lit.html')

# Display the plot
show(p)

########################

'''
A scatter plot with different shapes
By calling multiple glyph functions on the same figure object, we can overlay multiple data sets in the same figure.
In this exercise, you will plot female literacy vs fertility for two different regions, Africa and Latin America. Each set of x and y data has been loaded separately for you as fertility_africa, female_literacy_africa, fertility_latinamerica, and female_literacy_latinamerica.
Your job is to plot the Latin America data with the circle() glyph, and the Africa data with the x() glyph.
figure has already been imported for you from bokeh.plotting.

Create the figure p with the figure() function. It has two parameters: x_axis_label and y_axis_label.
Add a circle glyph to the figure p using the function p.circle() where the inputs are the x and y data from Latin America: fertility_latinamerica and female_literacy_latinamerica.
Add an x glyph to the figure p using the function p.x() where the inputs are the x and y data from Africa: fertility_africa and female_literacy_africa.
The code to create, display, and specify the name of the output file has been written for you, so after adding the x glyph, hit 'Submit Answer' to view the figure.
'''
# Create the figure: p
p = figure(x_axis_label='fertility', y_axis_label='female_literacy (% population)')

fertility_africa=[5.172999999999999,
 2.8160000000000003,
 5.211,
 5.9079999999999995,
 2.505,
 5.52,
 4.058,
 4.859,
 2.342,
 6.254,
 2.334,
 4.22,
 4.967,
 4.513999999999999,
 4.62,
 4.541,
 5.6370000000000005,
 5.841,
 5.455,
 7.069,
 5.405,
 5.737,
 3.363,
 4.89,
 6.081,
 1.841,
 5.329,
 5.33,
 5.377999999999999,
 4.45,
 4.166,
 2.642,
 5.165,
 4.5280000000000005,
 4.697,
 5.011,
 4.388,
 3.29,
 3.264,
 2.822,
 4.968999999999999,
 5.659,
 3.24,
 1.7919999999999998,
 3.45,
 5.2829999999999995,
 3.885,
 2.6630000000000003,
 3.718]


female_literacy_africa=[48.8,
 57.8,
 22.8,
 56.1,
 88.1,
 66.3,
 59.6,
 82.8,
 63.9,
 66.8,
 44.1,
 59.3,
 40.1,
 44.3,
 65.3,
 67.8,
 57.0,
 21.6,
 65.8,
 15.1,
 18.2,
 61.0,
 88.8,
 33.0,
 21.9,
 71.0,
 26.4,
 66.1,
 28.1,
 59.9,
 53.7,
 81.3,
 28.9,
 54.5,
 41.1,
 53.0,
 49.5,
 87.7,
 95.1,
 83.5,
 34.3,
 36.5,
 83.2,
 84.8,
 85.6,
 89.1,
 67.8,
 79.3,
 83.3]


fertility_latinamerica=[1.827,
 2.156,
 2.404,
 2.2230000000000003,
 2.53,
 2.498,
 1.926,
 4.018,
 2.513,
 1.505,
 2.612,
 3.3710000000000004,
 3.19,
 2.977,
 2.295,
 2.6830000000000003,
 1.943,
 2.516,
 2.089,
 2.362,
 1.6469999999999998,
 2.373,
 3.3710000000000004,
 1.732]

female_literacy_latinamerica=[90.2,
 91.5,
 93.4,
 97.7,
 84.6,
 94.9,
 98.7,
 68.7,
 81.7,
 99.8,
 88.3,
 86.0,
 83.5,
 93.5,
 81.4,
 77.9,
 96.2,
 92.8,
 98.5,
 90.8,
 98.2,
 88.4,
 96.5,
 98.0]

# Add a circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica)

# Add an x glyph to the figure p
p.x(fertility_africa, female_literacy_africa)

# Specify the name of the file
output_file('fert_lit_separate.html')

# Display the plot
show(p)

######################

'''
Customizing your scatter plots
The three most important arguments to customize scatter glyphs are color, size, and alpha. Bokeh accepts colors as hexadecimal strings, tuples of RGB values between 0 and 255, and any of the 147 CSS color names. Size values are supplied in screen space units with 100 meaning the size of the entire figure.
The alpha parameter controls transparency. It takes in floating point numbers between 0.0, meaning completely transparent, and 1.0, meaning completely opaque.
In this exercise, you'll plot female literacy vs fertility for Africa and Latin America as red and blue circle glyphs, respectively.

Using the Latin America data (fertility_latinamerica and female_literacy_latinamerica), add a blue circle glyph of size=10 and alpha=0.8 to the figure p. To do this, you will need to specify the color, size and alpha keyword arguments inside p.circle().
Using the Africa data (fertility_africa and female_literacy_africa), add a red circle glyph of size=10 and alpha=0.8 to the figure p.
'''
# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, color='blue', size=10, alpha=0.8)

# Add a red circle glyph to the figure p
p.circle(fertility_africa, female_literacy_africa, color='red', size=10, alpha=0.8)

# Specify the name of the file
output_file('fert_lit_separate_colors.html')

# Display the plot
show(p)


##########################

'''
Lines
We can draw lines on Bokeh plots with the line() glyph function.
In this exercise, you'll plot the daily adjusted closing price of Apple Inc.'s stock (AAPL) from 2000 to 2013.
The data points are provided for you as lists. 
date is a list of datetime objects to plot on the x-axis and 
price is a list of prices to plot on the y-axis.
Since we are plotting dates on the x-axis, you must add x_axis_type='datetime' when creating the figure object.

Import the figure function from bokeh.plotting.
Create a figure p using the figure() function with x_axis_type set to 'datetime'. The other two parameters are x_axis_label and y_axis_label.
Plot date and price along the x- and y-axes using p.line().
'''

#not display

import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/aapl.csv')

data.columns
data.info()

import numpy as np

date = data.index
price = data.close

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create a figure with x_axis_type="datetime": p
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')

# Plot date along the x axis and price along the y axis
p.line(date, price)

# Specify the name of the output file and show the result
output_file('line.html')
show(p)


############################


'''
Lines and markers
Lines and markers can be combined by plotting them separately using the same data points.
In this exercise, you'll plot a line and circle glyph for the AAPL stock prices. Further, you'll adjust the fill_color keyword argument of the circle() glyph function while leaving the line_color at the default value.
The date and price lists are provided. The Bokeh figure object p that you created in the previous exercise has also been provided.
INSTRUCTIONS
100XP
Plot date along the x-axis and price along the y-axis with p.line().
With date on the x-axis and price on the y-axis, use p.circle() to add a 'white' circle glyph of size 4. To do this, you will need to specify the fill_color and size arguments.
'''
# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create a figure with x_axis_type='datetime': p
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')

# Plot date along the x-axis and price along the y-axis
p.line(date, price)

# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p.circle(date, price, fill_color='white', size=4)

# Specify the name of the output file and show the result
output_file('line2.html')
show(p)


################################

'''
Patches
In Bokeh, extended geometrical shapes can be plotted by using the patches() glyph function. The patches glyph takes as input a list-of-lists collection of numeric values specifying the vertices in x and y directions of each distinct patch to plot.
In this exercise, you will plot the state borders of Arizona, Colorado, New Mexico and Utah. The latitude and longitude vertices for each state have been prepared as lists.
Your job is to plot longitude on the x-axis and latitude on the y-axis. The figure object has been created for you as p.

Create a list of the longitude positions for each state as x. This has already been done for you.
Create a list of the latitude positions for each state as y. The variable names for the latitude positions are az_lats, co_lats, nm_lats, and ut_lats.
Use p.patches() to add the patches glyph to the figure p. Supply the x and y lists as arguments along with a line_color of 'white'.
'''
# Create a list of az_lons, co_lons, nm_lons and ut_lons: x
x = [az_lons, co_lons, nm_lons, ut_lons]

# Create a list of az_lats, co_lats, nm_lats and ut_lats: y
y = [az_lats, co_lats, nm_lats, ut_lats]

# Add patches to figure p with line_color=white for x and y
p.patches(x, y, line_color='white')

# Specify the name of the output file and show the result
output_file('four_corners.html')
show(p)

######################

'''
Plotting data from NumPy arrays
In the previous exercises, you made plots using data stored in lists. You learned that Bokeh can plot both numbers and datetime objects.
In this exercise, you'll generate NumPy arrays using np.linspace() and np.cos() and plot them using the circle glyph.
np.linspace() is a function that returns an array of evenly spaced numbers over a specified interval. For example, np.linspace(0, 10, 5) returns an array of 5 evenly spaced samples calculated over the interval [0, 10]. np.cos(x) calculates the element-wise cosine of some array x.
For more information on NumPy functions, you can refer to the NumPy User Guide and NumPy Reference.
The figure p has been provided for you.

Import numpy as np.
Create an array x using np.linspace() with 0, 5, and 100 as inputs.
Create an array y using np.cos() with x as input.
Add circles at x and y using p.circle().
'''
# Import numpy as np
import numpy as np

# Create array using np.linspace: x
x = np.linspace(0, 5, 100)

# Create array using np.cos: y
y = np.cos(x)
p = figure()# Add circles at x and y
p.circle(x, y)

# Specify the name of the output file and show the result
output_file('numpy.html')
show(p)
######################

'''
Plotting data from Pandas DataFrames
You can create Bokeh plots from Pandas DataFrames by passing column selections to the glyph functions.
Bokeh can plot floating point numbers, integers, and datetime data types. In this example, you will read a CSV file containing information on 392 automobiles manufactured in the US, Europe and Asia from 1970 to 1982.
The CSV file is provided for you as 'auto.csv'.
Your job is to plot miles-per-gallon (mpg) vs horsepower (hp) by passing Pandas column selections into the p.circle() function. Additionally, each glyph will be colored according to values in the color column.
INSTRUCTIONS
100XP
Import pandas as pd.
Use the read_csv() function of pandas to read in 'auto.csv' and store it in the DataFrame df.
Import figure from bokeh.plotting.
Use the figure() function to create a figure p with the x-axis labeled 'HP' and the y-axis labeled 'MPG'.
Plot mpg (on the y-axis) vs hp (on the x-axis) by color using p.circle(). Note that the x-axis should be specified before the y-axis inside p.circle(). You will need to use Pandas DataFrame indexing to pass in the columns. For example, to access the color column, you can use df['color'], and then pass it in as an argument to the color parameter of p.circle(). Also specify a size of 10.
'''
# Import pandas as pd
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('C:/scripts/bokeh/auto-mpg.csv')

df.head()
df.info()
df.index
df.columns
df['hp'].head()
df['mpg'].head()

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create the figure: p
p = figure(x_axis_label='HP', y_axis_label='MPG')

# Plot mpg vs hp by color
p.circle(df['hp'], df['mpg'], color=df['color'], size=10)

# Specify the name of the output file and show the result
output_file('C:/scripts/bokeh/auto-mpg-df.html')
show(p)

#######################

'''
The Bokeh ColumnDataSource (continued)
You can create a ColumnDataSource object directly from a Pandas DataFrame by passing the DataFrame to the class initializer.
In this exercise, we have imported pandas as pd and read in a data set containing all Olympic medals awarded in the 100 meter sprint from 1896 to 2012. A color column has been added indicating the CSS colorname we wish to use in the plot for every data point.
Your job is to import the ColumnDataSource class, create a new ColumnDataSource object from the DataFrame df, and plot circle glyphs with 'Year' on the x-axis and 'Time' on the y-axis. Color each glyph by the color column.
The figure object p has already been created for you.

Import the ColumnDataSource class from bokeh.plotting.
Use the ColumnDataSource() function to make a new ColumnDataSource object called source from the DataFrame df.
Use p.circle() to plot circle glyphs of size=8 on the figure p with 'Year' on the x-axis and 'Time' on the y-axis. Be sure to also specify source=source and color='color' so that the ColumnDataSource object is used and each glyph is colored by the color column.
'''

# Import pandas as pd
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('C:/scripts/bokeh/sprint.csv')

df.head()
df.info()
df.index
df.columns
df['Year'].head()
df['Time'].head()

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource: source
source = ColumnDataSource(df)

#source.data
source.column_names

# Create the figure: p
p = figure(title=str('This data containing all Olympic medals awarded in 100 meter sprint from 1896-2012'), x_axis_label='YEAR', y_axis_label='TIME (Sec)')
p.legend.border_line_color = None
p.legend.location = (0, 50)


# Add circle glyphs to the figure p
p.circle(x='Year', y='Time', color='color', size=8, alpha=.8, source=source)

# Specify the name of the output file and show the result
output_file('C:/scripts/bokeh/sprint.html')
show(p)

#################################

'''
Selection and non-selection glyphs
In this exercise, you're going to add the box_select tool to a figure and change the selected and non-selected circle glyph properties so that selected glyphs are red and non-selected glyphs are transparent blue.
You'll use the ColumnDataSource object of the Olympic Sprint dataset you made in the last exercise. It is provided to you with the name source.
After you have created the figure, be sure to experiment with the Box Select tool you added! As in previous exercises, you may have to scroll down to view the lower portion of the figure.

Create a figure p with an x-axis label of 'Year', y-axis label of 'Time', and the 'box_select' tool. To add the 'box_select' tool, you have to specify the keyword argument tools='box_select' inside the figure() function.
Now that you have added 'box_select' to p, add in circle glyphs with p.circle() such that the selected glyphs are red and non-selected glyphs are transparent blue. This can be done by specifying 'red' as the argument to selection_color and 0.1 to nonselection_alpha. Remember to also pass in the arguments for the x ('Year'), y ('Time'), and source parameters of p.circle().
Click 'Submit Answer' to output the file and show the figure.
'''

import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('C:/scripts/bokeh/sprint.csv')

df.head()
df.info()
df.index
df.columns
df['Year'].head()
df['Time'].head()

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource: source
source = ColumnDataSource(df)

#source.data
source.column_names

# Create a figure with the "box_select" tool: p
p = figure(title=str('This data containing all Olympic medals awarded in 100 meter sprint from 1896-2012'), x_axis_label = 'Year', y_axis_label='Time', tools='box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle(x='Year', y='Time', source=source, selection_color='red', nonselection_alpha=0.1)

# Specify the name of the output file and show the result
output_file('C:/scripts/bokeh/selection_glyph.html')
show(p)

#######################

'''
Hover glyphs
Now let's practice using and customizing the hover tool.
In this exercise, you're going to plot the blood glucose levels for an unknown patient. The blood glucose levels were recorded every 5 minutes on October 7th starting at 3 minutes past midnight.
The date and time of each measurement are provided to you as x and the blood glucose levels in mg/dL are provided as y.
A bokeh figure is also provided in the workspace as p.
Your job is to add a circle glyph that will appear red when the mouse is hovered near the data points. You will also add a customized hover tool object to the plot.
When you're done, play around with the hover tool you just created! Notice how the points where your mouse hovers over turn red.

Import HoverTool from bokeh.models.
Add a circle glyph to the existing figure p for x and y with a size of 10, fill_color of 'grey', alpha of 0.1, line_color of None, hover_fill_color of 'firebrick', hover_alpha of 0.5, and hover_line_color of 'white'.
Use the HoverTool() function to create a HoverTool called hover with tooltips=None and mode='vline'.
Add the HoverTool hover to the figure p using the p.add_tools() function.
'''

import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('C:/scripts/bokeh/glucose.csv')

df.head()
df.info()
df.index
df.columns
df['isig'].head()
df['datetime'].head()

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource: source
source = ColumnDataSource(df)

#source.data
source.column_names

# Create a figure with the "box_select" tool: p
p = figure(title=str('plot the blood glucose levels for an unknown patient.'), x_axis_label = 'Time of the day', y_axis_label='Blood glucose (mg/dL)', tools='box_select')

# import the HoverTool
from bokeh.models import HoverTool

# Add circle glyphs to figure p
p.circle(x, y, size=10,
         fill_color='grey', alpha=0.1, line_color=None,
         hover_fill_color='firebrick', hover_alpha=0.5,
         hover_line_color='white')

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode='vline')

# Add the hover tool to the figure p
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('C:/scripts/bokeh/hover_glyph.html')
show(p)

###################################

'''
Colormapping
The final glyph customization we'll practice is using the CategoricalColorMapper to color each glyph by a categorical property.
Here, you're going to use the automobile dataset to plot miles-per-gallon vs weight and color each circle glyph by the region where the automobile was manufactured.
The origin column will be used in the ColorMapper to color automobiles manufactured in the US as blue, Europe as red and Asia as green.
The automobile data set is provided to you as a Pandas DataFrame called df. The figure is provided for you as p.
INSTRUCTIONS
100XP
Import CategoricalColorMapper from bokeh.models.
Convert the DataFrame df to a ColumnDataSource called source. This has already been done for you.
Make a CategoricalColorMapper object called color_mapper with the CategoricalColorMapper() function. It has two parameters here: factors and palette.
Add a circle glyph to the figure p to plot 'mpg' (on the y-axis) vs 'weight' (on the x-axis). Remember to pass in source and 'origin' as arguments to source and legend. For the color parameter, use dict(field='origin', transform=color_mapper).
'''
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('C:/scripts/bokeh/auto-mpg.csv')

df.head()
df.info()
df.index
df.columns
df['hp'].head()
df['mpg'].head()

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create the figure: p
p = figure(title=str('Automobile data: miles-per-gallon vs weight and color each circle glyph by the region'), x_axis_label='                                                          Weight                                     by: Abu Chowdhury', y_axis_label='MPG')

#Import CategoricalColorMapper from bokeh.models
from bokeh.models import CategoricalColorMapper

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(df)

# Make a CategoricalColorMapper object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                      palette=['red', 'green', 'blue'])

# Add a circle glyph to the figure p
p.circle('weight', 'mpg', source=source,
            color=dict(field='origin', transform=color_mapper),
            legend='origin')

# Specify the name of the output file and show the result
output_file('C:/scripts/bokeh/Auto-mpg-colormap.html')
show(p)


#Chap 2


'''
Creating rows of plots
Layouts are collections of Bokeh figure objects.
In this exercise, you're going to create two plots from the Literacy and Birth Rate data set to plot fertility vs female literacy and population vs female literacy.
By using the row() method, you'll create a single layout of the two figures.
Remember, as in the previous chapter, once you have created your figures, you can interact with them in various ways.
In this exercise, you may have to scroll sideways to view both figures in the row layout. Alternatively, you can view the figures in a new window by clicking on the expand icon to the right of the "Bokeh plot" tab.
INSTRUCTIONS
100XP
Import row from the bokeh.layouts module.
Create a new figure p1 using the figure() function and specifying the two parameters x_axis_label and y_axis_label.
Add a circle glyph to p1. The x-axis data is fertility and y-axis data is female_literacy. Be sure to also specify source=source.
Create a new figure p2 using the figure() function and specifying the two parameters x_axis_label and y_axis_label.
Add a circle() glyph to p2 and specify the x_axis_label and y_axis_label parameters.
Put p1 and p2 into a horizontal layout using row().
Click 'Submit Answer' to output the file and show the figure.
'''

import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/literacy_birth_rate.csv')

data.columns
import numpy as np

fertility=data.fertility
female_literacy=data.female_literacy

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(data)

from bokeh.plotting import figure
PLOT_OPTS1 = dict(
        height=400, x_axis_type='log', x_range=(1, 6), y_range=(0, 100),
)  #'''x_axis_type='log','''
# Import row from bokeh.layouts
from bokeh.layouts import row

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)', **PLOT_OPTS1)

# Add a circle glyph to p1
p1.circle('fertility', 'female_literacy', source=source)

PLOT_OPTS2 = dict(
        height=400,  x_axis_type='log', x_range=(100000, 1700000000), y_range=(0, 100),
) # '''x_axis_type='log','''
# Create the second figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)', **PLOT_OPTS2)

# Add a circle glyph to p2
p2.circle('population', 'female_literacy', source=source)

# Put p1 and p2 into a horizontal row: layout
layout = row(p1, p2)

# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/fert_row.html')
show(layout)



################################

'''
Creating columns of plots
In this exercise, you're going to use the column() function to create a single column layout of the two plots you created in the previous exercise.
Figure p1 has been created for you.
In this exercise and the ones to follow, you may have to scroll down to view the lower portion of the figure.
INSTRUCTIONS
100XP
Import column from the bokeh.layouts module.
The figure p1 has been created for you. Create a new figure p2 with an x-axis label of 'population' and y-axis label of 'female_literacy (% population)'.
Add a circle glyph to the figure p2.
Put p1 and p2 into a vertical layout using column().
Click 'Submit Answer' to output the file and show the figure.
'''
# Import column from the bokeh.layouts module
from bokeh.layouts import column

import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/literacy_birth_rate.csv')

data.columns
import numpy as np

fertility=data.fertility
female_literacy=data.female_literacy

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(data)

from bokeh.plotting import figure
PLOT_OPTS1 = dict(
        height=400, x_axis_type='log', x_range=(1, 6), y_range=(0, 100),
)  #'''x_axis_type='log','''
# Import row from bokeh.layouts
from bokeh.layouts import row

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)', **PLOT_OPTS1)

# Add a circle glyph to p1
p1.circle('fertility', 'female_literacy', source=source)

PLOT_OPTS2 = dict(
        height=400,  x_axis_type='log', x_range=(100000, 1700000000), y_range=(0, 100),
) # '''x_axis_type='log','''
# Create the second figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)', **PLOT_OPTS2)

# Add a circle glyph to p2
p2.circle('population', 'female_literacy', source=source)

# Put plots p1 and p2 in a column: layout
layout = column(p1,p2)

# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/fert_column.html')
show(layout)

##################

'''
Nesting rows and columns of plots
You can create nested layouts of plots by combining row and column layouts.
In this exercise, you'll make a 3-plot layout in two rows using the auto-mpg data set.
Three plots have been created for you of average mpg vs year, mpg vs hp, and mpg vs weight.
Your job is to use the column() and row() functions to make a two-row layout where the first row will have only the average mpg vs year plot and the second row will have mpg vs hp and mpg vs weight plots as columns.
By using the sizing_mode argument, you can scale the widths to fill the whole figure.
INSTRUCTIONS
100XP
Import row and column from bokeh.layouts.
Create a column layout called row2 with the figures mpg_hp and mpg_weight in a list and set sizing_mode='scale_width'.
Create a row layout called layout with the figure avg_mpg and the column layout row2 in a list and set sizing_mode='scale_width'.
'''

import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('C:/scripts/bokeh/auto-mpg.csv')

df.head()
df.info()
df.index
df.columns
df['hp'].head()
df['mpg'].head()

# =============================================================================
# # Import figure from bokeh.plotting
# from bokeh.plotting import figure
# 
# # Create the figure: p
# p = figure(x_axis_label='HP', y_axis_label='MPG')
# 
# # Plot mpg vs hp by color
# p.circle(df['hp'], df['mpg'], color=df['color'], size=10)
# 
# =============================================================================
# Import column and row from bokeh.layouts
from bokeh.layouts import column, row

# Make a column layout that will be used as the second row: row2
row2 = column([mpg_hp, mpg_weight], sizing_mode='scale_width')

# Make a row layout that includes the above column layout: layout
layout = row([avg_mpg, row2], sizing_mode='scale_width')

# Specify the name of the output_file and show the result
output_file('layout_custom.html')
show(layout)


#########################

'''
Creating gridded layouts
Regular grids of Bokeh plots can be generated with gridplot.
In this example, you're going to display four plots of fertility vs female literacy for four regions: Latin America, Africa, Asia and Europe.
Your job is to create a list-of-lists for the four Bokeh plots that have been provided to you as p1, p2, p3 and p4. The list-of-lists defines the row and column placement of each plot.
INSTRUCTIONS
100XP
Import gridplot from the bokeh.layouts module.
Create a list called row1 containing plots p1 and p2.
Create a list called row2 containing plots p3 and p4.
Create a gridplot using row1 and row2. You will have to pass in row1 and row2 in the form of a list.
'''

import pandas as pd
data = pd.read_csv('C:/scripts/literacy_birth_rate.csv')

data.columns
import numpy as np

fertility=data.fertility
female_literacy=data.female_literacy

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label ='female_literacy (% population)')

# Add a circle glyph to the figure p
p1.circle(fertility, female_literacy)

import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('C:/scripts/bokeh/sprint.csv')

df.head()
df.info()
df.index
df.columns
df['Year'].head()
df['Time'].head()

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource: source
source = ColumnDataSource(df)

#source.data
source.column_names

# Create a figure with the "box_select" tool: p
p2 = figure(title=str('This data containing all Olympic medals awarded in 100 meter sprint from 1896-2012'), x_axis_label = 'Year', y_axis_label='Time', tools='box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
p2.circle(x='Year', y='Time', source=source, selection_color='red', nonselection_alpha=0.1)


from bokeh.layouts import column

import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/literacy_birth_rate.csv')

data.columns
import numpy as np

fertility=data.fertility
female_literacy=data.female_literacy


# Convert df to a ColumnDataSource: source
source = ColumnDataSource(data)

EUR=(data.Continent=='EUR')
# Filter DataFrame
ASI=data[data['Continent'].isin(['ASI'])]
EUR=data[data['Continent'].isin(['EUR'])]
LAT=data[data['Continent'].isin(['LAT'])]
AF=data[data['Continent'].isin(['AF'])]


from bokeh.plotting import figure
PLOT_OPTS = dict(
        height=400, x_axis_type='log', x_range=(.5, 6), y_range=(0, 100),
)  #'''x_axis_type='log','''
# Import row from bokeh.layouts
from bokeh.layouts import row

# Create the first figure: p1
p3 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)', **PLOT_OPTS)

# Add a circle glyph to p1
p3.circle('fertility', 'female_literacy', source=source)

PLOT_OPTS4 = dict(
        height=400,  x_axis_type='log', x_range=(100000, 1700000000), y_range=(0, 100),
) # '''x_axis_type='log','''
# Create the second figure: p2
p4 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)', **PLOT_OPTS4)

# Add a circle glyph to p2
p4.circle('population', 'female_literacy', source=source)


# Import gridplot from bokeh.layouts
from bokeh.layouts import gridplot

# Create a list containing plots p1 and p2: row1
row1 = [p1,p2]

# Create a list containing plots p3 and p4: row2
row2 = [p3,p4]

# Create a gridplot using row1 and row2: layout
layout = gridplot([row1,row2])

# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/grid.html')
show(layout)

#########################



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
        height=500, width=600, x_axis_type='log', x_range=(.25, 6.60), y_range=(10, 100)
)  #'''x_axis_type='log','''  y_axis_type='log',
# Import row from bokeh.layouts
from bokeh.layouts import row

# Create the first figure: p1
p1 = figure(title=str('Asia :       The Literacy and Birth Rate data set to plot fertility vs female literacy.'), x_axis_label='                           fertility (children per woman)                   @AbuSChowdhury', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p2 = figure(title=str('Europe :        The Literacy and Birth Rate data set to plot fertility vs female literacy.'), x_axis_label='                            fertility (children per woman)                   @AbuSChowdhury', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p3 = figure(title=str('Latin America :       The Literacy and Birth Rate data set to plot fertility vs female literacy.'), x_axis_label='                           fertility (children per woman)                   @AbuSChowdhury', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p4 = figure(title=str('Africa :        The Literacy and Birth Rate data set to plot fertility vs female literacy.'), x_axis_label='                           fertility (children per woman)                   @AbuSChowdhury', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p5 = figure(title=str('North America :       The Literacy and Birth Rate data set to plot fertility vs female literacy.'), x_axis_label='                           fertility (children per woman)                   @AbuSChowdhury', y_axis_label='female_literacy (% population)', **PLOT_OPTS)
p6 = figure(title=str('Australia          The Literacy and Birth Rate data set to plot fertility vs female literacy.'), x_axis_label='                           fertility (children per woman)                   @AbuSChowdhury', y_axis_label='female_literacy (% population)', **PLOT_OPTS)


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
layout = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5, tab6])

# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/female_literacy_tabs_panel.html')
show(layout)

######################################

'''
Linked axes
Linking axes between plots is achieved by sharing range objects.
In this exercise, you'll link four plots of female literacy vs fertility so that when one plot is zoomed or dragged, one or more of the other plots will respond.
The four plots p1, p2, p3 and p4 along with the layout that you created in the last section have been provided for you.
Your job is link p1 with the three other plots by assignment of the .x_range and .y_range attributes.
After you have linked the axes, explore the plots by clicking and dragging along the x or y axes of any of the plots, and notice how the linked plots change together.
INSTRUCTIONS
100XP
Link the x_range of p2 to p1.
Link the y_range of p2 to p1.
Link the x_range of p3 to p1.
Link the y_range of p4 to p1.
Click 'Submit Answer' to output the file and show the figure.
'''
# Link the x_range of p2 to p1: p2.x_range
p2.x_range = p1.x_range

# Link the y_range of p2 to p1: p2.y_range
p2.y_range = p1.y_range

# Link the x_range of p3 to p1: p3.x_range
p3.x_range = p1.x_range

# Link the y_range of p4 to p1: p4.y_range
p4.y_range = p1.y_range

# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/female_literacy_linked_range.html')
show(layout)

###############

'''
Linked brushing
By sharing the same ColumnDataSource object between multiple plots, selection tools like BoxSelect and LassoSelect will highlight points in both plots that share a row in the ColumnDataSource.
In this exercise, you'll plot female literacy vs fertility and population vs fertility in two plots using the same ColumnDataSource.
After you have built the figure, experiment with the Lasso Select and Box Select tools. Use your mouse to drag a box or lasso around points in one figure, and notice how points in the other figure that share a row in the ColumnDataSource also get highlighted.
Before experimenting with the Lasso Select, however, click the Bokeh plot pop-out icon to pop out the figure so that you can definitely see everything that you're doing.
INSTRUCTIONS
100XP
Create a ColumnDataSource object called source from the data DataFrame.
Create a new figure p1 using the figure() function. In addition to specifying the parameters x_axis_label and y_axis_label, you will also have to specify the BoxSelect and LassoSelect selection tools with tools='box_select,lasso_select'.
Add a circle glyph to p1. The x-axis data is fertility and y-axis data is female literacy. Be sure to also specify source=source.
Create a second figure p2 similar to how you created p1.
Add a circle glyph to p2. The x-axis data is fertility and y-axis data is population. Be sure to also specify source=source.
Create a row layout of figures p1 and p2.
'''
# Import output_file and show from bokeh.io
from bokeh.io import output_file, show
# Import figure from bokeh.plotting
from bokeh.plotting import figure
from bokeh.layouts import column
# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/literacy_birth_rate.csv')

data.columns
import numpy as np

# Create ColumnDataSource: source
source = ColumnDataSource(data)

ASI=data[data['Continent'].isin(['ASI'])]
EUR=data[data['Continent'].isin(['EUR'])]
LAT=data[data['Continent'].isin(['LAT'])]
AF=data[data['Continent'].isin(['AF'])]
NAM=data[data['Continent'].isin(['NAM'])]
OCE=data[data['Continent'].isin(['OCE'])]

ALL=data[data['Continent'].isin(['ASI', 'EUR', 'LAT', 'AF', 'NAM', 'OCE'])]

from bokeh.plotting import figure
PLOT_OPTS1 = dict(
        height=400, width=400, x_axis_type='log', x_range=(.5, 7.15), y_range=(10, 100)
) 

PLOT_OPTS2 = dict(
        height=400, width=400, y_axis_type='log', x_range=(.5, 7.15), y_range=(10000, 1500000000)
)
# Create the first figure: p1
p1 = figure(title=str('Fertility vs. Female Literacy'), x_axis_label='fertility (children per woman)', y_axis_label='female literacy (% population)',
            tools='box_select,lasso_select', **PLOT_OPTS1)

# Add a circle glyph to p1
p1.circle('fertility', 'female_literacy', source=ALL)

# Create the second figure: p2
p2 = figure(title=str('Fertility vs. Population            - @AbuSChowdhury'), x_axis_label='fertility (children per woman)', y_axis_label='population (millions)',
            tools='box_select,lasso_select', **PLOT_OPTS2)

# Add a circle glyph to p2
p2.circle('fertility', 'population', source=ALL)

# Create row layout of figures p1 and p2: layout
layout = row(p1,p2)

# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/female_literacy_linked_brush.html')
show(layout)

############################

'''
How to create legends
Legends can be added to any glyph by using the legend keyword argument.
In this exercise, you will plot two circle glyphs for female literacy vs fertility in Africa and Latin America.
Two ColumnDataSources called latin_america and africa have been provided.
Your job is to plot two circle glyphs for these two objects with fertility on the x axis and female_literacy on the y axis and add the legend values. The figure p has been provided for you.
INSTRUCTIONS
100XP
Add a red circle glyph to the figure p using the latin_america ColumnDataSource. Specify a size of 10 and legend of Latin America.
Add a blue circle glyph to the figure p using the africa ColumnDataSource. Specify a size of 10 and legend of Africa.
'''

from bokeh.io import output_file, show
# Import figure from bokeh.plotting
from bokeh.plotting import figure
from bokeh.layouts import column
# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

import pandas as pd
data = pd.read_csv('C:/scripts/bokeh/literacy_birth_rate.csv')

data.columns
import numpy as np

# Create ColumnDataSource: source
source = ColumnDataSource(data)

ASI=data[data['Continent'].isin(['ASI'])]
EUR=data[data['Continent'].isin(['EUR'])]
LAT=data[data['Continent'].isin(['LAT'])]
AF=data[data['Continent'].isin(['AF'])]
NAM=data[data['Continent'].isin(['NAM'])]
OCE=data[data['Continent'].isin(['OCE'])]

ALL=data[data['Continent'].isin(['ASI', 'EUR', 'LAT', 'AF', 'NAM', 'OCE'])]

from bokeh.plotting import figure
PLOT_OPTS1 = dict(
        height=500, width=600, x_axis_type='log', x_range=(.5, 7.15), y_range=(10, 100)
) 

PLOT_OPTS2 = dict(
        height=500, width=600, y_axis_type='log', x_range=(.5, 7.15), y_range=(10000, 1500000000)
)
# Create the first figure: p1
p1 = figure(title=str('Fertility vs. Female Literacy'), x_axis_label='fertility (children per woman)', y_axis_label='female literacy (% population)',
            tools='box_select,lasso_select', **PLOT_OPTS1)

# Add the first circle glyph to the figure p
p1.circle('fertility', 'female_literacy', source=ASI, size=10, color='red', legend='Asia')
p1.circle('fertility', 'female_literacy', source=EUR, size=10, color='blue', legend='Europe')
p1.circle('fertility', 'female_literacy', source=LAT, size=10, color='pink', legend='Latin America')
p1.circle('fertility', 'female_literacy', source=AF, size=10, color='purple', legend='Africa')
p1.circle('fertility', 'female_literacy', source=NAM, size=10, color='green', legend='North America')
p1.circle('fertility', 'female_literacy', source=OCE, size=10, color='brown', legend='Australia')

# Create the second figure: p2
p2 = figure(title=str('Fertility vs. Population            - @AbuSChowdhury'), x_axis_label='fertility (children per woman)', y_axis_label='population (millions)',
            tools='box_select,lasso_select', **PLOT_OPTS2)

# Create row layout of figures p1 and p2: layout

p2.circle('fertility', 'population', source=ASI, size=10, color='red', legend='Asia')
p2.circle('fertility', 'population', source=EUR, size=10, color='blue', legend='Europe')
p2.circle('fertility', 'population', source=LAT, size=10, color='pink', legend='Latin America')
p2.circle('fertility', 'population', source=AF, size=10, color='purple', legend='Africa')
p2.circle('fertility', 'population', source=NAM, size=10, color='green', legend='North America')
p2.circle('fertility', 'population', source=OCE, size=10, color='brown', legend='Australia')

layout = row(p1,p2)

# Specify the name of the output_file and show the result
output_file('C:/scripts/bokeh/fert_lit_groups.html')
show(p)


































































































