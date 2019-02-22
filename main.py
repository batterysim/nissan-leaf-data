"""
Main driver script for data plots and analysis.

Arguments
---------
--cycle
    Plot original battery cell cycle data.
--hppc
    Plot original and processed HPPC data.
--temp
    Plot original and processed temperature discharge data. Takes parameters 1C, 2C, 3C.
"""

import argparse
import datalib

# Command line arguments ------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument('--cycle', action='store_true', help='plot original cycle data')
parser.add_argument('--hppc', action='store_true', help='plot original and processed hppc data')
parser.add_argument('--temp', help='plot original and processed temperature data')
args = parser.parse_args()

# Analyze data ----------------------------------------------------------------

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

if args.cycle:
    data = datalib.CellData(datafiles['cycle'])
    datalib.plot_cycle(data)

if args.hppc:
    data = datalib.CellData(datafiles['hppc'])
    proc = datalib.CellData(datafiles['hppc'])
    proc.process_data()
    datalib.plot_hppc(data, proc)

if args.temp == '1C':
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

elif args.temp == '2C':
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

elif args.temp == '3C':
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
