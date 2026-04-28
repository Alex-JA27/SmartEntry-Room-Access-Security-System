# Dorm Room Guest Tracking System (Raspberry Pi Pico)

**Author:** Alex Alvarado  
**Course:** GE 1111 — Northeastern University  
**Role:** Hardware & Software Engineer

---

## Project Website

View the full project documentation here:

https://site-duplicator--folakebiaou2.replit.app/#overview

---

## Overview

This project implements a standalone embedded security and occupancy tracking system designed for shared dormitory environments. The system allows roommates to log their presence and guests using dedicated buttons while providing real-time visual feedback and storing timestamped data for later analysis.

Built using a Raspberry Pi Pico, the system improves accountability between roommates without relying on internet connectivity or institutional infrastructure.

---

## Problem Statement

Residential dorm rooms lack a lightweight and low-cost way to track guest entry and occupancy per roommate. The goal of this project was to design a standalone embedded system that improves accountability and security awareness while remaining simple, reliable, and fully independent from institutional systems.

---

## Approach & Solution

The system uses four roommate-specific push buttons connected to a Raspberry Pi Pico. Each button press logs entry events with timestamps and updates the display in real time.

An RGB LED strip provides immediate feedback:
- Green = valid entry accepted
- Red = rejected or unrecognized input

A 16×2 LCD display shows live system status including the last entry and current guest count.

MicroPython controls all embedded logic on the Pico, and MATLAB processes exported logs to generate hourly traffic and per-roommate frequency charts.

---

## Hardware Components

- Raspberry Pi Pico
- Breadboard circuit design
- 4 Push buttons (roommate inputs)
- RGB LED strip
- 16×2 LCD display

---

## Software & Technologies

- MicroPython
- MATLAB
- Embedded system circuit design
- LCD interface control

---

## System Features

### Real-Time Entry Tracking

Roommates log their presence and guests using assigned buttons. Each interaction is recorded with timestamps.

### LED Feedback System

Immediate visual confirmation of input status:
- Green LED confirms valid entry
- Red LED signals invalid input

### Live LCD Dashboard

Displays:
- System status ("System Active")
- Last entry recorded
- Current guest count

---

## Data Logging & Visualization

Entry data is exported and analyzed using MATLAB to generate:

- Per-hour guest traffic graphs
- Per-roommate entry frequency charts
- Occupancy trend analysis

This provides insight into usage patterns across roommates.

---

## Results & Impact

- Fully standalone embedded tracking system
- Runs entirely on a single Raspberry Pi Pico
- No internet or external infrastructure required
- Provides structured guest accountability
- Enables occupancy trend visualization using MATLAB
- Demonstrates a low-cost and scalable dorm security solution

---


## Future Improvements

Potential future upgrades include:

- SD card persistent storage
- Wireless monitoring dashboard
- Mobile notifications
- Enclosure housing design
- Multi-room expansion support


---

## Team Contributions

Work was divided based on each member’s primary focus area while maintaining collaboration across all system components.

**Alex**  
Primarily responsible for circuit design and implementation, as well as developing the MicroPython firmware using Thonny for the Raspberry Pi Pico.

**Jenna**  
Focused on data processing and visualization, including translating system output into MATLAB and managing the text file used for structured data storage.

**Folake**  
Responsible for designing and developing the project website to present system functionality, documentation, and results.

---

## Future Improvements

Potential future upgrades include:

- SD card persistent storage
- Wireless monitoring dashboard
- Mobile notifications
- Enclosure housing design
- Multi-room expansion support
