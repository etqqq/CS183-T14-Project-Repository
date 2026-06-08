# Responsible Team Member: Dongjin Yang
# Description: The Python file to train QC model
import numpy as np
from sklearn.linear_model import LogisticRegression # Using logistic regression (for classification)
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# 1. Prepare mock data [evaType, trimming_time]
# Logic: If trimming time is too short (rushed) or too long (machine lag), the probability of failing (0) is high. If the time is moderate, the probability of passing (1) is high.
X = np.array([
    [0, 55], [0, 56], [0, 10], [0, 100],  # Various time durations for category 0
    [1, 37], [1, 38], [1, 5],  [1, 80],   # Various time durations for category 1
    [2, 18], [2, 19], [2, 2],  [2, 60]    # Various time durations for category 2
], dtype=np.float32)

# Corresponding quality labels (1 for pass, 0 for fail)
y = np.array([1, 1, 0, 0,
              1, 1, 0, 0,
              1, 1, 0, 0], dtype=np.int64)

# 2. Train the classification model
model = LogisticRegression()
model.fit(X, y)

# 3. Convert to ONNX and ensure compatibility with the AnyLogic engine (version 8)
initial_type = [('input', FloatTensorType([None, 2]))]
onnx_model = convert_sklearn(model, initial_types=initial_type, target_opset=15)
onnx_model.ir_version = 8

# 4. Save the model
with open("predict_qc.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("AI QC classification model (predict_qc.onnx) generated successfully!")
