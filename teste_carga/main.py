from locust import HttpUser, task


class LoadTest(HttpUser):
    @task
    def load_test(self):
        self.client.get("/items/key2")