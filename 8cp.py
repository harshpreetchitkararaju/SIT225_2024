import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.graph_objs as go

# App setup
app = dash.Dash(__name__)
app.title = "Live Accelerometer Plot"

# Initial layout
app.layout = html.Div([
    html.H2("📱 Live Accelerometer Data (x, y, z)"),
    dcc.Graph(id='live-graph', animate=True),
    dcc.Interval(
        id='interval-component',
        interval=500,  # update every 500ms
        n_intervals=0
    )
])

# Global pointer to simulate live data chunk
pointer = 0
window_size = 100

@app.callback(Output('live-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    global pointer

    df = pd.read_csv("moving_accelerometer_data.csv")
    max_len = len(df)

    # Check if we've reached the end of the data
    if pointer + window_size > max_len:
        pointer = max_len - window_size  # Keep pointer at the last possible window

    # Get the window of data
    df_window = df.iloc[pointer:pointer + window_size]
    pointer += 5  # move the window forward

    # Create the figure with the new data
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_window['time'], y=df_window['x'], mode='lines', name='x'))
    fig.add_trace(go.Scatter(x=df_window['time'], y=df_window['y'], mode='lines', name='y'))
    fig.add_trace(go.Scatter(x=df_window['time'], y=df_window['z'], mode='lines', name='z'))

    # Update the layout of the graph
    fig.update_layout(
        title="Real-time Accelerometer Data",
        xaxis_title="Time",
        yaxis_title="Acceleration (m/s²)",
        template="plotly_dark",
        xaxis=dict(tickangle=-45),
        legend=dict(orientation="h")
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
