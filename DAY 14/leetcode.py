def longest_common(s1,s2):
    powerset1 = []
    powerset2 = set()
    def combinations(s,i,st):
        if i == len(s):
            powerset1.append("".join(st[:]))
            return
        st.append(s[i])
        combinations(s,i+1,st)
        st.pop()
        combinations(s,i+1,st)
        return powerset1
    def combinations2(s,i,sst):
        if i == len(s):
            powerset2.add("".join(sst[:]))
            return
        sst.append(s[i])
        combinations2(s,i+1,sst)
        sst.pop()
        combinations2(s,i+1,sst)
        return powerset2
    combinations(s1,0,[])
    combinations2(s2,0,[])

    max_length =0
    max_str = ""
    for i in powerset1:
        if i in powerset2 and len(i) >max_length:
            max_length =  len(i)
            max_str = i
    return max_str
print(longest_common("apple","banana"))