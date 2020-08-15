import os, sys

dir_list = [i for i in os.listdir('.') if sys.argv[0].split('\\')[-1] != i and i != '.git'] 
# 자기자신 및 .git 파일을 제외 (그 외에도 제외할 게 많을 수 있지만 일반적으로는 없다고 가정)
extensions = set() 
for i in dir_list:
    extensions.add(i.split('.')[-1])

dir_list_dict_by_extension = {}

for extension in extensions:
    dir_list_dict_by_extension[extension] = []

for i in dir_list:
    dir_list_dict_by_extension[i.split('.')[-1]].append(i)
    # 확장자가 없는 파일의 경우는 고려하지 않음

for i in dir_list_dict_by_extension.values():
    i.sort()

def get_rename_only_name(origin_name, rename_name):
    return '.'.join(rename_name.split('.')[0:-1]) + '.' + origin_name.split('.')[-1]

a = None
for i in dir_list_dict_by_extension.values():
    a = len(i)
    break
min_name = None
for e in extensions:
    if len(dir_list_dict_by_extension[e]) < a:
        min_name = e
for i in range(len(dir_list_dict_by_extension[min_name])):
    for j in extensions:
        os.rename(dir_list_dict_by_extension[j][i], get_rename_only_name(dir_list_dict_by_extension[j][i], dir_list_dict_by_extension[min_name][i]))