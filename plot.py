"""
Main driver script to plot Nissan Leaf battery data. Start and end time for
first temperature section is also printed to screen.

Command line usage
------------------
python plot.py cycle
python plot.py hppc
python plot.py temp 1c
python plot.py temp 2c
python plot.py temp 3c
"""

import argparse
import datalib

# Command line arguments
# ----------------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument('data', help='plot data; valid inputs are cycle, hppc, temp')
parser.add_argument('dis', nargs='?', help='discharge rate; valid inputs are 1c, 2c, or 3c')
args = parser.parse_args()

# Analyze data
# ----------------------------------------------------------------------------

datafiles = {
    'cycle': 'data/NissanLeaf-cell-Cycling-10C-24C-40C.csv',
    'hppc': 'data/NissanLeaf-cell-Low-Current-HPPC-25C-2.csv',
    'bitrode_1c': 'data/1C-Discharge-Bitrode-data.csv',
    'bitrode_2c': 'data/2C-Discharge-Bitrode-data.csv',
    'bitrode_3c': 'data/3C-Discharge-Bitrode-data.csv',
    'temp_1c': 'data/Temperature-1C-discharge.lvm',
    'temp_2c': 'data/Temperature-2C-discharge.lvm',
    'temp_3c': 'data/Temperature-3C-discharge.lvm'
}

if args.data == 'cycle':
    data = datalib.CellData(datafiles['cycle'])
    datalib.plot_cycle(data)

if args.data == 'hppc':
    data = datalib.CellData(datafiles['hppc'])
    proc = datalib.CellData(datafiles['hppc'])
    proc.process_data()
    datalib.plot_hppc(data, proc)

if args.data == 'temp':
    if args.dis is None:
        print('Error: provide discharge rate as 1c, 2c, or 3c')

    elif args.dis == '1c':
        data = datalib.BitrodeData(datafiles['bitrode_1c'])
        proc = datalib.BitrodeData(datafiles['bitrode_1c'])
        proc.process_data()
        print(f'Time at start of first section:\t {proc.ti} s')
        print(f'Time at end of first section:\t {proc.tf} s')
        datalib.plot_bitrode(data, proc, '1C')

        data = datalib.TemperatureData(datafiles['temp_1c'], proc.ti, proc.tf)
        proc = datalib.TemperatureData(datafiles['temp_1c'], proc.ti, proc.tf)
        proc.process_data()
        datalib.plot_temp(data, proc, '1C')

    elif args.dis == '2c':
        data = datalib.BitrodeData(datafiles['bitrode_2c'])
        proc = datalib.BitrodeData(datafiles['bitrode_2c'])
        proc.process_data()
        print(f'Time at start of first section:\t {proc.ti} s')
        print(f'Time at end of first section:\t {proc.tf} s')
        datalib.plot_bitrode(data, proc, '2C')

        data = datalib.TemperatureData(datafiles['temp_2c'], proc.ti, proc.tf)
        proc = datalib.TemperatureData(datafiles['temp_2c'], proc.ti, proc.tf)
        proc.process_data()
        datalib.plot_temp(data, proc, '2C')

    elif args.dis == '3c':
        data = datalib.BitrodeData(datafiles['bitrode_3c'])
        proc = datalib.BitrodeData(datafiles['bitrode_3c'])
        proc.process_data()
        print(f'Time at start of first section:\t {proc.ti} s')
        print(f'Time at end of first section:\t {proc.tf} s')
        datalib.plot_bitrode(data, proc, '3C')

        data = datalib.TemperatureData(datafiles['temp_3c'], proc.ti, proc.tf)
        proc = datalib.TemperatureData(datafiles['temp_3c'], proc.ti, proc.tf)
        proc.process_data()
        datalib.plot_temp(data, proc, '3C')
