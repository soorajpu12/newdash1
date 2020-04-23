
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pymongo
import dns
import json
import dash_bootstrap_components as dbc
from yahoofinancials import YahooFinancials
import pandas as pd
import quandl
import pymongo
import os
import numpy as np    
import pyfolio as pf    
import chart_studio.plotly as py    
import plotly.graph_objs as go    
import plotly    
import plotly.io as pio    
from plotly import tools
import backtrader as bt
from ib_insync import *
import datetime

# View the pandas dataframe

url1 = 'https://raw.githubusercontent.com/soorajpu12/newdash1/master/GOOG_daily_price_yahooFinance1.csv'
df = pd.read_csv(url1, error_bad_lines=False)

#df.head()
df["Date"] = pd.to_datetime(df["formatted_date"])
df["year"] = df["Date"].dt.year
df['month'] = df['Date'].dt.month
df['volume_higher_than_4M'] = np.where(df['volume']>4000000, 1, 0)
#df.head()

# View the pandas dataframe

url2 = 'https://raw.githubusercontent.com/soorajpu12/newdash1/master/MSFT_daily_price_yahooFinance1.csv'
df2 = pd.read_csv(url2, error_bad_lines=False)

#df2.head()
df2["Date"] = pd.to_datetime(df2["formatted_date"])
df2["year"] = df2["Date"].dt.year
df2['month'] = df2['Date'].dt.month
#df2.head()

# View the pandas dataframe

url3 = 'https://raw.githubusercontent.com/soorajpu12/newdash1/master/AAPL_daily_price_yahooFinance1.csv'
df3 = pd.read_csv(url3, error_bad_lines=False)

#df3.head()
df3["Date"] = pd.to_datetime(df3["formatted_date"])
df3["year"] = df3["Date"].dt.year
df3['month'] = df3['Date'].dt.month
df['volume_higher_than_5M'] = np.where(df['volume']>5000000, 1, 0)
#df3.head()

# View the pandas dataframe

url4 = 'https://raw.githubusercontent.com/soorajpu12/newdash1/master/AAPL_daily_price_yahooFinance1.csv'
df4 = pd.read_csv(url4, error_bad_lines=False)

#df4.head()
df4["Date"] = pd.to_datetime(df4["formatted_date"])
df4["year"] = df4["Date"].dt.year
df4['month'] = df4['Date'].dt.month
#df4.head()

# View the pandas dataframe

url4 = 'https://raw.githubusercontent.com/soorajpu12/newdash1/master/AMZN_daily_price_yahooFinance1.csv'
df4 = pd.read_csv(url4, error_bad_lines=False)

#df4.head()
df4["Date"] = pd.to_datetime(df4["formatted_date"])
df4["year"] = df4["Date"].dt.year
df4['month'] = df4['Date'].dt.month
#df4.head()

# using plotly dash

external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {'background': '#111111', 'text': '#7FDBFF','button':'#FFFF00'}
feature1 = df['formatted_date'].unique()
server=app.server

app.layout = html.Div([
        html.Br(),
        html.Br(),
        
        # select id
        html.Div([
            html.H3('Select the date of Google stock:', style={'paddingRight':'30px','color': '#9999FF'}),
            dcc.Dropdown(
            id = 'formatted_date',
            options = [{'label':i, 'value':i} for i in feature1],
            value = '2013-01-02'
            )
        ], style={"width": "40%"}),
    
    
    #####################################################################################################################
        
        # Bar chart graph- Google
        html.Div([
             html.H3('Bar chart of daily Google stock', style={'paddingRight':'30px','color': colors['text']}),
        html.Div([
                dcc.Graph(id = 'main')
            ], className = 'twelve columns'),
        ], className = 'row',style={"height" : '80vh', "width" : "70%",'margin-left': 0, 
                                    'margin-right': 0,'margin-top':0,'margin-bottom':0}),
    
        # select date range of Google stock
 
        html.Div([dcc.Dropdown(id="selected-value", multi=True, value=["high"],
                              options=[{"label": "High Price", "value": "high"},
                                       {"label": "Low Price", "value": "low"}])],
                className="row", style={"display": "block", "width": "20%", "margin-left": "auto",
                                        "margin-right": "auto"}),
    
    ###################################
    
        # Scatter chart- Microsoft
        html.Div([
             html.H3('Scatter chart of daily Microsoft stock', style={'paddingRight':'30px','color': colors['text']}),
        html.Div([
                dcc.Graph(id = 'scatter')
            ], className = 'twelve columns'),
        ], className = 'row',style={"height" : '80vh', "width" : "70%",'margin-left': 0, 
                                    'margin-right': 0,'margin-top':0,'margin-bottom':0}),
        html.Br(),
    
        # Select time range of Microsoft stock
        html.Div([dcc.RangeSlider(id="year-range", min=2015, max=2020, step=1, value=[2016, 2017],
                                 marks={"2013": str(2013),"2014": str(2014),"2015":str(2015),"2016":str(2016),"2017": str(2017),"2018":str(2018),"2019":str(2019), "2020": str(2020)})]),

    #################################### 
    
        # Pie chart Input- Apple
        html.Div([
            html.Div([html.H3("Apple stock Pie chart monthly data")], style={'paddingRight':'30px','color': colors['text']}),
        html.Div([
                dcc.Graph(id = 'pie')
            ], className = 'twelve columns'),
        ], className = 'row',style={"height" : '80vh', "width" : "70%",'margin-left': 0, 
                                    'margin-right': 0,'margin-top':0,'margin-bottom':0}),
        html.Br(),
            html.Div([dcc.Slider(id='month-selected', min=3, max=12, value=8,
                                 marks={1: 'Januanry', 2: 'Febuanry', 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
                                        10: "October", 11: "November", 12: "December"})],
                     style={'textAlign': "center", "margin": "30px", "padding": "10px", "width": "65%", "margin-left": "auto",
                            "margin-right": "auto"}),
       
    ####################################
    
        #Table Input- Amazon
        html.Div([
            html.Div([html.Span("Information to provide", style={'textAlign': "center", "display": "block"}),
                      dcc.Dropdown(id='column-selected',multi=True, value=['adjclose'],
                                   options=[{"label": i, 'value': i} for i in df.columns[1:3].append(df.columns[4:9])],
                                   style={"display": "block", "margin-left": "auto", "margin-right": "auto", "width": "60%"})
                      ], className="row", style={"padding": 10}),
            html.Div([
            html.Div([html.H3("Amazon stock Table")], style={'paddingRight':'30px','color': colors['text']}),
        html.Div([
                dcc.Graph(id = 'table')
            ], className = 'twelve columns'),
        ], className = 'row',style={"height" : '80vh', "width" : "70%",'margin-left': 0, 
                                    'margin-right': 0,'margin-top':0,'margin-bottom':0}),
        html.Br(),
        ]),
        ],style = {'backgroundColor': colors['background']}) 


######################################################################################################################
        


@app.callback(
    Output('main', 'figure'),
    [Input('formatted_date', 'value')])

def update_graph(selected_date):
    df_selected = df[df['formatted_date']==selected_date]
    x1 = df_selected.values[0][5]
    x2 = df_selected.values[0][6]
    y1 = df_selected.columns[5]
    y2 = df_selected.columns[6]
    
    trace1 = go.Bar(
        x=[x1],y=[y1],
        name = 'Daily High price of Google stock '+ selected_date,
        marker=dict(color='rgba(58,71,80,0.6)',
                   line=dict(color='rgba(58,71,80,1.0)',width=3)),
        orientation = 'h', width=0.2)
        
    trace2 = go.Bar(
        x=[x2],y=[y2],
        name = 'Daily Low price of Google stock ' + selected_date,
        marker=dict(
            color='rgba(210, 105, 30, 1)',
            line = dict(color='rgba(210,105,30,1)',width=3)),
        orientation = 'h',
        width=0.2)
     
    
    #Plot the figure. 
    figure = go.Figure(data=[trace1,trace2],
              layout= go.Layout(
                  plot_bgcolor = colors['background'],
                  paper_bgcolor = colors['background'],
                  font = {'color': colors['text']},
                  title = 'Daily information of Google stock :' + selected_date,
                  showlegend=True,
                  hovermode = 'closest'
                ))
    return figure

@app.callback(
    Output('scatter', 'figure'),
    [Input('selected-value', 'value'), Input('year-range', 'value')])
def update_figure(selected, year):
    text = {'high':'high', 'low':'low'}
    dff = df2[(df2["year"] >= year[0]) & (df2["year"] <= year[1])]
    trace = []
    for i in selected:
        trace.append(go.Scatter(x=dff["Date"], y=dff[i], name=text[i], mode='lines',
                                marker={'size': 8, "opacity": 0.6, "line": {'width': 0.5}}, ))
    return {"data": trace,
            "layout": go.Layout(plot_bgcolor = colors['background'],
                  paper_bgcolor = colors['background'],font = {'color': colors['text']},title="Stock Daily Price of Microsoft", colorway=['#fdae61', '#abd9e9'],
                                yaxis={"title": "Price"}, xaxis={"title": "Date"})}

@app.callback(
    Output('pie', 'figure'),
    [Input('month-selected', 'value')])
def update_graph(selected):
    return {
        "data": [go.Pie(labels=df['formatted_date'].unique().tolist(), values=df[df["month"] == selected]['volume_higher_than_4M'].tolist(), textinfo='label')],
        "layout": go.Layout(plot_bgcolor = colors['background'],
                  paper_bgcolor = colors['background'], font = {'color': colors['text']}, title=f"Volume Reported Monthly", margin={"l": 300, "r": 300, },
                            legend={"x": 1, "y": 0.7})}

@app.callback(
    Output("table", "figure"),
    [Input("column-selected", "value")])
def update_graph(column):
    value_header = ['Date']
    value_cell = [df5['formatted_date']]
    for col in column:
        value_header.append(col)
        value_cell.append(df5[col])
    trace = go.Table(
        header={"values": value_header, "fill": {"color": "#FFD957"}, "align": ['center'], "height": 35,
                "line": {"width": 2, "color": "#685000"}, "font": {"size": 15}},
        cells={"values": value_cell, "fill": {"color": "#FFE89A"}, "align": ['left', 'center'],
               "line": {"color": "#685000"}})
    layout = go.Layout(plot_bgcolor = colors['background'],
                  paper_bgcolor = colors['background'],title="Entry Draft", height=600)
    return {"data": [trace], "layout": layout}


if __name__ == '__main__':
    app.run_server()
