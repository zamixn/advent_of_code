from anytree import Node, RenderTree

data = open("input_test.txt", 'r').readlines()
template = data[0].rstrip()
pairDict = [data[x].rstrip() for x in range(2, len(data))]
pairDict = {p.split(' -> ')[0]:p.split(' -> ')[1] for p in pairDict}

template = [template[i: i+2: 1] for i in range(0, len(template) - 1)]

root = Node('root')
nodes = [Node(x, parent=root) for x in template]

for step in range(0, 2):
    for node in nodes:
        nodesToAdd = []
        if node.name in pairDict:
            nodesToAdd.append(Node(node.name[0] + pairDict[node.name], parent=node))
            nodesToAdd.append(Node(pairDict[node.name] + node.name[1], parent=node))

    nodes = nodesToAdd


for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

