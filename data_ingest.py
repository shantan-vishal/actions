import pymongo
import pandas as pd

# MongoDB connection
mongo_uri = "mongodb://root:sa123@10.10.10.142:27018/"
client = pymongo.MongoClient(mongo_uri)

# Specify the database and collection
db = client['your_database']  # Replace 'your_database' with the actual database name
collection = db['your_collection']  # Replace 'your_collection' with the actual collection name

# Fetch data from MongoDB
data = pd.DataFrame(list(collection.find()))

# Save the data locally as CSV
data.to_csv('ingested_data.csv', index=False)

print("Data ingestion completed and saved as ingested_data.csv")
