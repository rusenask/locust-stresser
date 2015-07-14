from locust import HttpLocust, TaskSet, task

class ServiceBehavior(TaskSet):
     
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    # You can add more testing URLs here
    # @task(2)
    # def index(self):
    #     self.client.get("/")

    @task(1)
    def get_response(self):
        """

        Gets response from random scenario
        """
        self.client.get('/quote')


class WebsiteUser(HttpLocust):
    task_set = ServiceBehavior
    min_wait = 15
    max_wait = 40
