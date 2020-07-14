import sys; x = 'runoob'; sys.stdout.write(x + '\n');

print('===========Python import mode===========')
print('命令参数为：')
for i in sys.argv :
    print(i)
print('\n python 路径为', sys.path)


from sys import argv, path
print('path: ', path)