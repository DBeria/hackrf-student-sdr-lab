# ADS-B from IQ – Basics for Aircraft Tracking

These notes are my beginner-friendly explanation of what ADS-B is and
how it fits into my SDR project. The goal is to understand what kind of
signals aircraft transmit, what information they contain, and how IQ
data and spectrum relate to ADS-B.

---

## 1. What is ADS-B?

ADS-B stands for **Automatic Dependent Surveillance – Broadcast**.

- **Automatic** – sent periodically without a request.
- **Dependent** – depends on aircraft sensors (GPS, barometric altitude, etc.).
- **Surveillance** – used for tracking aircraft.
- **Broadcast** – transmitted openly over the air, not encrypted.

Typical ADS-B message contains:

- aircraft identity (24-bit ICAO address),
- callsign (flight ID),
- position (latitude, longitude),
- altitude,
- velocity and heading,
- some status information.

These messages are broadcast so that ATC and other aircraft can receive
them. Hobbyists are allowed to **receive and decode** them in many
countries, but of course not to interfere with aviation systems.

---

## 2. ADS-B signal basics

Key technical points:

- Frequency: **1090 MHz**
- Modulation: **Pulse-Position Modulation (PPM)**
- Symbol rate: **1 Mbit/s**
- Message length: 56 or 112 bits (short and long frames)

In the RF domain:

- An ADS-B message is a short **burst of pulses** at 1090 MHz.
- Each bit is represented by a pulse in one half of the bit time
  (pulse-position).

In the baseband IQ domain (after tuning and downconversion):

- We see short amplitude bursts in time,
- With a specific pattern that corresponds to bits.

---

## 3. ADS-B in spectrum and waterfall

When looking at ADS-B around 1090 MHz:

- **Spectrum**:
  - The 1090 MHz channel is relatively narrow,
  - ADS-B bursts appear as **short spikes** in the spectrum if you look
    at a fine time resolution.

- **Waterfall**:
  - Each message appears as a short **horizontal dash** at 1090 MHz,
  - Many aircraft → many dashes over time.

So:

- FM broadcast: wide, continuous band.
- ADS-B: narrow frequency, short intermittent bursts.

---

## 4. ADS-B and IQ data

From the SDR perspective:

1. HackRF is tuned so that 1090 MHz is within the passband.
2. HackRF outputs complex IQ samples around that center frequency.
3. Software (GNU Radio, dump1090, etc.) processes IQ data to:
   - detect bursts,
   - recover the pulse pattern,
   - decode bits into ADS-B messages.

Important distinction:

- **IQ data** = what HackRF (or a recording) provides.
- **ADS-B messages** = decoded information (position, altitude, etc.)
  extracted from IQ using a demodulator and decoder.

For this project, I am focusing first on:

- understanding IQ, spectrum, and waterfall,
- then learning how ADS-B demodulation works conceptually,
- and finally using existing decoders (or simple experiments) to
  visualize aircraft data.

---

## 5. Safety and legality

ADS-B messages are broadcast in the clear and are widely received by
hobbyists. However:

- I will only **receive and decode** ADS-B, never attempt to transmit or
  interfere with aircraft signals.
- Transmission on aviation bands is highly regulated and must not be
  done without proper authorization.
- This project is strictly for learning, visualization, and legal
  reception of public broadcast signals.

---

## 6. How ADS-B fits into my project

In my project roadmap:

1. **FM broadcast**:
   - Learn basic IQ, spectrum, and simple demodulation.

2. **ADS-B**:
   - Work with a narrower, bursty, digital signal at 1090 MHz.
   - Learn how to:
     - visualize bursts in time/frequency,
     - understand the basic idea of pulse-position modulation,
     - use existing tools to decode and plot aircraft positions.

3. **Satellites**:
   - Move from aircraft to weather and amateur satellites where legally
     allowed to receive, using the same IQ and SDR concepts.

The goal is not to write a full ADS-B decoder from scratch, but to
understand enough theory and IQ-level behaviour to appreciate what
existing tools are doing and to document the process for other students.
