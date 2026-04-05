class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Dictionary to map: Original Node -> Cloned Node
        old_to_new = {}
        
        def dfs(curr):
            # If we already cloned this node, return the clone to prevent infinite loops
            if curr in old_to_new:
                return old_to_new[curr]
                
            # 1. Create the clone
            copy = Node(curr.val)
            
            # 2. Add it to our hash map IMMEDIATELY before exploring neighbors
            old_to_new[curr] = copy
            
            # 3. Recursively clone all neighbors and attach them to the copy
            for neighbor in curr.neighbors:
                cloned_neighbor = dfs(neighbor)
                copy.neighbors.append(cloned_neighbor)
                
            return copy
            
        # Kick off the DFS from the starting node
        return dfs(node)