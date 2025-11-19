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
     - show how much energy there
