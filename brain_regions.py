import pandas as pd

# Read AllBrainRegions.csv and create a DataFrame
brain_regions_df = pd.read_csv('AllBrainRegions.csv')

# Read all_points.csv and create a DataFrame
all_points_df = pd.read_csv('all_points.csv')
all_points_df.head()
# Perform the lookup and append the id column to all_points DataFrame
all_points_df['brain_region_id'] = all_points_df['structure_name'].map(brain_regions_df.set_index('name')['id'])

# Display the updated DataFrame
all_points_df.to_csv("all_points_id.csv")