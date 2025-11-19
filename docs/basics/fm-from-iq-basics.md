# FM from IQ – How Frequency Modulation Looks and How to Demodulate It

These are my beginner notes on how **frequency modulation (FM)** looks in
IQ data and how it can be demodulated. The goal is to understand what
the SDR and software are actually doing when I “listen to FM”.

This is written for future me and other students learning SDR step by step.

---

## 1. What is FM (Frequency Modulation)?

In FM (Frequency Modulation):

- The **instantaneous frequency** of the carrier is changed according to
  the message (audio) signal.
- The **amplitude** of the carrier stays (ideally) constant.

If we have an audio signal m(t), we use it to “wiggle” the frequency of
a carrier around some center frequency f_c.

Very roughly:

- Louder audio → bigger deviation of frequency from f_c  
- Quieter audio → smaller deviation

For broadcast FM (like 100.3 MHz):

- Carrier: around 88–108 MHz (depends on the station)
- Deviation: up to about ±75 kHz around the carrier

So instead of the signal getting taller/shorter (AM), its **frequency**
moves up and down around the centre.

---

## 2. FM in IQ: amplitude vs phase

In IQ (complex baseband):

> s(t) = I(t) + j·Q(t)

We can rewrite this in polar form:

> s(t) = A(t) · e^{j·φ(t)}

where:

- **A(t)** = amplitude = √(I² + Q²)  
- **φ(t)** = phase = atan2(Q, I)

For **FM**:

- A(t) ≈ constant (the amplitude doesn’t carry the information)
- φ(t) changes in time
- The **derivative of phase** (how fast φ(t) changes) corresponds to
  the **instantaneous frequency**

Intuition:

- The complex vector rotates in the IQ plane.
- The speed of rotation is the instantaneous frequency.
- FM audio is hidden in the way that rotation speed changes over time.

---

## 3. Visualising FM: spectrum and waterfall

If we tune to an FM broadcast station (with HackRF or a recording):

- In the **spectrum**, a wide bump appears (about 150–200 kHz wide).
- The **waterfall** shows a thick band that is always present, with some
  structure inside.

Because FM broadcast uses wide deviation and extra features (stereo,
RDS, etc.) the signal looks **wide** in frequency, not like a thin line.

So:

- Narrow, single carrier → thin line in spectrum  
- Wideband FM broadcast → fat “hill” in the spectrum

---

## 4. Basic idea of FM demodulation

In complex baseband, a simple FM demodulator can be built from phase.

Recall:

> s(t) = A(t) · e^{j·φ(t)}

If we ignore amplitude and focus on phase:

- The **instantaneous frequency** is proportional to **dφ(t)/dt**  
  (the time derivative of phase)
- So FM demodulation can be done by:
  1. Compute the phase of each sample
  2. Look at how the phase changes between neighbouring samples

one simple digital method:

1. Normalise the signal to unit magnitude:

   > s_norm(t) = s(t) / |s(t)|

   So we remove amplitude variations and keep only phase.

2. Multiply the current sample by the **conjugate** of the previous one:

   > z[n] = s_norm[n] · conj(s_norm[n−1])

3. The **angle** of z[n] gives the **phase difference**, which is
   proportional to instantaneous frequency, i.e. the FM audio.

Conceptually:

- `conj(s[n−1])` rotates the previous vector back to the real axis
- `s[n] · conj(s[n−1])` tells us how much rotation happened between
  sample n−1 and n
- That rotation is the FM information

---

## 5. Simple FM demodulation example (Python sketch)

Below is a simple *illustrative* example of wideband FM demodulation
from IQ. This is not tuned or filtered for real broadcast quality, but
it shows the core idea.

```python
import numpy as np

def fm_demod(iq):
    """
    Simple FM demodulator for complex64 IQ array.

    This assumes that `iq` is already centered on the FM station and
    that appropriate filtering/downsampling will be done around it.
    """
    # Remove amplitude variations (normalize to unit magnitude)
    iq = iq / (np.abs(iq) + 1e-9)

    # Multiply by conjugate of previous sample
    z = iq[1:] * np.conj(iq[:-1])

    # Angle of the result ~ instantaneous frequency
    audio = np.angle(z)

    return audio
