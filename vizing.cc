#include <bits/stdc++.h>
//#include <iostream>
//#include <vector>
//#include <utility>

using namespace std;

const int MAXN = 10; // Tamanho máximo do grafo + 1 (para indexação)

int C[MAXN][MAXN], G[MAXN][MAXN];
int X[MAXN] = {}, a;

void clear(int N){
    for(int i=0; i<=N; i++){
        for(int j=0; j<=N; j++) C[i][j] = G[i][j] = 0;
    }
}

void update(int u){
    for(X[u] = 1; C[u][X[u]]; X[u]++);
}

int color(int u, int v, int c){
    int p = G[u][v];
    G[u][v] = c;
    G[v][u] = c;
    C[u][c] = v;
    C[v][c] = u;
    C[u][p] = 0;
    C[v][p] = 0;
    if(p){
        X[u] = X[v] = p;
    }else{
        update(u);
        update(v);
    }
    return p; 
}

int flip(int u, int c1, int c2){
    int p = C[u][c1];
    swap(C[u][c1], C[u][c2]);
    if(p){
        G[u][p] = c2;
        G[p][u] = c2;
    }
    if(!C[u][c1]){
        X[u] = c1;
    }
    if(!C[u][c2]){
        X[u] = c2;
    }
    return p; 
}

void solve(vector<pair<int,int>> &E, int N, int M){
    for(int i = 1; i <= N; i++){
        X[i] = 1;
    }
    for(int t = 0; t < E.size(); t++){
        int u = E[t].first, v0 = E[t].second, v = v0, c0 = X[u], c = c0, d;
        vector<pair<int,int>> L;
        int vst[MAXN] = {};
        while(!G[u][v0]){
            L.emplace_back(v, d = X[v]);
            if(!C[v][c]){
                for(a = (int)L.size()-1; a >= 0; a--){
                    c = color(u, L[a].first, c);
                }
            }
            else if(!C[u][d]){
                for(a=(int)L.size()-1;a>=0;a--){
                    color(u,L[a].first,L[a].second);
                }
            }
            else if( vst[d] ){
                break;
            }
            else{
                vst[d] = 1;
                v = C[u][d];
            }
        }
        if(!G[u][v0]){
            for(;v; v = flip(v, c, d), swap(c, d));
            if(C[u][c0]){
                for(a = (int)L.size()-2; a >= 0 && L[a].second != c; a--);
                for(; a >= 0; a--){
                    color(u, L[a].first, L[a].second);
                }
            }else{
                t--;
            }
        }
    }
}

int main() {
    vector<pair<int,int>> edges = {{1, 2}, {1, 3}, {1, 4}, {1, 6}, {1, 7}, {1, 8},
                                   {2, 3}, {2, 5}, {2, 6}, {2, 8}, {2, 9}, 
                                   {3, 4}, {3, 5}, {3, 7}, {3, 9},
                                   {4, 5}, {4, 6}, {4, 8}, {4, 9},
                                   {5, 6}, {5, 7}, {5, 8},
                                   {6, 7}, {6, 9},
                                   {7, 8}, {7, 9},
                                   {8, 9}};
/*                                   {2, 1}, {3, 1}, {4, 1}, {6, 1}, {7, 1}, {8, 1},
                                   {3, 2}, {5, 2}, {6, 2}, {8, 2}, {9, 2}, 
                                   {4, 3}, {5, 3}, {7, 3}, {9, 3},
                                   {5, 4}, {6, 4}, {8, 4}, {9, 4},
                                   {6, 5}, {7, 5}, {8, 5},
                                   {7, 6}, {9, 6},
                                   {8, 7}, {9, 7},
                                   {9, 8}};*/
                                   
    int N = 9, M = 54; // Número de vértices e arestas

    clear(N);
    solve(edges, N, M);

    // Imprimir cores das arestas
    for(auto edge : edges){
        int i = edge.first, j = edge.second;
        cout << "Aresta (" << i << ", " << j << ") colorida com cor " << G[i][j] << endl;
    }

    return 0;
}
