from natcap.invest import coastal_vulnerability as cv
import os
import logging
import time

LOGGER = logging.getLogger()
logging.basicConfig(level='INFO')

WORKSPACE = 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/sampledata/intermediate'

base_shore_point_vector_path = os.path.join(WORKSPACE, 'wind_wave/wwiii_shore_points.gpkg')
landmass_polygon_pickle_path = os.path.join(WORKSPACE, 'shore_points/landmass_polygon.pickle')
landmass_line_rtree_path = os.path.join(WORKSPACE, 'shore_points/landmass_line_rtree.dat')
landmass_lines_pickle_path = os.path.join(WORKSPACE, 'shore_points/landmass_line_index.pickle')
target_fetch_rays_path = 'fetch_rays.gpkg'
max_fetch_distance = 12000
target_shore_point_vector_path = 'fetch_points.gpkg'
target_wind_exposure_pickle_path = 'wind.pickle'

start = time.time()

cv.calculate_wind_exposure(
        base_shore_point_vector_path, landmass_polygon_pickle_path,
        landmass_line_rtree_path, landmass_lines_pickle_path,
        target_fetch_rays_path, max_fetch_distance,
        target_shore_point_vector_path, target_wind_exposure_pickle_path)

LOGGER.info(time.time() - start)