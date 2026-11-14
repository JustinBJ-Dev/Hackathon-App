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
                if entry[0].strip() == self.task_host:
                    if user == (self.task_host):  ### User should have a function to check if it is in the group. Ex user.is_in(self.task_host)
                        importance = int(entry[1].strip())
                    pass
        return importance

hackathon = Task("Hackathon", "2026-11-13", "11:20", "BITHCH", "McNair Hall", "COE", ["compsci", "robotics", "nerd", "programming"])
black = Task("Black in big tech", "2026-11-13", "11:20", "BITHCH", "McNair Hall", "COE", ["compsci", "robotics", "programming"])
lobby = Task("Lobby day", "2026-11-13", "11:20", "BITHCH", "McNair Hall", "COE", ["compsci", "robotics", "nerd", "programming"])

test = [hackathon, black, lobby]

def sort_task(list: type = list, by: int = 0, tag: type = str, user: type = str):
    # If by is 0: sort by tag
    # If by is 1: sort by importance
    # If by is 2: sort of both

    def sort_by_name(task: Task):
        return task.task_name.lower()

    def sort_by_tag(task: Task): ## Sorts by tag
        if task.has_tag(tag):
            return task.task_name # Returns the task name to be sort if it has the tag
        else:
            return "🐘" # Returns the largest unicode that I can find so that it sorted to the bottom
    
    def sort_by_importance(task: Task): ## Gets the importance of each task to sort by 
        return task.get_importance(user) # Needs the user to work properly this may change when user is implemented

    sorted_list = []
    if by == 0:
        sorted_list = sorted(sorted_list, key=(sort_by_tag))
    elif by == 1:
        sorted_list = sorted(list, key=(sort_by_importance), reverse=True)
    elif by == 2:
        sorted_list = sorted(list, key=(sort_by_tag)) ## Sorts by tag first
        sorted_list = sorted(sorted_list, key=(sort_by_importance), reverse=True) ## Sorts by importance next
    
    return sorted_list


for i in test:
    print(i.task_name)

for i in (sort_task(test, 1, "nerd", "COE")):
    print(i.task_name, i.get_importance("COE"))

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
