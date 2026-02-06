# Healio – Circadian Health Monitoring Agent

## Overview

Healio is a health monitoring application that analyzes long-term wearable health data and provides personalized lifestyle recommendations. The system uses a multi-agent architecture and integrates ScaleDown to efficiently compress health history while preserving important trends and anomalies.

This project focuses on circadian-aware insights by aligning sleep, activity, and nutrition recommendations with the user’s daily biological rhythm.

## Objectives

- Monitor health data from wearable devices (simulated)
- Analyze sleep, exercise, and nutrition patterns
- Maintain long-term health context using ScaleDown
- Provide personalized recommendations
- Track progress and detect health anomalies
- Generate health summaries for doctor visits

## System Workflow

1. Health data is collected from simulated wearable sources.
2. Daily data is processed and compressed using ScaleDown.
3. Specialized agents analyze the compressed data.
4. Personalized recommendations are generated.
5. Results are displayed through a dashboard and health summary.

## ScaleDown Integration

ScaleDown is used to compress 12 months of daily health data into summarized trends, achieving significant data reduction while retaining critical health patterns. This improves application performance and enables context-aware personalization with lower latency.

## Multi-Agent Design

### Sleep Agent
- Analyzes sleep duration and quality
- Identifies sleep inconsistencies
- Provides sleep improvement recommendations

### Exercise Agent
- Evaluates physical activity levels
- Suggests adaptive workout routines
- Aligns exercise timing with energy patterns

### Nutrition Agent
- Tracks calorie intake and meal timing
- Provides balanced meal suggestions
- Supports user-defined health goals

---

## Key Features

- Personalized health recommendations
- Circadian-aware lifestyle planning
- Progress tracking dashboard
- Health anomaly detection
- Doctor visit preparation summary

---

## Anomaly Detection

The system detects unusual health patterns such as sudden changes in activity levels, irregular sleep patterns, and abnormal heart rate trends. These anomalies are highlighted to help users take early action.

---

## Technology Stack

- Programming Language: Python
- Framework: Streamlit
- Data Processing: Pandas, NumPy
- Visualization: Streamlit Charts
- Data Source: Simulated wearable data

---

## Installation and Usage

```bash
git clone https://github.com/lahari3009/healio.git
cd healio
pip install -r requirements.txt
streamlit run app.py
