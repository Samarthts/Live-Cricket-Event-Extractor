import os
import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from main import app

class TestCricketEventExtractor(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch.dict(os.environ, {"GEMINI_API_KEY": "fake_key"})
    @patch("google.generativeai.GenerativeModel")
    def test_extract_events_success(self, mock_generative_model):
        # Mock the model's response
        mock_response = MagicMock()
        mock_response.text = '[{"over": "10.4", "event_type": "Wicket", "description": "Kohli out!"}]'
        
        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.return_value = mock_response
        mock_generative_model.return_value = mock_model_instance

        payload = {"text": "10.4: WICKET! Kohli is caught at long on!"}
        response = self.client.post("/extract-events", json=payload)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(len(data["events"]), 1)
        self.assertEqual(data["events"][0]["event_type"], "Wicket")

    def test_extract_events_missing_api_key(self):
        payload = {"text": "Some commentary"}
        
        # Temporarily remove GEMINI_API_KEY from environment if it exists
        with patch.dict(os.environ, {}):
            if "GEMINI_API_KEY" in os.environ:
                del os.environ["GEMINI_API_KEY"]
            response = self.client.post("/extract-events", json=payload)
            self.assertEqual(response.status_code, 500)
            self.assertIn("Gemini API key is not configured", response.json()["detail"])

if __name__ == "__main__":
    unittest.main()
