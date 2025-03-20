import dash
from dash import dcc, html
import pandas as pd
import os

# Set the correct file path
csv_file = "F:/111/data1.csv"  # Update with full path

# Check if file exists
if not os.path.exists(csv_file):
    print(f"Error: File '{csv_file}' not found. Please check the path.")
    exit()

# Load CSV file
df = pd.read_csv(csv_file)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("CSV Data Viewer"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df[df.columns[0]], 'y': df[df.columns[1]], 'type': 'bar', 'name': 'Data'},
            ],
            'layout': {
                'title': 'Sample CSV Data Visualization'
            }
        }
    )
])

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)
