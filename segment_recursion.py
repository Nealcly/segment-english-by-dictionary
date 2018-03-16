def split(d,s):
    return_list = []
    def segmention(d,s):
        if len(s) < 1:
            return True
        for i in range(len(s)):

            word = s[:i+1]
            last = s[i+1:]
            if word in d:
                if segmention(d,last) == True:
                    return_list.append(word)
                    return True
        return False

    return segmention(d,s),return_list[::-1]
if __name__ == "__main__":
    d = ["he", "like","likes" ,"cat"]
    s = "helikescat"
    print (split(d,s))


