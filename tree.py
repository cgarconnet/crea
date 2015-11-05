# Lancement en Python 3.x
#  exec(open("tree.py").read())

class NewPartner():

	def __init__(self,rootid):
		self.left = None
		self.right = None
		self.rootid = rootid

	def __repr__(self, level=0):
		ret = "\t"*level+repr(self.rootid)+"\n"
		for child in self.right:
			ret += child.__repr__(level+1)
		for child in self.left:
			ret += child.__repr__(level+1)
		return ret

	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def setNodeValue(self,value):
		self.rootid = value
	def getNodeValue(self):
		return self.rootid

	def insertRight(self,newNode):
		if self.right == None:
			self.right = NewPartner(newNode)
		else:
			tree = NewPartner(newNode)
			tree.right = self.right
			self.right = tree

	def insertLeft(self,newNode):
		if self.left == None:
			self.left = NewPartner(newNode)
		else:
			tree = NewPartner(newNode)
			self.left = tree
			tree.left = self.left

def test2Tree():
	my2Tree = NewPartner("Maud")
	my2Tree.insertLeft("Bob")
	my2Tree.insertRight("Tony")
	my2Tree.insertRight("Steven")
	return my2Tree


class Partner():

	def __init__(self,rootid, left=None, right=None):
		self.left = left
		self.right = right
		self.rootid = rootid

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
		if not self: return False # x + " not founded" #None
		if self.rootid == x:
			return True #"I founded: " + self.rootid #+ ", at level " + str(level)
		return self.left.find(x) or self.right.find(x) #, level+1

	def insertRight(self,newNode):
		if self.right == None:
			self.right = Partner(newNode)
		else:
			tree = Partner(newNode)
			tree.right = self.right
			self.right = tree

	def insertLeft(self,newNode):
		if self.left == None:
			self.left = Partner(newNode)
		else:
			tree = Partner(newNode)
			self.left = tree
			tree.left = self.left

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
	printTree(myTree)
	print('1st research')
	print(myTree.find("Maud"))
	print('2nd research')
	print(myTree.find("Bob"))
	print('3rd research')
	print(myTree.find("Tony"))
  

class node(object):
	def __init__(self, value, children = []):
		self.value = value
		self.children = children
		# self.depth = 0

	def __repr__(self, level=0):
		ret = "\t"*level+ repr(self.value)+"\n"
		for child in self.children:
			ret += child.__repr__(level+1)
		return ret

	# def set_depth(self, depth):
	# 	if self.left is not None:
	# 		self.left.set_depth(depth+1)
	# 	if self.right is not None:
	# 		self.right.set_depth(depth+1)
	# 	self.depth = depth


tree = node("grandmother", [
	node("daughter", [
		node("granddaughter"),
		node("grandson")]),
	node("son", [
		node("granddaughter"),
		node("grandson")])
	]);