def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False
    dict_s = {}
    dict_t = {}
    for i in range (len(s)):
        if s[i] not in dict_s and t[i] not in dict_t:
            dict_s[s[i]] = t[i]
            dict_t[t[i]] = s[i]
        elif dict_s.get(s[i])  != t[i]  or dict_t.get(t[i]) != s[i]:
            return False
    return True 

print(isomorphic_strings("egg", "add"))  
print(isomorphic_strings("foo", "bar"))   
print(isomorphic_strings("paper", "title"))  
print(isomorphic_strings("ab", "aa"))