import numpy as np

def multi_level_fuzzy_evaluation():
    print("=" * 50)
    print("二级模糊综合评价：远程服务器体验评估")
    print("=" * 50)
    
    # ==========================================
    # 第一步：底层（二级指标）模糊综合评价
    # ==========================================
    
    # 1. 评估 U1 (网络连通性体验)
    # 权重 W1：假设我们极其看重本地 Clash 代理的连通性，权重分配为 [0.3, 0.7]
    W1 = np.array([0.3, 0.7])
    # 评价矩阵 R1：(基于专家或用户打分得出的隶属度)
    R1 = np.array([
        [0.2, 0.4, 0.3, 0.1],  # u11: 基础直连延迟打分
        [0.6, 0.3, 0.1, 0.0]   # u12: 本地 Clash 代理表现打分
    ])
    # 计算 U1 的评价结果 B1
    B1 = np.dot(W1, R1)
    print(f"-> U1(网络连通性) 评价结果 B1: {B1}")
    
    
    # 2. 评估 U2 (开发环境体验)
    # 权重 W2：假设 VS Code SSH 和 终端编辑器同等重要，权重分配为 [0.5, 0.5]
    W2 = np.array([0.5, 0.5])
    # 评价矩阵 R2
    R2 = np.array([
        [0.5, 0.4, 0.1, 0.0],  # u21: VS Code SSH 稳定性
        [0.7, 0.2, 0.1, 0.0]   # u22: LazyVim 运行流畅度
    ])
    # 计算 U2 的评价结果 B2
    B2 = np.dot(W2, R2)
    print(f"-> U2(开发环境)   评价结果 B2: {B2}")
    
    # ==========================================
    # 第二步：高层（一级指标）模糊综合评价
    # ==========================================
    
    # 1. 构造高层评价矩阵 R_total (直接将 B1 和 B2 堆叠起来)
    R_total = np.vstack((B1, B2))
    print("\n高层综合评价矩阵 R_total:")
    print(R_total)
    
    # 2. 定义一级指标权重 W_total
    # 假设整体来看，开发环境(0.6)比纯粹的网络连通性(0.4)稍重要
    W_total = np.array([0.4, 0.6])
    
    # 3. 计算最终综合结果 B_final
    B_final = np.dot(W_total, R_total)
    
    print("-" * 50)
    print(f"最终综合评价向量 B_final: {B_final}")
    
    # 4. 结论判定 (最大隶属度原则)
    eval_levels = ["优秀", "良好", "一般", "较差"]
    max_index = np.argmax(B_final)
    
    print(f"最大隶属度为: {B_final[max_index]:.4f}")
    print(f"结论: 该远程服务器的综合体验评级为【{eval_levels[max_index]}】")
    print("=" * 50)

if __name__ == "__main__":
    multi_level_fuzzy_evaluation()