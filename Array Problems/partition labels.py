def partitionLabels(s):
        dic = {}
        for i, char in enumerate(s):
            dic[char] = i
        res = []
        l, r = 0, 0
        for i, char in enumerate(s):
            r = max(r, dic[char])
            if i == r:
                res.append(r - l + 1)
                l = r + 1
        print(res)
S = "ababcbacadefegdehijhklij"
partitionLabels(S)