import numpy as np

def ahp_method(matrix):
    """
    层次分析法 (AHP) 权重计算与一致性检验
    :param matrix: 输入的判断矩阵 (Numpy array)
    """
    n = matrix.shape[0]
    
    # 1. 计算矩阵的特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    # 2. 提取最大特征值及其对应的特征向量
    # 注意：特征值可能是复数，但在正反交矩阵中最大特征值一定是实数，直接取实部
    max_eigenvalue = np.max(np.real(eigenvalues))
    max_index = np.argmax(np.real(eigenvalues))
    principal_eigenvector = np.real(eigenvectors[:, max_index])
    
    # 3. 将特征向量归一化，得到权重向量 W
    weights = principal_eigenvector / np.sum(principal_eigenvector)
    
    # 4. 一致性检验
    CI = (max_eigenvalue - n) / (n - 1)
    
    # 标准 RI 查表 (1到9阶)
    RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    RI = RI_dict.get(n, 1.49) # 超过9阶近似处理
    
    CR = CI / RI if RI != 0 else 0
    
    # 5. 打印结果
    print("=" * 40)
    print("层次分析法 (AHP) 计算结果")
    print("-" * 40)
    print(f"最大特征值 (lambda_max): {max_eigenvalue:.4f}")
    print(f"计算得到的权重向量 W: {[round(w, 4) for w in weights]}")
    print(f"一致性指标 CI: {CI:.4f}")
    print(f"一致性比率 CR: {CR:.4f}")
    
    if CR < 0.1:
        print("\n结论: CR < 0.1，判断矩阵通过一致性检验，权重有效！")
    else:
        print("\n结论: CR >= 0.1，判断矩阵未通过检验，请重新调整指标比较尺度！")
    print("=" * 40)

if __name__ == "__main__":
    # 输入我们在例子中构造的 4x4 判断矩阵
    A = np.array([
        [1,   1/2, 2,   3],
        [2,   1,   2,   4],
        [1/2, 1/2, 1,   2],
        [1/3, 1/4, 1/2, 1]
    ])
    
    ahp_method(A)