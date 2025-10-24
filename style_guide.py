# app/pages/style_guide.py
# -*- coding: utf-8 -*-
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app.component.page_scaffold import page, kpi_card

dash.register_page(__name__, path="/style", name="Style Guide", order=999)

BRAND_COLORS = {
    "Purple":  "#732282",
    "Teal":    "#00747A",
    "Navy":    "#002664",
    "Olive":   "#9C9A00",
    "Amber":   "#B06F00",
    "Crimson": "#882345",
    "Black":   "#000000",
}
TINTS = {
    "Purple 40%": "#BC7BD1",
    "Purple 60%": "#D2A7E1",
    "Purple 80%": "#E9D3F0",
}

def swatch(label, color):
    return dbc.Card(
        dbc.CardBody([
            html.Div(style={ "height":"44px", "borderRadius":"6px", "backgroundColor": color }),
            html.Div(label, className="mt-2"),
            html.Code(color)
        ]),
        className="mb-3", style={"minWidth":"160px"}
    )

def swatch_row(items):
    return dbc.Row([dbc.Col(it, md=2) for it in items], className="gy-3")

kpi_row = dbc.Row(
    [
        dbc.Col(kpi_card("Total Users", "12,480"), md=3),
        dbc.Col(kpi_card("Sessions", "34,902"), md=3),
        dbc.Col(kpi_card("Conversion", "3.2%"), md=3),
        dbc.Col(kpi_card("Satisfaction", "84%"), md=3),
    ],
    className="gy-3"
)

def brand_line():
    dates = pd.date_range("2025-01-01", periods=14, freq="W")
    df = pd.DataFrame({
        "date": list(dates)*3,
        "value": [x*1.5 for x in range(14)] + [x*1.1 for x in range(14)] + [x for x in range(14)],
        "series": (["A"]*14)+(["B"]*14)+(["C"]*14),
    })
    color_seq = [BRAND_COLORS[c] for c in ["Purple","Teal","Amber","Navy","Olive","Crimson","Black"]]
    fig = px.line(df, x="date", y="value", color="series",
                  color_discrete_sequence=color_seq,
                  markers=True, title="Brand Line Chart")
    fig.update_layout(margin=dict(l=10,r=10,t=60,b=10))
    return fig

buttons_row = dbc.Row(
    [
        dbc.Col(dbc.Button("Primary", color="primary"), md="auto"),
        dbc.Col(dbc.Button("Secondary", color="secondary"), md="auto"),
        dbc.Col(dbc.Button("Success", color="success"), md="auto"),
        dbc.Col(dbc.Button("Warning", color="warning"), md="auto"),
        dbc.Col(dbc.Button("Danger", color="danger"), md="auto"),
        dbc.Col(dbc.Button("Outline", outline=True, color="primary"), md="auto"),
    ],
    className="gy-2 gx-2"
)

table = dbc.Table(
    [
        html.Thead(html.Tr([html.Th("Metric"), html.Th("Value"), html.Th("Status")])),
        html.Tbody([
            html.Tr([html.Td("A&E wait < 4h"), html.Td("76.2%"), html.Td("Amber")]),
            html.Tr([html.Td("Cancer 62d target"), html.Td("85.5%"), html.Td("Green")]),
            html.Tr([html.Td("GP access < 7d"), html.Td("64.1%"), html.Td("Red")]),
        ])
    ],
    bordered=True, hover=True, responsive=True, striped=True, className="mb-0"
)

layout = page(
    "Style Guide",
    html.H4("Brand Colours"),
    swatch_row([swatch(name, hexv) for name, hexv in BRAND_COLORS.items()]),
    html.Hr(),
    html.H5("Tints"),
    swatch_row([swatch(name, hexv) for name, hexv in TINTS.items()]),

    html.Hr(),
    html.H4("KPI Cards"),
    kpi_row,

    html.Hr(),
    html.H4("Buttons"),
    buttons_row,

    html.Hr(),
    html.H4("Chart Preview (Brand Palette)"),
    dcc.Graph(figure=brand_line()),

    html.Hr(),
    html.H4("Table Preview"),
    dbc.Card(dbc.CardBody(table)),
)
