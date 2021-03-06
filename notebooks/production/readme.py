
# coding: utf-8

# # Steps for Aqueduct 30
# 
# This document will keep track of what scripts to run to get to the results. 
# 
# 
# ## HydroBasins and FAO names
#     
# 1. **Y2017M08D02_RH_Merge_HydroBasins_V01**  
#     copy hydrobasin files from S3 and merge in pyhton using Fiona. It ingests the data into ee 
# 1. **Y2017M08D22_RH_Upstream_V01**  
#     add upstream PFAFIDs to the merged hydrobasin shp/csv file. 
# 1. **Y2017M08D23_RH_Downstream_V01**  
#     add downstream PFAFIDs to he merged hydrobasin csv file
# 1. **Y2017M08D23_RH_Merge_FAONames_V01**  
#     merge the FAO shapefiles into one Shapefile (UTF-8) and also rasterize using gdal
# 1. **Y2017M08D23_RH_Buffer_FAONames_V01**  
#     Create a negative buffer for the FAO basins to avoid sliver polygons
# 1. **Y2017M08D25_RH_spatial_join_FAONames_V01**  
#     Add the FAO Names to the HydroBasins shapefile
# 1. **Y2017M08D29_RH_Merge_FAONames_Upstream_V01**  
#     join the tables with the FAO names and the upstream / downstream relations
# 
#     
# ### PCRGlobWB 2.0
# 
# 1.  **Y2017M07D31_RH_copy_S3raw_s3process_V01.ipynb**  
#     Copy files from raw data folder to process data folder, all within S3. 
# 1.  **Y2017M07D31_RH_download_PCRGlobWB_data_V01.ipynb**  
#     Download the data to your machine, unzip files
# 1.  **Y2017M07D31_RH_Convert_NetCDF_Geotiff_V01**  
#     convert netCDF4 to Geotiff
# 1.  **Y2017M08D02_RH_Upload_to_GoogleCS_V01**  
#     upload files to Google Cloud Storage. 
# 1. **Y2017M08D02_RH_Ingest_GCS_EE_V01**  
#     ingest data from Google Cloud Storage to EarthEngine, adding metadata
# 1. **Y2017M08D08_RH_Convert_Indicators_ASC_Geotiff_V01**  
#     A couple of indicators are shared in ASCII format. Converting to geotiff
# 1. **Y2017M08D02_RH_Ingest_Additional_Rasters_EE_V01**  
#     This script ingests some auxiliary datafile onto earth engine included DEM, StreamFlow Network etc. 
# 1. **Y2017M08D30_RH_Average_Supply_EE_V01**  
#     This script will canculate the average PCRGlobWB2.0 supply (local runoff) using the ee python API
# 1. **Y2017M09D01_RH_linear_trend_Ag_Demand_EE_V01**  
#     Due to the sensitivity of the model to irrigation demand we take the linear trend of 2004 - 2014 for ag demand
# 1. **Y2017M09D05_RH_create_area_image_EE_V01**  
#     Create an image with the pixel area size in m2 o go from flux to volumen and vice versa
# 1. **Y2017M09D11_RH_zonal_stats_EE_V01**  
#     Calculate zonal statistics for EE images and HydroBasin level 6 zones. Export to GCS 
# 1. **Y2017M09D14_RH_merge_EE_results_V01**  
#     This script will merge the csv files into one big file/dataFrame    
# 1. **Y2017M09D15_RH_Add_Basin_Data_V01**  
#     add data from upstream, downstream and basin to dataframe
# 1. **Y2017M10D02_RH_Calculate_Water_Stress_V01**  
#     calculate total demand (Dom, IrrLinear, Liv, Ind) and Reduced Runoff and water stress.  
# 1. **Y2017M10D04_RH_Threshold_WaterStress_V02**  
#     set arid and low water use, add numerical and labeled thresholds 
#     
# 
# ### Groundwater Branch
# 
# ### Flood Risk Branch
# 
# ### Country Shapefile Branch
# 
# ### Other Indicators Branch
#     
# ### Aux Files  
# 
# 1. **Y2017M10D09_RH_create_Line_Shape_File_V01**
#     Create a shapefile to visualize the flow network
#     
# 

# In[ ]:



