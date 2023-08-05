from F import LIST
from F.LOG import Log
from FCM import MCServers
from FCM.MCCore import MCCore
from FCM.FQ import Q

Log = Log("fCollection")

""" Master Class to work with a Collection """
class fCollection(MCCore):

    def construct_collection_with_host(self, dbUri, dbName, collectionName):
        try:
            if not dbUri:
                dbUri = MCServers.MONGO_DATABASE_URI
                dbName = MCServers.db_name
            # MCDB.GET_SET_CUSTOM_HOST(dbUri, dbName, ARTICLES_COLLECTION)
            self.constructor(dbUri, dbName)
            self.set_ccollection(collectionName)
            self.mcollection = self.core_collection
            return self
        except Exception as e:
            Log.e("Failed to Connect to DB.", error=e)
            return False

    def get_field_names(self):
        fields = []
        oneResult = self.base_query({}, 0, 1)
        oneDoc = LIST.get(0, oneResult)
        for doc in oneDoc:
            fields.append(doc)
        return fields

    def search_field(self, search_term, field_name, page=0, limit=100):
        return self.base_query(kwargs=Q.SEARCH(field_name, search_term), page=page, limit=limit)

    # def search_all(self, search_term, page=0, limit=100, strict=False):
    #     if strict:
    #         return self.base_query(kwargs=JQ.SEARCH_ALL_STRICT(search_term), page=page, limit=limit)
    #     return self.base_query(kwargs=JQ.SEARCH_ALL(search_term), page=page, limit=limit)
    #
    # def search_unlimited(self, search_term):
    #     return self.base_query(kwargs=JQ.SEARCH_ALL(search_term), page=False, limit=False)
    #
    # def search_cli(self, search_term, filters):
    #     kwargs = Q.AND([JQ.SEARCH_ALL(search_term), filters])
    #     return self.base_query(kwargs=kwargs, page=False, limit=False)
    #
    # def search_unlimited_filters(self, search_term, filters):
    #     kwargs = Q.AND([JQ.SEARCH_ALL(search_term), filters])
    #     return self.base_query(kwargs=kwargs, page=False, limit=False)
    #
    # def search_before_or_after_date(self, search_term, date, page=0, limit=100, before=False):
    #     if before:
    #         return self.base_query(kwargs=JQ.SEARCH_ALL_BY_DATE_LTE(search_term, date), page=page, limit=limit)
    #     return self.base_query(kwargs=JQ.SEARCH_ALL_BY_DATE_GTE(search_term, date), page=page, limit=limit)
    #
    # def search_field_by_date(self, date, search_term, field_name):
    #     return self.base_query(kwargs=JQ.SEARCH_FIELD_BY_DATE(date, field_name, search_term))


if __name__ == '__main__':
    f = fCollection().construct_collection_with_host(MCServers.MONGO_DATABASE_URI, "research", "virtual_worlds")
    print(f.get_field_names())





