# Main file for app

import os
import time
import calendar
import datetime
from datetime import date

current = str(date.today())
print(current) # yyyy-mm-day

#def main():

def current_calendar():
    text_calendar = calendar.TextCalendar()
    text_calendar.formatyear(2026)
    text_calendar.pryear(2026)
current_calendar()

class Task:
    def __init__(self, name: type = str, date: type = str, time: type = str, desc: type = str, location: type = str, host: type = str, tags: type = list):
        self.task_name = name ## Task name 
        self.task_date = date ## The Date
        self.task_time = time #The time of the task
        self.task_host = host ## The host
        self.task_desc = desc ## The description
        self.task_location = location ### Location
        self.task_tags = tags ### Extra tags

        self.task_importance: type = int

        pass

    def time_til(self, current):
        #Returns the time until this task
        pass

    def has_tag(self, tag):
        for i in self.task_tags:
            if i == tag:
                return True
        return False

    def get_importance(self, user):
        importance = -1
        with open ("host.txt") as file: 
            file.readline()
            for i in file.readlines():
                entry = i.split(",")
                if entry[0] == self.task_host:
                    if user == (self.task_host):  ### User should have a function to check if it is in the group. Ex user.is_in(self.task_host)
                        importance = int(entry[1].strip())
                    pass


        return importance
    pass

hackathon = Task("Name", "2026-11-13", "11:20", "BITCH", "McNair Hall", "COE", ["H", "Y"])

print(hackathon.get_importance("COE"))
#def sort(list, by):

#def notify():

#def register():

#def search(query):
    #if query:
        # Additional logic goes here

#def deadline(current, date):

def today(current):
    """Get the current day as an integer from the date"""
    new_current = int(current[8:])
    return new_current
today(current)
