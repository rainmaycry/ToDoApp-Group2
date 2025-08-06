# task_model.py
class TaskModel:
    def _init_(self, task_name):
        self.task_name = task_name

    def get_task_name(self):
        return self.task_name