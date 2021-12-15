class Node:
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.next = nextNode

    def toString(self):
        return self.value

class SLinkedList:
    def __init__(self, headNode):
        self.head = headNode
        self.end = headNode
        self.histogram = { headNode.value:1 }

    def print(self):
        node = self.head
        s = node.toString() + " -> "
        while node.next != None:
            node = node.next
            s += node.toString() + " -> "
        print(s)

    def append(self, value):
        self.end.next = value
        self.end = value
        self.histogram[value.value] = 1 if value.value not in self.histogram else (self.histogram[value.value] + 1)

    def insert(self, node, value):
        prevNext = node.next
        node.next = value
        value.next = prevNext
        self.histogram[value.value] = 1 if value.value not in self.histogram else (self.histogram[value.value] + 1)

    def count(self, value):
        return self.histogram[0] if value in self.histogram else 0




      
data = open("input.txt", 'r').readlines()
template = data[0].rstrip()
pairDict = [data[x].rstrip() for x in range(2, len(data))]
pairDict = {p.split(' -> ')[0]:p.split(' -> ')[1] for p in pairDict}

list = SLinkedList(Node(template[0]))
for i in range(1, len(template)):
    list.append(Node(template[i]))


for step in range(0, 40):
    print(step)
    nodesToInsert = {}
    node = list.head
    while node.next != None:
        pair = node.value + node.next.value

        if pair in pairDict:
            nodesToInsert[node] = Node(pairDict[pair])

        node = node.next

    for node in nodesToInsert:
        list.insert(node, nodesToInsert[node])


#list.print()

print(list.histogram)
max = list.histogram[max(list.histogram, key = lambda x: list.histogram[x])]
min = list.histogram[min(list.histogram, key = lambda x: list.histogram[x])]
print(max - min)

