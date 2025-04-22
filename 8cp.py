import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from collections import deque
from datetime import datetime

# === Load CSV Data ===
df_x = pd.read_csv("accel_x.csv", parse_dates=['timestamp'])
df_y = pd.read_csv("accel_y.csv", parse_dates=['timestamp'])
df_z = pd.read_csv("accel_z.csv", parse_dates=['timestamp'])

# === Data Buffers ===
BUFFER_SIZE = 50  # Change for how many points you want visible
timestamps = deque(maxlen=BUFFER_SIZE)
x_data = deque(maxlen=BUFFER_SIZE)
y_data = deque(maxlen=BUFFER_SIZE)
z_data = deque(maxlen=BUFFER_SIZE)

# Track current row index
data_index = {'i': 0}

# === Dash App Setup ===
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H3("Real-Time Accelerometer Data"),
    dcc.Graph(id='live-graph'),
    dcc.Interval(id='graph-update', interval=500, n_intervals=0)  # Update every 0.5 sec
])

# === Graph Update Callback ===
@app.callback(
    Output('live-graph', 'figure'),
    Input('graph-update', 'n_intervals')
)
def update_graph(n):
    i = data_index['i']
    
    # Append next row if available
    if i < len(df_x):
        timestamps.append(df_x.iloc[i]['timestamp'])
        x_data.append(df_x.iloc[i]['value'])
        y_data.append(df_y.iloc[i]['value'])
        z_data.append(df_z.iloc[i]['value'])
        data_index['i'] += 1

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(timestamps), y=list(x_data), name='X', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=list(timestamps), y=list(y_data), name='Y', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=list(timestamps), y=list(z_data), name='Z', line=dict(color='blue')))

    # Create sliding window effect
    if len(timestamps) > 2:
        fig.update_layout(
            xaxis=dict(range=[timestamps[0], timestamps[-1]]),  # Moving window
            yaxis_title='Acceleration',
            xaxis_title='Time',
            title='Real-Time Accelerometer Data',
            showlegend=True
        )

    return fig

# === Run Server ===
if __name__ == '__main__':
    app.run(debug=True)
