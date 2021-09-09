# Multi-temporal images based on sentinel-hub 

Clone repository and install dependencies in `pip install -r requirements.txt`

Create account on Sentinelhub to obtain [credentials](https://apps.sentinel-hub.com/dashboard/#/): 

Install repository: 

`pip install sentinelhub`

`pip install sentinelhub --upgrade`

For more information, refer to [official documentation](https://sentinelhub-py.readthedocs.io/en/latest/install.html).

## Data per year 

Based on [epi week](https://www.cmmcp.org/mosquito-surveillance-data/pages/epi-week-calendars-2008-2021)

* 2016: (2016,1,3) - (2016,12,31)

* 2017: (2017,1,1) - (2017,12,30) 

* 2018: (2018,12,30) - (2018,12,29). First week from (2018,1,1) - (2018,1,6)

* 2019: (2018,12,29) to end first week the (2019,1,5), end (2019,12,31)

* 2020: (2019,12,28) to end first week the  (2020,1,4), end (2019,12,31)

* 2021: (2020,12,26) to end first week the  (2021,1,2), end (2021,9,8)


## About dataset version 1: 

Extracted from [sentinel-hub](https://docs.sentinel-hub.com/api/latest/data/sentinel-2-l1c/), starting from august 2015 to december of 2018, every week. 

* Sampled weekly based on epiweek

* 10 m resolution - customizable

* (765, 1205) pixels per image - customizable

* Stored in `tiff`format as it contains 7 bands: "B02", "B03", "B04", "B05", "B06", "B07", "B08"

* Filtered by least amount of Clouds: leastCC - pixel is selected from tile with the least cloud coverage metadata. Note that "per tile" information is used here, each covering about a 12,000 sq. km area, so this information is only an estimate .

[Download dataset version 1 for 7 bands and RGB - zip file or use in drive](https://drive.google.com/drive/folders/1pBPLmzGg1gNGP2oIfeurb_Rsp2E9k9cU?usp=sharing)

