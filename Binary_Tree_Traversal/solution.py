# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
        
    result = []
    result.append(node.data)
    result.extend(pre_order(node.left))
    result.extend(pre_order(node.right))
    
    return result

def in_order(node):
    if node is None:
        return []
        
    result = []
    result.extend(in_order(node.left))
    result.append(node.data)
    result.extend(in_order(node.right))
    
    return result

def post_order(node):
    if node is None:
        return []
        
    result = []
    result.extend(post_order(node.left))
    result.extend(post_order(node.right))
    result.append(node.data)
    
    return result
