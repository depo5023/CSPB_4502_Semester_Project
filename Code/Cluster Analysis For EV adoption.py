from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Selecting relevant features for clustering
clustering_features = ['Electric Range', 'Model Year', 'Base MSRP']

# Handling missing values
ev_data_clustering = ev_data[clustering_features].dropna()

# Scaling the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(ev_data_clustering)

# Performing K-means clustering with an arbitrary choice of 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
ev_data_clustering['Cluster'] = kmeans.fit_predict(scaled_features)

# Adding cluster labels to the original data
ev_data['Cluster'] = np.nan
ev_data.loc[ev_data_clustering.index, 'Cluster'] = ev_data_clustering['Cluster']

# Visualizing the clusters based on the first two features (Electric Range and Model Year)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Electric Range', y='Model Year', hue='Cluster', data=ev_data_clustering, palette='viridis')
plt.title('Cluster Analysis of Electric Vehicles')
plt.xlabel('Electric Range')
plt.ylabel('Model Year')
plt.grid(True)
plt.legend(title='Cluster')
plt.show()





