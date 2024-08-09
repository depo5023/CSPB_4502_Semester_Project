import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
file_path = 'Cleaned_Electric_Vehicle_Population_Data.csv'
data = pd.read_csv(file_path)

# Set up the matplotlib figure aesthetics
plt.style.use('ggplot')

# 1. Distribution of Electric Vehicle Types
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Electric Vehicle Type', order=data['Electric Vehicle Type'].value_counts().index)
plt.title('Distribution of Electric Vehicle Types')
plt.xlabel('Electric Vehicle Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('electric_vehicle_type_distribution.png')
plt.show()

# 2. Electric Range Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Electric Range'], bins=30, kde=True)
plt.title('Electric Range Distribution')
plt.xlabel('Electric Range (miles)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('electric_range_distribution.png')
plt.show()

# 3. Top Electric Vehicle Makes
top_makes = data['Make'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_makes.index, y=top_makes.values, palette='viridis')
plt.title('Top 10 Electric Vehicle Makes')
plt.xlabel('Make')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_electric_vehicle_makes.png')
plt.show()

# 4. Count of Electric Vehicles by Model Year
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Model Year', palette='viridis')
plt.title('Count of Electric Vehicles by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('count_of_electric_vehicles_by_model_year.png')
plt.show()

# 5. Electric Vehicles by County
plt.figure(figsize=(12, 8))
top_counties = data['County'].value_counts().head(10)
sns.barplot(x=top_counties.values, y=top_counties.index, palette='coolwarm')
plt.title('Top 10 Counties by Number of Electric Vehicles')
plt.xlabel('Number of Electric Vehicles')
plt.ylabel('County')
plt.tight_layout()
plt.savefig('top_counties_by_electric_vehicles.png')
plt.show()

# 6. Distribution of Electric Vehicle Makes over Years
plt.figure(figsize=(12, 8))
sns.countplot(data=data, x='Model Year', hue='Make', palette='Set3', order=sorted(data['Model Year'].unique()))
plt.title('Distribution of Electric Vehicle Makes over Years')
plt.xlabel('Model Year')
plt.ylabel('Count')
plt.legend(title='Make', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('distribution_of_electric_vehicle_makes_over_years.png')
plt.show()

# 7. Electric Range by Make
plt.figure(figsize=(12, 8))
sns.boxplot(data=data, x='Make', y='Electric Range', palette='Set2')
plt.title('Electric Range by Make')
plt.xlabel('Make')
plt.ylabel('Electric Range (miles)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('electric_range_by_make.png')
plt.show()

# 8. Clean Alternative Fuel Vehicle Eligibility by Electric Vehicle Type
plt.figure(figsize=(12, 8))
sns.countplot(data=data, x='Electric Vehicle Type', hue='Clean Alternative Fuel Vehicle (CAFV) Eligibility', palette='muted')
plt.title('CAFV Eligibility by Electric Vehicle Type')
plt.xlabel('Electric Vehicle Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='CAFV Eligibility', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('cafv_eligibility_by_ev_type.png')
plt.show()