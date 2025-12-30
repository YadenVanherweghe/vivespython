class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title

    def __str__(self):
        return f"{self.id} - {self.title}"
