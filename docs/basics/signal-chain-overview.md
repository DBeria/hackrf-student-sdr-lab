# Signal Chain Overview – From Radio Waves to IQ and Plots

This document explains, in simple terms, how signals travel from the
real world into my computer, and how HackRF One and software defined
radio (SDR) fit into that chain.

The goal is to understand where **IQ data** comes from and how it
relates to spectrum, waterfall plots, and later decoding.

---

## 1. High-level signal chain

From "waves in the air" to something I can see or process:

1. **Real-world RF signals**

   Examples:
   - FM broadcast stations
   - ADS-B signals from aircraft (1090 MHz)
   - Weather satellites
   - Various other legal-to-receive transmissions

2. **Antenna**

   The antenna picks up electromagnetic waves and converts them into
   a small RF voltage that can be fed into the SDR.

3. **HackRF One (RF front end + ADC)**

   HackRF One:
   - tunes to a chosen **center frequency** (for example 100 MHz for FM),
   - selects a **bandwidth** (sample rate),
   - amplifies and filters the signal,
   - converts the analog signal to digital using an ADC.

   The digital output is a stream of **complex IQ samples**:

   > I(t) + j·Q(t)

   where **I** is the in-phase component and **Q** is the quadrature
   component. These samples represent the amplitude and phase of the
   RF signal around the tuned center frequency.

4. **USB connection**

   HackRF sends the IQ samples over USB to the computer. At this point,
   we still do not have "sound" or "bits", only raw complex samples.

5. **SDR software on the computer**

   Different programs can receive the IQ stream:

   - GQRX / SDRangel / SDR#:
     - show **spectrum** and **waterfall**,
     - demodulate FM/AM/SSB and play **audio**,
     - optionally save **IQ recordings** to files.

   - GNU Radio:
     - processes IQ using flowgraphs,
     - can filter, demodulate, and decode many different signals,
     - can also generate new IQ signals for transmission.

   - Custom scripts (like the ones in this repository):
     - read IQ files,
     - visualise them (spectrum, waterfall),
     - later: demodulate and decode specific signals.

6. **Processing and visualisation**

   From IQ data, software can:

   - Compute a **spectrum**:
     - show how much energy there is at each frequency in a short time window.
   - Build a **waterfall**:
     - show how the spectrum changes over time.
   - Demodulate and decode:
     - FM audio,
     - ADS-B aircraft messages,
     - data from satellites (where legally allowed),
     - other protocols.

---

## 2. Live vs recorded IQ

There are two common ways to work with IQ data:

1. **Live mode**

   - HackRF streams IQ samples in real time.
   - Software (GQRX, SDRangel, GNU Radio) shows:
     - spectrum and waterfall,
     - live demodulated audio or decoded messages.

2. **Recorded mode**

   - IQ samples are saved to a file (for example `recording.cfile`).
   - Later, scripts or GNU Radio flowgraphs can:
     - replay the file,
     - analyse it,
     - try new filters and decoders without needing live hardware.

In this project I start with **offline analysis**:

- generate synthetic IQ data (`generate_test_tone.py`),
- plot spectrum and waterfall (`plot_spectrum.py`, `plot_waterfall.py`).

Later, I plan to move to **real recordings from HackRF One** and apply
the same tools to actual FM, ADS-B and satellite signals.

---

## 3. Where IQ fits in the protocol stack

IQ data is at the **lowest digital level** of the radio signal:

- IQ: samples that describe the waveform near a certain frequency.
- From IQ, we can demodulate to:
  - audio (for analog modes like FM/AM),
  - bits (for digital modes).

From those bits, higher-level protocols appear:

- For example:
  - IQ at 1090 MHz → demodulation → ADS-B frames → aircraft positions.
  - IQ in the FM band → FM demodulation → audio samples → sound.

HackRF only gives IQ. All higher-level decoding happens in software.

---

## 4. Relation to this repository

In this repository:

- `examples/` contains Python scripts that:
  - generate test IQ data (`generate_test_tone.py`),
  - plot spectra (`plot_spectrum.py`),
  - plot waterfalls (`plot_waterfall.py`).

- `docs/iq-and-spectra-basics.md` explains:
  - what IQ data is,
  - how spectrum and waterfall plots are computed from it.

- Later, I plan to add:
  - GNU Radio flowgraphs for FM, ADS-B, and satellites,
  - demodulation and decoding examples,
  - tutorials (English + Georgian) that connect the theory to real
    HackRF experiments.
