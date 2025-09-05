import argparse
import os
from models import Task, User, Project
from file_ops import load_json, save_json

DATA_FILE = "data/users.json"
users = {}

def load_data():
    global users
    data = load_json(DATA_FILE)
    users = {}
    for u in data:
        user = User.from_dict(u)
        users[user.name] = user

def save_data():
    save_json(DATA_FILE, [u.to_dict() for u in users.values()])

def add_user(args):
    if args.name in users:
        print(f"User '{args.name}' already exists.")
        return
    user = User(args.name)
    users[args.name] = user
    save_data()
    print(f" User '{args.name}' added.")

def add_project(args):
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user
    project = Project(args.title)
    user.add_project(project)
    save_data()
    print(f" Project '{args.title}' added for '{args.user}'.")

def add_task(args):
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user
    task = Task(args.title)
    user.add_task(task)
    save_data()
    print(f" Task '{args.title}' added for '{args.user}'.")

def complete_task(args):
    user = users.get(args.user)
    if not user:
        print(f"User '{args.user}' not found.")
        return
    task = user.get_task_by_title(args.title)
    if not task:
        print(f"Task '{args.title}' not found for user '{args.user}'.")
        return
    task.complete()
    save_data()
    print(f" Task '{args.title}' completed for '{args.user}'.")

def main():
    if not os.path.exists("data"):
        os.makedirs("data")
    load_data()

    parser = argparse.ArgumentParser(description= "Manage users, projects, and tasks")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add-user", help="Add a new user")
    add_parser.add_argument("name")
    add_parser.set_defaults(func=add_user)

    add_parser = subparsers.add_parser("add-project", help="Add a project for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_project)

    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()