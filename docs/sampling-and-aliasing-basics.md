# Sampling Rate and Aliasing – Beginner Notes

These are my beginner notes on how sampling rate, bandwidth, and aliasing
work in SDR. The goal is to understand how to choose a good sample rate,
what can go wrong, and how this affects HackRF experiments.

---

## 1. What is sampling?

In SDR, the analog RF signal is converted to digital by taking samples:

> sample, sample, sample, sample, …

The **sampling rate** (Fs) tells us how many samples per second we take.

Examples:

- Fs = 1 000 000 samples/second (1 MS/s)
- Fs = 2 000 000 samples/second (2 MS/s)
- Fs = 10 000 000 samples/second (10 MS/s)

Each sample is a complex value: I + jQ.

---

## 2. Nyquist: how fast do we need to sample?

The basic rule:

> To represent a signal correctly, we need  
> **Fs ≥ 2 × B**

where **B** is the signal bandwidth.

This is called the **Nyquist criterion**.

Examples:

- If a signal has bandwidth ~100 kHz → Fs should be at least 200 kS/s.  
- If a signal has bandwidth ~2 MHz → Fs should be at least 4 MS/s.

In practice, we often choose a sample rate a bit higher than 2×B to make
filtering easier and to have some guard space.

---

## 3. What is aliasing?

If we sample **too slowly**, different frequencies start to “fold” on top
of each other and look the same in the digital world. This is called
**aliasing**.

Analogy:

- Imagine a spinning wheel recorded with a low frame-rate camera.
- Sometimes the wheel looks like it is spinning slowly backwards.
- The camera is **aliasing** the true motion into something that looks
  different.

In SDR:

- Frequencies above **Fs/2** “fold” back into the [−Fs/2, +Fs/2] range.  
- As a result, a high-frequency signal can appear in the wrong place in
  the spectrum plot.

Mathematically, the spectrum repeats every Fs Hz. The SDR only shows one
“copy” of that spectrum, in the baseband window.

---

## 4. Baseband bandwidth and centre frequency

When using an SDR (like HackRF), we choose:

1. A **centre frequency** (F_center) – where we tune in the RF spectrum.  
2. A **sample rate** (Fs) – how wide our baseband window is.

The baseband bandwidth is roughly:

> from −Fs/2 to +Fs/2 around 0 Hz

If we tune HackRF to F_center, then:

- the **absolute RF range** we “see” is roughly:

> [F_center − Fs/2, F_center + Fs/2]

Anything outside that range in the real world either:

- is not captured, or
- may alias back into the window if there isn’t enough filtering.

So:

- Higher Fs → **wider window** of spectrum, more bandwidth visible.  
- Lower Fs → **narrower window**, less spectrum, but less data to process.

---

## 5. Why filtering before decimation matters

Often we want to **reduce** the sample rate after capturing, for example:

- start at Fs = 10 MS/s
- then reduce (decimate) to Fs = 1 MS/s to make processing easier

We cannot just “throw away samples” without thinking.

Steps:

1. **Low-pass filter** the signal to keep only the part we care about.  
2. Then **decimate** (keep one every N samples).

If we skip the low-pass filter, higher-frequency content will **alias** into
the smaller bandwidth after decimation.

Rule:

> Filter first so that the signal fits into the new [−Fs_new/2, +Fs_new/2] range,  
> then decimate.

---

## 6. Choosing a sample rate in practice

For HackRF experiments, some typical choices:

- **Narrow signal (~100 kHz)**  
  e.g. narrow FM, some digital modes  
  → Fs on the order of 500 kS/s to 1 MS/s is usually enough.

- **FM broadcast (~200 kHz, plus guard)**  
  → Fs = 1–2 MS/s is common.

- **ADS-B at 1090 MHz**  
  The RF pulse structure is quite fast, so people often use Fs in the
  2–4 MS/s range (or more), then decimate after filtering.

Trade-offs:

- Higher Fs:
  - + see more bandwidth  
  - + capture fast details  
  - − larger files, more CPU

- Lower Fs:
  - + easier to process  
  - − less bandwidth, risk of aliasing if set too low

---

## 7. How this connects to my example scripts

In this project, I often use:

> Fs = 2 000 000 (2 MS/s)

For `generate_test_tone.py` and the test plots:

- choosing Fs = 2 MS/s gives a baseband range of about:
  -1 MHz to +1 MHz.

If I place two test tones inside that range, they appear as two peaks in
the spectrum plot.

Experiments I want to try with this knowledge (once I have more time):

- Generate a tone close to Fs/2 and see how it behaves.  
- Intentionally generate a tone above Fs/2 and see how it aliases.  
- Capture a real signal at a too-low Fs and compare the spectrum to the
  same signal captured at a higher Fs.

These experiments should make aliasing feel more “real” instead of just
being a formula.

---

## 8. Summary

- Sampling rate (Fs) is how many samples per second we take.  
- Nyquist says Fs should be at least **2× the signal bandwidth**.  
- If Fs is too low, different frequencies **alias** and appear in the
  wrong place.  
- In SDR, we tune a centre frequency and capture a baseband window of
  roughly [F_center − Fs/2, F_center + Fs/2].  
- When reducing sample rate, we must **filter first, then decimate**.  
- Understanding these ideas helps choose good sample rates and avoid
  confusing results when plotting spectra and waterfalls.

These notes are written for myself as I learn, and will guide how I choose
sample rates and design future experiments with HackRF One.
