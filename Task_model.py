# task_model.py
class TaskModel:
    def _init_(self, task_name):
        self.task_name = task_name

    def get_task_name(self):
        return self.task_name
    
    def delete_task_name(self):
        self.task_name = None
        self.is_completed = False

    def is_completed(self):
        return self.is_completed