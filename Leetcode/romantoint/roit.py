def romantoint(s):
        prev = 0
        sumcount = 0
        Roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in s[::-1]:
            curr = Roman[i]
            if prev > curr:
                sumcount -= curr
            else:
                sumcount += curr
            prev = curr
        return sumcount

print(romantoint("I"))
print(romantoint("IV"))
