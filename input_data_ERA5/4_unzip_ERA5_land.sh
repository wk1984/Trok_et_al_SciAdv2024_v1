#!/bin/bash

####################################################
## Unzip all ERA5 Land .zip files to netcdf files ##
####################################################

proj_dir="/path/to/main_project_folder/" # edit this line

regions=('southcentral_north_america' 'southern_europe' 'western_russia' 'western_india' 'pacific_northwest')
variables=("swvl1" "t2m")

## To unzip pacific northwest precipitation data, uncomment the following ##
# regions=('pacific_northwest')
# variables=("pr")

for region_str in ${regions[*]}; do
for VAR in ${variables[*]}; do
    
    echo ${VAR} 
    FILES=${proj_dir}'input_data_ERA5/'${region_str}'/hourly/'${VAR}'/*.netcdf.zip'
    
    for f in ${FILES[@]}
    do  
        if [[ $f =~ ".netcdf.zip" ]]; then
            outfile=${f%.netcdf.zip}.nc
            if [ ! -f ${outfile} ]
            then 
                echo $f
                echo $outfile
                echo "unzipping and renaming..."
                unzip ${f} 
                mv data.nc ${outfile}           
            fi
        fi
        
    done
done
done

echo "all files unzipped"
