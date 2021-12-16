from matplotlib import pyplot as plt
import numpy as np

def degrees(graph_file):
    graph = open(graph_file, "r")
    nodes = int(graph.readline())
    undir_degrees = [0 for _ in range(nodes)]
    in_degrees = [0 for _ in range(nodes)]
    out_degrees = [0 for _ in range(nodes)]
    for line in graph:
        nodes = line.split(" ")
        undir_degrees[int(nodes[0])] += 1
        undir_degrees[int(nodes[1])] += 1
        in_degrees[int(nodes[1])] += 1
        out_degrees[int(nodes[0])] += 1
    return (undir_degrees, in_degrees, out_degrees)

def histogram(degrees, degree_type):
    labels = {"in":("in degrees", "in degree"),
            "out":("out degrees", "out degree"),
            "undir":("degrees", "degree")}
    title, x_label = labels[degree_type]
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel("count")
    plt.show()

def plot_histograms(graph_file):
    un_deg, in_deg, out_deg = degrees(graph_file)
    histogram(un_deg, "undir")
    histogram(in_deg, "in")
    histogram(out_deg, "out")

if __name__ == '__main__':
    plot_histograms("./graphs/n10.txt")
    plot_histograms("./graphs/n100.txt")
    plot_histograms("./graphs/n1000.txt")
    plot_histograms("./graphs/n10000.txt")
    plot_histograms("./graphs/s1.txt")
