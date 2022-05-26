
# Project Description:-
# This project is part of Microsoft Engage Program
# The project based on Developing an application to demonstrate how the Automotive Industry could harness data to take informed decisions via a user friendly Environment(website)
# Here I have demonstrated the use of data analytics in identifying:
# Customer segments, Most popular car specification combination per age group , choice of Cars per age group , state wise cars sale in financial years , and top sellers etc.
# Project by :- Surbhi Sinha(linkedin = 'https://www.linkedin.com/in/surbhi-sinha-554902176/' )

# ---------------importing liberaries---------------------------------------
import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import json
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Statewise Data", top_nav=True)
#-----------------------------Map requirements-----------------------------

india_states = json.load(open('states_india.geojson', 'r'))

df = pd.read_csv('statewisesalesof car17_18_19_20.csv')

state_id_map = {}
for feature in india_states['features']:
      feature['id'] = feature['properties']['state_code']
      state_id_map[feature['properties']['st_nm']] = feature['id']

# -----------------------------dataframe and cleaning-----------------------------------
df['id'] = df['state'].apply(lambda x: state_id_map[x])


# ----------------------------- layout--------------------------------
layout = html.Div([

    html.H2("STATE WISE CAR SALES IN INDIA", style={'text-align': 'center'}),
    dbc.Alert(
    [
        # html.H4("Hope You like the project so far!", className="alert-heading"),
        html.H4(
            "Please wait upto few seconds as the map takes time to upload",
            className="mb-0"  
        ),
        html.Hr(),
        # html.P(
        #     "You must have been seeing two blank graph right now!!"
        #     " First! You need to select the company from the drop down",
        #     className="mb-0",
        # ),
    ],dismissable = True,
    color="info"
),
    # html.P("! Please wait upto 10 seconds as the map takes time to upload",style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2017", "value": '2017sales'},
                     {"label": "2018", "value": '2018sales'},
                     {"label": "2019", "value": '2019sales'},
                     ],
                 multi=False,
                 value='2019sales',
                 style={'width': "40%", 'margin-left': '2%'}
                 ),
      html.Div([
            html.Div(id='output_container1', children=[],
                     style={'margin-left': '2%'}),
            html.Div(id='output_container2', children=[],
                     style={'margin-left': '2%'}),

      ],),

    html.Br(),
    html.Div([

      dcc.Graph(id='my_map1', figure={}, style={
                'width': '50%', 'float': 'left', 'margin-left': '2%', 'margin-bottom': '2%'}),
      dcc.Graph(id='my_graph2', figure={}, style={
                'width': '40%', 'float': 'left', 'margin-left': '2%', 'margin-bottom': '2%'}),
    ], style={'display': 'table', 'width': '100%'})

], style={'background-color': '#bbbbbb'})

# --------------------------- connections:----------------------------------------------------------------


@callback(
      [Output(component_id='output_container1', component_property='children'),
      Output(component_id='my_map1', component_property='figure')],
      [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
      print(option_slctd)
      print(type(option_slctd))
      container = "The Map shows the number of car's sale as per state for year: {} while Q1 is the sale in first Quater of the year , You can also zoom the map for better precision.".format(option_slctd)
      dff = df.copy()
      if(option_slctd == '2017sales'):
            fig = px.choropleth(df, locations='id',
                              geojson=india_states,
                              color='2017sales',
                              scope='asia',
                              hover_name='state',
                              hover_data=['Q1sales2017',
                                  'Q1sales2018', 'Q1sales2019'],
                              template='plotly_dark',
                              height=600)
            # fig.update_layout(margin={“r”:0,“t”:0,“l”:0,“b”:0},)  
            fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))  
                         
            fig.update_geos(fitbounds="locations", visible=False)
      elif(option_slctd == '2018sales'):
            fig = px.choropleth(df, locations='id',
                              geojson=india_states,
                              color='2018sales',
                              scope='asia',
                              hover_name='state',
                              hover_data=['Q1sales2017',
                                  'Q1sales2018', 'Q1sales2019'],
                              template='plotly_dark',
                              height=600)
            fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
            fig.update_geos(fitbounds="locations", visible=False)
      elif(option_slctd == '2019sales'):
            fig = px.choropleth(df, locations='id',
                              geojson=india_states,
                              color='2019sales',
                              scope='asia',
                              hover_name='state',
                              hover_data=['Q1sales2017',
                                  'Q1sales2018', 'Q1sales2019'],
                              template='plotly_dark',
                              height=600)
            fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
            fig.update_geos(fitbounds="locations", visible=False)

      return container, fig

# ---------------------------------connection of chart------------------------------------------------


@callback(
    [Output(component_id='output_container2', component_property='children'),
     Output(component_id='my_graph2', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The bar graph shows the number of car's sale as per state for year: {} while Q1 is the sale in first Quater of the year.".format(
        option_slctd) 
    if(option_slctd == '2017sales'):
            fig1 = px.bar(
                  data_frame=df,
                  x='state',
                  y='2017sales',
                  hover_data=['state', 'Q1sales2017',
                      'Q1sales2018', 'Q1sales2019'],
                  template='plotly_dark',
                  height=600,
            )
    elif(option_slctd == '2018sales'):
          fig1 = px.bar(
                  data_frame=df,
                  x='state',
                  y='2018sales',
                  hover_data=['state', 'Q1sales2017',
                      'Q1sales2018', 'Q1sales2019'],
                  template='plotly_dark',
                  height=600,
            )
    elif(option_slctd == '2019sales'):
          fig1 = px.bar(
                  data_frame=df,
                  x='state',
                  y='2019sales',
                  hover_data=['state', 'Q1sales2017',
                      'Q1sales2018', 'Q1sales2019'],
                  template='plotly_dark',
                  height=600,
            )

    return container, fig1