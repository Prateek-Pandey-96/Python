from fastapi import FastAPI, status, HTTPException
from models.task import Task
from models.response import Response
from database.db import task_col

app = FastAPI()

@app.post('/task')
def createTask(task: Task):
    try:
        x = task_col.insert_one(task.to_dict())
    except TypeError:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, f"failed to create the task")
    return Response(status=status.HTTP_200_OK, desc=f"task created with id: {x.inserted_id}")


@app.get("/task/{task_title}")
def getTask(task_title: str):
    try:
        query = { "title": task_title }
        doc = task_col.find_one(query)
        return Response(status=status.HTTP_200_OK, desc=Task(title=doc['title'], description=doc['description']))
    except TypeError:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"no task with the title: {task_title}")


@app.put("/task")
def updateTask(task: Task):
    try:
        doc = task_col.update_one({"title": task.title}, {"$set": task.to_dict()})
        if doc.modified_count == 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"no task with the title: {task.title} or the description didn't change")
        return Response(status=status.HTTP_200_OK, desc=f"task updated!")
    except TypeError:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, f"some error occured while updating the task")
    
@app.delete("/task/{task_title}")
def deleteTask(task_title: str):
    try:
        query = { "title": task_title }
        doc = task_col.delete_one(query)
        if doc.deleted_count == 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"no task with the title: {task_title}")
        return Response(status=status.HTTP_200_OK, desc=f"task deleted!")
    except TypeError:
         raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, f"some error occured while deleting the task")