# import altair as alt
import pandas
import os

# alt.data_transformers.enable('json')

WORKSPACE = 'C:/Users/dmf/projects/invest_dev/coastal_vulnerability/jess_stacie/CV_output_MAR_CV36_test2'

# load a simple dataset as a pandas DataFrame
# data1 = pandas.read_csv('/home/dmf/invest_dev/coastal_vulnerability/bahamas/coastal_exposure.csv')
data = pandas.read_csv(os.path.join(WORKSPACE, 'outputs/coastal_exposure/coastal_exposure.csv'))

# print(list(data))

for var in ['relief', 'wave_exposure', 'surge_potential']:
    print(var)
    print(data[var].value_counts().sort_index())
    # print('\n')