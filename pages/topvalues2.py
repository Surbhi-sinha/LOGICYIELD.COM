
# Project Description:-
# This project is part of Microsoft Engage Program
# The project based on Developing an application to demonstrate how the Automotive Industry could harness data to take informed decisions via a user friendly Environment(website)
# Here I have demonstrated the use of data analytics in identifying:
# Customer segments, Most popular car specification combination per age group , choice of Cars per age group , state wise cars sale in financial years , and top sellers etc.
# Project by :- Surbhi Sinha(linkedin = 'https://www.linkedin.com/in/surbhi-sinha-554902176/' )


# -------------------------importing libraries ------------------------
import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__,  name="Top lists", top_nav=True)

# df = pd.read_csv('top25sellingCarsInInsdia.csv')
df = pd.read_csv('2020carsSalesdata.csv')


# layout
layout = html.Div([

    dbc.Alert(
    [
        html.H4("Hope You like the project so far!", className="alert-heading"),
        html.P(
            "In this section the You will see the top sellers of car companies"
            
        ),
        html.Hr(),
        html.P(
            "You must have been seeing two blank graph right now!!"
            " First! You need to select the company from the drop down",
            className="mb-0",
        ),
    ],dismissable = True,
),
    html.H2("Top selling cars of Brands", style={'text-align': 'center'}),

    dcc.Dropdown(
        id="find_brand",
        options=[{'label' : x , 'value' :x} for x in df['make'].unique()
        ],
        multi=False,
        value='tata',
        placeholder='select a car company',
        style={'width': "40%", 'margin-left': '5%'},
    ),
    html.Br(),

    html.Div([
        dcc.Graph(id='cars_sales_bar', figure={}, style={
            'width': '200', 'float': 'left', 'margin-left': '7%', 'margin-bottom': '2%' ,}),
        dcc.Graph(id='cars_sales_pie', figure={}, style={
            'width': '100', 'float': 'left', 'margin-left': '7%', 'margin-bottom': '2%'}),
    ], style={'display': 'table', 'width': '100%' , 'height': '100%'}),

    
], style={'background-color': '#bbbbbb'})

# defining the bar chart of sales
def get_sales_bar(company_slctd):
    global df
    comp_df = df.copy()
    comp_df = comp_df[comp_df['make'] == company_slctd]

    fig = px.bar(comp_df, x='model', y='sales', height=500, width=600,
                 title="Sales made by different models of "+company_slctd + " in year 2020")

    return fig

# defining the pir chart of the sales of the company
def get_sales_pie(company_slctd):
    global df
    comp_pie_df = df.copy()
    
    comp_pie_df = comp_pie_df[comp_pie_df['make'] == company_slctd]

    fig = px.pie(comp_pie_df, names='model', values='sales', height=500, width=600,
                 title="Sales made by different models of "+company_slctd + " in year 2020",template="plotly_dark")
    
    return fig

# connections of input and output
@callback([Output(component_id='cars_sales_bar', component_property='figure'),
           Output(component_id='cars_sales_pie', component_property='figure')],
          [Input(component_id='find_brand', component_property='value')]
      )


def the_Callback_func(find_brand):
    fig1 = get_sales_bar(find_brand)
    fig2 = get_sales_pie(find_brand)
    return fig1, fig2
