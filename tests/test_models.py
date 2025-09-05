import pytest
from models import User, Project, Task

def setup_function():
    # reset class state before each test
    User._id_counter = 1
    User.users = []
    Project._id_counter = 1
    Project.projects = []
    Task._id_counter = 1
    Task.tasks = []

def test_create_user():
    u = User("Alice")
    assert u.id == 1
    assert u.name == "Alice"
    assert len(User.get_all()) == 1

def test_add_project_to_user():
    u = User("Bob")
    p = Project("Test Project")
    u.add_project(p)
    assert p in u.projects
    assert u.list_projects() == ["Test Project"]

def test_add_task_to_user():
    u = User("Charlie")
    t = Task("Do homework")
    u.add_task(t)
    assert t in u.tasks
    assert u.get_task_by_title("Do homework") == t

def test_complete_task():
    t = Task("Finish report")
    assert not t.completed
    t.complete()
    assert t.completed
