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

# Core Inference Logic of V1

predictProcessingTime( currentQueueSize, evaType )  //currentQueueSize is set as 5 temporarily in v1.

## Experimental Results
Experimental runs showed a clear linear/non-linear response to the evaType slider:

**evaType 0:** ~55.9s (Standard)

**evaType 1:** ~37.1s (Fast Cure)

**evaType 2:** ~18.4s (Ultra Fast Cure)

## Credits
This project was developed as a group assignment for the AI-Simulation Integration module.

## V2: Multi-Agent AI Architecture & Decoupled Digital Twin
In the Version 2 release, the simulation transitions from a single-point static prediction model to a fully adaptive, multi-agent digital twin. We integrated four heterogeneous AI models into the AnyLogic physical execution layer via the ONNX Runtime Java API, establishing a robust Event-driven Closed-loop Feedback Workflow.

### 🧠 Core AI Modules
**1. Dynamic Process Time Prediction (DNN Model)**

Role: Trimming Station Optimization

Mechanism: Replaces the static 60-second processing time. It dynamically calculates the optimal trimming time by tensorizing real-time physical states, specifically the current queue length (queueLength) and the EVA material type (evaType).

**2. Temporal Congestion Alerting (LSTM Model)**

Role: Conveyor Buffer Management

Mechanism: Utilizes a Temporal Sliding-Window Tensor to evaluate historical and current flow rates. It provides real-time congestion probability alerts, allowing the production line to foresee bottlenecks before they occur.

**3. Automated Quality Control (QC Classification Model)**

Role: Defect Probability Evaluation

Mechanism: Extracts cross-sectional physical features of individual solar panels (e.g., historical soldering time and environmental dwell time) to perform real-time binary classification, determining whether a panel meets the quality threshold.

4. Intelligent Routing Decisions (DQN Model)

Role: Robotic Arm & Path Dispatching

Mechanism: Formulates the routing logic as a Markov Decision Process (MDP). It analyzes global production line snapshots to output discrete action policies, autonomously dispatching materials to the most efficient operational paths.

🛡️ Engineering Robustness
All cross-environment communications between the Java-based simulation and the C++-based ONNX engine are strictly encapsulated. A comprehensive try-catch fallback mechanism is implemented to ensure zero simulation deadlocks, seamlessly degrading to safe default parameters during unexpected inference timeouts.
---
# V2: Multi-Agent AI Architecture & Decoupled Digital Twin

In the Version 2 release, the simulation transitions from a single-point static prediction model to a fully adaptive, multi-agent digital twin. We integrated four heterogeneous AI models into the AnyLogic physical execution layer via the ONNX Runtime Java API, establishing a robust Event-driven Closed-loop Feedback Workflow.

## 🧠 Core AI Modules & Implementation Details

### 1. Dynamic Process Time Prediction (DNN Model)
* **Role:** Trimming Station Optimization
* **Mechanism:** Replaces the rigid static processing time. By tracking the real-time buffer queue length before the laminator and the current material type (`evaType`), the AI dynamically predicts and adjusts the trimming processing time. This effectively prevents deadlocks caused by backlog in the laminating and cooling stages, ensuring optimal material flow efficiency under varying loads.

### 2. Proactive Congestion Control (LSTM Model)
* **Role:** Conveyor Buffer Management
* **Mechanism:** Utilizing the `predictCongestion` function, the LSTM model predicts the congestion probability of the buffer zone. Instead of passive reactions, it enables proactive defense: if a high congestion risk is predicted, a `testEvent` is instantly triggered.
* **Dynamic Equilibrium Action:** The system automatically intervenes by temporarily increasing the Layup station capacity (e.g., to 2), decreasing the batch size (e.g., to 3), and compressing the `flippingStation` processing time (e.g., to 6s). Standard parameters are restored once the congestion is cleared.

### 3. Automated Quality Control (QC Classification Model)
* **Role:** Defect Probability Evaluation
* **Mechanism:** The `predictQuality` function loads `predict_qc.onnx` to perform binary classification. It extracts specific physical features, combining `evaType` and actual processing time (`procetime`), to infer whether a product is qualified (returns `true`) or defective (returns `false`).
* **Fail-Safe Design:** It features a high-robustness fallback. If the AI environment fails to load or encounters dimensional errors, it defaults to returning `true`, guaranteeing zero unexpected downtime for the production line.

### 4. Intelligent Routing Decisions (DQN Model)
* **Role:** Robotic Arm & Transport Dispatching
* **Mechanism:** The `predictRobotPolicy` function utilizes a DQN model (`robot_policy.onnx`) trained through rigorous avoidance learning tests. It takes a global `double[] features` array to output the optimal expected routing. This ensures that robotic arms can smoothly sort solar panels while carts efficiently transport stacked finished products.
* **Resource Management:** Specific logic is implemented in Main's startup and destroy codes to securely load the model and strictly release underlying resources (GPU VRAM/CPU memory) occupied by the inference engine upon termination.
---

#### Annotation:
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


