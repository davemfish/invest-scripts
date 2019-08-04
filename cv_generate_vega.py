import altair as alt
import pandas
import os

# alt.data_transformers.enable('json')

WORKSPACE = '/home/dmf/invest_dev/coastal_vulnerability/bahamas/'

# load a simple dataset as a pandas DataFrame
# data1 = pandas.read_csv('/home/dmf/invest_dev/coastal_vulnerability/bahamas/coastal_exposure.csv')
data2 = pandas.read_csv(os.path.join(WORKSPACE, 'intermediate/intermediate_exposure.csv'))

# longdata = ranks.melt(var_name='variable', value_name='value')

print(data2.head())

# chart = alt.Chart(ranks).mark_point().encode(
#     x='R_wind',
#     y='R_wave',
#     opacity=alt.value(0.01)
# )

# chart = alt.Chart(data2).mark_point().encode(
#     x='R_wind',
#     y='R_wave',
#     opacity=alt.value(0.1)
# )

# chart = alt.Chart(data2).mark_point().encode(
#     alt.X(alt.repeat("column"), type='quantitative'),
#     alt.Y(alt.repeat("row"), type='quantitative'),
#     opacity=alt.value(0.1)
#     # color='Origin:N'
# ).properties(
#     width=150,
#     height=150
# ).repeat(
#     row=['R_wind', 'R_wave', 'R_surge', 'R_relief'],
#     column=['R_wind', 'R_wave', 'R_surge', 'R_relief']
# )

base_scatter = alt.Chart().mark_point(
        strokeWidth=1,  # pixels
        size=4,  # pixels
    ).encode(
        opacity=alt.value(0.3),
        # color='species:N'
    ).properties(
        width=200,
        height=200
    )

base_histogram = alt.Chart().mark_area(
        # thickness=10
        interpolate='step'
    ).encode(
    ).properties(
        width=200,
        height=200
    )


# with a matrix of charts, global config needs to happen at this level:
chart = alt.vconcat(data=data2).configure_axis(
            grid=False,
            labelFontSize=13,
            titleFontSize=16
        ).configure_view(
            strokeWidth=0
        )

variables = ['R_wind:Q', 'R_wave:Q', 'R_surge:Q', 'R_relief:Q']
remaining_vars = set(variables)
for y_encoding in sorted(variables):
    row = alt.hconcat()
    for x_encoding in sorted(list(remaining_vars.difference(y_encoding))):
        if x_encoding == y_encoding:
            # continue
            row |= base_histogram.encode(
                alt.X(y_encoding, bin=alt.Bin(maxbins=80)), y='count()')
        else:
            row |= base_scatter.encode(x=x_encoding, y=y_encoding)
    remaining_vars.remove(y_encoding)
    chart &= row

# chart.height = 800
# chart.width = 800

chart.save(os.path.join(WORKSPACE, 'figs/scatter_matrix_intermediate_v2.html'))