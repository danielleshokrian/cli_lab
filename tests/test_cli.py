import subprocess
import os
import tempfile
import shutil

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
MAIN = os.path.join(PROJECT_DIR, "main.py")

def run_cli(args):
    result = subprocess.run(
        ["python", MAIN] + args,
        capture_output=True,
        text=True,
        cwd=PROJECT_DIR
    )
    return result.stdout.strip()

def setup_function():
    # reset data dir before each test
    data_dir = os.path.join(PROJECT_DIR, "data")
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)
    os.makedirs(data_dir)

def test_add_user():
    output = run_cli(["add-user", "Alice"])
    assert "User 'Alice' added." in output

def test_add_project_and_task():
    run_cli(["add-user", "Bob"])
    output_proj = run_cli(["add-project", "Bob", "CLI Project"])
    output_task = run_cli(["add-task", "Bob", "Finish CLI setup"])

    assert "Project 'CLI Project' added for 'Bob'." in output_proj
    assert "Task 'Finish CLI setup' added for 'Bob'." in output_task

def test_complete_task():
    run_cli(["add-user", "Charlie"])
    run_cli(["add-task", "Charlie", "Do homework"])
    output = run_cli(["complete-task", "Charlie", "Do homework"])
    assert "Task 'Do homework' completed for 'Charlie'." in output
