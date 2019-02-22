import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


def _config(ax, xlabel, ylabel, title=None, legend=True):
    """Configure appearance of plot."""
    ax.grid(True, color='0.9')
    ax.set_frame_on(False)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(color='0.9')
    if title is not None:
        ax.set_title(title)
    if legend:
        ax.legend(loc='best')


def plot_cycle(data):
    """Plot original cycle data."""

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, tight_layout=True)
    ax1.plot(data.time / 3600, data.current, 'C0')
    ax1.grid(True, color='0.9')
    ax1.tick_params(color='0.9')
    ax1.set_frame_on(False)
    ax1.set_ylabel('Current [A]')
    ax1.set_title('Battery cell cycle data')
    ax2.plot(data.time / 3600, data.voltage, 'C3')
    ax2.grid(True, color='0.9')
    ax2.tick_params(color='0.9')
    ax2.set_frame_on(False)
    ax2.set_xlabel('Time [hr]')
    ax2.set_ylabel('Voltage [V]')

    plt.show()


def plot_hppc(data, proc):
    """Plot original and processed HPPC data."""

    fig, ax = plt.subplots()
    ax.plot(data.time, data.voltage, 'C3')
    ax.arrow(15474, 4.06, 0, -0.14, head_width=1000, head_length=0.05, zorder=20)
    ax.grid(True, color='0.9')
    ax.set_frame_on(False)
    ax.set_title('HPPC original data')
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Voltage [V]')
    ax.tick_params(color='0.9')
    axins = inset_axes(ax, 2, 2, loc='lower left', borderpad=4)
    axins.plot(data.time, data.voltage, 'C3')
    axins.set_xlim(15420, 15540)
    axins.set_ylim(4.08, 4.21)
    plt.xticks(visible=False)
    plt.yticks(visible=False)

    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(data.time, data.current, 'C0')
    _config(ax, 'Time [s]', 'Current [A]', 'HPPC original data', legend=False)

    fig, ax1 = plt.subplots(tight_layout=True)
    ax1.plot(data.time, data.current, 'C0')
    ax1.set_title('HPPC original data')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Current [A]', color='C0')
    ax1.tick_params('y', colors='C0')
    ax1.set_frame_on(False)
    ax2 = ax1.twinx()
    ax2.plot(data.time, data.voltage, 'C3')
    ax2.set_frame_on(False)
    ax2.set_ylabel('Voltage [V]', color='C3')
    ax2.tick_params('y', colors='C3')

    ids = proc.get_ids()
    idq = proc.get_idq()
    idrc = proc.get_idrc()

    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(proc.time, proc.voltage, 'C3', label='data')
    ax.plot(proc.time[ids], proc.voltage[ids], 'x', label='ids')
    ax.plot(proc.time[idq], proc.voltage[idq], 'x', label='idq')
    ax.plot(proc.time[idrc[0]], proc.voltage[idrc[0]], 'o', alpha=0.8, mew=0, label='id0')
    ax.plot(proc.time[idrc[1]], proc.voltage[idrc[1]], 'o', alpha=0.8, mew=0, label='id1')
    ax.plot(proc.time[idrc[2]], proc.voltage[idrc[2]], 'o', alpha=0.8, mew=0, label='id2')
    ax.plot(proc.time[idrc[3]], proc.voltage[idrc[3]], 'o', alpha=0.8, mew=0, label='id3')
    ax.plot(proc.time[idrc[4]], proc.voltage[idrc[4]], 'o', alpha=0.8, mew=0, label='id4')
    _config(ax, 'Time [s]', 'Voltage [V]', 'HPPC processed data for model development')

    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(proc.time, proc.current, 'C0', label='data')
    ax.plot(proc.time[ids], proc.current[ids], 'x', label='ids')
    ax.plot(proc.time[idq], proc.current[idq], 'x', label='idq')
    _config(ax, 'Time [s]', 'Current [A]', 'HPPC processed data for model development')

    plt.show()


def plot_bitrode(data, proc, dis):
    """Plot original and processed temperature discharge data."""

    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(data.time, data.current, 'C0', label='data')
    ax.plot(data.time[data.ids], data.current[data.ids], 'x', label='ids')
    ax.plot(data.time[data.id0], data.current[data.id0], 'o', alpha=0.8, mew=0, label='id0')
    ax.plot(data.time[data.id1], data.current[data.id1], 'o', alpha=0.8, mew=0, label='id1')
    ax.plot(data.time[data.id2], data.current[data.id2], 'o', alpha=0.8, mew=0, label='id2')
    ax.plot(data.time[data.id3], data.current[data.id3], 'o', alpha=0.8, mew=0, label='id3')
    _config(ax, 'Time [s]', 'Current [A]', f'Bitrode original data {dis} discharge')

    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(data.time, data.voltage, 'C3', label='data')
    ax.plot(data.time[data.ids], data.voltage[data.ids], 'x', label='ids')
    ax.plot(data.time[data.id0], data.voltage[data.id0], 'o', alpha=0.8, mew=0, label='id0')
    ax.plot(data.time[data.id1], data.voltage[data.id1], 'o', alpha=0.8, mew=0, label='id1')
    ax.plot(data.time[data.id2], data.voltage[data.id2], 'o', alpha=0.8, mew=0, label='id2')
    ax.plot(data.time[data.id3], data.voltage[data.id3], 'o', alpha=0.8, mew=0, label='id3')
    _config(ax, 'Time [s]', 'Voltage [V]', f'Bitrode original data {dis} discharge')

    fig, ax1 = plt.subplots(tight_layout=True)
    ax1.plot(data.time, data.current, 'C0')
    ax1.set_frame_on(False)
    ax1.set_title(f'Bitrode original data {dis} discharge')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Current [A]', color='C0')
    ax1.tick_params('y', colors='C0')
    ax2 = ax1.twinx()
    ax2.plot(data.time, data.voltage, 'C3')
    ax2.set_frame_on(False)
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('Voltage [V]', color='C3')
    ax2.tick_params('y', colors='C3')

    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(np.diff(proc.time), 'o', alpha=0.4)
    _config(ax, 'Item [-]', 'Time step [s]', f'Bitrode processed data {dis} discharge', legend=False)

    fig, ax1 = plt.subplots(tight_layout=True)
    ax1.plot(proc.time, proc.current, 'C0')
    ax1.set_frame_on(False)
    ax1.set_title(f'Bitrode processed data {dis} discharge')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Current [A]', color='C0')
    ax1.tick_params('y', colors='C0')
    ax2 = ax1.twinx()
    ax2.plot(proc.time, proc.voltage, 'C3')
    ax2.set_frame_on(False)
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('Voltage [V]', color='C3')
    ax2.tick_params('y', colors='C3')


def plot_temp(data, proc, dis):
    """Plot original and processed temperature discharge data."""

    id0, id1 = data.get_idx()

    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(data.time, data.tc1, label='tc1')
    ax.plot(data.time, data.tc2, label='tc2')
    ax.plot(data.time, data.tc3, label='tc3')
    ax.plot(data.time, data.tc4, label='tc4')
    plt.axvspan(data.time[id0], data.time[id1], facecolor='0.9')
    _config(ax, 'Time [s]', 'Temperature [°C]', f'Temperature original data {dis} discharge')

    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(proc.time, proc.tc1, label='tc1')
    ax.plot(proc.time, proc.tc2, label='tc2')
    ax.plot(proc.time, proc.tc3, label='tc3')
    ax.plot(proc.time, proc.tc4, label='tc4')
    _config(ax, 'Time [s]', 'Temperature [°C]', f'Temperature processed data {dis} discharge')

    plt.show()
