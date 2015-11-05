from collections import deque

class Partner():

	def __init__(self,rootid, left=None, right=None):
		self.left = left
		self.right = right
		self.rootid = rootid

	def __repr__(self):
		return str(self.rootid)

	# def __repr__(self, level=0):
	# 	ret = "\t"*level+repr(self.rootid)+"\n"
	# 	for child in self.children:
	# 		ret += child.__repr__(level+1)
	# 	return ret

	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def setNodeValue(self,value):
		self.rootid = value
	def getNodeValue(self):
		return self.rootid

	def find(self, x): #level=0
		print(self.rootid)
		if self.left != None and self.rootid != x:
			self.left.find(x)
		if self.right != None and self.rootid != x:
			self.right.find(x) #, level+1
		return "I founded: " + self.rootid if self.rootid == x else x + " not founded"

	def BFT(node):

	    node.level = 1
	    queue = deque([node])
	    output = []
	    current_level = node.level

	    while len(queue)>0:

	          current_node = queue.popleft()

	          if(current_node.level > current_level):
	              output.append("\n")
	              current_level += 1

	          output.append(str(current_node))

	          if current_node.left != None:
	             current_node.left.level = current_level + 1 
	             queue.append(current_node.left) 

	          if current_node.right != None:
	             current_node.right.level = current_level + 1 
	             queue.append(current_node.right)

	                 
	 
	    return ''.join(output)

	def insertRight(self,newNode):
		if self.right == None:
			self.right = Partner(newNode)
		else:
			self.right.insertRight(newNode)
			# tree = Partner(newNode)
			# tree.right = self.right
			# self.right = tree

	def insertLeft(self,newNode):
		if self.left == None:
			self.left = Partner(newNode)
		else:
			self.left.insertLeft(newNode)
			# tree = Partner(newNode)
			# self.left = tree
			# tree.left = self.left

	# def set_depth(self, depth):
	# 	#Set depth of root node to 0, then all of its children to 1, and so on
	# 	child = node(number_of_depth)

	# 	if self.left is None and self.right is None:
	# 		return self.number_of_depth
	# 	else:
	# 		if self.left is not None or self.right is not None:
	# 			self.number_of_depth += 1
	# 			self.set_depth(number_of_depth)
	# 			child.left = child


def printTree(tree,level=0):
	if tree != None:
		printTree(tree.getLeftChild(),level+1)
		print("\t"*level+tree.getNodeValue())
		printTree(tree.getRightChild(),level+1)


def testTree():
	myTree = Partner("Maud")
	myTree.insertLeft("Bob")
	myTree.insertRight("Tony")
	myTree.insertRight("Steven")
	myTree.insertLeft("Matt")
	printTree(myTree)
	print myTree.BFT()	
	# print('1st research')
	# print(myTree.find("Maud"))
	# print('2nd research')
	# print(myTree.find("Bob"))
	# print('3rd research')
	# print(myTree.find("Tony"))
  