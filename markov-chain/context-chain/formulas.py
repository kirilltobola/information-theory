import math
import numpy as np 


def init(string: str, alphabet: str, k: int, p: dict, q: dict):
    n: int = len(alphabet)
    for i in range(len(string) - k):
        sub_word = string[i:i+k]
        p[sub_word] = dict()
        for symbol in alphabet:
            p[sub_word][symbol] = 1
        q[sub_word] = n
    return p, q


# def somefunc(word: str, alphabet: str, string: str, p: dict, q: dict):
#     res = 0
#     k = len(word)
#     for symbol in string:
#         if word in q:
#             p[word][symbol] += 1
#             q[word] += 1
#         else:
#             p[word] = dict()
#             for sym in alphabet:
#                 p[word][sym] = 1
#             q[word] = len(alphabet)

#         h = 0
#         for i in alphabet:
#             h += H(p[word][i] / q[word])
#         res += h

#         word = word[1:]
#         word += symbol
#     return res / len(word)


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

