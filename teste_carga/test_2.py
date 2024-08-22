from uuid import uuid4
from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        ''' Will be executed at the start of the test for each user. '''
        self.email = f"user{str(uuid4())}@example.com"
        self.password = "password"
        self.user_id = None
        self.purchase_id = None
        self.register_user()

    def register_user(self):
        ''' Registers a new user and stores the ID. '''
        response = self.client.post(
            "/users",
            json={"email": self.email, "password": self.password}
        )
        if response.status_code == 200:
            self.user_id = response.json()["user_id"]

    @task
    def make_purchase(self):
        ''' Makes a purchase using the registered user's ID. '''
        if self.user_id:
            response = self.client.post(
                "/purchases",
                json={"user_id": self.user_id, "item_name": "item1", "price": 10.0}
            )

            if response.status_code == 200:
                self.purchase_id = response.json()["purchase_id"]
                self.make_payment()

    def make_payment(self):
        ''' Makes the payment for the purchase using the purchase ID. '''
        if self.user_id and self.purchase_id:
            _ = self.client.post(
                "/payments",
                json={"user_id": self.user_id, "purchase_id": self.purchase_id}
            )


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]