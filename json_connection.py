import urllib2
import json
import pymysql
class json_l:

    def fetch_data_from_api(self,url):
        self.url=url
        self.json_obj=urllib2.urlopen(self.url)
        self.data = json.load(self.json_obj)
        self.data1 = json.dumps(self.data, indent=2)
        return self.data

    def return_data(self):
        print self.data1
        return self.data1

        
class database:
    def connect(self,data_base):
        """Connect to the SQLite3 database."""
        self.data_base=data_base
        self.db=pymysql.connect(host='127.0.0.1',user='root',password='password',db=data_base);
        self.cursor = self.db.cursor()

    def close(self): 
        """Close the SQLite3 database."""

        self.db.commit()
        self.db.close()    

