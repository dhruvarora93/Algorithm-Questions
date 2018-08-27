from collections import defaultdict


def accountsMerge(accounts):

    email_to_name = {}
    graph = defaultdict(set)

    for i in accounts:
        name = i[0]
        for email in i[1:]:
            graph[i[1]].add(email)
            graph[email].add(i[1])
            email_to_name[email] = name
    seen = set()
    result = []
    for email in graph:
        if email not in seen:
            seen.add(email)
            stack = [email]
            component = set()
            while stack:
                node = stack.pop()
                component.add(node)
                for neighbors in graph[node]:
                    if neighbors not in seen:
                        seen.add(neighbors)
                        stack.append(neighbors)
                        component.add(neighbors)

            result.append([email_to_name[email]] + sorted(component))

    return result


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

print(accountsMerge(accounts))