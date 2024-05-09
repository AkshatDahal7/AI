#Took help from GeeksForGeeks
def cost(H, condition, weight = 1):
	cost = {}
	if 'AND' in condition:
		AND_nodes = condition['AND']
		path_1 = ' AND '.join(AND_nodes)
		PathA = sum(H[node]+weight for node in AND_nodes)
		cost[path_1] = PathA

	if 'OR' in condition:
		OR_nodes = condition['OR']
		path_2 =' OR '.join(OR_nodes)
		PathB = min(H[node]+weight for node in OR_nodes)
		cost[path_2] = PathB
	return cost

def update(H, Conditions, weight=1):
	all_nodes = list(Conditions.keys())
	all_nodes.reverse()
	least_cost= {}
	for key in all_nodes:
		condition = Conditions[key]
		print(key,':', Conditions[key],'>>>', cost(H, condition, weight))
		c = cost(H, condition, weight) 
		H[key] = min(c.values())
		least_cost[key] = cost(H, condition, weight)		 
	return least_cost

def AO(Start,Updated_cost, H):
	Path = Start
	if Start in Updated_cost.keys():
		Min_cost = min(Updated_cost[Start].values())
		key = list(Updated_cost[Start].keys())
		values = list(Updated_cost[Start].values())
		Index = values.index(Min_cost)
		
		Next = key[Index].split()

		if len(Next) == 1:

			Start =Next[0]
			Path += ' = ' +AO(Start, Updated_cost, H)

		else:
			Path +='=('+key[Index]+') '

			Start = Next[0]
			Path += '[' +AO(Start, Updated_cost, H) + ' + '

			Start = Next[-1]
			Path += AO(Start, Updated_cost, H) + ']'

	return Path
		
H1 = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}

Conditions = {
'A': {'OR': ['D'], 'AND': ['B', 'C']},
'B': {'OR': ['G', 'H']},
'D': {'AND': ['E', 'F']},
}

weight = 1

print('Updated cost :')
Updated_cost = update(H1, Conditions, weight=1)
print('*'*75)
print('Shortest Path :\n',AO('A', Updated_cost,H1))