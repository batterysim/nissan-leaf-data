import numpy as np
import pandas as pd


class CellData:
    """
    Battery cell cycle data or HPPC data.

    Parameters
    ----------
    path : str
        Path to battery cell cycle data file or HPPC data file.

    Attributes
    ----------
    time : vector
        Time vector for battery test data [s]
    current : vector
        Current from battery during test [A]
    voltage : vector
        Voltage from battery during test [V]
    data : vector
        Data flags from battery test [-]
    """

    def __init__(self, path):
        df = pd.read_csv(path)
        self.time = df['Time(s)'].values
        self.current = df['Current(A)'].values
        self.voltage = df['Voltage(V)'].values
        self.data = df['Data'].fillna(' ').values

    def get_ids(self):
        """Return indices of start and stop points in data."""
        ids = np.where(self.data == 'S')[0]
        return ids

    def get_idq(self):
        """Return index of final stop point in data."""
        idq = np.where(self.data == 'Q')[0]
        return idq

    def get_idx(self):
        """
        Indices used for equivalent circuit model development.

        Returns
        -------
        tuple
            For example idx = id0, id1, id2, id3, id4 where
            id0 = start of pulse discharge
            id1 = time step after pulse discharge starts
            id2 = end of pulse discharge ends
            id3 = time step after pulse discharge ends
            id4 = end of pulse discharge rest period
        """
        ids = self.get_ids()
        id0 = ids[0::5]
        id1 = id0 + 1
        id2 = ids[1::5]
        id3 = id2 + 1
        id4 = ids[2::5]
        return id0, id1, id2, id3, id4

    def get_idrc(self):
        """
        Indices used to determine resistor and capacitor parameters.

        Returns
        -------
        tuple
            For example idrc = id0, id1, id2, id3, id4 where
            id0 = start of constant discharge
            id1 = time step after constant discharge starts
            id2 = end of constant discharge
            id3 = time step after constant discharge ends
            id4 = end of rest period
        """
        ids = self.get_ids()
        id0 = ids[3::5][:-1]
        id1 = id0 + 1
        id2 = ids[4::5]
        id3 = id2 + 1
        id4 = ids[5::5]
        return id0, id1, id2, id3, id4

    def process_data(self):
        """
        Use data for equivalent circuit model development. The S-flag determines
        start and stop indices `ids` in the data. Data preceding the first
        start/stop point is removed then assign remaining data to class
        attributes.
        """
        ids = np.where(self.data == 'S')[0]
        self.time = self.time[ids[1]:]
        self.current = self.current[ids[1]:]
        self.voltage = self.voltage[ids[1]:]
        self.data = self.data[ids[1]:]
