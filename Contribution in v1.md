//Member Huang Boyu
2026/4/30
Here is the plan for training an advanced model to replace the existing onnx file and expanding AI applications for V2:
Training and replacing the advanced trimming model:
**Add feature dimensions:** Beyond queue length and evaType, extract more continuous variables as input features.
Examples include the total number of cells (nCellsInRow multiplied by nCellsInColumn), the actual time spent in the previous edgeSealing process, or the current meanProdCycleTime.
**Upgrade the algorithm network:** In Python, replace basic linear regression with Random Forest, XGBoost, or a Deep Neural Network (MLPRegressor) with hidden layers. 
Fit the collected multi-dimensional feature data to capture complex non-linear production patterns.
**Export and replace seamlessly:** Export the new model to onnx format using the same code, and directly overwrite the old predict_time.onnx file in the project folder.
**Update interface calls:** In the Main agent of AnyLogic, locate the predictProcessingTime function and add parameters to match the new model's feature count.
Finally, pass these new real-time variables in order within the trimming station's delay time code.

Other production stages for AI integration:
**Laminator stage:** Current lamination time is a static parameter based on evaType. 
You can train a dynamic time prediction model to estimate the shortest lamination cycle time ensuring quality, based on current panel backlog, laminatorCapacity, and average flow rate of preceding stages.
**Quality testing stage (EL Tester / Solar Simulation):** Introduce a binary classification AI model. 
Predict the defect probability of a panel based on historical data like solderingTime and environment dwell time. 
If the defect probability is extremely low, the AI can dynamically reduce the exposure and testing time (elTesterExpositionTime) to clear bottlenecks.
**Robot predictive maintenance (LayupRobot / UnloadRobot):** The timeBetweenFailures for robots is currently a probability distribution. 
Use AI to analyze continuous run times, processed batches, and current queue pressure to dynamically predict the optimal next maintenance window, triggering downtime maintenance without impacting line flow.
Reference source：https://blog.csdn.net/pioneer_plus/article/details/131607502
                  https://blog.csdn.net/m0_68275685/article/details/154383034

//Member Gan Zhichen
2026/4/29
The comparison testing process was carried out according to the experimental plan.
The original unmodified model (fixed 60 seconds trimming time) was run first,
and the total simulation time required to process 100 battery panels or the final output rate of the production line was recorded.
Then the AI-upgraded version was run. In the upgraded version,
the evaType slider was adjusted to 0, 1, and 2 respectively,
and the total duration or output rate was recorded for each case.
After eliminating issues such as non-technical errors and insufficient raw materials,
a simple conclusion was drawn, for example:
"After introducing AI dynamic adjustment, the overall production line efficiency increased by XX% when processing ultra-fast curing materials."



//Member Huang Jingxuan
2026/4/29
To the Main agent's "On destroy" code block, be sure to add code to close the ONNX session and environment (e.g., ortSession.close(); ortEnv.close();).This effectively prevents memory leaks, which can avoid software crashes or lag
When loading the model, in addition to printing failure messages, you could add a boolean flag (e.g., isModelLoaded).If the model fails to load, the system can automatically fall back to using traditional fixed delays
Reference source: https://onnxruntime.ai/docs/api/java/ai/onnxruntime/OrtSession.html
                  https://blog.csdn.net/qq_38461344/article/details/135053898

2026/4/30
Instead of using default configurations when creating SessionOptions, leverage ONNX Runtime's built-in graph optimization levels to significantly boost inference speed.
Encapsulate a reloadModel(String modelPath) method. This allows the application to safely close the old session and load a new model without requiring a full application restart. 
Reference source: https://onnxruntime.ai/docs/performance/tune-performance.html
                  https://onnxruntime.ai/docs/performance/model-test.html



//Member Yang Dongjin
2026/4/28
The long-term testing process lasted until the entire model was completed for production.
The performance optimization and safety tests of the entire production line were carried out according to the actual industrial process.
After eliminating issues such as non-technical errors and insufficient raw materials, 
the following steps will be taken to complete the adaptation by integrating with ONNX based on a more refined set of requirements.
Reference source：https://www.sohu.com/a/871013007_121643760
                  https://www.whyoha.com/news/industry/266.html

2026/4/29
Quantify the actual sales volume and production output of solar photovoltaic panels in reality, to alleviate the computational burden for the next model expansion
Reference source：https://www.ceicdata.com/zh-hans/china/photovoltaic-capacity-and-production
