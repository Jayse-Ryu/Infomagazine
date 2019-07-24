import pymongo
from bson import ObjectId
from bson.json_util import dumps

from infomagazine.settings import MONGO_CLOUD_ACCOUNT, MONGO_CLOUD_PASSWD


class LandingPage:
    def __init__(self, choice_db):
        client = pymongo.MongoClient(
            "mongodb+srv://%s:%s@production-vpq2e.mongodb.net/test?retryWrites=true&w=majority" % (
                MONGO_CLOUD_ACCOUNT, MONGO_CLOUD_PASSWD))

        self.db = client[choice_db]

    def list(self, choice_collection, projection=None):
        find_option = ({}, projection,)
        queryset = self.db[choice_collection].find(*find_option)
        queryset = dumps(queryset)
        return queryset

    def create(self, choice_collection, document):
        queryset = self.db[choice_collection].insert_one(document)
        return queryset.acknowledged

    def retrieve(self, choice_collection, doc_id, projection=None):
        find_option = ({'_id': ObjectId(doc_id)}, projection,)
        queryset = self.db[choice_collection].find_one(*find_option)
        queryset = dumps(queryset)
        return queryset

    def update(self, choice_collection: str, doc_id: str, data_to_update: dict, option: dict = None) -> dict:
        if option is None:
            option = {'returnNewDocument': True}
        else:
            option.update({'returnNewDocument': True})
        data_to_update.update({
            '$currentDate':
                {
                    'lastModified': True,
                    'updated_date':
                        {
                            '$type': 'timestamp'
                        }
                }
        })
        find_option = ({'_id': ObjectId(doc_id)}, data_to_update, option)
        queryset = self.db[choice_collection].find_one_and_update(*find_option)
        queryset = dumps(queryset)
        return queryset

    def destroy(self):
        pass
