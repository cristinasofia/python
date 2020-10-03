# Trees

## Tree
- Each tree has a root node
- Root node has 0 or more child nodes
- Each child node has zero (called a leaf) or more child nodes

## Binary Tree
- Each node has up to 2 children

## Binary Search Tree
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

<table>
    <tbody><tr>
      <th>Data Structure</th>
      <th colspan="8">Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="4">Average</th>
      <th colspan="4">Worst</th>
      <th>Worst</th>
    </tr>
    <tr>
      <th></th>
      <th>Access</th>
      <th>Search</th>
      <th>Insertion</th>
      <th>Deletion</th>
      <th>Access</th>
      <th>Search</th>
      <th>Insertion</th>
      <th>Deletion</th>
      <th></th>
    </tr>
    <tr>
      <td>Binary Search Tree</td>
      <td align="center" colspan="4" style="color:#9acd32">O(log(n))</td>
      <td align="center" colspan="5" style="color:#CCCC00">O(n)</td>
    </tr>
    </tr>
    <tr>
        <td><a href="http://en.wikipedia.org/wiki/AVL_tree">AVL Tree</a></td>
        <td align="center" colspan="8" style="color:#9acd32">O(log(n))</td>
        <td style="color:#CCCC00">O(n)</td>
    </tr>
    <tr>
      <td><a href="http://en.wikipedia.org/wiki/Red-black_tree">Red-Black Tree</a></td>
      <td align="center" colspan="8" style="color:#9acd32">O(log(n))</td>
      <td style="color:#CCCC00">O(n)</td>
    </tr>
</tbody>
</table>

## Balanced
### AVL
Stores in each node the height of the subtrees rooted at this node.
Check if height balanced: height of left subtree and height of right subtree differ by 1:
```
  balance(n) = n.left.height - n.right.height
```

**Inserts**
Upon insertion, balance might change to -2 or 2.
- If balance is 2: rotate Left, rotate Right
- If balance is -2: rotate Right, rotate Left


**Pros:** Frequent data lookup queries.
**Cons:** Frequent insertions and deletions.


### Red-Black Trees
1. Every node is red or black.
2. The root is black.
3. The leaves (NULL nodes) are black.
4. Every red node must have two black children (red node cannot have black children, nlack node can have black children).
5. Every path from node to its leaves must have the same number of black children.

**Pros:** Less memory, can rebalance faster (faster insertion/deletions), used in situations where tree will be modified frequently.
**Cons:** Lookups aren't as good as Hashtables.


## Complete Binary Tree
- Every level of tree is filled, except for perhaps the last level.
- Filled form left to right.

## Full Binary Tree
- Every node has either 0 or 2 children (no node has only 1 child).

## Perfect Binary Tree
- Both **complete** and **full**.
- All leaf nodes will be at the same level. This level will be the maximum number of nodes.
- Number of nodes where k is the number of levels:
$$2^k - 1 $$

## Binary Tree Traversal
- In-Order: Left, Root, Right

```python
# 94 https://leetcode.com/problems/binary-tree-inorder-traversal/
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    if not root:
        return res
    
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        res.append(root.val)
        root = root.right
    
    return res
```

- Pre-Order: Root, Left, Right

```python
# 144 https://leetcode.com/problems/binary-tree-preorder-traversal/
def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    if not root:
        return res
    
    stack = [root]
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    
    return res
```

- Post-Order: Left, Right, Root

```python
# 145 https://leetcode.com/problems/binary-tree-postorder-traversal/
def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    res = []
    if not root:
        return res
    
    stack = [root]
    while stack:
        root = stack.pop()
        res = [root.val] + res
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    
    return res
```

## Traversing Nodes
```python
while node:
    if current node > target node:
        go left
    if current node < target node:
        go right
```
Good for:
- Lowest common ancestor of binary search tree
- Inorder successor

## Counting Nodes
```python
def helper(root):
    # identify here if we are searching for all nodes, internal, leaves, etc. 
    count = 1

    # visit left then right
    if root.left:
        count += helper(root.left)
    if root.right:
        count += helper(root.right)
    return count


total = 0
if root:
    total = helper(root)
return total
```

## BFS with Queue
Pop from left, then go left, then go right
```python
if not root:
    return False

q = [root]
while q:
    # pop left
    n = q.pop(0)
    if not n.left and not n.right:
        return True
    if n.left:
        # left conditions
        q.append(n.left)
    if n.right:
        # right conditions
        q.append(n.right)

return False
```
Good for:
- Validating a BST

## DFS Recursive
```python
res = []

def dfs(root):
    if root:
        if not root.left and not root.right:
            res.append(True)
        if root.left:
            dfs(root.left)
        if root.right:
            dfs(root.right)

dfs(root)
return res
```

## DFS with Stack
Pop from right, then go right, then go left
```python
if not root:
    return False

s = [root]
while s:
    # pop right
    n = s.pop()
    if not n.left and not n.right:
        return True
    if n.right:
        # right conditions
        s.append(n.right)
    if n.left:
        # left conditions
        s.append(n.left)

return False
```
Good for:
- Depth of binary tree
- Finding a path sum

### Minimum Spanning Trees
In a **weighted, connected, undirected graph**, a spanning tree is a tree that connects all the vertices. The minimum spanning tree is the spanning tree with minimum weight. There are various algorithms to do this.

### B-Trees
A self-balancing search tree (not a binary search tree) that is commonly used on disks or other storage devices. It is similar to a red-black tree, but uses fewer I/O operations.

### Interval Trees
An extension of a balanced binary search tree, but storing intervals (low -> high ranges) instead of simple values. A hotel could use this to store a list of all reservations and then effiCiently detect who is staying at the hotel at a particular time. 

# Graphs

## Union Find
https://leetcode.com/problems/friend-circles/
https://leetcode.com/problems/redundant-connection/
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
https://leetcode.com/problems/satisfiability-of-equality-equations/
https://leetcode.com/problems/accounts-merge/
https://leetcode.com/problems/connecting-cities-with-minimum-cost/

## Depth-First Search
Follows a path from the starting node to an ending node, then another path from start to end, etc. until all nodes are visited.
1.	Pick a node. If unvisited, mark it as visited and recur on all adjacent nodes.
2.	Repeat until all nodes are visited, or node to be searched is found.

```python
visited = set()
def dfs(grid, v):
	if v in visited:
		return

visited.add(v) 				    # v = initial vertex 
labeled as “discovered”
	for neighbor in grid[v]:	# neighbors = vertices 
		adjacent to v		  
		dfs(grid, neighbor)		    # recursion
```

https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/friend-circles/
https://leetcode.com/problems/pacific-atlantic-water-flow/
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

## From Boundary
https://leetcode.com/problems/surrounded-regions/
https://leetcode.com/problems/number-of-enclaves/

## Shortest Time
https://leetcode.com/problems/time-needed-to-inform-all-employees/

## Islands
https://leetcode.com/problems/number-of-closed-islands/
https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/keys-and-rooms/
https://leetcode.com/problems/max-area-of-island/
https://leetcode.com/problems/flood-fill/
https://leetcode.com/problems/coloring-a-border/

## Hash
https://leetcode.com/problems/employee-importance/
https://leetcode.com/problems/find-the-town-judge/

## Cycle Find

# BFS
Proceeds ‘level by level’, visiting all nodes on one level before moving on to the next.
1.	Pick a node, visit the adjacent unvisited vertex, mark as visited, and insert it in a queue.
2.	If no adjacent vertices left, remove first vertex from queue.
3.	Repeat 1 & 2 until queue is empty or node to be searched is found.

```python
visited = []
queue = []

visited.append(node)
queue.append(node)
while queue:					# while queue not empty
	v = queue.pop(0) 				# remove from front of queue
	for neighbor in grid[v]:		# search all adjacent vertices to v
		if neighbor not in visited:
			visited.append(neighbor)# mark neighbor as “visited”
			queue.append(neighbor) 	# add to back of queue
```

https://leetcode.com/problems/01-matrix/
https://leetcode.com/problems/as-far-from-land-as-possible/
https://leetcode.com/problems/rotting-oranges/
https://leetcode.com/problems/shortest-path-in-binary-matrix/

## Topological Sort
https://leetcode.com/problems/course-schedule-ii/

## Dijkstras and Bellman Ford
https://leetcode.com/problems/network-delay-time/
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
https://leetcode.com/problems/cheapest-flights-within-k-stops/

## Connectivity
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

## Strongly Connected Components: Tarjan's Algorithm 
https://leetcode.com/problems/critical-connections-in-a-network/

## Coloring
https://leetcode.com/problems/possible-bipartition/
https://leetcode.com/problems/is-graph-bipartite/

## Prim's and Kruskal's algorithm
https://leetcode.com/problems/optimize-water-distribution-in-a-village/

## Hierholzer's algorithm for Eulerian circuits
https://leetcode.com/problems/reconstruct-itinerary/

## A* search
https://leetcode.com/problems/sliding-puzzle/