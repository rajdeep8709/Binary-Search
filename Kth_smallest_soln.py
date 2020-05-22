def kthsmallest(root,k):
	count = [0]
	def inorder(root,count,k):
		if root==None:
			return
		inorder(root.left,count,k)
		if count[0]==k:
			count.append(root.val)
			return 
		inorder(root.right,count,k)
	inorder(root,count,k)
	return count[1]
print(kthsmallest(root,k))
