from natcap.invest import coastal_vulnerability as cv
import pandas

# def compute_wave_height(Un, Fn, dn):
#     # if mask == 0.:
#     #     return -1.
#     # if Un < 1.:
#     #     bad_wind_value[0] = True
#     #     Un = 1.
#     dn = -dn
#     ds = 9.81*dn/Un**2
#     Fs = 9.81*Fn/Un**2
#     A = np.tanh(0.343*ds**1.14)
#     if Fs < 0:
#         print('Fs=', Fs, 'Fn=', Fn)
#     B = np.tanh(4.41e-4*Fs**0.79/A)  # 4.41e-4 is a mismatch with UG
#     H_n = 0.24*Un**2/9.81*(A*B)**0.572
#     return H_n


# def compute_wave_period(Un, Fn, dn):
#     # if mask == 0.:
#     #     return -1.
#     # if Un < 1.:
#     #     Un = 1.
#     dn = -dn
#     ds = 9.81*dn/Un**2
#     Fs = 9.81*Fn/Un**2
#     A = np.tanh(0.1*ds**2.01)
#     B = np.tanh(2.77e-7*Fs**1.45/A)
#     return 7.69*Un/9.81*(A*B)**0.187

def E_l(wave_height, wave_period, REI_PCT):
    # if mask == 0:
    #     return -1.
    return 0.5 * wave_height**2 * wave_period * REI_PCT

# import random

# sector_degrees = ['0', '22', '45', '67', '90', '112', '135', '157', '180', '202', '225', '247', '270', '292', '315', '337']
# wwiii_data = pandas.read_csv('MAR_fetch_point_data.csv')

# rand_fids = random.sample(100, wwiii_data['fid'])

# for fid in rand_fids:


# subscript n is a sector
Un = 12  # wind speed m/s: highest 10% observed for sector?
Fn = 300  # fetch distance meters
# dn = -2000  # average depth over fetch area

for dn in [-0.2, -0.1, -1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0, -9.0, -10.0, -100.0]:
    # functions are flipping sign of dn to positive.
    height = cv.compute_wave_height(Un, Fn, dn)
    period = cv.compute_wave_period(Un, Fn, dn)
    local_wave_energy = E_l(height, period, 1)

    print('DEPTH: %f' % dn)
    print('HEIGHT: %f' % height)
    print('PERIOD: %f' % period)
    print('E_local: %f' % local_wave_energy)
    print('---------')