"""1. Creați clasa TimeConverter cu două proprietăți(atribute): 
- hours - numărul de ore (int)- minutes - numărul de minute (int) 
2. Clasa trebuie să conțină următoarele metode publice:- toMinutes() - convertește timpul total în minute- toHours() - convertește timpul total în ore- addTime() - adună încă un interval de timp și returnează rezultatul în minute- diffTime() - calculează diferența față de alt interval de timp și returnează rezultatul 
în minute """

class TimeConverter:
    def __init__(self, hours, minutes):
        self.__hours = hours
        self.__minutes = minutes

    @property
    def h(self):
        return self.__hours
    
    @h.setter
    def h(self, new_value):
        if isinstance(new_value, int) and new_value >= 0:
            self.__hours = new_value

    @property
    def m(self):
        return self.__minutes
    
    @m.setter
    def m(self, new_value):
        if isinstance(new_value, int) and new_value >= 0:
            self.__minutes = new_value % 60
            self.h += new_value // 60


    def __str__(self):
        return f"{self.h} ore {self.m} minute"
    
    def toMinutes(self):
        return self.h * 60 + self.m

    @property
    def total_minutes(self):
        return self.h * 60 + self.m

    def toHours(self):
        return round(self.h + self.m / 60, 2)
    
    @property
    def total_hours(self):
        return round(self.h + self.m / 60, 2)
    

    def addTime(self, other_tc):
        self.h += other_tc.h
        self.m += other_tc.m
        
    def diffTime(self, other_tc):
        self.h -= other_tc.h
        if self.m >= other_tc.m:
            self.m -= other_tc.m
        else:
            self.m = (60 + self.m - other_tc.m)
            self.h -= 1
        


tc = TimeConverter(6, 30)
print(tc)
print(tc.toMinutes())
print(tc.total_minutes)
print(tc.toHours())
print(tc.total_hours)
    
tc2 = TimeConverter(1, 33)
tc.diffTime(tc2)
print(tc)

        