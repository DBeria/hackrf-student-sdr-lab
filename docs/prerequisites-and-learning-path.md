# Prerequisites and Learning Path for This Project

This document explains what I think is useful to learn in order to follow
or contribute to this project. It is not a strict requirement list, but
a roadmap for myself and other beginners.

---

## 1. Basic skills (non-SDR)

Before going deep into SDR, it helps to be somewhat comfortable with:

- **Operating system basics**
  - using a terminal (PowerShell, cmd, or Linux shell),
  - installing programs,
  - navigating folders.

- **Programming basics**
  - some Python experience (variables, arrays, simple scripts),
  - basic use of `pip` to install packages.

- **Math basics**
  - sine and cosine,
  - complex numbers (real + imaginary),
  - very basic understanding of what a Fourier transform does
    (turns time-domain into frequency-domain).

You do not need to be an expert; the project is also meant to teach
these concepts gradually.

---

## 2. SDR and radio fundamentals

To work with SDR and HackRF, it is helpful to understand:

- **What radio waves are**
  - frequency, wavelength,
  - relationship between frequency and band (FM band, 1090 MHz, etc.).

- **Bandwidth and sample rate**
  - wider bandwidth → more spectrum visible, but more data,
  - sample rate in SDR ≈ how wide a slice of spectrum we capture.

- **IQ data**
  - what I and Q are,
  - why SDR uses complex samples (see `docs/iq-and-spectra-basics.md`).

- **Spectrum and waterfall**
  - how to read them,
  - how different kinds of signals (FM, ADS-B, noise) look in these plots.

---

## 3. Software tools to know

For this project, I plan to use:

- **Python**
  - `numpy`, `matplotlib` for processing and plotting IQ data,
  - small scripts in `examples/`.

- **GNU Radio (later)**
  - for building more complex flowgraphs (FM, ADS-B, satellite signals).

- **SDR receivers**
  - GQRX / SDRangel / similar:
    - good for quickly seeing spectrum and listening to signals,
    - useful for debugging antenna and frequency settings.

You do not need to know all of these at once. The idea is to start with
Python and simple visualisation, then add GNU Radio and live reception
later.

---

## 4. Learning path inside this project

A rough path I imagine for myself and other learners:

1. **IQ and spectrum basics**
   - Read: `docs/iq-and-spectra-basics.md`
   - Try: `examples/generate_test_tone.py`, `plot_spectrum.py`,
     `plot_waterfall.py`
   - Goal: understand what IQ is and how spectrum/waterfall are created.

2. **Signal chain understanding**
   - Read: `docs/signal-chain-overview.md`
   - Goal: see the big picture: antenna → HackRF → IQ → software →
     plots/audio/data.

3. **FM broadcast**
   - Read: `docs/fm-from-iq-basics.md`
   - Try later: `examples/fm_demo_from_file.py` with real FM IQ recordings.
   - Goal: understand FM as an example of analog modulation and get
     first real „sound“ from IQ.

4. **ADS-B aircraft tracking**
   - Read: `docs/adsb-from-iq-basics.md`
   - Later: capture or use existing ADS-B IQ recordings, and/or use
     existing tools to decode aircraft positions.
   - Goal: move to a digital, bursty signal (1090 MHz) and see how
     real-world data can be extracted from IQ.

5. **Satellites (future work)**
   - Plan to add notes and experiments for weather and amateur
     satellites when possible and legal to receive.
   - Goal: connect IQ, FFT, demodulation, and decoding to something
     visually exciting (Earth images, telemetry, etc.).

---

## 5. Legal and ethical mindset

Throughout all of this, it is important to keep in mind:

- Work only with **signals that are legal to receive** in your country.
- Do **not** transmit or replay signals on bands where you are not
  licensed or allowed to do so.
- Treat this project as a way to learn, teach, and explore the radio
  spectrum responsibly.

This project is meant to be a friendly learning lab, not a hacking kit.

---

## 6. How this roadmap may change

This learning path is not fixed:

- As I learn more, I will update these notes.
- I may add extra steps (e.g., basic AM demodulation, simple FSK),
- or adjust the order as I discover better ways to explain topics.

Contributions and suggestions are welcome, especially if you are also a
beginner and want to improve the explanations.
