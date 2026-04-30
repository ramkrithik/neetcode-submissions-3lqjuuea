class MyCalendar:
    
    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        for time in self.calendar:
            if startTime < time[1] and endTime > time[0]:
                return False

        self.calendar.append([startTime,endTime])
        return True 
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)