from natcap.invest import coastal_vulnerability as cv
import pygeoprocessing
import logging
import time
import shutil
from osgeo import gdal, ogr

LOGGER = logging.getLogger()
logging.basicConfig(level='INFO')

fetch_ray_vector_path = 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/MAR/intermediate/wind_wave/fetch_rays.gpkg'
vector_info = pygeoprocessing.get_vector_info(fetch_ray_vector_path)
model_resolution = 500
file_suffix = ''
base_bathy_path = 'C:/Users/dmf/projects/invest/data/invest-sample-data/Base_Data/Marine/DEMs/global_dem'
target_bathy_path = 'bathy_utm.tif'
working_dir = '.'
target_fetch_depth_path = 'fetch_depth_v2.gpkg'

start = time.time()

cv.clip_and_project_raster(
        base_bathy_path, vector_info['bounding_box'],
        vector_info['projection'],
        model_resolution, working_dir, file_suffix,
        target_bathy_path)

result = pygeoprocessing.zonal_statistics(
    (target_bathy_path, 1), fetch_ray_vector_path,
    polygons_might_overlap=True)

shutil.copy(fetch_ray_vector_path, target_fetch_depth_path)

target_vector = gdal.OpenEx(
    target_fetch_depth_path, gdal.OF_VECTOR | gdal.GA_Update)
target_layer = target_vector.GetLayer()
target_layer.CreateField(ogr.FieldDefn('depth', ogr.OFTReal))
target_layer.StartTransaction()

for feature in target_layer:
    fid = feature.GetFID()
    depth = 9999
    if result[fid]['count'] > 0:
        depth = float(result[fid]['sum']) / float(result[fid]['count'])
    feature.SetField('depth', depth)
    target_layer.SetFeature(feature)

target_layer.CommitTransaction()
target_layer = None
target_vector.FlushCache()
target_vector = None


LOGGER.info(time.time() - start)