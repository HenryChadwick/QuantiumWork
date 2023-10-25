import numpy as np
import pandas as pd
import dash 

file1 = pd.read_csv('data/daily_sales_data_0.csv')
file2 = pd.read_csv('data/daily_sales_data_1.csv')
file3 = pd.read_csv('data/daily_sales_data_2.csv')

all_data = pd.concat([file1, file2, file3])
all_data['product'] = all_data['product'].str.lower()
search_term = 'pink morsel'.lower()
pink_morsel_data = all_data[all_data['product'].str.contains(search_term)]

pink_morsel_data.loc[:, 'price'] = pd.to_numeric(pink_morsel_data['price'].str.replace('$', ''), errors='coerce')
pink_morsel_data.loc[:, 'quantity'] = pd.to_numeric(pink_morsel_data['quantity'], errors='coerce')
pink_morsel_data.loc[:, 'Sales ($)'] = pink_morsel_data.loc[:, 'quantity'] * pink_morsel_data.loc[:, 'price']

file6 = pink_morsel_data[['Sales ($)','date','region']]
output_data = file6
output_data.to_csv('PinkMorselSales.csv', index=False)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

pink_morsel_data = pd.read_csv('PinkMorselSales.csv')
external_stylesheets = ['Stylesheet.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("Impact of Pink Morsels Price Increase on Sales"),

    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all'
    ),
    dcc.Graph(id='sales-chart')
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_data = pink_morsel_data
    else:
        filtered_data = pink_morsel_data[pink_morsel_data['region']==selected_region]

    return px.line(filtered_data, x='date', y='Sales ($)', title=f'Total Sales Over Time - {selected_region} Region')

if __name__ == '__main__':
    app.run_server(debug=True)