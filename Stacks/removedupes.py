def removdupes(S):

    list = []

    for i in S:

        if list and i == list[-1]:
            list.pop()

        else:
            list.append(i)

    return "".join(list)

S = "abcababbbbbbbb"

print(removdupes(S))
