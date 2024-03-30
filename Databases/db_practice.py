from pymongo import MongoClient

# Connecting to the database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['users']

# Inserting documents
user1 = {'name': 'John Doe', 'email': 'john@example.com', 'age': 30}
user2 = {'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25}
inserted_ids = collection.insert_many([user1, user2]).inserted_ids
print("Inserted IDs:", inserted_ids)

# Querying documents
query = {'age': {'$gte': 25}}
results = collection.find(query)
for user in results:
    print(user)

# Updating documents
update_query = {'name': 'John Doe'}
update_data = {'$set': {'age': 31}}
collection.update_one(update_query, update_data)

# Deleting documents
delete_query = {'name': 'Jane Smith'}
collection.delete_one(delete_query)

# Indexing for performance optimization
collection.create_index('email')

# Aggregation and grouping
pipeline = [
    {'$group': {'_id': '$age', 'count': {'$sum': 1}}},
    {'$sort': {'count': -1}}
]
results = collection.aggregate(pipeline)
for result in results:
    print(result)

# Transactions (MongoDB 4.0+)
with client.start_session() as session:
    with session.start_transaction():
        try:
            collection.insert_one({'name': 'Alice', 'email': 'alice@example.com', 'age': 28}, session=session)
            collection.insert_one({'name': 'Bob', 'email': 'bob@example.com', 'age': 35}, session=session)
            session.commit_transaction()
        except Exception as e:
            print("Transaction aborted:", e)
            session.abort_transaction()

# Text search
collection.create_index([('name', 'text'), ('email', 'text')])
search_query = {'$text': {'$search': 'John'}}
results = collection.find(search_query)
for user in results:
    print(user)

# Geospatial queries
collection.create_index([('location', '2dsphere')])
collection.insert_one({'name': 'Restaurant', 'location': {'type': 'Point', 'coordinates': [-73.97, 40.77]}})
query = {
    'location': {
        '$near': {
            '$geometry': {'type': 'Point', 'coordinates': [-73.98, 40.76]},
            '$maxDistance': 1000
        }
    }
}
results = collection.find(query)
for result in results:
    print(result)

# Closing the connection
client.close()