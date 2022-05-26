
# Project Description:-
# This project is part of Microsoft Engage Program
# The project based on Developing an application to demonstrate how the Automotive Industry could harness data to take informed decisions via a user friendly Environment(website)
# Here I have demonstrated the use of data analytics in identifying:
# Customer segments, Most popular car specification combination per age group , choice of Cars per age group , state wise cars sale in financial years , and top sellers etc.
# Project by :- Surbhi Sinha(linkedin = 'https://www.linkedin.com/in/surbhi-sinha-554902176/' )


import dash
from dash import html
import dash_bootstrap_components as dbc


def sidebar():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/ca")
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    )
