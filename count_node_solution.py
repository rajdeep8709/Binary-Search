def height(node):
	count = 0
	while node:
		count+=1
		node = node.left
	return count

def count_node(root):
	ans = 0
	while root:
		left = height(root.left)
		if left == height(root.right):
			ans+=pow(2,left)
			root = root.right
		else:
			ans+=pow(2,left-1)
			root = root.left
	return ans
print(count_node(root))
