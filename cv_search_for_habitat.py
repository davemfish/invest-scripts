from natcap.invest import coastal_vulnerability as cv

import logging
import time

LOGGER = logging.getLogger()
logging.basicConfig(level='INFO')

base_shore_point_vector_path = '/home/dmf/bahamas-mpa/cv/cv-fromjess/CV_Bahamas_snappedPts.shp'
search_radius = 1000
habitat_rank = 1
habitat_id = 'mangrove'
habitat_vector_path = '/home/dmf/bahamas-mpa/cv/cv-fromjess/Bahamas_regionalCV_Inputs/Habitats_Final/DenseMangroveCoppice_1.shp'
target_habitat_pickle_path = 'hab.pickle'

start = time.time()

cv.search_for_habitat(
        base_shore_point_vector_path, search_radius, habitat_rank,
        habitat_id, habitat_vector_path, target_habitat_pickle_path)

LOGGER.info(time.time() - start)