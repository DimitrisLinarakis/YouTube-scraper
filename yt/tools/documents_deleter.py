import json
from pymongo import MongoClient

class DocumentsDeleter:

    myClient = MongoClient("mongodb+srv://linarakisvlachos:linarakisvlachos-2020@cluster0.8oq45.mongodb.net/test?authSource=admin&replicaSet=atlas-abru45-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true") 
    db = myClient['Thesis']
    collection=db['YouTubeChannels']

    def deleteDocument(self,id):
        self.collection.delete_one({"channel_data.id":id})