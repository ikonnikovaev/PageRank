import numpy as np
import numpy.linalg as la

def print_matrix(M):
    from io import StringIO
    s = StringIO()
    np.savetxt(s, M, fmt="%.3f")
    print(s.getvalue().strip())

N_PATS = 100
eps = 0.01

L = np.array([
    [0,   1/2, 1/3, 0, 0,   0],
    [1/3, 0,   0,   0, 1/2, 0],
    [1/3, 1/2, 0,   1, 0,   1/2],
    [1/3, 0,   1/3, 0, 1/2, 1/2],
    [0,   0,   0,   0, 0,   0],
    [0,   0,   1/3, 0, 0,   0]
])

L2 = np.array([
    [0,   1/2, 1/3, 0, 0,   0,   0],
    [1/3, 0,   0,   0, 1/2, 0,   0],
    [1/3, 1/2, 0,   1, 0,   1/3, 0],
    [1/3, 0,   1/3, 0, 1/2, 1/3, 0],
    [0,   0,   0,   0, 0,   0,   0],
    [0,   0,   1/3, 0, 0,   0,   0],
    [0,   0,   0,   0, 0,   1/3, 1]
])


print_matrix(L2)
print()

n_sites = L2.shape[0]
r_prev = N_PATS * np.ones(n_sites) / n_sites
r_next = L2 @ r_prev
while la.norm(r_prev - r_next) > eps:
    r_prev = r_next
    r_next = L2 @ r_prev
print_matrix(r_next)
print()

d = 0.5
J = np.ones(L2.shape)
#print_matrix(L2)
c = (1 - d) / n_sites
#print(c)
M = d * L2 + c * J
#print_matrix(M)
#print()

r_prev = N_PATS * np.ones(n_sites) / n_sites
r_next = M @ r_prev
while la.norm(r_prev - r_next) > eps:
    r_prev = r_next
    r_next = M @ r_prev
print_matrix(r_next)

