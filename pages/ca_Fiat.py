
# Project Description:-
# This project is part of Microsoft Engage Program
# The project based on Developing an application to demonstrate how the Automotive Industry could harness data to take informed decisions via a user friendly Environment(website)
# Here I have demonstrated the use of data analytics in identifying:
# Customer segments, Most popular car specification combination per age group , choice of Cars per age group , state wise cars sale in financial years , and top sellers etc.
# Project by :- Surbhi Sinha(linkedin = 'https://www.linkedin.com/in/surbhi-sinha-554902176/' )

import dash
import dash_table
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

#----------------------------------------------------------------
import dash_bootstrap_components as dbc

from .side_bar import sidebar

dash.register_page(
    __name__,
    name="Fiat",
)


df = pd.read_csv('cars_engage_2022_sorted.csv')
df = df[df['Make'] == 'Fiat']

df['Car_length']=df['Length'].apply(lambda x: int(x.split(" ")[0]))

fig1 = px.bar(df , x = 'Model' , y = 'Car_length' , color = 'Model',title='Length Of Car As Per Model')

def layout():
    return dbc.Row(
        [dbc.Col(sidebar(), width=2), dbc.Col(html.Div(htmlwork()), width=10)]
    )



def htmlwork():
    return html.Div([
        html.Div([
            dash_table.DataTable(
            id = 'datatable_id',
            data = df.to_dict('records'), 
            columns= [
                {"name" : i , "id" : i , "deletable" : False} for i in df.columns
            ],
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_deletable=False,
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 10,
            style_table={'overflowX': 'auto'},
            )
        ],className='row'), 
        html.Div([
            dcc.Graph(
                figure={
                    'data' : [
                        {'x' : df["Ex-Showroom_Price"] , 'y' : df["Displacement"] ,'label-x' : 'Car Price','label-y' : 'Engine Displacement' ,'type' : 'bar'}
                    ],
                    'layout':{
                        'title' : 'Showroom Price As Per Engine Displacement',
                        'colorway' : ["#5293ff"],
                        'xaxis':{
                            'title' : 'Car Price',
                        },
                        'yaxis' : {
                            'title':'Engine Displacement',
                        }
                    }
                }
            )   
        ]),

        html.Div([
            html.Div([
            dcc.Graph(
                figure={
                    'data' : [
                        {'x' : df["Fuel_Tank_Capacity"] , 'y' : df["Power"] , 'type' : "bar"},
                    ],
                    'layout' : {
                        'title' : 'Comparison of Power /  Fuelcapacity',
                        'colorway' :['#eb0953'],
                        'xaxis':{
                            'title' : 'Fuel Capacity',
                        },
                        'yaxis' : {
                            'title':'Power',
                        },
                        
                    },
                    
                }
            )
        ],style={'width':'40%' , 'float' : 'left',}),


        html.Div([
            dcc.Graph(figure = fig1)
        ],style={'width':'50%' , 'float' : 'left' , 'margin-left' :'2%'})
        
        ])
        
    ])



# ---------------------------------------------------------------- 
