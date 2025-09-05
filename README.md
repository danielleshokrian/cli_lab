# cli_lab

A simple command-line interface (CLI) project manager built in Python.
You can create users, assign projects, add tasks, and mark them as completed.
All data is stored in local JSON files for persistence.

## Features

Users: create and manage users.

Projects: assign projects to users.

Tasks: add tasks, link to users, mark as completed.

Persistence: automatically saves to data/users.json.

CLI-based: manage everything directly from the terminal.

Tests: unit tests + CLI tests with pytest.

## Installation

Clone or download this repository.

Create a virtual environment:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Run the CLI tool with:

python main.py <command> [arguments]

### Available Commands:

Add a user
python main.py add-user Alice

Add a project for a user
python main.py add-project Alice "CLI Project"

Add a task for a user
python main.py add-task Alice "Finish CLI setup"

Complete a task
python main.py complete-task Alice "Finish CLI setup"