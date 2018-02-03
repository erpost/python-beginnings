class Date():
    def get_date(self):
        return '2017-08-06'

class Time(Date):
    def get_time(self):
        return '08:15:00'

dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())    # Method is in Date(), but can be called from Time()