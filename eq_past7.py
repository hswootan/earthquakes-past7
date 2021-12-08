import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = '/Users/hongwoo/Desktop/eq_past_7days/all_week.json'
with open(filename) as f:
    eq_past7_data = json.load(f)

eq_past7_dict = eq_past7_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in eq_past7_dict:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        # 'size': [3*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

eq_layout = Layout(title=eq_past7_data['metadata']['title'])

fig = {'data': data, 'layout': eq_layout}
offline.plot(fig, filename='past7_days_earthquakes.html')

