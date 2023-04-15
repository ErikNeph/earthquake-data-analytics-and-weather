# https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data/readable_eq_data_30_days_m4.5_14.04.2023.json'
with open(filename) as f:
    all_eq_data = json.load(f)

data_title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']
mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title=data_title)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_m4.html')
