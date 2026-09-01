
# new = []
# for i in arr:
#     if i not in new:
#         new.append(i)
# print(len(new))

# a = [1,1,2,4]
# a[:] = sorted(set(a))


# a = [1.2,3,4,5,6]
# print(a[-1])


b = [1,3,4,5,6,7,8]
for i in range (len(b)-1,-1,-1):
    if b[i]==8:
       continue
    print(b[i])