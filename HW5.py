import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def Barabasi_Albert_Model(n, m=4, intermediate_stp=None):
    internal_networks = []
    G = nx.complete_graph(m + 1)
    for t in range(m + 1, n):

        #sum_k_i = 2 * G.number_of_edges() #for 5.1
        #probs = np.array(list(float(G.degree(i)) / sum_k_i for i in range(t))) #for 5.1
        candidate_nodes = list(range(t))
        new_edges = []
        for i in range(m):
            #u = np.random.choice(candidate_nodes, p=probs) #for 5.1
            u = np.random.choice(candidate_nodes)

            new_edges.append((t, u))
            #probs = np.delete(probs, candidate_nodes.index(u)) #for 5.1
            candidate_nodes.remove(u)
            #probs /= sum(probs) #for 5.1

        G.add_node(t)
        G.add_edges_from(new_edges)

        if intermediate_stp:
            if t + 1 in intermediate_stp:
                internal_networks.append(G.copy())

    if intermediate_stp:
        return G, internal_networks
    return G

def deg_distribution(degrees):
    dmax = max(degrees)
    deg_dist = np.zeros([dmax+1,])
    for d in degrees:
        deg_dist[d] += 1
    return deg_dist

def line_fitting(G, m, ax=None):
    degrees = [d for n, d in G.degree()]
    dmax = max(degrees)
    deg_dist = np.zeros([dmax+1,]) 
    for n, d in G.degree():
        deg_dist[d] += 1
    y = deg_dist[m:]
    x = np.arange(m, len(deg_dist))
    
    to_remove = []
    for i in range(m, len(deg_dist)-m): 
        if y[i] == 0:
            to_remove.append(i)
    x = np.delete(x, to_remove)
    y = np.delete(y, to_remove)
    
    
    x = x[3:-int(np.floor(len(x)/2))]
    y = y[3:-int(np.floor(len(y)/2))]


    logX = np.log10(x)
    logY = np.log10(y)
    a, b = np.polyfit(logX, logY, 1)
    x_0, x_i = m, dmax
    y_0 = 10**b * x_0**a
    y_i = 10**b * x_i**a

    ax.loglog(deg_dist, 'ro', alpha=.5)
    ax.loglog([x_0, x_i], [y_0, y_i], linestyle='dotted', color='k', linewidth=3, alpha=.75)
    ax.set_ylabel("degree")
    ax.set_xlabel("rank")

    return ax

def main():
    N = 10**4
    m0 = 4
    intermediate_stp=[100, 1000, 5000, N]
    G, internal_G = Barabasi_Albert_Model(n=N, m=m0, intermediate_stp=intermediate_stp)

    #(a)

    internal_degdists = {}
    for Graph in internal_G:
        dis_g = deg_distribution(list(d for n,d in Graph.degree()))
        internal_degdists['N=' + str(Graph.number_of_nodes())] = dis_g / sum(dis_g)

    #(b)

    fig, axs = plt.subplots(2, 2, figsize=(30, 20))
    axs = axs.ravel()

    for i, dic in zip(range(len(internal_degdists)), internal_degdists.items()):
        k, degDist = dic
        axs[i].loglog(degDist,'ro', alpha=.6)
        axs[i].set_title(k)
        axs[i].set_xlabel('$k$')
        axs[i].set_ylabel('$p(k)$')

    plt.show()


    fig, axs = plt.subplots(2,2,figsize=(30, 20))
    axs = axs.ravel()

    for i, dic in zip(range(len(internal_degdists)), internal_degdists.items()):
        k, degDist = dic
        line_fitting(internal_G[i], m0, axs[i])
        axs[i].set_title(k)
        axs[i].set_xlabel('$k$')
        axs[i].set_ylabel('$p(k)$')

    plt.show()

    #(c)

    fig, axs = plt.subplots(2,2,figsize=(30, 20))
    axs = axs.ravel()

    for i, dic in zip(range(len(internal_degdists)), internal_degdists.items()):
        k, degDist = dic
        CMF = list(sum(degDist[:j]) for j in range(len(degDist)))
        axs[i].loglog(CMF,'ro', alpha=.6)
        axs[i].set_title(k)
        axs[i].set_xlabel('$k$')
        axs[i].set_ylabel('$p(k)$')

    plt.show()

    #(d)

    lcc = []
    k = []

    nn = np.round(m0*np.arange(1, 100)**1.70268).astype(int)

    for i in nn:
        k_G = G.subgraph(range(i))
        lcc.append(nx.average_clustering(k_G))
        k.append(i)

    print('Clustering Coefficient for N=100 is:',lcc[6])
    print('Clustering Coefficient for N=1000 is:', lcc[25])
    print('Clustering Coefficient for N=10000 is:',lcc[-1])

    plt.figure(figsize=(30,10))
    plt.loglog(k, lcc, 'ko', alpha=.5)
    plt.loglog(k, lcc, 'r')
    plt.ylabel('$Clustering Coefficient$')
    plt.xlabel('$N$')
    plt.title('The Clustering Coefficient Plot')
    plt.legend(['The Clustering Coefficient for $m={}$'.format(m0)])
    plt.show()

    #(e)

    w_nodes = [np.random.randint(m0),] + intermediate_stp[:-1]
    w_degs = np.zeros( (len(w_nodes), N) )

    for i in range(m0+1, G.number_of_nodes()):
        tmp_G = G.subgraph(range(i))

        for j in range(w_degs.shape[0]):
            if w_nodes[j] < i:
                w_degs[j, i] = tmp_G.degree(w_nodes[j])
            else:
                break


    plt.figure(figsize=(30,15))
    legend = []
    for i in range(len(w_nodes)):
        plt.loglog(w_degs[i,:])
        legend.append('Node: {}'.format(w_nodes[i]))

    plt.ylabel('$k$')
    plt.xlabel('$t$')
    plt.title('Degree Dynamics Plot')
    plt.legend(legend)
    plt.show()

if __name__ == '__main__':
    main()

