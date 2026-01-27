# 🧠 Bio-Inspired Low-Light Motion Perception System (Vibe coding)
*(Inspired by Canine Vision)*

## Overview
Humans struggle to perceive weak motion signals in low-light environments.
This project explores a **bio-inspired, real-time perception pipeline**
that adapts visual processing based on ambient brightness.

The system is inspired by canine vision, particularly how dogs detect
motion at night that often goes unnoticed by humans.Also figure out reason behind dogs howling at night.

This is an **engineering approximation**, not a biological replica.


## Problem Statement
In low illumination:
 Human vision loses motion sensitivity
 Camera noise increases
 Weak but real motion signals are missed.
 
Assumptions:

Also dogs don't bite everyone.There is a        reason behind it.Nobody hurts someone     without a reason.So maybe we could figure out the reason behind dog attacks if we can simulate properly.Probably a highly radio active compound can answer lots of questions(which is not poison) .


**Goal:** Build a real-time system that amplifies weak motion cues while
remaining computationally efficient and explainable.



## System Overview

Camera → Brightness Estimation → Day / Night Pipeline → Display + Metrics

Mode switching uses hysteresis to avoid flicker.



## Vision Modes

### Day Mode
 Blue & yellow color emphasis
 Red/green suppression
 Moderate motion enhancement

### Night Mode
 Grayscale (rod-dominant vision)
 Light amplification
 Edge + strong motion sensitivity
 Noise suppression



## Evaluation
The system logs:
 Brightness
 Motion intensity
 Perception mode
 FPS

Logs are stored as CSV for offline analysis.



## Limitations
 Camera sensor limits low-light fidelity
 No infrared input
 No biological neural processing



## Run Instructions


pip install -r requirements.txt
python src/unified_dog_vision.py

## Has used AI coding assistant for the project

##Disclaimer

This project is for educational and exploratory research only
No supernatural claims have been made

