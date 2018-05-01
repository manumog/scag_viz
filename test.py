import pandas as pd
import plotly.offline as pyo
from ScagApp import ScagApp

HDV = ScagApp('HDV','S:\E3 Projects\SCAG Pathways\PlotlyDev\PATHWAYS_csvs')

# print(HDV)
# print(HDV.stock_years)
# print(HDV.technologies)
# print(HDV.scenarios, type(HDV.scenarios))
print(HDV.technologies)

fig1 = HDV.stock_rollover_figure()
fig2 = HDV.shares_figure()




