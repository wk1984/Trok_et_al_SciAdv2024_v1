#!/bin/bash

###############################################################
## Convert all ERA5 input data files to 128x64 lonxlat grids ##
###############################################################

proj_dir="/path/to/main_project_folder/" # edit this line

regions=('southcentral_north_america' 'southern_europe' 'western_russia' 'western_india' 'pacific_northwest')
variables=("psl" "swvl1" "tmax" "z250" "z500" "z700")

## To unzip pacific northwest precipitation data, uncomment the following ##
# regions=('pacific_northwest')
# variables=("pr")

for region_str in ${regions[*]}; do
for VAR in ${variables[*]}; do

    echo ${VAR}  
    FILES=${proj_dir}'input_data_ERA5/'${region_str}'/daily/'${VAR}'/*.nc'
    
    for f in ${FILES[@]}
    do  
        if [[ ! $f =~ "r128x64" ]]; then
            outfile=${f%.nc}_r128x64.nc
            if [ ! -f ${outfile} ]
            then 
                echo $f
                echo $outfile
                echo "regridding..."
                if [[ $VAR == "swvl1" ]]; then
                    cdo remapcon,r128x64 ${f} ${outfile}
                else
                    cdo remapbil,r128x64 ${f} ${outfile}
                fi
            fi
        fi
        
    done
done
done