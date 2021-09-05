# Multi-temporal images based on sentinel-hub 

Clone repository and install dependencies in `pip install -r requirements.txt`

Then: 

`pip install sentinelhub --upgrade`

or Manually:

`conda install -c conda-forge sentinelhub`

` pip install -e . --upgrade`

For more information, refer to [official documentation](https://sentinelhub-py.readthedocs.io/en/latest/install.html).

## About dataset version 1: 

Extracted from [sentinel-hub](https://docs.sentinel-hub.com/api/latest/data/sentinel-2-l1c/), starting from august 2015 to december of 2018, every week. 

* Sampled weekly

* Stored in `tiff`format as it contains 7 bands: "B02", "B03", "B04", "B05", "B06", "B07", "B08"

* Filtered by least amount of Clouds: leastCC - pixel is selected from tile with the least cloud coverage metadata. Note that "per tile" information is used here, each covering about a 12,000 sq. km area, so this information is only an estimate .


[Download dataset version 1 here - zip file or use in drive](https://drive.google.com/drive/folders/1pBPLmzGg1gNGP2oIfeurb_Rsp2E9k9cU?usp=sharing)

