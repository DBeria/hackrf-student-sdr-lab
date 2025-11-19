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
> both English and Georgian, so that students here can have an easier
> starting point than I did.

## Table of Contents

- [Goals](#goals)
- [Why this project matters (especially in Georgia)](#why-this-project-matters-especially-in-georgia)
- [Current Status](#current-status)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Planned Experiments](#planned-experiments)
- [Tools](#tools)
- [Contributing](#contributing)
- [License](#license)

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
- Gradually provide bilingual material (English + Georgian) so local
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
- A learning plan, roadmap, and ideas for future workshops
- Plans for future HackRF One setups and antennas
- Example Python scripts for working with IQ recordings (`examples/`)

As soon as I have access to HackRF One, I will start adding:

- GNU Radio flowgraphs
- Example scripts for decoding different signals
- Step-by-step tutorials with screenshots
- Short explanations and summaries in Georgian alongside English

## Repository Structure

A quick overview of the main folders in this project:

- `docs/` – learning plan, roadmap, HackRF study notes and experiment ideas  
- `notes/` – external links and references I use while learning SDR and satellites  
- `examples/` – small Python scripts for generating and analysing IQ recordings  
- `images/` (planned) – screenshots of spectra, waterfalls, and satellite experiments

## Quick Start

These scripts are designed to work with any complex64 IQ recordings,
so they can be used even before I have HackRF One.

Clone the repository and install the basic Python dependencies:

```bash
git clone https://github.com/DBeria/hackrf-student-sdr-lab.git
cd hackrf-student-sdr-lab
pip install -r requirements.txt
