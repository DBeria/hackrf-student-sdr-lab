# HackRF One – Study Notes

These are my personal notes while reading the official HackRF
documentation from Great Scott Gadgets. I use this as a quick
reference while learning SDR and planning experiments.

## Basic Features

- Half-duplex transceiver (can transmit or receive, but not both at the same time).
- Frequency range: 1 MHz to 6 GHz.
- Typical sample rates: about 2 Msps to 20 Msps (quadrature).
- 8-bit samples.
- Powered over high-speed USB 2.0.
- SMA antenna connector, clock input and output.
- Open source hardware and open source firmware.

## Power and Safety

- TX power is usually in the range of about 0–10 dBm through most of
  the spectrum up to around 4 GHz.
- Maximum safe RX input level is about −5 dBm. Stronger signals can
  damage the front end, so an external attenuator is recommended for
  very strong signals.
- Before transmitting, it is important to know and respect local radio
  regulations. HackRF is a test/development tool, not a certified
  transmitter.

## Gain Controls (Receive)

HackRF has three receive gain stages:

- RF gain (“amp”) – either off or roughly +11 dB.
- IF gain (“lna”) – 0 to 40 dB in steps.
- Baseband gain (“vga”) – 0 to 62 dB in small steps.

For transmit there are two gain stages. For most experiments I’ll
start with modest gains and slowly increase them while watching the
spectrum and signal quality.

## DC Spike in the Center

- A spike in the middle of the spectrum display is usually a DC offset,
  not a real signal.
- It comes from the way IQ sampling works and is normal for SDRs.
- Common ways to deal with it:
  - ignore it if it doesn’t disturb the signal of interest
  - use offset tuning and shift in software
  - apply DC correction options in the software

## Host and USB Notes

- SDR work can be demanding for the computer and USB bus.
- HackRF expects about 500 mA at 5 V from USB.
- A short, shielded USB cable (ideally with a ferrite bead) often
  gives better performance and less noise.
- If HackRF is not detected, trying a different USB cable often fixes it.

---

These notes are a starting point. As I gain real-world experience with
HackRF One, I will add practical examples (for example, preferred gain
settings and screenshots for FM, ADS-B, satellite reception, etc.).
