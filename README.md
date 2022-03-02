# Satellite data - Dengue Project

1-. Clone repository and install dependencies in `pip install -r requirements.txt`

2. Create account on Sentinelhub to obtain [credentials](https://apps.sentinel-hub.com/dashboard/#/): 

22
https://drive.google.com/drive/folders/1SxKNhKO1czSFz50_31wS-jlF6jZHpj0O?usp=sharing
3. Install sentinelhub API: 

`pip install sentinelhub` if any errors then: `pip install sentinelhub --upgrade`

or manually:

`git clone https://github.com/sentinel-hub/sentinelhub-py.git`

`cd sentinelhub-py`

` python setup.py build`

` python setup.py install`

` cd ..`

` pip install -r requirements.txt`

For more information, refer to [official documentation](https://sentinelhub-py.readthedocs.io/en/latest/install.html).

## Data per year 

Based on [epi week](https://www.cmmcp.org/mosquito-surveillance-data/pages/epi-week-calendars-2008-2021)

* 2016: (2016,1,3) - (2016,12,31)

* 2017: (2017,1,1) - (2017,12,30) 

* 2018: (2018,12,30) - (2018,12,29). First week from (2018,1,1) - (2018,1,6)

* 2019: (2018,12,29) to end first week the (2019,1,5), end (2019,12,31)

* 2020: (2019,12,28) to end first week the  (2020,1,4), end (2019,12,31)

* 2021: (2020,12,26) to end first week the  (2021,1,2), end (2021,9,8)


## About data: 

Extracted from [sentinel-hub](https://docs.sentinel-hub.com/api/latest/data/sentinel-2-l1c/), starting from august 2015 to december of 2018, every week. 

* Sampled weekly based on epiweek

* 10 m resolution - customizable

* (765, 1205) pixels per image - customizable

* Stored in `tiff`format as it contains 7 bands: "B01" - "B12"

* Filtered by least amount of Clouds: leastCC - pixel is selected from tile with the least cloud coverage metadata. Note that "per tile" information is used here, each covering about a 12,000 sq. km area, so this information is only an estimate .

# Download

1. Download dataset for 5 cities [Here](https://console.cloud.google.com/storage/browser/colombia_sebasmos)

# About API

1. Code for downloading satellite data is mantained [here](https://github.com/sebasmos/satellite.extractor/blob/main/Reading_GCP_from_Colab.ipynbhttps://github.com/sebasmos/satellite.extractor/blob/main/Reading_GCP_from_Colab.ipynbhttps://github.com/sebasmos/satellite.extractor/blob/main/Reading_GCP_from_Colab.ipynb)
