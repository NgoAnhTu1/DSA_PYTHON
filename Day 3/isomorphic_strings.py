def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False
    dict_s = {}
    word_in_t = []
    for i in range(len(s)):
        if  s[i] in dict_s and dict_s[s[i]] != t[i]:
            return False
        elif s[i] not in dict_s and t[i] in word_in_t:
            return False
        else:
            dict_s[s[i]] = t[i]
            word_in_t.append(t[i])
    
    return True

print(isomorphic_strings("egg", "add"))  
print(isomorphic_strings("foo", "bar"))   
print(isomorphic_strings("paper", "title"))  
print(isomorphic_strings("ab", "aa"))