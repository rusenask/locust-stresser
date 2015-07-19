from locust import HttpLocust, TaskSet, task
from locust import events
import json
import requests
from random import randint

HOST = "http://localhost"
PORT = "8001"

TARGET = "%s:%s" % (HOST, PORT)

class ServiceBehavior(TaskSet):

    scenario_name = None

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        scenario_inserted = False

        while not scenario_inserted:
            sn_no = randint(0, 100)
            payload = {'scenario': 'scenario_name_locust_%s' % sn_no }
            headers = {'content-type': 'application/json'}
            with self.client.put("/stubo/api/v2/scenarios",
                                 data=json.dumps(payload),
                                 headers=headers,
                                 catch_response=True) as response:
                if response.status_code == 201:
                    scenario_inserted = True
                    self.scenario_name = payload['scenario']
                # duplicate scenario - continue trying to create
                if response.status_code == 422:
                    response.success()

    @task(2)
    def get_scenario_details(self):
        self.client.get("/stubo/api/v2/scenarios/objects/%s" % self.scenario_name)

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
