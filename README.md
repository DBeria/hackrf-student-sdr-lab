# hackrf-student-sdr-lab

![Status](https://img.shields.io/badge/status-learning_in_progress-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Topic](https://img.shields.io/badge/topic-SDR_&_satellites-orange)

Student SDR & satellite lab with HackRF One – open learning project.

I am a student teaching myself software defined radio and satellite
reception. Using HackRF One and open source tools, I want to turn my
learning process into something other beginners can reuse. This repo
collects my notes, examples and tutorials step by step.

> I live in Tbilisi, Georgia, where SDR and HackRF are still almost
> unknown and there are very few local learning resources. With this
> project I want to create simple, practical examples and tutorials in
> **both English and Georgian**, so that students here can have an easier
> starting point than I did.

## Goals

- Understand the basics of SDR, sampling and modulation in a practical way.
- Receive and decode real-world signals that are legal to receive:
  - FM broadcast
  - ADS-B from aircraft
  - Weather satellites (NOAA / Meteor)
  - Amateur satellites and other interesting signals
- Turn “invisible” radio waves into something human and visual
  (images, graphs, audio).
- Publish simple, beginner-friendly guides and scripts that others can reuse.
- Gradually provide **bilingual material (English + Georgian)** so local
  learners don’t get blocked by language.

## Why this project matters (especially in Georgia)

- SDR and HackRF are not widely known in Georgia.
- There are almost no local workshops, clubs, or tutorials in Georgian.
- By documenting my progress in an open way, I hope to:
  - give other students a concrete place to start,
  - show that you can explore radio and satellites even without a big lab,
  - translate key explanations and tutorials into Georgian so that people
    who are not confident in English can still learn,
  - eventually inspire small local meetups or study groups.

## Current Status

I am just starting this project.

Right now this repo contains:

- Study notes and links I use to learn the basics (`docs/` and `notes/`)
- A learning plan and ideas for future workshops
- Plans for future HackRF One setups and antennas
- Example Python scripts for working with IQ recordings (`examples/`)

As soon as I have access to HackRF One, I will start adding:

- GNU Radio flowgraphs
- Example scripts for decoding different signals
- Step-by-step tutorials with screenshots
- Short explanations and summaries in **Georgian** alongside English

## Planned Experiments

1. **FM Broadcast** – basic tuning, filtering and demodulation.  
2. **ADS-B** – receive aircraft beacons and visualize nearby flights.  
3. **Weather Satellites** – record a pass and decode an image of the Earth.  
4. **Amateur Satellites** – listen to and decode amateur radio satellites
   where allowed.

## Tools

- HackRF One (planned main SDR)
- GNU Radio / GQRX / SDRangel (FOSS tools)
- Linux or Windows laptop

## Contributing

If you are also learning SDR and want to share ideas, corrections or better
examples, feel free to open an issue or pull request. This is a learning
project, so feedback is very welcome.

## License

- Code and scripts: **MIT License**  
- Text and tutorials: **CC BY-SA 4.0**
