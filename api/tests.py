from django.test import TestCase
from rest_framework import status

class APITestCase(TestCase):
    def test_api_with_token(self):
        # Replace this with an actual token if required for your tests
        token = 'ea6a55e91db49c2f350d251befce9ec3ff03fafb'
        
        # Send a GET request to the endpoint using Django's test client with token in headers
        response = self.client.get(
            '/api/food-items/', 
            HTTP_AUTHORIZATION=f'Token {token}'
        )
        
        # Print status code and response data (for testing purposes)
        print(response.status_code)
        print(response.json())

        # You can also assert expected results, e.g.:
        self.assertEqual(response.status_code, status.HTTP_200_OK)
