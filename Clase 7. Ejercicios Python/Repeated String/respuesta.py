
if __name__ == "__main__":
    s = str(input())
    num = int(input())
    counter = s.count('a')
    limit = int(num/len(s))*len(s)
    res = int(num/len(s))*counter
    for x in s:
        if limit == num: break
        elif x == 'a':
            res=res+1
            limit=limit+1
        else: limit=limit+1
    print(res)

