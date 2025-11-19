# hackrf-student-sdr-lab

Student SDR & satellite lab with HackRF One – open learning project.

I am a student teaching myself software defined radio and satellite
reception. Using HackRF One and open source tools, I want to turn my
learning process into something other beginners can reuse. This repo
collects my notes, examples and tutorials step by step.

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

## Current Status

I am just starting this project.

Right now this repo contains:

- Study notes and links I use to learn the basics (`docs/` and `notes/`)
- A learning plan and ideas for future workshops
- Plans for future HackRF One setups and antennas

As soon as I have access to HackRF One, I will start adding:

- GNU Radio flowgraphs
- Example scripts for decoding different signals
- Step-by-step tutorials with screenshots

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

