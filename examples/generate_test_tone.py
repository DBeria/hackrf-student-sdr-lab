"""
Generate a simple complex IQ test signal (one or two tones) and save it
to a binary file in complex64 format.

Usage:
    python generate_test_tone.py output.cfile 2_000_000

where 2_000_000 is the sample rate in Hz.
"""

import sys
import numpy as np


def generate_tone(sample_rate, duration_s=1.0):
    """Generate a test signal: two complex tones at different offsets."""
    num_samples = int(sample_rate * duration_s)
    t = np.arange(num_samples) / sample_rate

    # Frequencies as offsets from center (in Hz)
    f1 = 50_000.0   # 50 kHz
    f2 = -120_000.0 # -120 kHz

    # Complex exponentials
    tone1 = np.exp(2j * np.pi * f1 * t)
    tone2 = 0.6 * np.exp(2j * np.pi * f2 * t)

    # Sum and normalize a bit
    iq = (tone1 + tone2) * 0.5
    return iq.astype(np.complex64)


def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_test_tone.py <output_file> <sample_rate_hz>")
        sys.exit(1)

    out_path = sys.argv[1]
    sample_rate = float(sys.argv[2])

    iq = generate_tone(sample_rate)
    iq.tofile(out_path)
    print(f"Saved test IQ file to: {out_path}")


if __name__ == "__main__":
    main()
