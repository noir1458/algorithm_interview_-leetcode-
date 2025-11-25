def Solution(strs):
        d = {}
        for str in strs:
            d[''.join(sorted(list(str)))] = d.get(''.join(sorted(list(str))),[]) + [str]
        return [v for v in d.values()]

if __name__ == "__main__":
    s = Solution(["eat","tea","tan","ate","nat","bat"])
    print(s)