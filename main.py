import numpy as np
from sklearn.linear_model import LogisticRegression # 这次我们用逻辑回归（做分类选择题）
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# 1. 准备模拟数据 [evaType, 修边耗时]
# 逻辑：修边时间过短（太仓促）或过长（机器卡顿），不合格(0)的概率大。时间适中，合格(1)概率大。
X = np.array([
    [0, 55], [0, 56], [0, 10], [0, 100],  # 类别0的各种耗时
    [1, 37], [1, 38], [1, 5],  [1, 80],   # 类别1的各种耗时
    [2, 18], [2, 19], [2, 2],  [2, 60]    # 类别2的各种耗时
], dtype=np.float32)

# 对应的合格标签 (1为合格，0为不合格)
y = np.array([1, 1, 0, 0,
              1, 1, 0, 0,
              1, 1, 0, 0], dtype=np.int64)

# 2. 训练分类模型
model = LogisticRegression()
model.fit(X, y)

# 3. 转换为 ONNX 并兼容 AnyLogic 引擎 (版本8)
initial_type = [('input', FloatTensorType([None, 2]))]
onnx_model = convert_sklearn(model, initial_types=initial_type, target_opset=15)
onnx_model.ir_version = 8

# 4. 保存模型
with open("predict_qc.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("AI 质检分类模型 (predict_qc.onnx) 生成成功！")
