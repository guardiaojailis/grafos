MAXN = 10  # Tamanho máximo do grafo + 1 (para indexação)

C = [[0] * MAXN for _ in range(MAXN)]
G = [[0] * MAXN for _ in range(MAXN)]
X = [0] * MAXN
a = 0

def clear(N):
    global C, G
    for i in range(N+1):
        for j in range(N+1):
            C[i][j] = G[i][j] = 0

def update(u):
    global X, C
    X[u] = 1
    while C[u][X[u]]:
        X[u] += 1

def color(u, v, c):
    global G, C, X
    p = G[u][v]
    G[u][v] = c
    G[v][u] = c
    C[u][c] = v
    C[v][c] = u
    C[u][p] = 0
    C[v][p] = 0
    if p:
        X[u] = X[v] = p
    else:
        update(u)
        update(v)
    return p

def flip(u, c1, c2):
    global G, C, X
    p = C[u][c1]
    C[u][c1], C[u][c2] = C[u][c2], C[u][c1]
    if p:
        G[u][p] = c2
        G[p][u] = c2
    if not C[u][c1]:
        X[u] = c1
    if not C[u][c2]:
        X[u] = c2
    return p

def solve(E, N, M):
    global X
    for i in range(1, N+1):
        X[i] = 1
    for t in range(len(E)):
        u, v0 = E[t]
        v, c0, c = v0, X[u], X[u]
        d = 0
        L = []
        vst = [0] * MAXN
        while not G[u][v0]:
            L.append((v, X[v]))
            d = X[v]
            if not C[v][c]:
                for a in range(len(L)-1, -1, -1):
                    c = color(u, L[a][0], c)
            elif not C[u][d]:
                for a in range(len(L)-1, -1, -1):
                    color(u, L[a][0], L[a][1])
            elif vst[d]:
                break
            else:
                vst[d] = 1
                v = C[u][d]
        if not G[u][v0]:
            while v:
                v = flip(v, c, d)
                c, d = d, c
            if C[u][c0]:
                for a in range(len(L)-2, -1, -1):
                    if L[a][1] == c:
                        break
                for a in range(a, -1, -1):
                    color(u, L[a][0], L[a][1])
            else:
                t -= 1

def main():
    edges = [(1, 2), (1, 3), (1, 4), (1, 6), (1, 7), (1, 8),
             (2, 3), (2, 5), (2, 6), (2, 8), (2, 9),
             (3, 4), (3, 5), (3, 7), (3, 9),
             (4, 5), (4, 6), (4, 8), (4, 9),
             (5, 6), (5, 7), (5, 8),
             (6, 7), (6, 9),
             (7, 8), (7, 9),
             (8, 9)]

    N = 9
    M = 54  # Número de vértices e arestas

    clear(N)
    solve(edges, N, M)

    # Imprimir cores das arestas
    for edge in edges:
        i, j = edge
        print(f"Aresta ({i}, {j}) colorida com cor {G[i][j]}")

if __name__ == "__main__":
    main()
