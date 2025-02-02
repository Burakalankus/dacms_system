import psycopg2
from pymongo import MongoClient
import redis
import time

conn = psycopg2.connect(
    dbname="my_database", user="balankus", password="135246bba", host="compose_2-postgres-1"
)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, data TEXT);")
cursor.execute("INSERT INTO test (data) VALUES ('Hello PostgreSQL');")
conn.commit()
cursor.close()
conn.close()
print("PostgreSQL succesfully connected.")

client = MongoClient("mongodb://compose_2-mongodb-1:27017/")
db = client["testdb"]
collection = db["testcollection"]
collection.insert_one({"message": "Hello MongoDB"})
print("MongoDB connected succesfully.")

r = redis.Redis(host="compose_2-redis-1", port=6379)
r.set("message", "Hello Redis")
print("Redis connected succesfully.")

time.sleep(1800)
