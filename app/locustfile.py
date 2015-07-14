from locust import HttpLocust, TaskSet, task
import random


class ServiceBehavior(TaskSet):
    matcher = '<request><a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> <a>lot of xml</a> </request>'

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # self._load_testing_stubs()
        pass

    def _load_testing_stubs(self):
        """

        Load performance test data (over 10,000 stubs in 100 scenarios).
        This will take some time to run and leaves 100 sessions in playback mode.
        """
        self.client.get("/stubo/api/exec/cmds?cmdfile=/static/cmds/perf/perf_setup.commands")

    # @task(2)
    # def index(self):
    #     self.client.get("/")

    @task(1)
    def get_response(self):
        self.client.post("/stubo/api/get/response?session=playback_%s" % random.randint(1, 100), self.matcher)


class WebsiteUser(HttpLocust):
    task_set = ServiceBehavior
    min_wait = 15
    max_wait = 40
