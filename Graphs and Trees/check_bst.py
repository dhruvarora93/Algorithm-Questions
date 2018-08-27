def check_bst(root, lower = float('-inf'), upper = float('inf')):

    if not root:
        return True

    if root.value < lower or root.value > upper:
        return False

    return check_bst(root.left, lower, root.value) and check_bst(root.right,root.value,upper)
