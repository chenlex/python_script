#! -*-coding=utf-8 -*-

import subprocess

cmd = 'phoronix-test-suite openbenchmarking-refresh'
# 把 stdout 加入到一个新的管道， stderr 加入到另一个管道 ,这样再stderr 中就有值
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# 标准输出和标准错误输出到两个值里
# output = p.communicate()[0]
output, stderr = p.communicate()
# 进行编码解码处理,python 本身默认编码unicode,这里就是unicode
out = output.decode(encoding="utf-8")

# 迭代输出
for o in out.split("\\n"):
    print(o)

print("***********************************************************************")

p2 = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

# 标准输出和标准错误都输出，只显示一个值里边,第二个值为None
output2 = p2.communicate()
print(output2)
# 进行编码解码处理,python 本身默认编码unicode,这里就是unicode
out2 = output2[0].decode(encoding="utf-8")

# 迭代输出
for o in out2.split("\\n"):
    print(o)


