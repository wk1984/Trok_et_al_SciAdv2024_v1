#!/bin/bash

####################################################
## create nested directories for input data files ##
####################################################

proj_dir="/home/" # edit this line

regions=('southcentral_north_america' 'southern_europe' 'western_russia' 'western_india' 'pacific_northwest')
timescale=("daily" "hourly" "monthly")
variables=("psl" "swvl1" "tmax" "z250" "z500" "z700" "pr")

for reg in ${regions[*]}; do
    mkdir ${proj_dir}"input_data_ERA5/"${reg}
    for time in ${timescale[*]}; do
        mkdir ${proj_dir}"input_data_ERA5/"${reg}"/"${time}
        if [[ $time == "monthly" ]]; then
            mkdir ${proj_dir}"input_data_ERA5/"${reg}"/"${time}"/tmean"
        else
            for var in ${variables[*]}; do
                if [[ $time == "hourly" && $var == "tmax" ]]; then
                    mkdir ${proj_dir}"input_data_ERA5/"${reg}"/"${time}"/t2m"
                else
                    mkdir ${proj_dir}"input_data_ERA5/"${reg}"/"${time}"/"${var}
                fi
            done
        fi
    done
done
