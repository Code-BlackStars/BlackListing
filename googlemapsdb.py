import urllib.request, json
import os
import pymongo
from pymongo import MongoClient

def mongoReadDb():
    client = pymongo.MongoClient("mongodb+srv://PelumiA:dbtest@cluster0.qqike.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client.test
    collection = db["BlackListing"]
    result = collection.find({})
    businsess = {}
    for results in result:
        #print(results)
        name = results["name"]
        address = results["address"]
        city = results["city"]
        state = results["state"]
        query = (address + ","+  city + ","+ state).replace(' ','+')
        businsess[name] = query
    return businsess


def calculateDistance(query, origin):
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = "AIzaSyDbzu4BBKopAZkuse2svqFm1pYWoGoRfXs"
    real_Distance = {}
    origin = origin.replace(' ','+')
    for name, destination in query.items():
        nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        directions = json.loads(response)
        routes = directions['routes']
        legs = routes[0]['legs']
        distance = legs[0]['distance']['text']
        real_Distance[name] = distance
        sorted_Dict = {k: v for k, v in sorted(real_Distance.items(), key=lambda item: item[1])}
    return sorted_Dict

finalQuery = mongoReadDb()
distances = calculateDistance(finalQuery, "20707")
print(distances)
