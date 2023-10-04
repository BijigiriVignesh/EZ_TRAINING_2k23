def paranthesis(n):
    res =[]
    l =[]
    def recur(opc , cc):
        if opc == cc == n:
            res.append("".join(l))
        if opc <n:
            l.append('(')
            recur(opc+1 , cc)
            l.pop()
        if cc < opc:
            l.append(")")
            recur(opc , cc+1)
            l.pop()
        return res
    return recur(0,0)
print(paranthesis(3))
