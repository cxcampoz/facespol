import json


class SearchData:
    def __init__(self):
        self.a = "a"

    def testAPI(self, search):
        data = json.load(open('fake_db/data.json'))
        finalReturn = data[search]
        print(finalReturn)
        return finalReturn
