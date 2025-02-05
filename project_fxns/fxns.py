import numpy as np
import pandas as pd
import xarray as xr
from project_fxns import parameters as param
from project_fxns import load_region
from scipy.stats import t
import os

#####################################################

def CMIP6_select_input_bbox(ds, region):
    region_input_lat_bbox, region_input_lon_bbox, _, _, _, _, _, _, _ = load_region.load_region_constants_modules(region)
    lat_bbox = slice(region_input_lat_bbox.stop, region_input_lat_bbox.start)
    lon_bbox = region_input_lon_bbox
    if type(lon_bbox) is list:
        ds_left = ds.sel(lat = lat_bbox, lon = lon_bbox[0])
        ds_right = ds.sel(lat = lat_bbox, lon = lon_bbox[1])
        ds = xr.concat([ds_left, ds_right], dim="lon")
    else:
        ds = ds.sel(lat = lat_bbox, lon = lon_bbox)

    return ds

#####################################################

def ERA5_select_input_bbox(ds, region):
    region_input_lat_bbox, region_input_lon_bbox, _, _, _, _, _, _, _ = load_region.load_region_constants_modules(region)
    lat_bbox = slice(region_input_lat_bbox.stop, region_input_lat_bbox.start)
    lon_bbox = region_input_lon_bbox
    if np.any([coord == "latitude" for coord in list(ds.coords)]):
        ds = ds.rename({"latitude":"lat", "longitude":"lon"})

    if type(lon_bbox) is list:
        ds_left = ds.sel(lat = lat_bbox, lon = lon_bbox[0])
        ds_right = ds.sel(lat = lat_bbox, lon = lon_bbox[1])
        ds = xr.concat([ds_left, ds_right], dim="lon")
    else:
        ds = ds.sel(lat = lat_bbox, lon = lon_bbox)

    return ds

#####################################################

def select_input_bbox(ds, region):
    region_input_lat_bbox, region_input_lon_bbox, _, _, _, _, _, _, _ = load_region.load_region_constants_modules(region)
    lat_bbox = slice(region_input_lat_bbox.stop, region_input_lat_bbox.start)
    lon_bbox = region_input_lon_bbox
    if type(lon_bbox) is list:
        ds_left = ds.sel(lat = lat_bbox, lon = lon_bbox[0])
        ds_right = ds.sel(lat = lat_bbox, lon = lon_bbox[1])
        ds = xr.concat([ds_left, ds_right], dim="lon")
    else:
        ds = ds.sel(lat = lat_bbox, lon = lon_bbox)
    return ds

#####################################################

def map_polyfit(arr):
    return arr.polyfit(dim="gmt", deg=1).polyfit_coefficients

#####################################################

def overwrite_nc(f1, ds):
    if os.path.exists(f1):
        os.remove(f1)
    ds.to_netcdf(f1)

#####################################################

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

#####################################################

def convert_num_to_rank(int_num):
    if (int_num % 100 <= 19) & (int_num % 100 >= 11):
        suffix = 'th'
    else:
        mod10 = int_num % 10
        if mod10 == 1:
            suffix = 'st'
        elif mod10 == 2:
            suffix = 'nd'
        elif mod10 == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    return str(int_num)+suffix

#####################################################

def count_distinct_events(date_list, event_date_range):
    len_hot_idx = (pd.to_datetime(event_date_range.stop) - pd.to_datetime(event_date_range.start)).days
    if len(date_list) == 0:
        num_distinct_events = 0
    elif len(date_list) == 1:
        num_distinct_events = 1
    else:
        num_distinct_events = 0
        non_event_length = 100000 
        event_length = 1
        ## count distict events ##
        for ii, dd in enumerate(date_list):
            if ii > 0:
                if (date_list[ii]-date_list[ii-1]).astype('timedelta64[D]') == np.timedelta64(1,'D'): # 1-day increment found
                    event_length = event_length+1
                else: # > 1-day increment found
                    ## add subevents if 1 continuous event is long enough ##
                    number_of_qualifying_subevents = (event_length + min(non_event_length, len_hot_idx-1)) / len_hot_idx
                    num_distinct_events = num_distinct_events + number_of_qualifying_subevents
                    ## new event found, reset event length counter ##
                    event_length = 1 
                    ## new event found, reset non-event length counter to avoid double counting ##
                    num_days_str = str((date_list[ii]-date_list[ii-1]).astype('timedelta64[D]'))
                    non_event_length = int(num_days_str[:-5])-1 

        ## add any remaining subevents in case date_list ends on a continuous event ##
        number_of_qualifying_subevents = (event_length + min(non_event_length, len_hot_idx-1)) / len_hot_idx
        num_distinct_events = num_distinct_events + number_of_qualifying_subevents
                
    return num_distinct_events

#####################################################

def get_stat_sig(arr, alpha=0.05):
    nn = np.shape(arr)[0]
    sd = np.std(arr, axis=0)
    t_stat = (np.mean(arr, axis=0) - 0) / (sd / np.sqrt(nn))
    pvals = 2*(t.cdf(-abs(t_stat), nn-1))
    stat_sig = (pvals < alpha).astype(int)

    return stat_sig

#####################################################