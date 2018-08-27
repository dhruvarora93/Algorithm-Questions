def validator(string):
    openers = ['(','{','[']
    closers = [')','}',']']
    opener_stack = []
    for s in string:
        if s in openers:
            opener_stack.append(s)
        elif s in closers:
            if not opener_stack:
                return False
            ch = opener_stack.pop()
            index = openers.index(ch)
            if s != closers[index]:
                return False
    return True

print(validator('{ [ ] ( ) }'))