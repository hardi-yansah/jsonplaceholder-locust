from locust import HttpUser, between, task

class ApiReport(HttpUser):
    wait_time = between(1, 5)  # Add some randomness to the wait time

    headers = {"Content-Type": "application/json"}
     
    @task(1)
    def get_posts(self):
        # Define the API endpoint
        api_url = "/posts"

        # Send an HTTP GET request
        response = self.client.get(api_url, headers=self.headers)
    
    @task(2)
    def get_posts_detail(self):
        # Define the API endpoint
        api_url = "/posts/1"

        # Send an HTTP GET request
        response = self.client.get(api_url, headers=self.headers)
    
    @task(3)
    def post(self):
        # Define the API endpoint
        api_url = "/posts"

        # Send an HTTP GET request
        response = self.client.post(api_url, headers=self.headers, json={"title":"test tittle", "body":"test body", "userId": 1})
