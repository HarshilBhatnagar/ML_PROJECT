import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

filenames = {
    '1 Hour Intervals' : '/Users/harshilbhatnagar/Downloads/Hackathon_IITK/Hackathon_IITK/PROCESSED DATA/processed_btc_1h.csv',
    '2 Hour Intervals' : '/Users/harshilbhatnagar/Downloads/Hackathon_IITK/Hackathon_IITK/PROCESSED DATA/processed_btc_2h.csv',
    '3 Minutes Intervals' : '/Users/harshilbhatnagar/Downloads/Hackathon_IITK/Hackathon_IITK/PROCESSED DATA/processed_btc_3m.csv',
    '4 Hour Intervals' : '/Users/harshilbhatnagar/Downloads/Hackathon_IITK/Hackathon_IITK/PROCESSED DATA/processed_btc_4h.csv',
    '5 Minutes Intervals' : '/Users/harshilbhatnagar/Downloads/Hackathon_IITK/Hackathon_IITK/PROCESSED DATA/processed_btc_5m.csv',
    '6 Hour Intervals' : '/Users/harshilbhatnagar/Downloads/Hackathon_IITK/Hackathon_IITK/PROCESSED DATA/processed_btc_6h.csv',
    '15 Minutes Intervals' : '/Users/harshilbhatnagar/Downloads/Hackathon_IITK/Hackathon_IITK/PROCESSED DATA/processed_btc_15m.csv',
    '30 Minutes Intervals' : '/Users/harshilbhatnagar/Downloads/Hackathon_IITK/Hackathon_IITK/PROCESSED DATA/processed_btc_30m.csv'
}

dataframes = {name: pd.read_csv(filepath) for name, filepath in filenames.items()}

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='file-selector',
        options=[{'label': name, 'value': name} for name in filenames.keys()],
        value=list(filenames.keys())[0] 
    ),
    dcc.Graph(id='data-visualization') 
])

@app.callback(
    Output('data-visualization', 'figure'),
    Input('file-selector', 'value')
)
def update_graph(selected_file_name):
    df = dataframes[selected_file_name]
    fig = px.line(df, x='datetime', y='close', title=f'{selected_file_name} Data')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
