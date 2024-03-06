import pandas as pd
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt


# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="Nigeria_Election_by_state",
    user="postgres",
    password="animashaun"
)

# Define your SQL query
sql_query = "SELECT * FROM Nigeria_Election_by_state;"

# Load the data into a pandas DataFrame
df = pd.read_sql_query(sql_query, conn)

# Close the database connection
conn.close()

first_column = df.iloc[:, 0]  # Select all rows from the first column, excluding the index
print(first_column)

# Display the DataFrame


# *** AFTER THE TABLE HAVE BEEN EXTRACTED FROM THE DATABASE***#
# I CLEAN , ANALISE AND CREATE A GOOD VISUALIZATION OF THE DATASET



# Create the dataframe from the given data
#
# # Exclude the 'AGGREGATE' row
# df = df[df['state'] != 'AGGREGATE']

# Melt the dataframe to have the state column as the id variable
df_melted = df.melt(id_vars='state', var_name='party', value_name='votes')

# Plot the data using Seaborn
# Plot the data using Seaborn
plt.figure(figsize=(14, 8))
sns.barplot(data=df_melted, x='state', y='votes', hue='party')
plt.title('Votes by State')
plt.xlabel('State')
plt.ylabel('Votes')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()



