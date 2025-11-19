"""
Plot a simple waterfall (time vs frequency vs power) from a complex64
IQ recording.

Usage:
    python plot_waterfall.py example.cfile 2_000_000

where 2_000_000 is the sample rate in Hz.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt


def compute_waterfall(path, sample_rate, fft_size=2048, hop=1024):
    iq = np.fromfile(path, dtype=np.complex64)
    if iq.size < fft_size:
        raise ValueError("IQ file too short for given fft_size.")

    # Number of columns (time steps)
    num_cols = 1 + (iq.size - fft_size) // hop

    spec = np.empty((num_cols, fft_size), dtype=np.float32)

    window = np.hanning(fft_size)

    for i in range(num_cols):
        start = i * hop
        chunk = iq[start:start + fft_size]
        chunk_win = chunk * window
        fft = np.fft.fftshift(np.fft.fft(chunk_win))
        power_db = 20 * np.log10(np.abs(fft) + 1e-9)
        spec[i, :] = power_db

    # Time axis (seconds)
    time_axis = np.arange(num_cols) * (hop / sample_rate)
    # Frequency axis (MHz)
    freq_axis = np.linspace(-sample_rate / 2, sample_rate / 2, fft_size) / 1e6

    return spec, time_axis, freq_axis


def plot_waterfall(path, sample_rate):
    spec, time_axis, freq_axis = compute_waterfall(path, sample_rate)

    plt.figure()
    # Waterfall: time on Y, frequency on X
    plt.imshow(
        spec,
        aspect="auto",
        origin="lower",
        extent=[freq_axis[0], freq_axis[-1], time_axis[0], time_axis[-1]],
    )
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Time (s)")
    plt.title("Waterfall of IQ recording")
    plt.colorbar(label="Power (dB)")
    plt.show()


def main():
    if len(sys.argv) != 3:
        print("Usage: python plot_waterfall.py <iq_file> <sample_rate_hz>")
        sys.exit(1)

    path = sys.argv[1]
    sample_rate = float(sys.argv[2])
    plot_waterfall(path, sample_rate)


if __name__ == "__main__":
    main()
