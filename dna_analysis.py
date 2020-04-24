# 姓名：余娥，陈思怡，吴丽娜，谭乐贇，曹梦茹
# Python程序设计
# Teamwork1: DNA分析

#这个程序读取DNA测序器的输出并计算统计数据，比如GC的含量。
#从如下命令行运行：python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# sys模块支持读取文件、命令行参数等。
import sys


###########################################################################
### 将核苷酸读入一个名为seq的变量中
###

# 需要指定文件名
if len(sys.argv) < 2:
    print( "运行此程序时，必须提供一个文件名作为参数。")
    sys.exit(2)
# 在命令行上指定的文件名，作为字符串。
filename = sys.argv[1]
# 可以从中读取数据的文件对象。
inputfile = open(filename)

# 输入文件中迄今为止已读取的所有核苷酸。
seq = ""
# 当前行号（=到目前为止读取的行数）。
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # 如果我们在2，6，10行
    if linenum % 4 == 2:
        # 从行尾删除换行符
        line = line.rstrip()
        seq = seq + line


###########################################################################
### 计算统计
###

# 迄今为止发现的总核苷酸。
total_count = 0
# G和C核苷酸的数量。
gc_count = 0
# 核苷酸A的数量。
a_count = 0
# 核苷酸T的数量。
t_count = 0
# 核苷酸C的数量。
c_count = 0
# 核苷酸G的数量。
g_count = 0
# A和T核苷酸的数量。
at_count = 0

# 对于字符串中的每个碱基（bp），
for bp in seq:
    # 增加我们看到的碱基总数
    total_count = total_count + 1

    # 接下来，如果bp是G或C，
    if bp == 'C' or bp == 'G':
        # 增加bp的计数
        gc_count = gc_count + 1

    elif bp == 'A' or bp== 'T' :
        # 增加bp('A''T')的计数
        at_count = at_count + 1
        # 用AT碱基计数at_count 除以总计数total_count
        at_content=  float(at_count) / total_count
for bp in seq:
    # 如果bp是A
    if bp == 'A':
          # 增加A的计数
        a_count=a_count+1

     # 如果bp是T
    elif bp == 'T':
          # 增加T的计数
        t_count=t_count+1

     # 如果bp是C
    elif bp == 'C':
         # 增加C的计数
        c_count=c_count+1

     # 如果bp是G
    elif bp == 'G' :
          # 增加G的计数
        g_count=g_count+1

#综合：A计数 C计数  G计数和T计数
sum_count=at_count+gc_count
#seq的长度。
seq_length=len(seq)
#计算AT/GC：（A+T）/(G+C)
ratio=at_count/gc_count
# 用GC碱基总计数gc_count 除以总计数total_count
gc_content = gc_count / total_count

if gc_content>0.6:
    print('content of organisms by gas chromatography is high ')
elif gc_content<0.4:
    print('content of organisms by gas chromatography is low')
else:
    print('content of GC  is medium ')


# 打印答案
print ('GC-content:', gc_content)
print (' A_count:',  a_count)
print (' T_count:',  t_count)
print (' C_count:', c_count)
print (' G_count:',  g_count)
print ('AT-content:', at_content)
print ('Sum count:',sum_count)
print ('Total count:', total_count)
print('seq length:',seq_length)
print('AT/GC Ratio:',ratio)