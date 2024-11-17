from locust import HttpUser, task, between

class HelloWorld(HttpUser):
    wait_time = between(5, 15)

    @task#
    # run command :  locust -f "./src/hello_world.py " -u 100 -r 1
    def test(self):
        self.client.get("https://www.demoblaze.com/")