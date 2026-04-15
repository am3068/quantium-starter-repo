import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("data/processed_sales.csv")

df.columns = df.columns.str.lower()   
df["date"] = pd.to_datetime(df["date"])


df["region"] = df["region"].str.strip()

df = df.sort_values("date")
# Create app
app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "Arial", "padding": "20px"}, children=[

    html.H1(
        "Soul Foods Sales Visualiser",
        style={"textAlign": "center", "color": "#2c3e50"}
    ),

    html.P(
        "Explore Pink Morsel sales performance across regions",
        style={"textAlign": "center", "color": "#7f8c8d"}
    ),

    # 🔘 Radio Buttons
    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        labelStyle={"display": "inline-block", "margin": "10px"},
        style={"textAlign": "center"}
    ),

    dcc.Graph(id="sales-line-chart")
])


# 🔁 Callback to update chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # 🚨 Prevent empty dataframe crash
    if filtered_df.empty:
        return px.line(title="No data available")

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region" if selected_region == "all" else None,
        title="Pink Morsel Sales Over Time"
    )

    fig.add_shape(
        type="line",
        x0="2021-01-15",
        x1="2021-01-15",
        y0=0,
        y1=1,
        xref="x",
        yref="paper",
        line=dict(color="red", dash="dash")
    )

    fig.add_annotation(
        x="2021-01-15",
        y=1,
        xref="x",
        yref="paper",
        text="Price Increase",
        showarrow=False,
        xanchor="left"
    )
    

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="#f9f9f9",
        paper_bgcolor="#ffffff"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)