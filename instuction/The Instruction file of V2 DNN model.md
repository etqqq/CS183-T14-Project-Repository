# The Instruction File of My Branch "refactor/advanced-AI-model-replace"
## By Member Boyu Huang

## 1.Executive Summary 
Based on v1 which embeded a basic linear regression model, I embeded a DNN (Deep Neural Networks) model in the "trimming" station of the Anylogic model "Solar Panel Production Line" to fulfil better effect to predict trimming time of Solar Panel Production, and record initial testing data including advanced trimming time predicted by the new model and former trimming time predicted by the old linear regression model.

## 2.Background
In the initial Anylogic model (creator: Anylogic official), their is a station named as **Trimming** which controls the process of the edge trimming or cleaning steps after the battery panel are cut, and its process time is a double parameter named as "trimmingTime", and its value is locked at 60. \
**Drawback:** Fixed time fails to reflect the dynamic nature of a real factory. In actual production, machine speed often fluctuates based on the operator's pace, material properties, or upstream congestion.

![01_original_alp](image_assets\05_former_model\01_original_alp.png)

To introduce adaptability, a linear regression model was previously embedded using the formula: Time = Base - (Queue * 1.5) - (Material * 18). This allowed the station to "speed up" when the queue was long.
**Drawback:**The linear model lacks "boundary awareness." Since it is a simple straight-line equation, it continues to decrease indefinitely as input values increase. Under extreme conditions—such as a queue of 15 panels and high-speed material(Actually the biggest queue length isn't usually larger than 12) —the model predicts a **negative** processing time. Additionally, it assumes the impacts of queueSize and evaType are completely independent and additive, ignoring potential complex interactions between material properties and operator stress.

![01_original_alp](image_assets\05_former_model\01_original_alp.png)

The transition to a Deep Neural Network (MLPRegressor) is required to capture the non-linear "saturation" behavior of the machine and to enforce physical constraints, ensuring the simulation remains stable while maintaining high predictive accuracy under all stress conditions.

![02_alp_embedding_linear_regression](image_assets\05_former_model\02_alp_embedding_linear_regression.png)

## 3. Development Workflow
### 3.1 Data preparation
In the early stages of model training, instead of collecting running data from the physical simulation, a script was written to instantly generate 100,000 rows of synthetic data using a mathematical formula with added noise. This "Data Synthesis" approach was not a shortcut, but a deliberate engineering decision based on three core reasons:


**I. Overcoming Software Limitations (Cold Start Problem)**
The AnyLogic Personal Learning Edition restricts Material Handling models to 5 simulated hours, yielding merely ~60 rows of data per run. Training a robust Neural Network requires massive datasets. By using a programmatic for-loop script at model startup, we bypassed the physics engine and generated 100,000 data points in under a second, successfully overcoming the "Cold Start" data scarcity.


**II. Forcing Edge Case Coverage (Data Augmentation)**
In a well-optimized simulation, extreme congestion (e.g., 15 panels in the queue) rarely occurs naturally. If the AI is only trained on "normal" data (queues of 0-2), it will fail unpredictably when a rare breakdown causes a massive queue. By forcing the queue length using uniform_discr(0, 15), we artificially injected extreme stress cases into the training set, forcing the AI to learn how to handle severe bottlenecks.

**III. Establishing a Verifiable Benchmark**
By synthesizing data using a known formula with a hard physical limit (Math.max(5.0, ...)), we established an absolute "Ground Truth." This allowed us to explicitly test whether the DNN architecture (128, 64 layers) was capable of learning non-linear boundary conditions before deploying it into the unpredictable dynamics of the real production line.

![01_textfile](image_assets/01_data_generation/01_textfile.png)
![02_textfileProperties](image_assets/01_data_generation/02_textfileProperties.png)
The text file that record 100,000 synthetic data and input these data in the form of a csv file.

![03_input_CSV_headers](image_assets/01_data_generation/03_input_CSV_headers.png)
![04_main_action1](image_assets/01_data_generation/04_main_action1.png)
![05_main_action2](image_assets/01_data_generation/05_main_action2.png)
Codes to record 100,000 fake data.

![06_csv_data](image_assets/01_data_generation/06_csv_data.png)
A part of fake data.

### 3.1 Model training

![01_training_model_py](image_assets/02_model_training/01_training_model_py.png)
The Python file used for training the deep neural network model.

### 3.1 Model embedding
The result of DNN model training is **"predict_time_dnn.onnx"** replacing old linear regression model "predict_time.onnx“。

![01_main](image_assets/03_embedding_new_model_in_alp/01_main.png)
Code for loading the new ONNX model in agent Main

![03_position_of_counter](image_assets/03_embedding_new_model_in_alp/03_position_of_counter.png)
![02_position_on_conveyor](image_assets/03_embedding_new_model_in_alp/02_position_on_conveyor.png)
3 positions on conveyor to calculate current queue length (serving as 3 counters). When an solar panel pass one of these positions, the queue length adds 1. the queue length will minus 1 just after an solar panel enters trimming station.

## 4. Initial Test
![03_simulation_interface](image_assets/04_testing/03_simulation_interface.png)
The running interface of alp file after embedding new DNN model.

To verify the simulation results, I record 2 csv file for reference when initial test:

**20260511_dnn_v1_inference_log.csv**: Logging the running data of the new DNN model. 
**20260511_sim_test_dnn_vs_linear.csv**: While logging the runtime data of the new DNN model, the output of the previous linear regression model was also recorded simultaneously as a comparative baseline. 

![01_test_data_recording_code_in_main](image_assets/04_testing/01_test_data_recording_code_in_main.png)
![02_test_data_recording_code_in_trimming](image_assets/04_testing/02_test_data_recording_code_in_trimming.png)
The relevant code used to record the running results of the DNN and the previous linear regression model.

![04_test_data](image_assets/04_testing/04_test_data.png)
![05_test_data_2](image_assets/04_testing/05_test_data_2.png)
The logging result of running.

## 5. Conclusion
In summary, this branch completes the architectural upgrade of the Trimming station from a rigid linear formula to a dynamic Deep Learning model. It not only resolves the critical bug of negative processing time but also establishes a robust data logging mechanism (Shadow Testing), laying a solid foundation for the future intelligentization of the entire production line.

