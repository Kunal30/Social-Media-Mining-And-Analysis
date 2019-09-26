import pickle
import networkx as nx
import warnings
import matplotlib.pyplot as plt
import collections
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def main():
	print('Network Measures Visualizer Running....')
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

	#Measure 1
	display_degree_distribution(G)
	
	#Measure 2
	closeness_centrality(G)

	#Measure 3
	betweeness_centrality(G)

def display_degree_distribution(G):
	"""
	Calculates degree distribution and 
	displays it as a Histogram
	"""
	degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
	degreeCount = collections.Counter(degree_sequence)
	deg, cnt = zip(*degreeCount.items())	
	df=pd.DataFrame.from_dict(degreeCount,orient='index').reset_index()
	df=df.rename(columns={"index":"Degree",0:"Count"})
	
	fig=px.bar(df,x='Degree',y='Count',title='Degree Distribution Histogram')
	fig.show()	

def closeness_centrality(G):
	"""
	Calculates closeness centrality and 
	displays it as a Histogram
	"""
	cc=nx.closeness_centrality(G=G)
	df=pd.DataFrame.from_dict(cc,orient='index').reset_index()
	df=df.rename(columns={"index":"TwitterID",0:"Closeness"})
	fig=px.bar(df,y='Closeness',title='Closeness Centrality Histogram')
	fig.show()		

def betweeness_centrality(G):
	"""
	Calculates closeness centrality and 
	displays it as a Histogram
	"""
	bc=nx.betweenness_centrality(G=G)
	count=0
	ids=[]
	bc_list=[]
	for i in bc.keys():
		ids.append(count)
		bc_list.append(bc[i])

	fig = go.Figure([go.Bar(x=ids, y=bc_list)])
	fig.show()	

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