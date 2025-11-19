# First Steps – FM Broadcast with SDR

This will be my first full tutorial once I have HackRF One, but I am
already preparing the structure and notes.

## 1. What is FM broadcast?

- Frequency range: around 88–108 MHz (depends on country).
- Wideband FM, good first signal to experiment with.
- Strong and easy to receive in most cities.

## 2. Tools I plan to use

- HackRF One as the SDR
- GQRX or SDR# for first tests
- GNU Radio for more advanced experiments
- `plot_spectrum.py` from the `examples/` folder to look at recordings

## 3. Basic workflow (draft)

1. Connect antenna and HackRF One to the laptop.
2. Start GQRX/SDR# and select HackRF One as the device.
3. Set the center frequency near a known FM station.
4. Adjust gain so that the signal is strong but not clipping.
5. Listen to the audio and watch the spectrum/waterfall.

Later I will add:

- Screenshots of my setup
- Recommended gain values that worked for me
- Example IQ recording and how to plot its spectrum
- Troubleshooting notes (“no audio”, “too noisy”, etc.)

For now this is a draft. It reminds me what to document when I run the
experiment for real.
