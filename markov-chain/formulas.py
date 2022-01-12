import math
import numpy as np


def H(h_i: list, q_i: list) -> float:
    res = 0
    n = len(h_i)
    
    for i in range(n):
        res += q_i[i] * h_i[i]
    
    return res


def Hi(arr: list) -> list:
    res = list()
    n, m = len(arr), len(arr[0])
    
    for i in range(n):
        res.append(0)
        for j in range(m):
            p_ij = arr[i][j]
            if p_ij:
                res[i] += p_ij * math.log2(p_ij)
        res[i] *= -1
    return res


def get_Q(P: np.array) -> np.array:
    row_size = len(P[0])
    
    P_trans = np.transpose(P)
    P_trans[np.diag_indices_from(P_trans)] -= 1
    P_trans[0] = np.ones(row_size)
    
    right = np.zeros(row_size)
    right[0] = 1
    
    return np.linalg.solve(P_trans, right)
    