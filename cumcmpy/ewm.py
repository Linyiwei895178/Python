import numpy as np
import pandas as pd

def entropy_weight_method(data, indicator_directions):
    """
    熵权法计算指标权重
    :param data: 原始数据矩阵 (m行 n列, m为样本数, n为指标数) (Numpy Array)
    :param indicator_directions: 指标方向列表, 1表示正向指标, -1表示负向指标
    :return: 各指标的权重向量
    """
    m, n = data.shape
    
    # 1. 数据标准化
    Y = np.zeros((m, n))
    for j in range(n):
        col_max = np.max(data[:, j])
        col_min = np.min(data[:, j])
        
        # 处理正向指标
        if indicator_directions[j] == 1:
            Y[:, j] = (data[:, j] - col_min) / (col_max - col_min)
        # 处理负向指标
        elif indicator_directions[j] == -1:
            Y[:, j] = (col_max - data[:, j]) / (col_max - col_min)
            
    # 为了防止后续计算 ln(0) 报错，给标准化后的矩阵加一个极小值
    Y = Y + 1e-4 
    
    # 2. 计算比重 P
    # np.sum(Y, axis=0) 表示按列求和
    P = Y / np.sum(Y, axis=0)
    
    # 3. 计算信息熵 E
    E = - (1 / np.log(m)) * np.sum(P * np.log(P), axis=0)
    
    # 4. 计算差异系数 D
    D = 1 - E
    
    # 5. 计算最终权重 W
    W = D / np.sum(D)
    
    return W

if __name__ == "__main__":
    print("=" * 50)
    print("熵权法 (EWM) 权重计算示例：智能手机评估")
    print("=" * 50)
    
    # 构建原始数据矩阵
    # 每一行代表一款手机(A, B, C, D)
    # 每一列代表一个指标: [续航时间, 手机价格, 机身重量]
    raw_data = np.array([
        [12, 3000, 180],
        [15, 4500, 210],
        [14, 3500, 190],
        [10, 2500, 170]
    ])
    
    # 定义指标方向: 1代表正向指标(越大越好), -1代表负向指标(越小越好)
    directions = [1, -1, -1] 
    
    # 调用函数计算权重
    weights = entropy_weight_method(raw_data, directions)
    
    # 使用 Pandas 格式化输出结果，方便阅读
    indicators = ["续航时间(正向)", "手机价格(负向)", "机身重量(负向)"]
    result_df = pd.DataFrame({
        "评价指标": indicators,
        "客观权重": [f"{w:.4f}" for w in weights],
        "百分比": [f"{w*100:.2f}%" for w in weights]
    })
    
    print("\n各指标的客观权重计算结果：")
    print(result_df.to_string(index=False))
    print("=" * 50)