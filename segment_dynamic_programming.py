def dynamic_simple(D, s):
    table = [False for i in range(len(s) + 1)]  # table[i] -> s[:i] can be segmented or not
    cutoff = [None for i in range(len(s) + 1)]
    table[0] = True

    for i in range(1, len(s) + 1):
        try:
            k = next(j for j in range(i) if table[j] and s[j:i] in D)
            table[i] = True
            cutoff[i] = k
        except StopIteration:
            pass

    return (table,cutoff)

def dynamic(D, s):
    table = [False for i in range(len(s) + 1)]  # table[i] -> s[:i] can be segmented or not
    cutoff = [None for i in range(len(s) + 1)]
    table[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if table[j] and s[j:i] in D:
                    table[i] = True
                    cutoff[i] = j
                    break
    return (table, cutoff)
#end def


if __name__ == "__main__":
    d = ["he", "like","likes" ,"cat"]
    s = "helikescat"
    print(dynamic(d, s))