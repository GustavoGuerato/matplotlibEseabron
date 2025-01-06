import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


data = dict(
    type="choropleth",
    locations=["AZ", "CA", "NY"],
    locationmode="USA-states",
    colorscale="Jet",
    text=["Arizona", "California", "New York"],
    z=[1.0, 2.0, 3.0],
    colorbar={"title": "ColorBar Title"},
)

print(data)
layout = dict(geo={"scope": "usa"})

choromap = go.Figure(data=[data], layout=layout)
plot(choromap)
