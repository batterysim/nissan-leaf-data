# Battery Cell Data

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2580327.svg)](https://doi.org/10.5281/zenodo.2580327)

This repository contains data files from experiments conducted on a 2013 Nissan Leaf battery cell. The purpose of the experiments was to development an equivalent circuit model of the cell. Specifications for the cell are given in the table shown below. Descriptions of the folders and files in this repository are provided in the following sections.

| Cell specs        | Properties          |
| ----------------- | ------------------: |
| cell type         | laminate            |
| cathode material  | LiMn2O4 with LiNiO2 |
| anode material    | graphite            |
| rated capacity    | 33.1 Ah             |
| average voltage   | 3.8 V               |
| length            | 11.417 in (290 mm)  |
| width             | 8.504 in (216 mm)   |
| thickness         | 0.2795 in (7.1 mm)  |
| weight            | 1.7624 lbs (799 g)  |

### data

Data files from charge/discharge cycling, HPPC, and discharge tests are in the `data` directory. These battery cell experiments and associated data files are discussed below.

**Charge and discharge cycling tests**

- Performed at ambient temperatures of 10°C, 24°C, and 40°C
- C/15 constant current discharge to 3.0 V
- C/15 constant current charge to 4.2 V
- No temperature data
- `NissanLeaf-cell-Cycling-10C-24C-40C.csv`

**HPPC tests**

- Performed at ambient temperatures of 10°C, 25°C, and 40°C
- 30 sec discharge pulse, 40 sec rest, 10 sec regen pulse
- Discharge to next 10% decrease in state of charge
- Rest for one hour
- Repeat above steps until cell is fully discharged
- No temperature data
- `NissanLeaf-cell-Low-Current-HPPC-25C-2.csv`

**Discharge tests**

- Constant current discharge tests were conducted at 1C, 2C, and 3C
- Temperature data available from three thermocouples
- TC1 is thermocouple close to tabs
- TC2 is thermocouple at middle of cell
- TC3 is thermocouple near bottom of cell
- `1C-Discharge-Bitrode-data.csv` and `Temperature-1C-discharge.lvm`
- `2C-Discharge-Bitrode-data.csv` and `Temperature-2C-discharge.lvm`
- `3C-Discharge-Bitrode-data.csv` and `Temperature-3C-discharge.lvm`

### datalib

Functions and modules for reading and analyzing the data files are available in the `datalib` Python package. This package is used by the `plot.py` script to create plots of the data.

### plot.py

Run `plot.py` to view plots of the data. Available command line arguments are presented below:

```bash
# plot voltage and current from the charge/discharge tests
$ python plot.py cycle

# plot voltage and current from the HPPC test
$ python plot.py hppc

# plot Bitrode and temperature data from 1C, 2C, 3C discharge tests
$ python plot.py temp 1c
$ python plot.py temp 2c
$ python plot.py temp 3c
```

## Citation

Click the blue DOI badge at the top of this README for citation options provided by Zenodo. Alternatively, cite this data in publications and presentations as:

```
Gavin Wiggins, Srikanth Allu, and Hsin Wang. Battery cell data from a 2013
Nissan Leaf. Oak Ridge National Laboratory. https://doi.org/10.5281/zenodo.2580327.
```
