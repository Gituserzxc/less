
n = input()

def palindrom(g):
    if g == g[::-1]:
        return True
    else:
        return False
    
print(palindrom(n))
