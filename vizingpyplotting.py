import networkx as nx
import matplotlib.pyplot as plt

def coloracao_arestas_vizing(G):
    grau_maximo = max(dict(G.degree()).values())
    cores_disponiveis = range(grau_maximo + 1)
    cor_aresta = {}

    def encontrar_cor_disponivel(aresta, cores_usadas):
        for cor in cores_disponiveis:
            if cor not in cores_usadas:
                return cor
        return None

    def obter_cores_usadas(no):
        return {cor_aresta[aresta] for aresta in G.edges(no) if aresta in cor_aresta}

    def colorir_aresta(aresta):
        u, v = aresta
        cores_usadas_u = obter_cores_usadas(u)
        cores_usadas_v = obter_cores_usadas(v)
        cores_usadas = cores_usadas_u.union(cores_usadas_v)
        cor = encontrar_cor_disponivel(aresta, cores_usadas)
        cor_aresta[aresta] = cor
        cor_aresta[(v, u)] = cor  # O grafo é não direcionado, então colore (u,v) e (v,u) da mesma forma

    for aresta in G.edges():
        colorir_aresta(aresta)

    return cor_aresta

def desenhar_grafo_colorido(G, cores_arestas):
    pos = nx.spring_layout(G)
    cores = [cores_arestas[aresta] for aresta in G.edges()]
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=cores, edge_cmap=plt.cm.rainbow)
    plt.show()

# Exemplo de uso
G = nx.cycle_graph(3)  # Cria um grafo ciclo com a quantidade de vértices informada
cores_arestas = coloracao_arestas_vizing(G)
desenhar_grafo_colorido(G, cores_arestas)
