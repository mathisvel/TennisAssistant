# TennisAssistant: Edge AI Stroke Analyzer

TennisAssistant is an ongoing computer vision project aimed at analyzing tennis mechanics in real-time. The ultimate goal is to deploy this as an iOS application leveraging on-device Machine Learning (CoreML/Vision) to provide immediate feedback to players without network latency.

## Project Roadmap
- [x] ** 1: Proof of Concept (Python/OpenCV)** - Basic video reading and object isolation.
- [ ] ** 2: Advanced Tracking** - Implementing YOLOv8 or MediaPipe to track the ball, the racket, and the player's posture.
- [ ] ** 3: Biomechanical Analysis** - Calculating racket head speed, impact zone (sweet spot), and stroke type (topspin, flat, slice).
- [ ] ** 4: iOS / Swift Port** - Converting the trained models to `.mlmodelc` and building the SwiftUI camera interface.

## Current Tech Stack
- **Python 3.x**
- **OpenCV** (Image processing and color-space tracking)
- **NumPy** (Matrix operations and mask filtering)

