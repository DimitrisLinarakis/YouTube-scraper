from pymongo import MongoClient

class DocumentsFinder:

    myClient = MongoClient("mongodb+srv://linarakisvlachos:linarakisvlachos-2020@cluster0.8oq45.mongodb.net/test?authSource=admin&replicaSet=atlas-abru45-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true") 
    db = myClient['Thesis']
    collection=db['YouTubeChannels']

    def findDocuments(self, filter, project, skip_num, limit_num):
        if skip_num != None:
            if limit_num != None:
                if project != None:
                    return self.collection.find(filter, project).skip(skip_num).limit(limit_num)
                return self.collection.find(filter).skip(skip_num).limit(limit_num)
            else:
                if project != None:
                    return self.collection.find(filter, project).skip(skip_num)
                return self.collection.find(filter).skip(skip_num)
        else:
            if limit_num != None:
                if project != None:
                    return self.collection.find(filter, project).limit(limit_num)
                return self.collection.find(filter).limit(limit_num)
            return self.collection.find(filter)