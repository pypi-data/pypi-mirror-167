"""
Author: Reme Ajayi
License: MIT License
Contains functions for data visualization
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.offline as py
py.init_notebook_mode(connected=True)

def set_size(func):
    def wrapper(*args, **kwargs):
        if "size" in kwargs:
            if kwargs["size"] == 'medium':
                plt.figure(figsize=(12, 6))
            if kwargs["size"] == 'large':
                plt.figure(figsize=(15, 8))
        return func(*args, **kwargs)
    return wrapper

def set_title(func):
    def wrapper(*args, **kwargs):
        if "title" in kwargs:
            plt.title(kwargs["title"], fontsize=20)
        return func(*args, **kwargs)
    return wrapper
    
    
class Plot:
    def __init__(self, data):
        self.data = data
    
class SeabornPlot(Plot):
        def __init__(self, data):
            super().__init__(data)
            sns.set_style("darkgrid")

        @set_size
        @set_title
        def hist(self, size=None, title=None, **kwargs):
            sns.histplot(data=self.data, **kwargs)
            
        @set_size
        @set_title
        def count(self, size=None, title=None, **kwargs):
            sns.countplot(data= self.data, **kwargs)
               
        @set_size
        @set_title    
        def line(self, size=None, title=None, **kwargs):
            sns.lineplot(data=self.data, **kwargs)
       
        @set_size
        @set_title             
        def heatmap(self, correlation, size=None, title=None, **kwargs):
            ax = sns.heatmap(correlation,annot=True,fmt='.3f',linewidths=0.3,annot_kws={"size": 18})
            ax.figure.axes[-1].tick_params(labelsize=18)
            plt.show()

        def show_info(self):
            print("""sample **kwargs 
                     x - for feature on x-axis
                     y - for feature on y-axis
                     (use for features with long names, where possible)
                     hue - Grouping variable that will produce points with different colors
                     title - title of the plot
                     heatmap takes a non-keyworded correlation before kwargs
                     """)
             
class PlotlyPlot(Plot):      
        def box(self, **kwargs):
            fig = px.box(self.data, **kwargs)
            fig.show()
            
        def strip(self, **kwargs):
            fig = px.strip(self.data, **kwargs)
            fig.show()
            
        def line(self, **kwargs):
            fig = px.line(self.data, **kwargs)
            fig.show()       
        def show_info(self):
            print("""sample **kwargs 
                     x - for feature on x-axis
                     y - for feature on y-axis
                     (use for features with long names, where possible)
                     color - Grouping variable that will produce points with different colors
                     title - title of the plot""")
