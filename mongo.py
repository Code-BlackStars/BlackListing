import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://PelumiA:dbtest@cluster0.qqike.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test

#cluster = MongoClient("mongodb+srv://PelumiA:dbtest@cluster0.5rsdr.mongodb.net/BlackListing?retryWrites=true&w=majority")
#db = cluster["Cluster0"]
#db = cluster.one
collection = db["BlackListing"]

#need to put in a POST
#property of the db
#post = {"_id":0, "name" : "Lu", "score" : 5}


    #build temp businesses
#collection.insert_one = {"_id":1, "name": "First Potomac Realty Trust", "address": "7600 Wisconsin Ave", "city":"Bethesda", "zipcode":"20814", "state: md"}
# collection.insert_one({"_id":1, "name": "First Potomac Realty Trust", "address": "7600 Wisconsin Ave", "city":"Bethesda", "zipcode":"20814", "state": "md"})
#
# collection.insert_one({"_id":2, "name": "Team Taylor Unltd LLC", "address":"11388 Livingston Rd", "city": "Fort Washington", "zipcode":"20744", "state":"md"})
#
# collection.insert_one({"_id":3, "name": "Coiffure Exclusive Salon", "address":"7718 Belair Rd", "city": "Nottingham", "zipcode":"21236", "state":"md"})
#
# collection.insert_one({"_id":4, "name": "Elle Braiding Salon", "address":"11160 Veirs Mill Rd", "city": "Silver Spring", "zipcode":"20902", "state":"md"})
#
# collection.insert_one({"_id":5, "name": "Fabulocs", "address":"7953 Central Ave", "city": "Capitol Heights", "zipcode":"20743", "state":"md"})
#
# collection.insert_one({"_id":6, "name": "Urban Nature", "address":"937 Bonifant St", "city": "Silver Spring", "zipcode":"20910", "state":"md"})

#remove first dummy field
#collection.delete_one({"_id":0})



#dblist = cluster.list_database_names()

#collection.insert_one(post)
#can do insert_many([post1,post2])

#results = collection.find({"name":"", "address": ""})
#.find_one() -- returns the first one found

#prints all
#result = collection.find({})
#print(type(result))

##To Delete ##
#res = collection.delete_one({"_id":0})
## can do delete_many

##to Update ##
#set adds the field to the attributes
#results.collection.update_one({"_id":0}, {"$set" : {"hello":5}})

#gives us a number of docs/entries in the DB
#post_count = collection.count_documents({})
#extracts address from DB
for results in result:
    #print(results)
    address = results["address"]
    city = results["city"]
    state = results["state"]

    #addy = collection.find({"address"})
    print(address + city + state)
    #if we want something specific from the result
    # print(result["_id"])