import pymongo
import matplotlib.pyplot as plt
import numpy as np

theDATABASEcONNECTION = 'mongodb://localhost:27017'
theDatabase = 'Music5'
myclient = pymongo.MongoClient(theDATABASEcONNECTION)
myNoSqlDBClient = pymongo.MongoClient(theDATABASEcONNECTION)
myDB = myNoSqlDBClient[theDatabase]
col1 = 'Music_song'
Genre = []
Songs = []

if col1 in myDB.list_collection_names():
    Songcollection = myDB['Music_song']
    print('Collection found')
    for x in Songcollection.find():
        Genre.append(x['Genre'])
    agg_result = Songcollection.aggregate(
        [{
            "$group":
            {"_id": "$Genre",
             "Song": {"$sum": 1}
             }}
         ])


x = np.array(Genre)
y = np.array(Songs)


plt.bar(x, y, color="red", width=.5)
plt.title("Faviourite genre by number")
plt.xlabel("Genre")
plt.ylabel("Number of Songs")
plt.show()
