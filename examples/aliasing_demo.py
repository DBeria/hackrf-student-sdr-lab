#!/usr/bin/env python3
"""
aliasing_demo.py

Generate a complex IQ file with a single tone at a chosen frequency
and print where that tone will appear in the sampled spectrum.

This is useful to experiment with sampling rate, Nyquist and aliasing.

Usage examples:

    # 2 MHz sample rate, tone at 300 kHz (no aliasing, well inside band)
    python aliasing_demo.py tone_300k.cfile 2000000 300000

    # 2 MHz sample rate, tone at 1.3 MHz (above Fs/2 = 1 MHz, will alias)
    python aliasing_demo.py tone_1300k.cfile 2000000 1300000

You can then plot the result with:

    python plot_spectrum.py tone_1300k.cfile 2000000

and see where the peak actually appears.
"""

import sys
import numpy as np

def wrap_to_baseband(f_hz: float, fs_hz: float) -> float:
    """
    Wrap a frequency f_hz into the baseband interval [-Fs/2, +Fs/2].
    This shows where the tone appears in the sampled spectrum.
    """
    # shift by Fs/2, take modulo Fs, then shift back by -Fs/2
    wrapped = (f_hz + fs_hz / 2.0) % fs_hz - fs_hz / 2.0
    return wrapped


def main():
    if len(sys.argv) != 4:
        print("Usage: python aliasing_demo.py <output.cfile> <fs_hz> <tone_freq_hz>")
        print("Example: python aliasing_demo.py tone_1300k.cfile 2000000 1300000")
        sys.exit(1)

    out_path = sys.argv[1]
    fs_hz = float(sys.argv[2])
    f_tone = float(sys.argv[3])

    # number of samples for the demo (a few milliseconds is enough)
    num_samples = 200000  # adjust if you want longer/shorter files

    t = np.arange(num_samples) / fs_hz

    # generate complex exponential: e^{j 2π f t}
    iq = np.exp(1j * 2.0 * np.pi * f_tone * t).astype(np.complex64)

    # save as binary complex64 (same format as other examples)
    iq.tofile(out_path)

    nyquist = fs_hz / 2.0
    f_wrapped = wrap_to_baseband(f_tone, fs_hz)

    print(f"Generated tone at f = {f_tone:.1f} Hz with Fs = {fs_hz:.1f} Hz.")
    print(f"Nyquist frequency (Fs/2) = {nyquist:.1f} Hz.")

    if abs(f_tone) > nyquist:
        print("NOTE: This tone is ABOVE Nyquist. In the discrete-time spectrum")
        print(f"      it will appear aliased at approximately {f_wrapped:.1f} Hz.")
    else:
        print("This tone is within the Nyquist range (no aliasing in baseband).")
        print(f"It will appear around {f_tone:.1f} Hz in the spectrum.")

    print(f"IQ data written to: {out_path}")
    print("You can visualise it with:")
    print(f"  python plot_spectrum.py {out_path} {int(fs_hz)}")


if __name__ == "__main__":
    main()
