import pymongo
import pandas as pd
black .
isort .


# MongoDB connection
mongo_uri = "mongodb://zk_admin:Zkteco*123@10.6.1.179:27019/?authMechanism=DEFAULT&authSource=ralvie_db"
client = pymongo.MongoClient(mongo_uri)

# Specify the database and collection
db = client['ralvie_db']  
collection = db['your_collection']  # Replace 'your_collection' with the actual collection name

# Fetch data from MongoDB
data = pd.DataFrame(list(collection.find()))

# Save the data locally as CSV
data.to_csv('ingested_data.csv', index=False)

print("Data ingestion completed and saved as ingested_data.csv")

