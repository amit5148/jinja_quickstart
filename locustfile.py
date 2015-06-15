from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task()
    def search(self):
        self.client.get("/search")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=500
    max_wait=5000