import time, logging, sys
import json
from locust import HttpUser, task, between, constant

class QuickstartUser(HttpUser):
    wait_time = constant(1)
    weight = 1

    @task
    def on_start(self):
        self.client.get(os.environ['LOCUST_TARGET_PATH'])
