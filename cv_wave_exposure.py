from natcap.invest import coastal_vulnerability as cv

import logging
import time

LOGGER = logging.getLogger()
logging.basicConfig(level='INFO')

base_fetch_point_vector_path = 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/MAR/intermediate/wind_wave/fetch_points.gpkg'
max_fetch_distance = 25000
target_wave_vector_path = 'wave_energies_dev.gpkg'
target_wave_exposure_pickle_path = 'wave.pickle'

start = time.time()

cv.calculate_wave_exposure(
        base_fetch_point_vector_path, max_fetch_distance,
        target_wave_vector_path,
        target_wave_exposure_pickle_path)

LOGGER.info(time.time() - start)