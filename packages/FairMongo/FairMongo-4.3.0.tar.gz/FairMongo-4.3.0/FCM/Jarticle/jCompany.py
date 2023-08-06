from F import DICT, LIST
from F.LOG import Log
from FCM.MCCore import MCCore

Log = Log("jCompany")

COLLECTION_NAME = "companies"

""" Master Class to work with Companies Collection """
class jCompany(MCCore):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect(COLLECTION_NAME)

    def add_companies(self, list_of_companies):
        for item in list_of_companies:
            print(item)
            self.insert_record(item)

    def find_company_by_ticker(self, ticker):
        company_record = self.base_query({'ticker': ticker})
        if company_record:
            single_record = LIST.get(0, company_record, False)
            return single_record
        return False

    def find_ticker_by_company(self, companyName, tickerOnly=False):
        company_record = self.base_query({'name': companyName})
        if company_record:
            single_record = LIST.get(0, company_record, False)
            if tickerOnly:
                ticker = DICT.get("ticker", single_record)
                return ticker
            return single_record
        return False

    def get_company_id_for_ticker(self, ticker):
        company = self.find_company_by_ticker(ticker)
        if company:
            id = DICT.get("_id", company)
            return id
        return False

    def get_list_of_all_companies(self):
        all_ = self.base_query({}, page=False, limit=False)
        return all_


if __name__ == '__main__':
    jc = jCompany()
    # record = jc.find_company_by_ticker("AMD")
    print(jc.get_field_names())