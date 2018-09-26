from collections import deque


def remove_invalid_parantheses(string):

    queue, ans, found, visited = deque(), [], False, set()
    queue.append(string)

    while queue:

        paran = queue.popleft()
        if isValid(paran):
            ans.append(paran)
            found = True

        if not found:
            for i in range(len(paran)):
                if paran[i] == '(' or paran[i] == ')':
                    candidate = paran[:i] + paran[i+1:]
                    if candidate not in visited:
                        visited.add(candidate)
                        queue.append(candidate)

    return ans


def isValid(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        if count < 0:
            return False

    return count == 0


print(remove_invalid_parantheses("(a)())()"))