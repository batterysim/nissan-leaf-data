import numpy as np
import pandas as pd


class TemperatureData:
    """
    Temperature discharge data.

    Parameters
    ----------
    path : str
        Path to temperature discharge data file.
    ti : float
        Start time of first section in original Bitrode data.
    tf : float
        End time of first section in original Bitrode data.

    Attributes
    ----------
    tc1 : dataframe series
        Temperature data from thermocouple 1 [°C]
    tc2 : dataframe series
        Temperature data from thermocouple 2 [°C]
    tc3 : dataframe series
        Temperature data from thermocouple 3 [°C]
    tc4 : dataframe series
        Temperature data from thermocouple 4 [°C]
    time : vector
        Time for temperature data aquisition,  time step is 3 seconds [s]
    ti : float
        Start time of first temperature section.
    tf : float
        End time of first temperature section.
    """

    def __init__(self, path, ti, tf):
        df = pd.read_csv(path, header=None, sep='\t', usecols=[1, 2, 3, 4])
        self.tc1 = df[1]
        self.tc2 = df[2]
        self.tc3 = df[3]
        self.tc4 = df[4]
        self.time = np.arange(len(self.tc1)) * 3
        self.ti = ti
        self.tf = tf

    def get_idx(self):
        """
        Determine indices of start and end of first section in discharge data.

        Returns
        -------
        tuple
            First item is start index and second item is end index of first
            section in Bitrode discharge data.
        """
        id0 = np.argmin(np.abs(self.ti - self.time))
        id1 = np.argmin(np.abs(self.tf - self.time))
        return id0, id1

    def process_data(self):
        """
        Use temperature data that represents first section of the original
        temperature discharge data.
        """
        id0, id1 = self.get_idx()
        self.tc1 = self.tc1[id0:id1 + 1]
        self.tc2 = self.tc2[id0:id1 + 1]
        self.tc3 = self.tc3[id0:id1 + 1]
        self.tc4 = self.tc4[id0:id1 + 1]
        self.time = np.arange(len(self.tc1)) * 3
