
class User:
    _id_counter = 1
    users = []

    def __init__(self, name, id=None):
        if id:   # restoring from JSON
            self.id = id
            if id >= User._id_counter:
                User._id_counter = id + 1
        else:    # new user
            self.id = User._id_counter
            User._id_counter += 1
        self.name = name
        self.projects = []
        self.tasks = []
        User.users.append(self)

    @classmethod
    def get_all(cls):
        return cls.users
    
    def __str__(self):
        return f"User(id={self.id}, name='{self.name}')"

    def add_project(self, project):
        self.projects.append(project)

    def list_projects(self):
        return [p.name for p in self.projects]

    def add_task(self, task):
        self.tasks.append(task)

    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.description == title:
                return task
        return None

    # JSON helpers
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "projects": [p.to_dict() for p in self.projects],
            "tasks": [t.to_dict() for t in self.tasks],
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], id=data["id"])
        # restore projects
        for p in data.get("projects", []):
            project = Project.from_dict(p)
            user.projects.append(project)
        # restore tasks
        for t in data.get("tasks", []):
            task = Task.from_dict(t)
            user.tasks.append(task)
        return user


class Project:
    _id_counter = 1
    projects = []

    def __init__(self, name, id=None):
        if id:
            self.id = id
            if id >= Project._id_counter:
                Project._id_counter = id + 1
        else:
            self.id = Project._id_counter
            Project._id_counter += 1
        self.name = name
        Project.projects.append(self)

    @classmethod
    def get_all(cls):
        return cls.projects
    
    def __str__(self):
        return f"Project(id={self.id}, name='{self.name}')"

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], id=data["id"])


class Task:
    _id_counter = 1
    tasks = []

    def __init__(self, description, project_id=None, id=None, completed=False):
        if id:
            self.id = id
            if id >= Task._id_counter:
                Task._id_counter = id + 1
        else:
            self.id = Task._id_counter
            Task._id_counter += 1
        self.project_id = project_id
        self.description = description
        self.completed = completed
        Task.tasks.append(self)

    @classmethod
    def get_all(cls):
        return cls.tasks
    
    def __str__(self):
        status = "✔" if self.completed else "✗"
        return f"[Task {self.id}] {self.description} ({status})"
    
    def complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "description": self.description,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data["description"],
            project_id=data.get("project_id"),
            id=data["id"],
            completed=data.get("completed", False),
        )

