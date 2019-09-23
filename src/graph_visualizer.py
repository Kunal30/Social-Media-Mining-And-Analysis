import pickle
import networkx as nx
import warnings
import matplotlib.pyplot as plt

def main():
	print('Visualizer Running....')
	file=open('../v_ids.pickle','rb')
	v_ids=pickle.load(file)
	file=open('../v_names.pickle','rb')
	v_names=pickle.load(file)
	file=open('../edges.pickle','rb')
	edges=pickle.load(file)

	# Removing duplicates
	v_names=list(set(v_names))	
	v_ids=list(set(v_ids))

	G=create_social_network_graph(v_names,v_ids,edges)
	
	nx.draw_networkx(G,node_color='red',font_color='black')
	plt.show()

def create_social_network_graph(v_names,v_ids,edges):
	"""
	Returns a social network graph
	"""
	warnings.filterwarnings("ignore", category=UserWarning)
	G=nx.DiGraph()

	#Adding nodes
	for i in v_ids:
		G.add_node(i)

	#Adding edges
	count=0
	for node1 in edges.keys():
		e_list=edges[node1]
		for node2 in e_list:
			G.add_edge(node1,node2)

	return G
	
if __name__ == '__main__':
		main()	