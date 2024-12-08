#!/usr/bin/env python
# coding: utf-8

# # Check if all necessary ERA5 data files exist in the input_data_ERA5 directory
# key:2a8c21bf-ffdb-42e5-97ad-04933ac3bd3e

# In[1]:


proj_dir='/home/' # edit this line

import cdsapi
import os
import itertools
import json
import multiprocessing as mp
import sys
sys.path.append(proj_dir)
from project_fxns import load_region
import importlib
importlib.reload(load_region)

# region_str_tpl = ['southcentral_north_america', 'southern_europe', 'western_russia', 'western_india', 'pacific_northwest']
variables = ["volumetric_soil_water_layer_1", "2m_temperature", "2m_temperature", "geopotential", "geopotential", "geopotential", "mean_sea_level_pressure"]
var_abbrev = ["swvl1", "tmean", "t2m", "z500", "z700", "z250", "psl"]

## To request pacific northwest precipitation data, run this script again with the following uncommented ##
region_str_tpl = [sys.argv[1]]

######### Define Dataset and Product Type ##########
global era5_land_dataset
era5_land_dataset = "reanalysis-era5-land"

global era5_psl_dataset
era5_psl_dataset = "reanalysis-era5-single-levels"
global era5_psl_product_type
era5_psl_product_type = "reanalysis"

global era5_tmean_dataset
era5_tmean_dataset = "reanalysis-era5-single-levels-monthly-means"
global era5_tmean_product_type
era5_tmean_product_type = "monthly_averaged_reanalysis"

global era5_z_dataset
era5_z_dataset = "reanalysis-era5-pressure-levels"
global era5_z_product_type
era5_z_product_type = "reanalysis"

print(region_str_tpl)


# In[2]:


def era5_land_download(
    dataset,
    variables,
    years,
    months,
    days,
    # times='00:00',
    format="netcdf",
    latmin=0,
    latmax=180,
    lonmin=-180,
    lonmax=180,
    outname='download.netcdf.zip'
):

    request = {"variable": variables,
               "year": years,
               "month": months,
               "day": days,
               "time": [
                   "00:00", "01:00", "02:00",
                            "03:00", "04:00", "05:00",
                            "06:00", "07:00", "08:00",
                            "09:00", "10:00", "11:00",
                            "12:00", "13:00", "14:00",
                            "15:00", "16:00", "17:00",
                            "18:00", "19:00", "20:00",
                            "21:00", "22:00", "23:00",

               ],
               "data_format": format,
               "area": [latmax, lonmin, latmin, lonmax],
               "download_format": "zip",
               }
    
    client = cdsapi.Client()
    client.retrieve(dataset, request, outname)
    
    return


# In[3]:


def era5_tmean_download(
    dataset,
    product_type,
    variables,
    years,
    months,
    format = "netcdf",
    outname = 'download.nc'
):

    request = {
                        "product_type": product_type,
                        "variable": variables,
                        "year": years,
                        "month": months,
                        "time": [
                            "00:00"
                            ],
                        "data_format": format,
                        # "download_format": "zip",
                    }
      
    client = cdsapi.Client()
    client.retrieve(dataset, request, outname)
    
    return


# In[4]:


def era5_psl_download(
    dataset,
    product_type,
    variables,
    years,
    months,
    days,
    # times = '00:00',
    format = "netcdf",
    latmin = 0,
    latmax = 180,
    lonmin = -180,
    lonmax = 180,
    outname = 'download.nc'
):

    request = {
                        "product_type": product_type,
                        "variable": variables,
                        "year": years,
                        "month": months,
                        "day": days,
                        "time": [
                            "00:00", "01:00", "02:00",
                            "03:00", "04:00", "05:00",
                            "06:00", "07:00", "08:00",
                            "09:00", "10:00", "11:00",
                            "12:00", "13:00", "14:00",
                            "15:00", "16:00", "17:00",
                            "18:00", "19:00", "20:00",
                            "21:00", "22:00", "23:00",

                            ],
                        "data_format": format,
                        "area": [latmax,lonmin,latmin,lonmax],
                    }
      
    client = cdsapi.Client()
    client.retrieve(dataset, request, outname)
    
    return


# In[5]:


def era5_z_download(
    dataset,
    product_type,
    pressure_level,
    variables,
    years,
    months,
    days,
    # times = '00:00',
    format = "netcdf",
    latmin = 0,
    latmax = 180,
    lonmin = -180,
    lonmax = 180,
    outname = 'download.nc'
):

    request = {
                        "product_type": product_type,
                        "pressure_level": pressure_level,
                        "variable": variables,
                        "year": years,
                        "month": months,
                        "day": days,
                        "time": [
                            "00:00", "01:00", "02:00",
                            "03:00", "04:00", "05:00",
                            "06:00", "07:00", "08:00",
                            "09:00", "10:00", "11:00",
                            "12:00", "13:00", "14:00",
                            "15:00", "16:00", "17:00",
                            "18:00", "19:00", "20:00",
                            "21:00", "22:00", "23:00",

                            ],
                        "data_format": format,
                        "area": [latmax,lonmin,latmin,lonmax],
                    }
      
    client = cdsapi.Client()
    client.retrieve(dataset, request, outname)
    
    return


# ## List all missing input data files

# In[ ]:


for region_str in region_str_tpl:
    print(region_str)

    region_input_lat_bbox, region_input_lon_bbox, region_box_x, region_box_y, region_lat, region_lon, region_lon_EW, region_t62_lats, region_t62_lons = load_region.load_region_constants_modules(region_str)
    
    input_latmin = region_lat.stop 
    input_latmax = region_lat.start

    if isinstance(region_input_lon_bbox, slice): 
        input_lonmin = region_lon.start
        input_lonmax = region_lon.stop 
    else:
        input_lonmin = region_input_lon_bbox[0].start
        input_lonmax = region_input_lon_bbox[1].stop

    print('lat:', input_latmin, input_latmax)
    print('lon:', input_lonmin, input_lonmax)

    if input_lonmin > 180:
        input_lonmin = input_lonmin-360

    if input_lonmax > 180:
        input_lonmax = input_lonmax-360

    print('lat:', input_latmin, input_latmax)
    print('lon:', input_lonmin, input_lonmax)

    ######### Define Time/Space Grid ###########
    global latmin
    latmin = input_latmin
    global latmax
    latmax = input_latmax
    global lonmin
    lonmin = input_lonmin
    global lonmax
    lonmax = input_lonmax

    global mons
    mons = list(range(1,13))
    
    global total_days
    total_days = list((range(1,32)))

    ######### Run Iterating Download Function ###########

    for i,var in enumerate(variables):
        request_id_dict = {}

        global curr_var
        curr_var = var

        global curr_var_abbrev
        curr_var_abbrev = var_abbrev[i]
        
        global era5_z_pressure_level
        
        if curr_var == "geopotential":
            if curr_var_abbrev == "z700":
                era5_z_pressure_level = "700"
            elif curr_var_abbrev == "z500":
                era5_z_pressure_level = "500"
            elif curr_var_abbrev == "z250":
                era5_z_pressure_level = "250"

        if ((curr_var_abbrev == "z700") | (curr_var_abbrev == "z500")) | (curr_var_abbrev == "z250"):
            print('pressure-levels', curr_var_abbrev, era5_z_pressure_level)
        elif curr_var_abbrev == "psl":
            print('single-levels', curr_var_abbrev)
        elif curr_var_abbrev == "tmean":
            print('single-levels-monthly', curr_var_abbrev)
        elif ((curr_var_abbrev == "t2m") | (curr_var_abbrev == "pr")) | (curr_var_abbrev == "swvl1"):
            print('LAND')
        else:
            print('VAR ABBREV ERROR')

        print(curr_var, curr_var_abbrev)
        
        if curr_var_abbrev == "tmean":
            timescale="monthly"
            yrs = list(range(2023,2024))
        else:
            timescale="hourly"
            yrs = list(range(2023,2024))
            
        path_out = proj_dir+"input_data_ERA5/"+region_str+"/"+timescale+"/"+curr_var_abbrev+"/"
            
        for yr in yrs:  
            f_out = '_'.join([region_str,curr_var_abbrev,timescale,str(yr)+'.nc'])
            if not os.path.exists(path_out+f_out):
                if ((curr_var_abbrev == "z700") | (curr_var_abbrev == "z500")) | (curr_var_abbrev == "z250"):
                    print(path_out+f_out)
                    print(path_out+f_out+" does NOT exist... requesting now")
                    request_id_dict[path_out+f_out] = era5_z_download(dataset = era5_z_dataset, 
                                                                    product_type = era5_z_product_type,
                                                                    pressure_level = era5_z_pressure_level,
                                                                    variables = curr_var, 
                                                                    years = yr, 
                                                                    months = mons, 
                                                                    days = total_days, 
                                                                    latmin = latmin, 
                                                                    latmax = latmax, 
                                                                    lonmin = lonmin, 
                                                                    lonmax = lonmax,
                                                                    outname = path_out+f_out)
                    
                elif curr_var_abbrev == "psl":
                    print(path_out+f_out)
                    print(path_out+f_out+" does NOT exist... requesting now")
                    request_id_dict[path_out+f_out] = era5_psl_download(dataset = era5_psl_dataset, 
                                                                    product_type = era5_psl_product_type,
                                                                    variables = curr_var, 
                                                                    years = yr, 
                                                                    months = mons, 
                                                                    days = total_days, 
                                                                    latmin = latmin, 
                                                                    latmax = latmax, 
                                                                    lonmin = lonmin, 
                                                                    lonmax = lonmax,
                                                                    outname = path_out+f_out)
                elif curr_var_abbrev == "tmean":
                    print(path_out+f_out)
                    print(path_out+f_out+" does NOT exist... requesting now")
                    request_id_dict[path_out+f_out] = era5_tmean_download(dataset = era5_tmean_dataset, 
                                                                    product_type = era5_tmean_product_type,
                                                                    variables = curr_var, 
                                                                    years = yr, 
                                                                    months = mons,
                                                                    outname = path_out+f_out)
                    
                elif ((curr_var_abbrev == "t2m") | (curr_var_abbrev == "pr")) | (curr_var_abbrev == "swvl1"):
                    for mon in mons:  
                        f_out = '_'.join([region_str,curr_var_abbrev,timescale,str(yr),str(mon).zfill(2)+'.netcdf.zip']) 
                        if not os.path.exists(path_out+f_out):
                            print(path_out+f_out)
                            print(path_out+f_out+" does NOT exist... requesting now")
                            request_id_dict[path_out+f_out] = era5_land_download(dataset = era5_land_dataset, 
                                                                            variables = curr_var, 
                                                                            years = yr, 
                                                                            months = mon,  
                                                                            days = total_days, 
                                                                            latmin = latmin, 
                                                                            latmax = latmax, 
                                                                            lonmin = lonmin, 
                                                                            lonmax = lonmax,
                                                                            outname = path_out+f_out)
                else:
                    print('VAR ABBREV ERROR')

            print(str(yr)+' done ...')

        # with open(path_out+region_str+'_'+curr_var_abbrev+'_missing.json', 'w') as fp:
        #     json.dump(request_id_dict, fp)


# In[ ]:





# In[ ]:




