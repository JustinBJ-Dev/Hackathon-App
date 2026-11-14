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
    def __init__(self, name: type = str, date: type = str, desc: type = str, location: type = str, host: type = str, tags: type = list):
        self.task_name = name
        self.task_date = date
        self.task_host = host
        self.task_desc = desc
        self.task_location = location
        self.task_tags = tags

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

    def get_importance(self):
        importance = 0


        return importance
    pass

hackathon = Task("Hackathon", "2026-11-13", "BITHCH", "McNair Hall", "COE", ["compsci", "robotics", "nerd", "programming"])

#def sort():

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
