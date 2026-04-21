def tree_by_levels(node):
    if node is None:
        return []
        
    result = []
    queue = []
    
    queue.append(node)
    
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.value)
        
        if current.left is not None:
            queue.append(current.left)
            
        if current.right is not None:
            queue.append(current.right)
            
    return result
