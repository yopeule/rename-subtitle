import os, sys

dir_list = [i for i in os.listdir('.') if sys.argv[0].split('\\')[-1] != i and i != '.git']
print(dir_list)
extensions = set() 
for i in dir_list:
    extensions.add(i.split('.')[-1])

dir_list_dict_by_extension = {}

for extension in extensions:
    dir_list_dict_by_extension[extension] = []
# for ename in extend_name:
#     ll.append([i for i in l if i.split('.')[-1] == ename])
for i in dir_list:
    for extension in extensions:
        if i.split('.')[-1] == extension:
            dir_list_dict_by_extension[extension].append(i)
            # 이 부분 조금 이상한 느낌인데. 분류 방법이 이거 말고 없나?
            # 아!! 
            #-> dir_list_dict_by_extension[i.split('.')[-1]].append(i)

for i in dir_list_dict_by_extension.values():
    i.sort()

print(dir_list_dict_by_extension)

def get_rename_only_name(origin_name, rename_name):
    return '.'.join(rename_name.split('.')[0:-1]) + '.' + origin_name.split('.')[-1]
# extension = [i for i in extensions]

# for i in range(len(ll[0])):
#     os.rename(ll[ename[0]][i], get_rename_only_name(ll[ename[0]][i], ll[ename[1]][i]))



a = extensions.pop()
for i in range(len(dir_list_dict_by_extension[a])):
    for j in extensions:
        try:
            os.rename(dir_list_dict_by_extension[j][i], get_rename_only_name(dir_list_dict_by_extension[j][i], dir_list_dict_by_extension[a][i]))
        except IndexError:
            pass
# 확장자를 기준으로 분리 ?
# 어차피 파일명은 재생 순서를 위해 사전순으로 만들어져있다. 
# 그리고 그 동영상 파일을 위해 제작된 어떤 자막들 또한... 마찬가지로 사전순으로 되어있다. 
# 즉, 한 쪽으로 바꿔주면 된다.
