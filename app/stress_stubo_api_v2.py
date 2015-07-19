from locust import HttpLocust, TaskSet, task
from locust import events
import json
import requests
from random import randint

HOST = "http://localhost"
PORT = "8001"

TARGET = "%s:%s" % (HOST, PORT)

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

def CleanUp( **kw):
    """
    Deleting scenarios after tests
    :param kw:
    """
    for sn_no in xrange(100):
        name = 'scenario_name_locust_%s' % sn_no
        requests.delete("%s/stubo/api/v2/scenarios/objects/%s" % (TARGET, name))

events.quitting += CleanUp

class APIUser(HttpLocust):
    task_set = ServiceBehavior
    host = TARGET
    min_wait = 50
    max_wait = 80
