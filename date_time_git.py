import datetime
import time
class cl_date_time_git:

    def __init__(self,str_date_time):
        self.str_date_time=str_date_time

    def convert_into_date(self):
        self.start_date=''
        self.start_date+=self.str_date_time[0:4]+'-'+self.str_date_time[5:7]+'-'+self.str_date_time[8:10]
        return self.start_date

    def convert_into_epoch(self):
        self.epoch_str=''
        self.epoch_str+=self.start_date+' '+self.str_date_time[11:19]
        self.epoch_pattern = '%Y-%m-%d %H:%M:%S'
        self.epoch_time = int(time.mktime(time.strptime(self.epoch_str, self.epoch_pattern)))
        return self.epoch_time

    def current_epoch_time(self):
        self.epoch_time = int(time.time())
        return self.epoch_time
