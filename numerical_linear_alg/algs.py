import numpy as np

def unstable_gram_QR(A):
    m,n = A.shape
    Q = np.zeros((m,n))
    R = np.zeros((n,n))
    for i in range(n):
        v = A[:, i]
        for j in range(0,i):
            R[j,i] = Q[:,j]@A[:,i]
            v -= R[j,i]*Q[:,j]
        R[i,i] = np.linalg.norm(v)
        Q[:,i] = v/R[i,i]
    return Q,R

def stable_gram_QR(A):
    m,n = A.shape
    Q = np.zeros((m,n))
    R = np.zeros((n,n))
    for i in range(n):
        R[i,i] = np.linalg.norm(A[:,i])
        Q[:,i] = A[:, i]/R[i,i]
        for j in range(i,n):
            R[i,j] = A[:, i]/R[i,i].T@A[:,j]
            A[:,j] = A[:,j]-R[i,j]*Q[:,i]
    return Q,R

def householder_QR(A):
    # First find R
    m,n = A.shape
    Q = np.eye(m)
    for i in range(n):
        x = A[i:,i]
        e1 = np.zeros_like(x)
        e1[0] = 1
        v = x+ np.sign(x[0])*np.linalg.norm(x)*e1
        v = v/np.linalg.norm(v)
        A[i:, i:] -= 2 * np.outer(v, v @ A[i:, i:])
        Q[:, i:] -= 2 * np.outer(Q[:, i:] @ v, v)
    return Q,A

A = np.array([[1.,2],[3,5]])
Q, R = householder_QR(A)
print(Q@R)
