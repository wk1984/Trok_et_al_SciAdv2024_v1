proj_dir = "/mnt/c/Users/kwang/Downloads/Trok_et_al_SciAdv2024_v1/Trok_et_al_SciAdv2024_v1-main/" # edit this line

import numpy as np
import pandas as pd
import xarray as xr
import time
import sys
sys.path.append(proj_dir)
from project_fxns import parameters as param
import importlib
importlib.reload(param)

#############################################################

def load_region_cnn_params(region_str, model_name, pr=False):
    batch_list = 250
    dw_list = 1.0
    sp = 40
  
    if (region_str == "southcentral_north_america") & (model_name == "CanESM5"):
        reg_list = 0.008
        decay_steps = 30
    elif (region_str == "southcentral_north_america") & (model_name == "UKESM1-0-LL"):
        reg_list = 0.02
        decay_steps = 30
    elif (region_str == "southern_europe") & (model_name == "CanESM5"):
        reg_list = 0.0045
        decay_steps = 20
    elif (region_str == "southern_europe") & (model_name == "UKESM1-0-LL"):
        reg_list = 0.0045
        decay_steps = 20
    elif (region_str == "western_russia") & (model_name == "CanESM5"):
        reg_list = 0.004
        decay_steps = 20
    elif (region_str == "western_russia") & (model_name == "UKESM1-0-LL"):
        reg_list = 0.004
        decay_steps = 20
    elif (region_str == "western_india") & (model_name == "CanESM5"):
        reg_list = 0.005
        decay_steps = 20
    elif (region_str == "western_india") & (model_name == "UKESM1-0-LL"):
        reg_list = 0.008
        decay_steps = 20
    elif (region_str == "pacific_northwest") & (model_name == "CanESM5"):
        reg_list = 0.001
        decay_steps = 30
    elif (region_str == "pacific_northwest") & (model_name == "UKESM1-0-LL"):
        reg_list = 0.001
        decay_steps = 30 

    if pr:
        if (region_str == "pacific_northwest") & (model_name == "CanESM5"):
            batch_list = 100
            dw_list = 1.0
            reg_list = 0.008
            decay_steps = 30
            sp = 43
        elif (region_str == "pacific_northwest") & (model_name == "UKESM1-0-LL"):
            batch_list = 100
            dw_list = 1.3 
            reg_list = 0.01
            decay_steps = 30
            sp = 52
            
    return batch_list, dw_list, reg_list, decay_steps, sp


######################################################


def load_region_constants_modules(region_str):
    if region_str == "southcentral_north_america":
        region_input_lat_bbox = param.southcentral_north_america_input_lat_bbox
        region_input_lon_bbox = param.southcentral_north_america_input_lon_bbox
        region_box_x = param.southcentral_north_america_box_x
        region_box_y = param.southcentral_north_america_box_y
        region_lat = param.southcentral_north_america_lat
        region_lon = param.southcentral_north_america_lon
        region_lon_EW = param.southcentral_north_america_lon_EW
        region_t62_lats = param.southcentral_north_america_input_t62_lats
        region_t62_lons = param.southcentral_north_america_input_t62_lons
    elif region_str == "southern_europe":
        region_input_lat_bbox = param.southern_europe_input_lat_bbox
        region_input_lon_bbox = param.southern_europe_input_lon_bbox
        region_box_x = param.southern_europe_box_x
        region_box_y = param.southern_europe_box_y
        region_lat = param.southern_europe_lat
        region_lon = param.southern_europe_lon
        region_lon_EW = param.southern_europe_lon_EW
        region_t62_lats = param.southern_europe_input_t62_lats
        region_t62_lons = param.southern_europe_input_t62_lons
    elif region_str == "western_russia":
        region_input_lat_bbox = param.western_russia_input_lat_bbox
        region_input_lon_bbox = param.western_russia_input_lon_bbox
        region_box_x = param.western_russia_box_x
        region_box_y = param.western_russia_box_y
        region_lat = param.western_russia_lat
        region_lon = param.western_russia_lon
        region_lon_EW = param.western_russia_lon_EW
        region_t62_lats = param.western_russia_input_t62_lats
        region_t62_lons = param.western_russia_input_t62_lons
    elif region_str == "western_india":
        region_input_lat_bbox = param.western_india_input_lat_bbox
        region_input_lon_bbox = param.western_india_input_lon_bbox
        region_box_x = param.western_india_box_x
        region_box_y = param.western_india_box_y
        region_lat = param.western_india_lat
        region_lon = param.western_india_lon
        region_lon_EW = param.western_india_lon_EW
        region_t62_lats = param.western_india_input_t62_lats
        region_t62_lons = param.western_india_input_t62_lons
    elif region_str == "pacific_northwest":
        region_input_lat_bbox = param.pacific_northwest_input_lat_bbox
        region_input_lon_bbox = param.pacific_northwest_input_lon_bbox
        region_box_x = param.pacific_northwest_box_x
        region_box_y = param.pacific_northwest_box_y
        region_lat = param.pacific_northwest_lat
        region_lon = param.pacific_northwest_lon
        region_lon_EW = param.pacific_northwest_lon_EW
        region_t62_lats = param.pacific_northwest_input_t62_lats
        region_t62_lons = param.pacific_northwest_input_t62_lons    

    return region_input_lat_bbox, region_input_lon_bbox, region_box_x, region_box_y, region_lat, region_lon, region_lon_EW, region_t62_lats, region_t62_lons

