# locust-stresser
performance testing for stubo and beyond

# installation 
pip install -r requirements.txt

# usage
Testing stubo:
locust --host=http://__your_stubo_hostname__:__port__

Testing stester:
locust -f stress-falconer.py --host=http://localhost:8000

then, access locust web ui via http://127.0.0.1:8089/ and specify user count and hatch rate

