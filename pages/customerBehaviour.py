
# Project Description:-
# This project is part of Microsoft Engage Program
# The project based on Developing an application to demonstrate how the Automotive Industry could harness data to take informed decisions via a user friendly Environment(website)
# Here I have demonstrated the use of data analytics in identifying:
# Customer segments, Most popular car specification combination per age group , choice of Cars per age group , state wise cars sale in financial years , and top sellers etc.
# Project by :- Surbhi Sinha(linkedin = 'https://www.linkedin.com/in/surbhi-sinha-554902176/' )


# ---------------------importing libraries---------------------------
from tempfile import template
import dash
from dash import Dash, dcc, html, Input, Output, callback
import dash_table
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import io

buffer = io.StringIO()

import dash_table
import dash_bootstrap_components as dbc


dash.register_page(__name__ ,name = "Customer's Behavior", top_nav = True)
# ---------------------------dataframe ----------------------------

df = pd.read_csv('Indian automoble buying behavour study 1.0.csv')


# ---------------------Figures and charts------------------------------------
fig1 = px.pie(df , values = 'Salary' ,
                    names = 'Profession' ,
                    color = 'Profession',
                    color_discrete_map={
                        'Salaried':'yellow',
                        'Business':'darkblue'}, )
fig1.update_layout(height= 400)

fig2 = px.pie(df , 
            values = 'Salary' ,
            names = 'Marrital Status' ,
             color = 'Salary' ,
             color_discrete_sequence=px.colors.sequential.Sunset)
fig2.update_layout(height= 400)

fig3 = px.pie(df ,
             values = 'Salary' ,
              names = 'Education')
fig3.update_layout(height= 400)

fig4 = px.bar(df ,
             x = 'Age' ,
             y = 'Salary' ,
             color="Age",
             color_discrete_sequence=px.colors.sequential.Sunset )
fig3.update_layout(height= 400)

fig5 = px.bar(df,
             x = 'Age' ,
             y = 'Make' ,
             color = 'Age',
             title='Choice Of Cars As Per Age Group In 1000' )

# ---------------------layouts --------------------
layout = html.Div([
    html.Div([
        html.H4("Car Purchaser's Income Status" , style= {'text-align':'center'}),
        html.P("Income Status of the Indian Citizens as per time of purchasing the Cars in India as a main Source of income." , style ={'text-align':'center'}),
        dcc.Graph( figure = fig1),

    ],style = {'width': '30%' , 'background-color':'#85b1ff' , 'float' : 'left','margin-left':'2%','height':'30%','border-radius':'5%'}),
    
    html.Div([
        html.H4("Car Purchaser's Marital Status" , style= {'text-align':'center'}),
        html.P("Marital Status of the Indian Citizens as per time of purchasing the Cars in India." , style ={'text-align':'center'}),
        dcc.Graph( figure = fig2),

    ],style = {'width': '30%' , 'background-color':'#85b1ff' ,'float' : 'left','margin-left':'2%','height':'30%','border-radius':'5%'}),
    
    html.Div([
        html.H4("Car Purchaser's Education Status" , style= {'text-align':'center'}),
        html.P("Education Status of the Indian Citizens as per time of purchasing the Cars in India." , style ={'text-align':'center'}),
        dcc.Graph( figure = fig3),

    ],style = {'width': '30%' , 'background-color':'#85b1ff' ,'float' : 'left','margin-left':'2%','height':'30%','border-radius':'5%'}),
    
    html.Div([
        html.H4("Salary vs Age Ratio Of The Customers" , style= {'text-align':'center'}),
        html.P("The below data shows the purchase made by Age group." , style ={'text-align':'center'}),
        dcc.Graph( figure = fig4),

    ],style = {'width': '40%' , 'background-color':'#85b1ff' ,'float' : 'left','margin-left':'2%','height':'30%' , 'margin-top':'2%','border-radius':'5%'}),
    
    html.Div([
        html.H4("Car Choice As Per Age Group" , style= {'text-align':'center'}),
        html.P("The below data shows the choice of cars made by Age group." , style ={'text-align':'center'}),
        dcc.Graph( figure = fig5),

    ],style = {'width': '50%' , 'background-color':'#85b1ff' ,'float' : 'left','margin-left':'2%','height':'30%' , 'margin-top':'2%','border-radius':'5%'}),
    
] , style = {'background-color':'	#eeeeee' , 'padding' : '2%' , 'display':'table'}    
)