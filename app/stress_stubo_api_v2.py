from locust import HttpLocust, TaskSet, task

class ServiceBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # creating some scenarios
        for sn_no in xrange(100):
            self.client.put("/stubo/api/v2/scenarios", data={'scenario': 'scenario_name_locust_%s' % sn_no})

    # You can add more testing URLs here
    # @task(2)
    # def index(self):
    #     self.client.get("/")

    @task(1)
    def get_response_scenario_list(self):
        """

        Gets response from random scenario
        """
        self.client.get('/stubo/api/v2/scenarios')


class WebsiteUser(HttpLocust):
    task_set = ServiceBehavior
    min_wait = 5500000
    max_wait = 10000000
