import logging
from natcap.invest import coastal_vulnerability
import time

logging.basicConfig(filename='geomorph_1_5.log', level='INFO')
LOGGER = logging.getLogger(__name__)
# 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/jess_stacie/CV_inputs_draft2_v2/geomorph_MAR_BZ_national.shp'
# 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/jess_stacie/CV_inputs_draft2_v2/geomorph_MAR_BZ_national.shp'
geomorphology_vector_path = 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/geomorph/workspace/intermediate/geomorphology/geomorphology_projected.shp'
geomorphology_fill_value = 6
base_shore_point_vector_path = 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/jess_stacie/dmf_wavedata/intermediate/shore_points/shore_points.gpkg'
model_resolution = 500
target_pickle_path = 'geomorph.pickle'

start = time.time()
coastal_vulnerability.calculate_geomorphology_exposure(
    geomorphology_vector_path, geomorphology_fill_value,
    base_shore_point_vector_path, model_resolution, target_pickle_path)
print(f'elapsed time: {time.time() - start}')
# print(time.time() - start)