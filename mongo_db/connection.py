import pymongo
client = pymongo.MongoClient("mongodb+srv://nitesh:nitesh@cluster0.huj0t.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# print(db)
database = client['nitesh'] # db_name
coll = database['fsds_8th']
data = {
    "class name":"full stack data science 2.0",
    "topic name":"mongo_db mysql",
    "todays date":"8th jan 2013"
}
data_1 = {
    "class name":"full stack data science 2.0",
    "topic name":"mongo_db mysql",
    "todays date":"8th jan 2013",
    "today confi":["mongo atlas","mysql connector","mongo compass"]
}
coll.insert_one(data_1)
