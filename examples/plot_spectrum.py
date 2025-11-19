"""
Simple example script for plotting the power spectrum of an IQ recording.

This does NOT require HackRF to run; it just expects a complex64
binary file exported from any SDR program (for example GNU Radio or GQRX).

Usage (example):
    python plot_spectrum.py example.cfile 2_000_000

where 2_000_000 is the sample rate in Hz.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt


def plot_spectrum(path, sample_rate):
    # Load complex64 IQ data from file
    iq = np.fromfile(path, dtype=np.complex64)

    if iq.size == 0:
        print("File is empty or not in complex64 format.")
        return

    # Apply a Hanning window to reduce spectral leakage
    window = np.hanning(iq.size)
    iq_win = iq * window

    # Compute FFT and convert to dB
    spectrum = np.fft.fftshift(np.fft.fft(iq_win))
    spectrum_db = 20 * np.log10(np.abs(spectrum) + 1e-9)

    # Frequency axis
    freqs = np.linspace(-sample_rate / 2, sample_rate / 2, iq.size) / 1e6  # MHz

    # Plot
    plt.figure()
    plt.plot(freqs, spectrum_db)
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Power (dB)")
    plt.title("Power spectrum of IQ recording")
    plt.grid(True)
    plt.show()


def main():
    if len(sys.argv) != 3:
        print("Usage: python plot_spectrum.py <iq_file> <sample_rate_hz>")
        sys.exit(1)

    path = sys.argv[1]
    sample_rate = float(sys.argv[2])
    plot_spectrum(path, sample_rate)


if __name__ == "__main__":
    main()
