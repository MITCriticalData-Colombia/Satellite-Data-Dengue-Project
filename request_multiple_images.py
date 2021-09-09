'''
We recommend to use eo-learn for more complex cases where you need multiple timestamps or high-resolution data for larger areas.
https://github.com/sentinel-hub/eo-learn

'''

from sentinelhub import SHConfig
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import sys
from datetime import timedelta
sys.path.insert(0,'..') # https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder 
from sentinelhub import MimeType, CRS, BBox, SentinelHubRequest, SentinelHubDownloadClient, DataCollection, bbox_to_dimensions, DownloadRequest

def plot_image(image, factor=1.0, clip_range = None, **kwargs):
    """
    Utility function for plotting RGB images.
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    if clip_range is not None:
        ax.imshow(np.clip(image * factor, *clip_range), **kwargs)
    else:
        ax.imshow(image * factor, **kwargs)
    ax.set_xticks([])
    ax.set_yticks([])

def multiple_stamps(betsiboka_coords_wgs84, start, end, year):

    # put here your credentials
    CLIENT_ID = "***"
    CLIENT_SECRET = "***"

    config = SHConfig()

    if CLIENT_ID and CLIENT_SECRET:
        config.sh_client_id = CLIENT_ID
        config.sh_client_secret=CLIENT_SECRET
    
    if not config.sh_client_id or not config.sh_client_secret:
        print("Warning! To use Process API, please provide the credentials (OAuth client ID and client secret).")

    resolution = 10
    betsiboka_bbox = BBox(bbox=betsiboka_coords_wgs84, crs=CRS.WGS84)
    betsiboka_size = bbox_to_dimensions(betsiboka_bbox, resolution=resolution)

    print(f'Image shape at {resolution} m resolution: {betsiboka_size} pixels')

    n_chunks = 53

    tdelta =  timedelta(days = 7)
    edges = [(start + i*tdelta).date().isoformat() for i in range(n_chunks)]
    slots = [(edges[i], edges[i+1]) for i in range(len(edges)-1)]

    print('Weekly time windows:\n')
    for slot in slots:
        print(slot)

    evalscript_true_color = """

        //VERSION=3
        function setup() {
            return {
                input: [{
                    bands: ["B02", "B03", "B04", "B05", "B06", "B07", "B08"]
                }],
                output: {
                    bands: 7
                }
            };
        }
        function evaluatePixel(sample) {
            return [sample.B08, 
                    sample.B07, 
                    sample.B06, 
                    sample.B05, 
                    sample.B04, 
                    sample.B03, 
                    sample.B02];
        }
    """
    
    evalscript_rgb ="""
    //VERSION=3
    
    function setup() {
      return {
        input: ["B02", "B03", "B04"],
        output: { bands: 3 }
      };
    }
    
    function evaluatePixel(sample) {
      return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];
    }
    """
    '''Check if directory exists, if not, create it'''
    
    # You should change 'test' to your preferred folder.
    path = os.path.abspath(os.getcwd()) + "/data"  + year
    CHECK_FOLDER = os.path.isdir(path)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(path)
        print("created folder : ", path)
    else:
            print(path, "folder already exists.")

    def get_true_color_request(time_interval):
        return SentinelHubRequest(
            data_folder= 'data' + year,
            evalscript=evalscript_rgb,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L1C,
                    time_interval=time_interval,
                    mosaicking_order='leastCC'
                )
            ],
            responses=[
                SentinelHubRequest.output_response('default', MimeType.TIFF)
            ],
            bbox=betsiboka_bbox,
            size=betsiboka_size,
            config=config
        )

    # create a list of requests
    list_of_requests = [get_true_color_request(slot) for slot in slots]
    list_of_requests = [request.download_list[0] for request in list_of_requests]
    print("Ended downloading")

    # download data with multiple threads

    data = SentinelHubDownloadClient(config=config).download(list_of_requests, max_threads=5)

    ncols = 4
    nrows = 3

    aspect_ratio = betsiboka_size[0] / betsiboka_size[1]
    subplot_kw = {'xticks': [], 'yticks': [], 'frame_on': False}

    #lot_image(data[3][:,:,:1], factor=1.0, cmap=plt.cm.Greys_r, vmin=0, vmax=120)

