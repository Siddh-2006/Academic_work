s="abcdabcdabcd"
sub = 'ab'
def R_index(s,sub):
    return [i+1 for i in range(len(s)-len(sub)-1,0,-1) if s[i:i+len(sub)] == sub] 
print("R_index :" ,R_index(s,sub)[0])