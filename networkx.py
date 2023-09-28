import networkx as nx
import matplotlib.pyplot as plt

# 그래프 생성
G = nx.Graph()

# 노드 추가 (성공화가와 기관)
G.add_node('성공화가')
G.add_node('저명한 기관')

# 엣지 추가 (연결)
G.add_edge('성공화가', '저명한 기관')

# 그래프 시각화
pos = nx.spring_layout(G)  # 노드의 위치를 결정합니다.
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue')
plt.show()
