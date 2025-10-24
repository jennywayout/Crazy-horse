# app/component/page_scaffold.py
from dash import html
import dash_bootstrap_components as dbc

def page(title, *children, fluid=True):
    return dbc.Container([ html.H2(title, className="mt-2 mb-3"), html.Hr(), *children ], fluid=fluid, className="page-wrap")

def kpi_card(label, value, color="light"):
    return dbc.Card(
        dbc.CardBody([ html.Div(label, className="label"), html.Div(value, className="value") ]),
        className="kpi-card", color=color, inverse=(color not in ["light","white"])
    )
