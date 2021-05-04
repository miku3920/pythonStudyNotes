from ipywidgets.embed import embed_minimal_html
import matplotlib.pyplot as plt
import gmaps

gmaps.configure(api_key='??????????????????????????????????')

new_york_coordinates = (40.75, -74.00)
fig = gmaps.figure(center=new_york_coordinates, zoom_level=12)

earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
locations = earthquake_df[['latitude', 'longitude']]
weights = earthquake_df['magnitude']
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))

embed_minimal_html('export.html', views=[fig])
