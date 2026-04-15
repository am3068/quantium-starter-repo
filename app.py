import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_sales.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(children=[
    
    html.H1("Soul Foods Sales Visualiser", 
            style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)