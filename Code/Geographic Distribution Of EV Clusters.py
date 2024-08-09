import geopandas as gpd
from shapely.geometry import Point

# Converting 'Vehicle Location' to separate latitude and longitude for mapping
ev_data['Latitude'] = ev_data['Vehicle Location'].apply(lambda x: float(str(x).split(' ')[1][1:]) if isinstance(x, str) else None)
ev_data['Longitude'] = ev_data['Vehicle Location'].apply(lambda x: float(str(x).split(' ')[2][:-1]) if isinstance(x, str) else None)

# Creating a GeoDataFrame
gdf = gpd.GeoDataFrame(ev_data.dropna(subset=['Latitude', 'Longitude', 'Cluster']),
                       geometry=gpd.points_from_xy(ev_data.dropna(subset=['Latitude', 'Longitude', 'Cluster'])['Longitude'],
                                                   ev_data.dropna(subset=['Latitude', 'Longitude', 'Cluster'])['Latitude']),
                       crs="EPSG:4326")

# Plotting the geographic distribution of clusters
plt.figure(figsize=(12, 8))
gdf.plot(column='Cluster', cmap='viridis', legend=True, markersize=10)
plt.title('Geographic Distribution of EV Clusters')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()
