from enum import StrEnum
from datetime import date, timedelta
from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints

StringConstraints(strip_whitespace=True, min_length=4, max_length=100)
StrippedName = Annotated[str, StringConstraints(strip_whitespace=True, min_length=4, max_length=100)]

class ProjectCreate(BaseModel):
    name: StrippedName
    description: str | None = Field(None, max_length=1000)

class TaskCreate(BaseModel):
    title: StrippedName
    description: str | None = Field(None, max_length=1000)
    due_date: date | None = None
    project_id: int

project = ProjectCreate(name="Payments API", description="Handles all payments")
print(project.name)  # Payments API
print(project.description)  # Handles all payments



# class TaskStatus(StrEnum):
#     planned = "planned"
#     in_progress = "in_progress"
#     blocked = "blocked"
#     done = "done"

# def is_overdue(due_date, status):
#     if due_date is None:
#         return False
#     if status == TaskStatus.done:
#         return True
#     return due_date < date.today()

# def next_status(current):
#     match current:
#         case TaskStatus.planned:
#             return TaskStatus.in_progress
#         case TaskStatus.in_progress:
#             return TaskStatus.done
#         case TaskStatus.done | TaskStatus.blocked:
#             return current
#     return None

# if __name__ == "__main__":
#     yesterday = date.today() - timedelta(days=1)
#
#     print(is_overdue(None, TaskStatus.planned))  # False
#     print(is_overdue(yesterday, TaskStatus.done))  # False
#     print(is_overdue(yesterday, TaskStatus.in_progress))  # True
#
#     print(next_status(TaskStatus.planned))  # TaskStatus.in_progress
#     print(next_status(TaskStatus.in_progress))  # TaskStatus.done
#     print(next_status(TaskStatus.done))  # TaskStatus.done
#     print(next_status(TaskStatus.blocked))  # TaskStatus.blocked

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# person = {
#     "name": "Deepak",
#     "num_pets" : 2
# }
# for key, value in person.items():
#     print(value)

# project_names = ["Payments API", "Developer Portal", "Ops Console"]
# # for project_name in project_names:
# #     print(f"{project_name.lower().replace(" ", "-")}")
# slugs = [project_name.lower().replace(" ", "-") for project_name in project_names]
# print(slugs)

# tasks = [
#     {"title": "ship docs", "done": False},
#     {"title": "cut release", "done": True},
#     {"title": "announce launch", "done": False},
# ]
#
# open_titles = [task['title'] for task in tasks if not task['done']]
# print(open_titles)

# def validate_project_name(name: str) -> str:
#     cleaned = name.strip()
#     if not cleaned:
#         raise ValueError("Project name must not be empty")
#     return cleaned
#
# print(validate_project_name("payment api"))

# file = open("task.txt")
# try:
#     content = file.read()
#     print(content)
# finally:
#     file.close()

# def shout(text: str) -> str:
#     return text.upper() + "!"

# yell = shout
# print(yell("Hello World!"))