from natcap.invest import coastal_vulnerability as cv
import os
import logging
import time

LOGGER = logging.getLogger()
logging.basicConfig(filename='assemble_results.log', level='INFO')

WORKSPACE = 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/sampledata/intermediate'
# WORKSPACE = 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/MAR/intermediate'

risk_id_path_list = [
	(os.path.join(WORKSPACE, 'geomorphology/geomorph.pickle'), False, 'R_geomorph'),
	# (os.path.join(WORKSPACE, 'population/population.pickle', False, None),
	(os.path.join(WORKSPACE, 'relief/relief.pickle'), True, 'R_relief'),
	(os.path.join(WORKSPACE, 'surge/surge.pickle'), True, 'R_surge'),
	(os.path.join(WORKSPACE, 'wind_wave/wind.pickle'), True, 'R_wind'),
	(os.path.join(WORKSPACE, 'wind_wave/wave.pickle'), True, 'R_wave')]

habitat_protection_path = os.path.join(WORKSPACE, 'habitats/habitat_protection.csv')
base_point_vector_path = os.path.join(WORKSPACE, 'shore_points/shore_points.gpkg')
target_intermediate_vector_path = os.path.join(WORKSPACE, 'intermediate_exposure.gpkg')
target_intermediate_csv_path = 'intermediate_exposure.csv'
target_output_vector_path = 'coastal_exposure.gpkg'
target_output_csv_path = 'coastal_exposure.csv'

start = time.time()

cv.assemble_results_and_calculate_exposure(
        risk_id_path_list, habitat_protection_path, base_point_vector_path,
        target_intermediate_vector_path, target_intermediate_csv_path,
        target_output_vector_path, target_output_csv_path)

LOGGER.info(time.time() - start)