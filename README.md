# CS183-T14-Project-Repository
### **Introduction:** The repository is the project of T14 of CS183, MIEC, with the theme of "AI in simulation".

Introduction:
# AI-Driven Solar Panel Production Line Optimization
This project demonstrates the integration of a Machine Learning (ML) model into an AnyLogic discrete-event simulation. By replacing static process logic with a dynamic, AI-driven inference engine (ONNX), we have transformed a traditional solar panel production line into a reactive Digital Twin.

## 🚀 Project Overview
The core of this simulation is a Solar Panel Production Line where panels undergo various stages, specifically focusing on the Trimming Station. We utilized an ONNX-based linear regression model to dynamically predict and control processing times based on real-time factory conditions.

## 🏗️ System Architecture
The project bridges the gap between Python-based AI development and Java-based industrial simulation:

**AI Training (Python)**: A model was trained using scikit-learn to learn the relationship between queue lengths, material types (evaType), and optimal processing times.

**Model Export (ONNX)**: The model was exported to the Open Neural Network Exchange (ONNX) format for cross-platform compatibility.

**Simulation (AnyLogic)**: The AnyLogic model acts as the physical environment, passing real-time parameters to the ONNX Runtime for sub-millisecond inference.
## Model Comparison: Original vs. AI-Enhanced

|Feature|Original Model (Static)|AI-Enhanced Model (Dynamic)|
| :--- | :----: | ---: |
|Logic Type|Rule-based / Static|Data-driven / Adaptive|
|Trimming Time|"Fixed (e.g., 60s) regardless of conditions."|Dynamically calculated via ONNX inference.|
|Material Sensitivity|Ignored or handled by simple if-else logic.|Deeply integrated via the evaType parameter.|
|Congestion Handling|No reaction to bottlenecks.|Adjusts processing speed based on currentQueueSize.|
|Decision Making|Pre-determined.|Predictive and optimized in real-time.|

# Advantages of AI Optimization in Simulation
## 1. Dynamic Adaptation to Material Variability
The model utilizes the evaType parameter (Standard, Fast, and Ultra-Fast cure EVA) to adjust station delays. Unlike static models, the AI understands the non-linear relationship between material properties and required processing effort, ensuring a more realistic representation of a smart factory.

## 2. Bottleneck Mitigation
By incorporating the currentQueueSize into the inference call, the trimming station can simulate "accelerated processing" or "adaptive pacing" when the production line is congested. This leads to a significant reduction in overall throughput variability.

## 3. Decoupled Logic & Future-Proofing
The use of the ONNX format allows the simulation logic to be completely decoupled from the AI algorithm. You can upgrade the underlying model from simple Linear Regression to a Deep Neural Network without changing a single line of Java code in AnyLogic.

## 4. High-Fidelity Digital Twin
This project moves beyond simple "animation" and creates a true Digital Twin loop:
Physical State (Data) → AI Inference (Decision) → Simulation Update (Action).

# Implementation Details
## Key Parameters
evaType: A global parameter in Main controlled by a slider (0, 1, or 2), representing different EVA film types.

predictProcessingTime(queueLength, type): The core Java function that communicates with the predict_time.onnx engine.

# Core Inference Logic

predictProcessingTime( currentQueueSize, evaType )  //currentQueueSize is set as 5 temporarily in v1.

## Experimental Results
Experimental runs showed a clear linear/non-linear response to the evaType slider:

**evaType 0:** ~55.9s (Standard)

**evaType 1:** ~37.1s (Fast Cure)

**evaType 2:** ~18.4s (Ultra Fast Cure)

# Credits
This project was developed as a group assignment for the AI-Simulation Integration module.

---
### Annotation:
**Folder "3d"**: The folder that contains dae files that shows the 3D models of Anylogic agents. e.g. forklift.dae store the model of forklifts. 
**File "contribution"**: The file shows the contributions that made by our team members.
**File "Solar Panel Production Line.alp"**: The file is the code we made that can be opened by anylogic.
---

**Original model source link:** https://cloud.anylogic.com/model/29d54a61-aaac-4c47-8e50-941c0f5bb36e?mode=SETTINGS
**Developer:** Anylogic

## CS183 T14 member
**Mentor:** Chris Roadknight
**Leader:** Boyu Huang
**Team Members:** Dongjing Yang, Jingxuan Huang, Zhichen Gan.


