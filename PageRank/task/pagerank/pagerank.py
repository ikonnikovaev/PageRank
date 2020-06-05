import numpy as np
import numpy.linalg as la

def read_matrix(n):
    M = np.zeros((n, n))
    for r in range(n):
        row = np.fromstring(input(), sep=' ')
        M[r][:] = row
    return M


def print_matrix(M):
    from io import StringIO
    s = StringIO()
    np.savetxt(s, M, fmt="%.3f")
    print(s.getvalue().strip())

def pagerank(link_matrix,d):
    N_PATS = 100
    eps = 0.01
    n_sites = link_matrix.shape[0]
    J = np.ones(link_matrix.shape)
    c = (1 - d) / n_sites
    M = d * link_matrix + c * J
    r_prev = N_PATS * np.ones(n_sites) / n_sites
    r_next = M @ r_prev
    while la.norm(r_prev - r_next) > eps:
        r_prev = r_next
        r_next = M @ r_prev
    return r_next



n = int(input())
sites = input().split()
L = read_matrix(n)
d = 0.5

# print_matrix(pagerank(L, d))
pr = np.ndarray.flatten(pagerank(L, d))


query = input()
top = min(n, 5)
for i in range(n):
    if sites[i] == query:
        top -= 1
        pr[i] = 0
        print(query)

sites_and_ranks = list(zip(sites, list(pr)))
sites_and_ranks.sort(key=lambda x: x[1])
sites_and_ranks.reverse()
#print(sites_and_ranks)
for i in range(top):
    print(sites_and_ranks[i][0])



