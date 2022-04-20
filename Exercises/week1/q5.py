def rev_no(n):
    s=0;
    while True:
        k=str(n);
        if k==k[::-1]:
            break
        else:
            m=int(k[::-1])
            n+=m
            s+=1
        return n;
print(rev_no(1234))