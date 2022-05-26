
# Project Description:-
# This project is part of Microsoft Engage Program
# The project based on Developing an application to demonstrate how the Automotive Industry could harness data to take informed decisions via a user friendly Environment(website)
# Here I have demonstrated the use of data analytics in identifying:
# Customer segments, Most popular car specification combination per age group , choice of Cars per age group , state wise cars sale in financial years , and top sellers etc.
# Project by :- Surbhi Sinha(linkedin = 'https://www.linkedin.com/in/surbhi-sinha-554902176/' )

# -----------------------importing modules------------------------------------
import dash
from dash import dcc , html ,Input , Output , State
import dash_labs as dl
import dash_bootstrap_components as dbc
import dash_auth



# -----------------------Initializing the Application-----------------------------
app = dash.Dash(
      __name__ ,
      plugins = [dl.plugins.pages] , 
      external_stylesheets= [dbc.themes.BOOTSTRAP]
)

# --------------------------login authentication---------------------------
auth = dash_auth.BasicAuth(
      app,
      {'System' : 'System123'}
      # username , user password
)
#------------------------- Navigation Bar for main dashboard---------------------
navbar = dbc.NavbarSimple(
      dbc.Nav(
            [
                  dbc.NavLink(page["name"],href = page["path"])
                  for page in dash.page_registry.values()
                  if page.get("top_nav")
            ]
      ),
      brand = "LOGICYIELD.COM",
      color="primary",
      dark = True,
      className="mb-1"
)

# --------------------App layout and plugins with the multi pages-------------------------------
app.layout = dbc.Container(
      [navbar , dl.plugins.page_container],
      fluid = True,
)


# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
      app.run_server(debug = True)