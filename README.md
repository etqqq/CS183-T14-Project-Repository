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

### Annotation:

**Folder "3d"** : The folder that contains dae files that shows the 3D models of Anylogic agents. e.g. forklift.dae store the model of forklifts. 
**File "contribution"**: The file shows the contributions that made by our team members.
**File "Solar Panel Production Line.alp"**: The file is the code we made that can be opened by anylogic.

### 🤖 Model Artifact Declarations

> 💡 **System Note:** The tracking blocks below specifically declare the core serialized machine learning models running within our Digital Twin engine. Declarations and specifications for all other functional code logic, execution dependencies, and utility helper files can be viewed directly within their respective source code files or standard inline documentation blocks.

"""
File: lstm_buffer.onnx
Responsible team member: Zhichen Gan
Description: An ONNX-exported Long Short-Term Memory (LSTM) network model utilized by the predictCongestion function to ingest real-time queue length data and evaluate active buffer station congestion probability.
"""

"""
File: lstm_model.keras
Responsible team member: Zhichen Gan
Description: The native native Keras model training checkpoint architecture that handles continuous factory-floor queue sequences before compilation and cross-platform open-format export to the deployment runtime.
"""

"""
File: predict_qc.onnx
Responsible team member: Dongjin Yang
Description: A quality control model driven by the predictQuality function that ingests evaType and processingTime features to instantly distinguish compliant panel outputs from defective units.
"""

"""
File: predict_time.onnx
Responsible team member: Boyu Huang
Description: The baseline Version 1 Linear Regression model utilized by the legacy predictTrimmingTime function to compute material-based machine operational intervals (succeeded by the enhanced Version 2 DNN architecture).
"""

"""
File: predict_time_dnn.onnx
Responsible team member: Boyu Huang
Description: The advanced Version 2 Deep Neural Network (DNN) model embedded within the advancedPredictTrimmingTime function, utilizing ONNX acceleration to inject highly adaptive process time predictions into the physical lamination block.
"""

"""
File: robot_policy.onnx
Responsible team member: Jingxuan Huang
Description: A Deep Q-Network (DQN) policy model evaluated via the predictRobotPolicy function, trained over continuous avoidance learning loops to guide sorting arms and transport automated guided vehicles (AGVs) on optimal dynamic paths.
"""

"""
File: robot_policy.onnx.data
Responsible team member: Jingxuan Huang
Description: The underlying binary weights tensor resource and network parameters companion file directly linked to initialize the active DQN reinforcement learning routing execution space.
"""

"""
Directory: /image_assets/01_data_generation
Responsible team member: Boyu Huang
Description: Contains telemetry logs and factory-floor data collection screenshots capturing the correlation between physical conveyor queue sizes and EVA material state features.
"""

"""
Directory: /image_assets/02_model_training
Responsible team member: Boyu Huang
Description: Holds training loss curves, evaluation hyperparameter metrics, and scikit-learn/PyTorch execution session logs leading to the compilation of the 'predict_time_dnn.onnx' architecture.
"""

"""
Directory: /image_assets/03_embedding_new_model_in_alp
Responsible team member: Boyu Huang
Description: Stores step-by-step IDE and AnyLogic interface screenshots verifying the structural deprecation of legacy variables and the clean wrapper integration of the advancedPredictTrimmingTime function.
"""

"""
Directory: /image_assets/04_testing
Responsible team member: Boyu Huang
Description: Documents active system testing, zero-lag latency verifications (validating the ~0.036ms response metric), and concurrent steady-state throughput evaluation milestones within the V2 environment.
"""

"""
Directory: /image_assets/05_former_model
Responsible team member: Boyu Huang
Description: Archival collection preserving the baseline Version 1 setup, highlighting the single-point Linear Regression mapping limits and structural context of 'predict_time.onnx' for regression delta auditing.
"""

### 📦 External Core Dependencies (.JAR Frameworks)

> 💡 **Dependency Note:** The baseline execution environment requires the Java Archive (.jar) stubs declared below to initialize the underlying cross-platform inference pipelines. These libraries serve as the foundational bridges mapping the Java-based AnyLogic discrete-event loop into the C++ compiled ONNX Runtime environment[cite: 5, 6].

"""
File: onnxruntime-1.15.1.jar
Responsible team member: Team T14 (System Integration)
Description: The official ONNX Runtime Java API deployment engine package required by all sub-agents to load native compiled neural network sessions and drive execution loops within the AnyLogic runtime layer[cite: 5, 6].
"""

"""
File: OnnxHelperLibrary.jar
Responsible team member: Team T14 (System Integration)
Description: A specialized helper bridge utility framework responsible for handling multi-dimensional primitive array conversions and formatting raw simulation state inputs into compatible tensors required by the ONNX engine, preventing structural dimension mismatches[cite: 5].
"""

---
**Original model source link:** https://cloud.anylogic.com/model/29d54a61-aaac-4c47-8e50-941c0f5bb36e?mode=SETTINGS
**Developer:** Anylogic

## CS183 T14 member
**Mentor:** Chris Roadknight
**Leader:** Boyu Huang
**Team Members:** Dongjing Yang, Jingxuan Huang, Zhichen Gan.
