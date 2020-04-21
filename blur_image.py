# 余娥，吴丽娜，陈思怡，谭乐赟，曹梦茹
# Python 程序设计
# Teamwork 2: 图像模糊

# 用于模糊图像的Python程序

from PIL import Image
import itertools
import sys
import os

def read_image(file_path):
    '''
	将文件路径处的图像文件读入像素的矩形网格，
	表示为整数列表。外部列表的每个元素是一行像素，
	其中每个像素是一个整数x，并且0<=x<256。
	最后返回像素网格。
    '''
	#不需要修改此函数。
	#不需要理解这个函数是如何工作的。
    print ("Reading image", file_path)

    # 以图像格式打开文件
    try:
        image = Image.open(file_path)
    except IOError as e:
        print( e)
        return
    except:
        print ("读取文件时出现意外错误", file_path)
        return
    
    width, height = image.size
    data = list(image.getdata())
    
    # 数据是一个列表。我们把它分成一个嵌套列表.
    result = []
    for r in range(height):
        # 获取与此行对应的列表部分.
        row_start = r * width
        row = data[row_start:row_start + width]
        
        result.append(row)
    return result

def write_image(file_path, pixel_grid):
    '''
	给定像素网格作为整数列表格式的图像，将其作为图像写入文件名文件路径。
	要求：
	*每行像素网格的长度相同
	*每个像素值是一个整数x，使得0<=x<256。
    '''
	#不需要修改此函数。
	#不需要理解这个函数是如何工作的。
    size = len(pixel_grid[0]), len(pixel_grid)
    image = Image.new("L", size)

    print( "将", size[0], 'x', size[1], "图像写入文件", file_path)

	#通过在内部列表上生成一个iterable序列，然后将整个列表具体化，来展平列表。
    data = list(itertools.chain.from_iterable(pixel_grid))
    image.putdata(data)
   
    try:
		#写下图像。file_path 的文件扩展名决定编码。
        image.save(file_path)
    except IOError as e:
        print( e)
    except:
        print( "写入文件时出现意外错误", file_path)

def csv_line_to_list(line):
    ''' 
	给定CSV格式的整数行，将整数作为列表返回。参数行必须是一个字符串，如
	“255，0，27”
	请注意
	*字符串的开头或结尾没有多余的空格，并且
	*逗号仅在元素之间（第一个元素前没有逗号，最后一个元素后没有逗号）。
	如果违反这些规则之一，此方法将显示错误。
    '''
	#不需要修改此函数。
	#不需要理解这个函数是如何工作的。
	#不过，如果你想了解一下string split函数，也不是太麻烦。
    row = []
    for pixel in line.split(','):
        row.append(int(pixel))
    return row

def read_grid(file_path):
    ''' 
	将文件路径处的CSV文件读入像素矩形网格，表示为整数列表。
	此方法应读取write_grid函数写入的任何文件。返回像素网格pixel_grid。
    '''
    open_file_path = open(file_path)
    pixel_grid = []
    for line in open_file_path:
        pixel_grid.append(csv_line_to_list(line))
    return pixel_grid

def write_grid(file_path, pixel_grid):
    ''' 将给定的像素网格作为CSV写入文件名输出网格文件。'''
	#不需要修改此函数。
	#不需要理解这个函数是如何工作的。
    output_file = open(file_path, 'w')

    for row in pixel_grid:
        output_file.write(str(row[0]))
        for column in range(1, len(row)):
            output_file.write(', ' + str(row[column]).rjust(3))
        output_file.write('\n')

    output_file.close()

def get_pixel_at(pixel_grid, i, j):
    '''
	返回第i行和第j列像素网格中的像素（零开始计数）。
	如果没有行i或列j，则返回0。
    '''
    n = len(pixel_grid)
    #列数
    m = len(pixel_grid[0])
    if i > -1 and i < n and j > -1 and j < m:
        return pixel_grid[i][j]
    else:
        return 0
def test_get_pixel_at():
    ''' 基本的，简短的 get_pixel_at 检查。'''

	#如果所有这些测试都返回true，那么获得像素的解决方案可能基本正确。
	#然而，通过这些测试并不意味着你的解决方案是完全正确的。有很多做法
	#可以通过这个test_get_pixel_at，但结果仍然是错误的。

    test_grid = [
        [1, 2, 3, 4, 5, 6],
        [0, 2, 4, 6, 8, 10],
        [3, 4, 5, 6, 7, 8]
    ]

    try:
        assert get_pixel_at(test_grid, 0, 0) == 1,   "在 get_pixel_at(0，0)处获取像素的调用应返回1."
        assert get_pixel_at(test_grid, -1, 0) == 0,  "在 get_pixel_at(-1, 0)处获取像素的调用应返回0."
        assert get_pixel_at(test_grid, 0, -1) == 0,  "在 get_pixel_at(0, -1)处获取像素的调用应返回0."
        assert get_pixel_at(test_grid, -1, -1) == 0, "在 get_pixel_at(-1, -1)处获取像素的调用应返回0."

        assert get_pixel_at(test_grid, 2, 5) == 8,   "在 get_pixel_at(2, 5)处获取像素的调用应返回8."
        assert get_pixel_at(test_grid, 3, 5) == 0,   "在 get_pixel_at(3, 6)处获取像素的调用应返回0."
        assert get_pixel_at(test_grid, 2, 6) == 0,   "在 get_pixel_at(2, 6)处获取像素的调用应返回0."
        assert get_pixel_at(test_grid, 3, 6) == 0,   "在 get_pixel_at(3, 6)处获取像素的调用应返回."

        assert get_pixel_at(test_grid, 1, 3) == 6,   "在 get_pixel_at(1, 3)处获取像素的调用应返回6."
    except AssertionError as e:
        # 打印一个亲切友好的错误消息
        print(e)

#运行测试。如果测试通过，此方法将不打印任何内容。此方法为打印遇到的第一个错误的消息。
#test_get_pixel_at()

def average_of_surrounding(pixel_grid, i, j):
    '''
	返回第i行和第j列的像素值及其周围八个像素的未加权平均值。
    '''
    a=get_pixel_at(pixel_grid, i-1, j-1)
    b=get_pixel_at(pixel_grid, i-1, j)
    c=get_pixel_at(pixel_grid, i-1, j+1)
    d=get_pixel_at(pixel_grid, i, j-1)
    e=get_pixel_at(pixel_grid, i, j)
    f=get_pixel_at(pixel_grid, i, j+1)
    g=get_pixel_at(pixel_grid, i+1, j-1)
    h=get_pixel_at(pixel_grid, i+1, j)
    i=get_pixel_at(pixel_grid, i+1, j+1)
    pixel_sum=a+b+c+d+e+f+g+h+i
    j=pixel_sum / 9	
	
	#像素总和应为整数。我们打算使用整除法。
    return j

def test_average_of_surrounding():
    '''对周围环境进行基本的、简短的检查。'''

	#与test_get_pixel_at类似，通过所有这些测试并不保证你对周围环境的平均值计算是正确的。
    test_grid = [
        [1, 2, 3, 4, 5, 6],
        [0, 2, 4, 6, 8, 10],
        [3, 4, 5, 6, 7, 8]
    ]

    try:
        assert average_of_surrounding(test_grid, 0, 0) == 0, "对average_of_surrounding(test_grid，0，0)的平均值的调用应该返回0."
        assert average_of_surrounding(test_grid, 2, 5) == 3, "对average_of_surrounding(test_grid，2，5)的平均值的调用应该返回3."
    except AssertionError as e:
        print(e)

#test_average_of_surrounding()

def blur(pixel_grid):
    '''
	给定像素网格（像素网格），返回一个新的像素网格，这是模糊像素网格的结果。
	在输出网格中，每个像素是输入网格中该像素及其八个相邻像素的平均值。
    '''
    file_path=[[0]*len(pixel_grid[0])for i in range(len(pixel_grid))]
    for i in range(len(pixel_grid)):
        for j in range(len(pixel_grid[0])):
            file_path[i][j]=average_of_surrounding(pixel_grid, i, j)
            
    return file_path

#
#主程序从这里开始。
#
#步骤A：处理命令行参数并获取输入文件名。
#
#sys.argv是程序参数的列表，包括正在运行的程序的名称。如果你执行：
#
#python blur_image_solution.py my_image.png
#
#那么sys.argv将是[“blur_image_solution.py”，“my_image.png”]
#
#如果程序使用不正确（参数数目错误），请正确print该程序。
if len(sys.argv) != 2:
    print( "Usage:", sys.argv[0], "<input_file>" )
    print( "  <input_file> 应该是 " )
    print( "    (a) CSV格式的文本文件（由write_grid函数生成），或" )
    print( "    (b) 黑白图像文件（由color_to_gray.py生成）。" )
    print()
    print( "  模糊给定的输入文件并将结果输出为<input_file>_blur.png" )
    print( "  (一个图像）和<input_file>_blur_grid.txt（一个CSV格式的文本文件）。")
    sys.exit()

# 获取用户想要模糊的文件的路径。
input_file = sys.argv[1]

#步骤B：确定输入文件的类型，将文件内容读取到存储为整数列表的像素网格中

# 获取输入文件的文件扩展名和文件名。
path_without_ext, ext = os.path.splitext(input_file)
input_filename = os.path.basename(path_without_ext)

#根据文件扩展名，将文件作为图像或网格读入。
if ext == ".txt":
    input_grid = read_grid(input_file)
else:
    input_grid = read_image(input_file)

	#如果出现错误，read_image将不返回任何值——如果发生错误，请退出程序。
    if input_grid == None:
        exit()

#步骤C：生成输出文件名

#根据输入文件的名称为输出文件生成名称。
out_image_file = input_filename + '_blur.png'
out_grid_file = input_filename + '_blur_grid.txt'

#应用模糊算法并将结果写入两个输出文件。

write_image(out_image_file,blur(input_grid))
write_grid(out_grid_file,blur(input_grid))


###
### 协作者
###

# ... 在这里写下你的答案，作为评论（在以“#”开头的行上）。
