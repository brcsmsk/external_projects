import unittest
from unittest.mock import patch

from site_outage_detector import detect_site_outages


class TestDetectSiteOutages(unittest.TestCase):
    @patch("site_outage_detector.get_all_outages")
    @patch("site_outage_detector.get_site_info")
    @patch("requests.post")
    def test_detect_site_outages(
        self, mock_post, mock_get_site_info, mock_get_all_outages
    ):
        # Mock responses
        mock_get_all_outages.return_value = [
            {
                "id": "outage_id",
                "begin": "2022-01-01T00:00:00.000Z",
                "end": "2022-01-02T00:00:00.000Z",
            }
        ]
        mock_get_site_info.return_value = {
            "devices": [
                {
                    "id": "outage_id",
                    "name": "device_name",
                }
            ]
        }
        mock_post.return_value.status_code = 200

        # Call the function
        detect_site_outages("norwich-pear-tree", "2022-01-01T00:00:00.000Z", "API_KEY")

        # Assertions
        mock_get_all_outages.assert_called_once_with("API_KEY")
        mock_get_site_info.assert_called_once_with("norwich-pear-tree", "API_KEY")
        mock_post.assert_called_once_with(
            "https://api.krakenflex.systems/interview-tests-mock-api/v1/site-outages/norwich-pear-tree",
            headers={
                "Content-Type": "application/json",
                "x-api-key": "API_KEY",
                "accept": "*/*",
            },
            json=[
                {
                    "id": "outage_id",
                    "name": "device_name",
                    "begin": "2022-01-01T00:00:00.000Z",
                    "end": "2022-01-02T00:00:00.000Z",
                }
            ],
        )


if __name__ == "__main__":
    unittest.main()
