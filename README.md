🦺 Edge AI Worker Safety Detection System

A Real-time PPE compliance monitoring using YOLOv8 on edge hardware — built to prevent workplace accidents before they happen.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Edge AI](https://img.shields.io/badge/Edge-AI%20Inference-FF6F00?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

# Overview :-
This project implements an end-to-end computer vision pipeline for automated worker safety monitoring in industrial environments. It detects Personal Protective Equipment (PPE) compliance in real time — identifying whether workers are wearing helmets, vests, and other required safety gear — and triggers an audible alarm when violations are detected.
Designed for deployment on edge devices, the system runs inference locally without requiring cloud connectivity, making it suitable for factories, construction sites, and warehouses.

# Key Features :-

1) Real-time PPE detection using a custom-trained YOLOv8 model
2) Audio alarm system that triggers instantly on safety violations
3) Edge-optimized inference — runs on CPU/GPU without internet dependency
4) Custom dataset curated and annotated for industrial safety scenarios
5) Google Colab training notebook for easy model retraining and experimentation
6) Modular codebase — separate scripts for training and inference

| Component            |   Technology           |
|----------------------|------------------------|
| Object Detection     | YOLOv8 (Ultralytics)   |
| Training Environment | Google Colab (GPU)     |
| Inference            | Python + OpenCV        |
| Audio Alert          | Pygame / playsound     |
| Dataset Format       | YOLO annotation format |
| Language             | Python 3.11            |

# Project Structure :-

```
Edge-AI-worker-Safety/
│
├── colab/                  # Google Colab training notebooks
├── dataset/                # Annotated training dataset (images + labels)
│
├── train.py                # Model training script
├── detect.py               # Real-time inference & alarm script
├── best.pt                 # Pre-trained YOLOv8 model weights
├── Alarm 2.mp3             # Audio alert triggered on PPE violation
└── requirements.txt        # Python dependencies
```

# Getting Started Prerequisites :-
1) Python 3.8+
2) pip
3)Webcam or video source (for live detection)

Installations:-

# Clone the repository
```bash
git clone https://github.com/Abdeali-Badri/Edge-AI-worker-Safety.git
```
```bash
cd Edge-AI-worker-Safety
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Run Real-Time Detection :-
```bash
python train.py
```
Or open the notebook in `colab/` and run it on Google Colab for GPU-accelerated training.

# How It Works :-

1) Data Collection & Annotation — A custom dataset of industrial workers was assembled and annotated with bounding boxes for safety gear classes (helmet, vest, etc.)
2) Model Training — YOLOv8 was fine-tuned on the dataset using transfer learning via Google Colab
3) Inference Pipeline — detect.py captures live video frames, runs the model, and evaluates per-frame detections
4) Alarm Trigger — When a worker is detected without required PPE, an audio alarm fires immediately

# Model :-
The included `best.pt/` file contains the trained YOLOv8 weights — the best checkpoint saved during training based on validation performance. You can swap this with a retrained model by running `detect.py/` with your own dataset.

# Use Cases :-

1) Factory floor compliance monitoring
2) Construction site PPE enforcement
3) Warehouse safety auditing
4) Any environment requiring real-time safety gear verification

# Future Improvements

1) Multi-camera support
2) Dashboard with violation logging and timestamps
3) Raspberry Pi / Jetson Nano deployment optimization
4) SMS/email alert integration
5) Extended PPE classes (gloves, goggles, masks)




## Author :-

**Abdeali Badri**
[github.com/Abdeali-Badri](https://github.com/Abdeali-Badri)

