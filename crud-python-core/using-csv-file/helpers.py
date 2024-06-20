import constants
import csv

def getTasks():
    try:
        with open(f"./{constants.FILENAME}", 'r') as file:
            csvreader = csv.reader(file)
            tasks = []
            for row in csvreader:
                tasks.append((row[0], row[1]))
            return tasks
    except:
        return []

def listTasks():
    try:
        tasks = getTasks()
        idx = 0
        for task in tasks:
            idx+=1
            print(idx, ' '*2, task[0], ' '*15, task[1])
    except FileNotFoundError:
        return []

def addTask():
    title = input('Enter the task title  ')
    duration = input('Enter the task duration  ')
    with open(f"./{constants.FILENAME}", 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow([f"{title}", f"{duration}"])
    

def deleteTask():
    id = input('Enter the id of task to remove  ')
    tasks = getTasks()
    try:
        with open(f"./{constants.FILENAME}", 'w', newline='') as file:
            csvwriter = csv.writer(file)
            idx = 0
            for task in tasks:
                idx+=1
                if idx==int(id):
                    continue
                csvwriter.writerow([f"{task[0]}", f"{task[1]}"])
    except FileNotFoundError:
        print('file not present')

def updateTask():
    id = input('Enter the id of task to remove  ')
    updatedtitle = input('Enter updated title of task  ')
    updatedduration = input('Enter updated duration of task  ')
    tasks = getTasks()
    try:
        with open(f"./{constants.FILENAME}", 'w', newline='') as file:
            csvwriter = csv.writer(file)
            idx = 0
            for task in tasks:
                idx+=1
                if idx==int(id):
                    csvwriter.writerow([f"{updatedtitle}", f"{updatedduration}"])
                    continue
                csvwriter.writerow([f"{task[0]}", f"{task[1]}"])
    except FileNotFoundError:
        print('file not present')