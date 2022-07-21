import pymongo

client = pymongo.MongoClient("mongodb+srv://gsreddyphysics:reddy1985@cluster1.luyvz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
     "name":"gsreddy",
     "email":"gsreddyphysics@gmail.com",
     "surname" : "gavinolla"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
#gnv.nmv/knvbj'kl/hvlcnlgj