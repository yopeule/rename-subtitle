import os, sys
l = [i for i in os.listdir('.') if sys.argv[0].split('\\')[-1] != i]
extend_name = set() 
for i in l:
    extend_name.add(i)
# ll = [[], []]
ll = {}
for ename in extend_name:
    ll[ename] = []
# for ename in extend_name:
#     ll.append([i for i in l if i.split('.')[-1] == ename])

for i in l:
    for ename in extend_name:
        if i.split('.')[-1] == ename:
            ll[ename].append(i)

for i in ll:
    i.sort()
    # i 가 왜 문자열이라고 하는거지? ??? 
# k = ll['a']

def get_rename_only_name(origin_name, rename_name):
    return rename_name.split('.')[0:-2] + origin_name.split('.')[-1]

ename = [i for i in extend_name]

# for i in range(len(ll[0])):
#     os.rename(ll[ename[0]][i], get_rename_only_name(ll[ename[0]][i], ll[ename[1]][i]))

for i in range(len(ll[0])):
    a = extend_name.pop()
    for j in extend_name:
        os.rename(ll[j][i], get_rename_only_name(ll[j][i], ll[a][i]))

# 확장자를 기준으로 분리 ?
# 어차피 파일명은 재생 순서를 위해 사전순으로 만들어져있다. 
# 그리고 그 동영상 파일을 위해 제작된 어떤 자막들 또한... 마찬가지로 사전순으로 되어있다. 
# 즉, 한 쪽으로 바꿔주면 된다.
