

class Nosql:
    def __init__(self, host='127.0.0.1', port=27017):
        import pymongo
        self.client = pymongo.MongoClient(host=host, port=port)
        self.table = self.client.ip_locate.iplocate

    def insert(self, data):
        self.table.insert(data)

    def get_data(self, ip):
        return self.table.find_one({'ip': ip})

    def update(self, ip, data):
        self.table.update({'ip': ip}, {'$set': data})

    def total_count(self):
        return self.table.find().count()

