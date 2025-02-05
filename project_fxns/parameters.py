import numpy as np
import xarray as xr

#### general analysis ####
time_period = slice("1850-01-01", "2014-12-31")
hgt_level = 500

###################################################
################### Regions #######################
###################################################

##### southcentral_north_america input #####
southcentral_north_america_input_lat_bbox = slice(45, 11)
southcentral_north_america_input_lon_bbox = slice(219, 303)
southcentral_north_america_input_t62_lats = np.array([12.65625, 15.46875, 18.28125, 21.09375, 23.90625, 26.71875, 29.53125,
       32.34375, 35.15625, 37.96875, 40.78125, 43.59375])
southcentral_north_america_input_t62_lons = np.array([219.375 , 222.1875, 225.    , 227.8125, 230.625 , 233.4375, 236.25  ,
       239.0625, 241.875 , 244.6875, 247.5   , 250.3125, 253.125 , 255.9375,
       258.75  , 261.5625, 264.375 , 267.1875, 270.    , 272.8125, 275.625 ,
       278.4375, 281.25  , 284.0625, 286.875 , 289.6875, 292.5   , 295.3125,
       298.125 , 300.9375])
southcentral_north_america_input_nlats = len(southcentral_north_america_input_t62_lats)
southcentral_north_america_input_nlons = len(southcentral_north_america_input_t62_lons)

##### southcentral_north_america region #####
southcentral_north_america_lat = slice(37, 21)
southcentral_north_america_lon = slice(254, 268)
southcentral_north_america_lon_EW = slice(southcentral_north_america_lon.start-360, southcentral_north_america_lon.stop-360)
southcentral_north_america_box_y = [southcentral_north_america_lat.start, southcentral_north_america_lat.start, southcentral_north_america_lat.stop, southcentral_north_america_lat.stop, southcentral_north_america_lat.start]
southcentral_north_america_box_x = [southcentral_north_america_lon.start, southcentral_north_america_lon.stop, southcentral_north_america_lon.stop, southcentral_north_america_lon.start, southcentral_north_america_lon.start]


###################################################


##### pacific_northwest input #####
pacific_northwest_input_lat_bbox = slice(62, 28)
pacific_northwest_input_lon_bbox = slice(200, 284)
pacific_northwest_input_t62_lats = np.array([29.53125, 32.34375, 35.15625, 37.96875, 40.78125, 43.59375, 46.40625,
       49.21875, 52.03125, 54.84375, 57.65625, 60.46875])
pacific_northwest_input_t62_lons = np.array([202.5   , 205.3125, 208.125 , 210.9375, 213.75  , 216.5625, 219.375 ,
       222.1875, 225.    , 227.8125, 230.625 , 233.4375, 236.25  , 239.0625,
       241.875 , 244.6875, 247.5   , 250.3125, 253.125 , 255.9375, 258.75  ,
       261.5625, 264.375 , 267.1875, 270.    , 272.8125, 275.625 , 278.4375,
       281.25  ])

pacific_northwest_input_nlats = len(pacific_northwest_input_t62_lats)
pacific_northwest_input_nlons = len(pacific_northwest_input_t62_lons)

##### pacific_northwest region #####
pacific_northwest_lat = slice(51, 41)
pacific_northwest_lon = slice(235, 245)
pacific_northwest_lon_EW = slice(pacific_northwest_lon.start-360, pacific_northwest_lon.stop-360)
pacific_northwest_box_y = [pacific_northwest_lat.start, pacific_northwest_lat.start, pacific_northwest_lat.stop, pacific_northwest_lat.stop, pacific_northwest_lat.start]
pacific_northwest_box_x = [pacific_northwest_lon.start, pacific_northwest_lon.stop, pacific_northwest_lon.stop, pacific_northwest_lon.start, pacific_northwest_lon.start]


###################################################


##### western_russia input #####
western_russia_input_lat_bbox = slice(71, 36)
western_russia_input_lon_bbox = slice(2,90)
#western_russia_input_t62_lats = np.array([37., 39., 41., 43., 45., 47., 49., 51., 53., 55., 57., 59., 61., 63.,
#       65., 67., 69., 71.])
#western_russia_input_t62_lons = np.array([ 2., 4.,  6.,  8., 10., 12., 14., 16., 18., 20., 22., 24., 26., 28., 30.,
#       32., 34., 36., 38., 40., 42., 44., 46., 48., 50., 52., 54., 56., 58.,
#       60., 62., 64., 66., 68., 70., 72., 74., 76., 78., 80., 82., 84., 86., 88., 90.])
western_russia_input_t62_lats = np.array([37.96875, 40.78125, 43.59375, 46.40625, 49.21875, 52.03125, 54.84375, 57.65625, 60.46875, 63.28125, 66.09375, 68.90625])
western_russia_input_t62_lons = np.array([ 2.8125,  5.625,   8.4375, 11.25,  14.0625, 16.875,  19.6875, 22.5,    25.3125, 28.125,  30.9375, 33.75,   36.5625, 39.375,  42.1875, 45.,     47.8125, 50.625, 53.4375, 56.25,   59.0625, 61.875,  64.6875, 67.5,    70.3125, 73.125,  75.9375, 78.75,   81.5625, 84.375,  87.1875, 90.    ])

western_russia_input_nlats = len(western_russia_input_t62_lats)
western_russia_input_nlons = len(western_russia_input_t62_lons)

##### western_russia region #####
western_russia_lat = slice(59, 51)
western_russia_lon = slice(37, 53)
western_russia_lon_EW = western_russia_lon
western_russia_box_y = [western_russia_lat.start, western_russia_lat.start, western_russia_lat.stop, western_russia_lat.stop, western_russia_lat.start]
western_russia_box_x = [western_russia_lon.start, western_russia_lon.stop, western_russia_lon.stop, western_russia_lon.start, western_russia_lon.start]


###################################################


##### southern_europe input #####
southern_europe_input_lat_bbox = slice(63, 27)
southern_europe_input_lon_bbox = [slice(325,360), slice(0,55)]
southern_europe_input_t62_lats = np.array([29.53125, 32.34375, 35.15625, 37.96875, 40.78125, 43.59375, 46.40625, 49.21875, 52.03125, 54.84375, 57.65625, 60.46875])
southern_europe_input_t62_lons = np.array([326.25,   329.0625 ,331.875,  334.6875 ,337.5,    340.3125, 343.125,  345.9375,  348.75 ,  351.5625, 354.375,  357.1875,   0. ,      2.8125 ,  5.625,    8.4375,  11.25,    14.0625 , 16.875 ,  19.6875,  22.5,     25.3125,  28.125,   30.9375,  33.75 ,   36.5625 , 39.375 ,  42.1875,  45. ,     47.8125 , 50.625 ,  53.4375])
southern_europe_input_nlats = len(southern_europe_input_t62_lats)
southern_europe_input_nlons = len(southern_europe_input_t62_lons)

##### southern_europe region #####
southern_europe_lat = slice(53, 43)
southern_europe_lon = slice(0, 20)
southern_europe_lon_EW = southern_europe_lon
southern_europe_box_y = [southern_europe_lat.start, southern_europe_lat.start, southern_europe_lat.stop, southern_europe_lat.stop, southern_europe_lat.start]
southern_europe_box_x = [southern_europe_lon.start, southern_europe_lon.stop, southern_europe_lon.stop, southern_europe_lon.start, southern_europe_lon.start]


###################################################


##### western_india input #####
western_india_input_lat_bbox = slice(46, 7)
western_india_input_lon_bbox = slice(28,118)

western_india_input_t62_lats = np.array([ 7.03125,  9.84375, 12.65625, 15.46875, 18.28125, 21.09375, 23.90625,
       26.71875, 29.53125, 32.34375, 35.15625, 37.96875, 40.78125, 43.59375])
western_india_input_t62_lons = np.array([ 28.125 ,  30.9375,  33.75  ,  36.5625,  39.375 ,  42.1875,  45.    ,
                                47.8125,  50.625 ,  53.4375,  56.25  ,  59.0625,  61.875 ,  64.6875,
                                67.5   ,  70.3125,  73.125 ,  75.9375,  78.75  ,  81.5625,  84.375 ,
                                87.1875,  90.    ,  92.8125,  95.625 ,  98.4375, 101.25  , 104.0625,
                               106.875 , 109.6875, 112.5   , 115.3125])
western_india_input_nlats = len(western_india_input_t62_lats)
western_india_input_nlons = len(western_india_input_t62_lons)

##### western_india region #####
western_india_lat = slice(30, 20)
western_india_lon = slice(65, 80)
western_india_lon_EW = western_india_lon
western_india_box_y = [western_india_lat.start, western_india_lat.start, western_india_lat.stop, western_india_lat.stop, western_india_lat.start]
western_india_box_x = [western_india_lon.start, western_india_lon.stop, western_india_lon.stop, western_india_lon.start, western_india_lon.start]
