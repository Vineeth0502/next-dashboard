from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ChartDataTests(APITestCase):
    """
    Tests for the chart data endpoints of the Django REST API.
    """

    def test_candlestick_data(self):
        """
        Test the endpoint for candlestick chart data.
        """
        # Generate the URL for the 'candlestick-data' view using its name
        url = reverse('candlestick-data')
        
        # Make a GET request to the URL
        response = self.client.get(url)
        
        # Check that the status code of the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify that the response data matches the expected output
        self.assertEqual(response.data, {
            "data": [
                {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
                {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
            ]
        })

    def test_line_chart_data(self):
        """
        Test the endpoint for line chart data.
        """
        # Generate the URL for the 'line-chart-data' view using its name
        url = reverse('line-chart-data')
        
        # Make a GET request to the URL
        response = self.client.get(url)
        
        # Check that the status code of the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify that the response data matches the expected output
        self.assertEqual(response.data, {
            "labels": ["Jan", "Feb", "Mar", "Apr"],
            "data": [10, 20, 30, 40]
        })

    def test_bar_chart_data(self):
        """
        Test the endpoint for bar chart data.
        """
        # Generate the URL for the 'bar-chart-data' view using its name
        url = reverse('bar-chart-data')
        
        # Make a GET request to the URL
        response = self.client.get(url)
        
        # Check that the status code of the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify that the response data matches the expected output
        self.assertEqual(response.data, {
            "labels": ["Product A", "Product B", "Product C"],
            "data": [100, 150, 200]
        })

    def test_pie_chart_data(self):
        """
        Test the endpoint for pie chart data.
        """
        # Generate the URL for the 'pie-chart-data' view using its name
        url = reverse('pie-chart-data')
        
        # Make a GET request to the URL
        response = self.client.get(url)
        
        # Check that the status code of the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify that the response data matches the expected output
        self.assertEqual(response.data, {
            "labels": ["Red", "Blue", "Yellow"],
            "data": [300, 50, 100]
        })
