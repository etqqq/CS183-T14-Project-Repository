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
Reference source:Scikit-learn.org. (2010). sklearn.neural_network.MLPRegressor — scikit-learn 0.21.3 documentation. [online] Available at: https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html.
                 Liu, C., Zhu, H., Tang, D., Nie, Q., Zhou, T., Wang, L. and Song, Y. (2022). Probing an intelligent predictive maintenance approach with deep learning and augmented reality for machine tools in IoT-enabled manufacturing. Robotics and Computer-Integrated Manufacturing, 77, p.102357. doi:https://doi.org/10.1016/j.rcim.2022.102357.
                 Rana, N. and Arora, S. (2021). A Review on Surface Defect Detection of Solar Cells Using Machine Learning. Algorithms for Intelligent Systems, pp.385–395. doi:https://doi.org/10.1007/978-981-16-1048-6_29.

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
Reference source: Onnxruntime.ai. (2026b). OrtSession (onnxruntime API). [online] Available at: https://onnxruntime.ai/docs/api/java/ai/onnxruntime/OrtSession.html [Accessed 4 Jun. 2026].

2026/4/30
Instead of using default configurations when creating SessionOptions, leverage ONNX Runtime's built-in graph optimization levels to significantly boost inference speed.
Encapsulate a reloadModel(String modelPath) method. This allows the application to safely close the old session and load a new model without requiring a full application restart. 
Reference source: Onnxruntime.ai. (2026a). ONNX Runtime Performance Tuning. [online] Available at: https://onnxruntime.ai/docs/performance/tune-performance.html [Accessed 4 Jun. 2026].


//Member Yang Dongjin
2026/4/28
The long-term testing process lasted until the entire model was completed for production.
The performance optimization and safety tests of the entire production line were carried out according to the actual industrial process.
After eliminating issues such as non-technical errors and insufficient raw materials, 
the following steps will be taken to complete the adaptation by integrating with ONNX based on a more refined set of requirements.
Reference source：Anylogic.help. (2026). External Java classes | AnyLogic Help. [online] Available at: https://anylogic.help/advanced/libraries/adding-external-jar-files-and-java-classes.html [Accessed 4 Jun. 2026].
                  Microsoft / Linux Foundation. (2026). ONNX Runtime: Cross-platform, high performance ML inferencing and training accelerator. [online] Available at: https://onnxruntime.ai/docs/ [Accessed: 28 Apr. 2026].

2026/4/29
Quantify the actual sales volume and production output of solar photovoltaic panels in reality, to alleviate the computational burden for the next model expansion
Reference source：IEA (2022). Solar PV Global Supply Chains – Analysis. [online] IEA. Available at: https://www.iea.org/reports/solar-pv-global-supply-chains.
                  

                  
                  
