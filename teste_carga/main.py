import time
from uuid import uuid4
from locust import HttpUser, between, task


class FastAPIUser(HttpUser):
    def on_start(self):
        self.email = f"user{str(uuid4())}@example.com"
        self.password = "password"
        self.user_id = None
        self.purchase_id = None
        self.payment_id = None
        self.register_user()
        self.register_purchase()
        self.register_payment()

    def register_user(self):
        response = self.client.post(
            "/users",
            json={"email": self.email, "password": self.password}
        )
        if response.status_code == 200:
            self.user_id = response.json()["user_id"]

    def register_purchase(self):
        response = self.client.post(
            "/purchases",
            json={"user_id": self.user_id, "item_name": "item1", "price": 10.0}
        )
        if response.status_code == 200:
            self.purchase_id = response.json()["purchase_id"]

    def register_payment(self):
        response = self.client.post(
            "/payments",
            json={"user_id": self.user_id, "purchase_id": self.purchase_id}
        )
        if response.status_code == 200:
            self.payment_id = response.json()["payment_id"]

    @task
    def get_user(self):
        self.client.get(f"/users/{self.user_id}")

    @task
    def get_purchase(self):
        self.client.get(f"/purchases/{self.purchase_id}", headers={"x-user-id": str(self.user_id)})

    @task
    def get_all_purchases(self):
        self.client.get("/purchases", headers={"x-user-id": str(self.user_id)})

    @task
    def get_payment(self):
        self.client.get(f"/payments/{self.payment_id}", headers={"x-user-id": str(self.user_id)})

    @task
    def get_all_payments(self):
        self.client.get("/payments", headers={"x-user-id": str(self.user_id)})