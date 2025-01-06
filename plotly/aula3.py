import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd


df = pd.read_csv("2014_World_GDP")
print(df.head())

data = dict(
    type="choropleth",
    locations=df["CODE"],
    z=df["GDP (BILLIONS)"],
    text=df["COUNTRY"],
    colorbar={"title": "GDP In Billions"},
)

layout = dict(
    title="2014 Global GDP", geo=dict(showframe=False, projection={"type": "mercator"})
)
choromap = go.Figure(data=[data], layout=layout)
plot(choromap)
