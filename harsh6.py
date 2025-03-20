import dash
from dash import dcc, html, Input, Output, State, dash_table
import pandas as pd
import plotly.express as px
import os

# Load data
csv_file = "F:/111/data1.csv"
if not os.path.exists(csv_file):
    print(f"Error: File not found: {csv_file}")
    exit()

df = pd.read_csv(csv_file)

# Initialize Dash app
app = dash.Dash(__name__)

# Global variable for tracking data window
start_idx = 0

app.layout = html.Div([
    html.H1("Gyroscope Data Dashboard"),
    dcc.Dropdown(
        id='graph-type',
        options=[
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Histogram', 'value': 'histogram'}
        ],
        value='line'
    ),
    dcc.Dropdown(
        id='variables',
        options=[
            {'label': 'X', 'value': 'x'},
            {'label': 'Y', 'value': 'y'},
            {'label': 'Z', 'value': 'z'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        multi=True
    ),
    dcc.Input(id='sample-count', type='number', value=100, style={'margin': '10px'}),
    html.Button('Previous', id='prev-button', n_clicks=0),
    html.Button('Next', id='next-button', n_clicks=0),
    dcc.Graph(id='gyro-graph'),
    dash_table.DataTable(
        id='stats-table',
        columns=[{'name': col, 'id': col} for col in ['Stat', 'X', 'Y', 'Z']]
    )
])

@app.callback(
    [Output('gyro-graph', 'figure'),
     Output('stats-table', 'data')],
    [Input('graph-type', 'value'),
     Input('variables', 'value'),
     Input('sample-count', 'value'),
     Input('prev-button', 'n_clicks'),
     Input('next-button', 'n_clicks')]
)
def update_graph(graph_type, variables, sample_count, prev_clicks, next_clicks):
    global start_idx
    total_samples = len(df)
    
    # Handle navigation buttons
    ctx = dash.callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'prev-button':
            start_idx = max(0, start_idx - sample_count)
        elif button_id == 'next-button':
            start_idx = min(total_samples - sample_count, start_idx + sample_count)
    
    # Slice data based on current window
    end_idx = start_idx + sample_count
    dff = df.iloc[start_idx:end_idx]
    
    # Handle variable selection
    if 'all' in variables:
        cols = ['x', 'y', 'z']
    else:
        cols = variables
    
    # Generate plot
    if graph_type == 'line':
        fig = px.line(dff, y=cols, title='Gyroscope Data (Line Chart)')
    elif graph_type == 'scatter':
        fig = px.scatter(dff, x=dff.index, y=cols, title='Gyroscope Data (Scatter Plot)')
    else:
        fig = px.histogram(dff, x=cols, title='Distribution (Histogram)')
    
    # Generate stats table
    stats = dff[cols].describe().reset_index().melt(id_vars='index')
    stats_pivot = stats.pivot(index='index', columns='variable', values='value').reset_index()
    stats_data = stats_pivot.to_dict('records')
    
    return fig, stats_data

if __name__ == '__main__':
    app.run_server(debug=True)