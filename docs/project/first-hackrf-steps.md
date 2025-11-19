# First Steps with HackRF One – Plan

These are my planned first experiments once I have access to a HackRF One.
The goal is to move from synthetic IQ files to real-world signals in small,
safe, receive-only steps, and to document everything in both English and
Georgian for other beginners in Georgia.

---

## 1. Setup and basic receive-only tests

**Goal:** verify that HackRF One works and that I can see real signals.

Planned steps:

1. Install and configure an SDR application (for example GQRX or SDRangel).
2. Connect a simple antenna (even a basic one to start).
3. Tune to a strong local **FM broadcast** station.
4. Adjust gain and sample rate until:
   - I can clearly see the FM signal in the spectrum,
   - I can hear the audio in the player.

I will take screenshots of:

- the spectrum + waterfall of the FM station,
- the basic configuration (frequency, sample rate, gains),

and add them to the `images/` folder and documentation.

---

## 2. Record real FM IQ and analyse it with my scripts

**Goal:** connect HackRF IQ → my Python tools → plots and simple FM demo.

Steps:

1. Use GQRX/SDRangel (or `hackrf_transfer`) to record a short FM IQ file, e.g.:

   - center frequency = local FM station,
   - sample rate = around 2 MHz,
   - duration = a few seconds.

2. Save the IQ file (complex64 or a format I can convert to complex64).

3. Use the scripts in `examples/`:

   - `plot_spectrum.py` – check how real FM looks compared to synthetic tones.
   - `plot_waterfall.py` – see how the FM signal behaves over time.
   - later: adapt `fm_demo_from_file.py` to try a simple FM demodulation from
     this real recording to WAV audio.

4. Document the result in a short note:
   - what command I used,
   - what I saw in the plots,
   - what worked / what was confusing.

---

## 3. Explore the 1090 MHz ADS-B band (receive-only)

**Goal:** see real ADS-B activity in the spectrum and waterfall and,
eventually, try an existing decoder.

Steps:

1. Connect or build a simple antenna that works reasonably at **1090 MHz**.
2. Tune HackRF to 1090 MHz with a suitable sample rate (for example 2–4 MHz).
3. Watch the spectrum and waterfall:
   - look for short, narrow bursts at 1090 MHz (ADS-B messages),
   - adjust gain until the bursts are clearly visible.

4. Record a short IQ file around 1090 MHz.

5. Use my Python scripts to:
   - plot the spectrum (showing the 1090 MHz channel),
   - plot a waterfall where bursts appear as short horizontal lines.

6. Once I have good recordings:
   - try an existing ADS-B decoder (for example dump1090 or similar),
   - compare the decoded aircraft list/map with what I see in my plots.

All of this will be strictly **receive-only** and for educational
visualisation of ADS-B signals.

---

## 4. First satellite experiments (when possible and legal)

**Goal:** take the first small step toward using HackRF for satellites,
even if it is just watching passes in the spectrum at first.

Ideas:

1. Identify a weather or amateur satellite that can be legally received in my
   location (e.g. a NOAA weather satellite).
2. Learn or build a simple antenna suitable for that band (for example a
   V-dipole or QFH for weather satellites).
3. Use HackRF + waterfall to:
   - watch a satellite pass as a moving, Doppler-shifted trace,
   - record a short IQ segment of the pass.

In the beginning I will focus only on **seeing** the pass in the waterfall
and getting clean recordings. Later I plan to:

- try existing open-source decoders to get images or telemetry, and
- document the full process in simple tutorials.

---

## 5. Documentation and local impact

For each of these steps I plan to:

- write short, practical notes in `docs/` (in English),
- add at least summary explanations in **Georgian**, so local students in
  Tbilisi and across Georgia can follow even if their English is not strong,
- collect screenshots in `images/` and small IQ snippets where possible,
- keep an experiment log of what worked, what failed, and what I learned.

Longer term, I want to turn these steps into:

- a small **SDR learning path** for beginners,
- and possibly a simple workshop or study group in Georgia, where HackRF One
  is still very rare and there are almost no local SDR resources.
