import numpy as np
import pandas as pd


class BitrodeData:
    """
    Bitrode discharge data.

    Parameters
    ----------
    path : str
        Path to Bitrode discharge data file.

    Attributes
    ----------
    time : dataframe series
        Time from experimental data [s]
    current : dataframe series
        Current from experimental data [A]
    voltage : dataframe series
        Voltage from experimental data [V]
    ids : array
        Indices of start and stop S-flags in data.
    id0 : int
        Index of first point in first discharge section of data.
    id1 : int
        Index of second point in first discharge section of data.
    id2 : int
        Index of third point in first discharge section of data.
    id3 : int
        Index of fourth point in first discharge section of data.
    ti : float
        Start time of first discharge section.
    tf : float
        End time of first discharge section.
    """

    def __init__(self, path):
        df = pd.read_csv(path, header=None)
        self.time = df[1]
        self.current = df[8]
        self.voltage = df[9]
        self.ids = np.where(df[14] == 'S')[0]
        self.id0 = self.ids[2]
        self.id1 = self.ids[3]
        self.id2 = self.ids[4]
        self.id3 = self.ids[5]
        self.ti = 0
        self.tf = 0

    def process_data(self):
        """
        Use Bitrode data that represents first section of the original Bitrode
        discharge data.
        """
        curr = self.current
        volt = self.voltage
        t = self.time
        id0 = self.id0
        id1 = self.id1
        id2 = self.id2
        id3 = self.id3

        if min(curr) > -40:
            self.time = t[id0:id2 + 1] - t[id0:id2 + 1].min()
            self.current = curr[id0:id2 + 1]
            self.voltage = volt[id0:id2 + 1]
            self.ti = t[id0]
            self.tf = t[id2]
        else:
            self.time = t[id1:id3 + 1] - t[id1:id3 + 1].min()
            self.current = curr[id1:id3 + 1]
            self.voltage = volt[id1:id3 + 1]
            self.ti = t[id1]
            self.tf = t[id3]
