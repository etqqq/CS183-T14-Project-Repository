# 🎬 CS183 Year 1 Group Project: Technical Explainer Video

This directory contains the required technical video submission and metadata for **Group T14**. This deliverable establishes the rigorous empirical evidence and engineering reflection comparing the structural evolution of our simulation model[cite: 5, 6].

## 📌 Video Metadata
* **Project Name:** AI in Simulation[cite: 4]
* **Target Use Case:** Solar Panel Manufacturing Production Line[cite: 4]
* **Core Paradigm:** Dual-Layer Decoupled Architecture (Java-based Physical Execution Layer ⇄ ONNX Runtime/C++ AI Decision Layer via JNI Wrapper Functions)[cite: 4]

---

## 👥 Team T14 Production Credits

This technical explainer video is a joint deliverable produced by Group T14, balancing macro-timeline orchestration, visual asset engineering, and strict architectural standardization:

* **Boyu Huang (Lead Video Editor):** Orchestrated the primary video timeline assembly, managed non-linear rendering, executed spatial keyframing for UI close-ups, and recorded the technical audio voiceover.
* **Zhichen Gan (Visual Asset Designer):** Conceptualized and engineered the comprehensive presentation slide framework, formulated the multi-agent architectural layouts, and designed the step-by-step vector loop animations within the presentation engine to visualize the closed-loop feedback logic.
* **[Member 3 Name] (Core System Engineer):** Spearheaded the V2 multi-agent codebase integration, trained the underlying intelligent components, and managed JNI wrapper performance.
* **[Member 4 Name] (Standardization & QA):** Managed repository restructuring to fulfill directory guidelines, conducted reproducible model execution tests, and finalized artifact optimization.

---

## 🛠️ System Interface Specification (Input & Output Framework)

To fulfill the rigorous evaluation criteria for project explanation, the video formally maps out the systemic boundaries and data pipelines driving our Digital Twin[cite: 5]:

## 🛠️ Distributed Multi-Agent Telemetry & Control Matrix (I/O Specification)

To explicitly demonstrate the precise engineering contributions of all four team members, the system interface is architected as a decoupled, multi-stream telemetry pipeline. Real-time state-space variables from the AnyLogic physical execution engine are concurrently ingested by four specialized AI models, which synchronously compute and return proactive control actions.

### 📊 System Input Matrix (Telemetry Ingestion: Physical ➔ AI Layer)
Physical state parameters are continuously tracked within the discrete-event loop and routed into dedicated sub-agent pipelines via custom JNI Wrapper functions:

1. **`queueLength` (Temporal Buffer Congestion Vector) ──► Consumed by [DNN Agent] & [LSTM Agent]**
   * Real-time monitoring of raw accumulation sizes across the three conveyors near the lamination block (`bufferBeforeLaminator`). It provides sequence and load contexts for predictive line throttling.
2. **`evaType` (Discrete Material Classification Feature) ──► Consumed by [DNN Agent] & [QC Agent]**
   * A global categorizer representing physical material properties (0: Standard, 1: Fast, 2: Ultra-Fast Curing). It serves as a primary feature weight for cycle regression and testing filter setups.
3. **`processingTime` (Historical Execution Runtime Record) ──► Consumed by [QC Agent]**
   * The actual elapsed processing duration captured directly from the upstream trimming station, used as a key continuous feature vector for quality compliance sorting.
4. **`features[]` (Multi-Dimensional System Observation Array) ──► Consumed by [DQN Agent]**
   * A serialized, continuous double array compiling active factory-floor state variables into a comprehensive observation tensor for deep reinforcement learning tracking.

---

### ⚡ System Output Matrix (Actuation Dispatched: AI ➔ Physical Layer)
The distributed AI Decision Layer synthesizes the multi-stream telemetry via independent ONNX inference runtimes, returning actionable variables to override legacy rigid delays:

1. **`advancedPredictTrimmingTime()` ──► Inferred by [DNN Trimming Agent] (Boyu Huang's Work)**
   * **Required Asset:** `predict_time_dnn.onnx`
   * **Actuation Action:** Evaluates material types and active queue lines to dynamically override static trimming station delays with sub-millisecond process adjustments, balancing downstream flow.
2. **`predictCongestion()` ──► Inferred by [LSTM Bottleneck Agent] (Gan Zhichen's Work)**
   * **Required Asset:** `lstm_buffer.onnx`
   * **Actuation Action:** Computes continuous buffer saturation probabilities ($0.0 \sim 1.0$). If risk metrics cross the critical threshold ($> 0.48$), it autonomously triggers proactive mitigation protocols: spikes layup robot capacity to 2, cuts batch size to 3, and tightens flipping station duration to 6 seconds.
3. **`predictRobotPolicy()` ──► Inferred by [DQN Robotic Routing Agent] (Jingxuan Huang's Work)**
   * **Required Asset:** `robot.policy.onnx`
   * **Actuation Action:** Processes spatial state observations to dispatch discrete optimization actions (0, 1, or 2), guiding material-handling robots along adaptive trajectories to maximize throughput and clear bottleneck zones.
4. **`predictQuality()` ──► Inferred by [QC Testing Agent] (Yang Dongjin's Work)**
   * **Required Asset:** `qc_model.onnx`
   * **Actuation Action:** Evaluates current panels against learned material parameters, outputting a clear binary compliance flag (`true` for qualified, `false` for defective). Features an embedded high-robustness fail-safe that defaults to `true` on exceptions to protect the physical line from sudden shutdowns.

---

## 📋 Standardized Video Architecture

The submitted `final_video.mp4` strictly adheres to the 6-stage required structural timeline to guarantee absolute assessment compliance[cite: 5, 6]:

1. **The Hook (10–20s):** Introduces the fundamental bottlenecks plaguing static control logic within traditional manufacturing simulations[cite: 5].
2. **Project Overview (20–30s):** Formally states the project name, core purpose, target case study, and system-wide input/output variables[cite: 6].
3. **Version 1 Explanation (30–60s):** Deconstructs our baseline implementation, detailing the naive transition to single-point linear regression and its structural limitations[cite: 4, 5, 6].
4. **Version 2 Explanation (30–60s):** Explains the expanded 4-agent ecosystem (DNN, LSTM, QC, DQN) and visualizes the event-driven decoupling mechanics[cite: 4, 5, 6].
5. **Comparison Segment (15–30s):** Directly compares both iterations using structured empirical evidence, focusing heavily on throughput optimization and ultra-low inference latency[cite: 5].
6. **Results & Reflection (15–30s):** Concludes with a macro takeaway of what worked, an honest assessment of our evaluation runtime constraints, and a clear trajectory for future routing optimization[cite: 4, 5].

---

## 🗂️ Project Artifact Directory

```text
/project-video
  ├── final_video.mp4             <-- Polished presentation MP4 (Voiceover & Audio Tracking Included)
  ├── README.md                   <-- This file (Credits, Metadata, & Core I/O Specs)
  └── /evidence                   <-- Standardized Empirical Evidence Assets
       ├── /screenshots           <-- Multi-Agent UI Overlays & Decoupled Architecture States
       ├── /diagrams              <-- Dual-Layer JNI Framework & Component Flowcharts
       └── /metrics               <-- Throughput Logs & Microsecond Latency Measurements