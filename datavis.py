# Built in imports
import pandas as pd
import numpy as np
import sys
# 3rd Party imports
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
# Local files
from Database import accessing_db


app = dash.Dash()   #initialising dash app
