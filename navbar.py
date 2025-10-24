# app/component/navbar.py
from dash import html
import dash_bootstrap_components as dbc
import dash

def _menu_items():
    items = []
    for p in sorted(dash.page_registry.values(), key=lambda x: x.get("order", 999)):
        items.append(dbc.NavItem(dbc.NavLink(p["name"], href=p["path"], active="exact")))
    return items

content = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand(
            html.Div([
                html.Img(src="/assets/logo-white.png", height="32", style={"marginRight": "10px"}),
                html.Span("{{cookiecutter.project_name}}", className="fw-bold")
            ], className="d-flex align-items-center"),
            href="/"
        ),
        dbc.Nav(_menu_items(), navbar=True, pills=True, className="ms-auto"),
    ]),
    color="primary", dark=True, className="mb-3"
)
