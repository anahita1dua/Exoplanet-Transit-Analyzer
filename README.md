# Exoplanet Transit Detector

A Python-based tool for detecting and analyzing exoplanet transits from astronomical light curve data. The project identifies periodic brightness dips caused by planets passing in front of their host stars and estimates key planetary parameters.

## Features

- Automatic light curve processing
- Transit event detection
- Transit depth calculation
- Orbital period estimation
- Planet radius estimation
- Data visualization using plots
- Supports real astronomical datasets from the Lightkurve package

## How It Works

1. Loads stellar light curve data.
2. Removes invalid data points and performs basic preprocessing.
3. Detects significant brightness dips (potential transit events).
4. Groups consecutive transit points into individual transit events.
5. Calculates:
   - Transit Depth
   - Orbital Period
   - Estimated Planet Radius
6. Displays results and visualizations.

## Requirements

- Python
- NumPy
- Matplotlib
- Lightkurve

## Scientific Background

When an exoplanet passes between its host star and an observer, it blocks a small fraction of the star's light. This temporary decrease in brightness is called a transit.

The transit depth is approximately:

Depth ≈ (Rp / Rs)²

where:

- Rp = Planet Radius
- Rs = Stellar Radius

Using the measured transit depth, the planet's radius can be estimated.

## About
This project was created as a part of my journey of learning Python and exploring the intersection of programming and astronomical research. Feedback and suggestions are always welcome!

If you find this project interesting, consider giving it a star!!
