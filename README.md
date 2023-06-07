# KrakenFlex Data Case

# Site Outage Detector

This project contains a Python script that detects site outages based on provided parameters using the KrakenFlex API. It retrieves outage and site information from the API, matches them based on device ID and begin date, and posts the resulting site outages back to the API.

## Installation

1. Clone the repository:

  ```bash
   git clone https://github.com/brcsmsk/krakenflex
   ```

2. Navigate to the project directory:

   ```bash
   cd krakenflex
   ```
3. Set up a virtual environment for the project

   ```bash
   python3.9 -m venv krakenflex_venv
   ```
4. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the Python script `site_outage_detector.py` in a text editor.
2. Modify the following variables at the top of the script to suit your needs:
- `OUTAGE_URL`: The URL for retrieving all outages.
- `SITE_INFO_URL`: The URL for retrieving site information.
- `SITE_OUTAGES_URL`: The URL for posting site outages.
- `BEGIN_DATE`: The begin date for filtering outages.
- `SITE`: The site for which to detect outages.
- `API_KEY`: Your API key for accessing the KrakenFlex API.
3. Save the changes to the script.
4. Run the script using the following command:
 ```bash
  python site_outage_detector.py
   ```


## Testing

To run the unit tests for the code, you can use a testing framework like `unittest`. The tests are located in the file `test_site_outage_detector.py`. You can run the tests using the following command:
   ```bash
  python -m unittest test_site_outage_detector.py
   ```
