import json
import shutil
import time

d_folder = "target_annotation"
v_folder = "target"
vdo = "video"
m = 'mp4'

def d_proceed_to_next(d_path, d_group, d_file):
    if d_path == "":
        d_group = "annotation_00000_01000"
        d_file = "00000.json"
        d_path = d_folder + '/' + d_group + '/' + d_file
    
    else:
        d_file, change_label = to_next_file(d_file)
        if change_label:
            d_group = to_next_group(d_group)
        d_path = d_folder + '/' + d_group + '/' + d_file

    return d_path, d_group, d_file 

def folder_index(num):
    num = num // 1000
    num *= 1000
    return convert_num(num)

def folder_index_next(num):
    num = num // 1000
    num += 1
    num *= 1000
    return convert_num(num)


def to_next_group(input):
    type, num1, num2 = input.split("_")
    num1 = int(num1)
    num1 += 1000
    num2 = int(num2)
    num2 += 1000

    return type + "_" + convert_num(num1) + "_" + convert_num(num2)

def to_next_file(input):
    num, type = input.split(".")
    num = int(num)
    num += 1
    change_folder = 0
    if num % 1000 == 0:
        change_folder = 1
    return convert_num(num) + "." + type, change_folder

def convert_num(num):
    num = str(num)
    t_l = 5
    c_l = len(num)
    if (c_l < 5):
        for i in range(t_l-c_l):
            num = '0' + num

    return num

def d_to_v(d_path):
    type, f1, f2 =  d_path.split("/")
    type, f11, f12 = f1.split('_')
    f21, f22 = f2.split('.')
    v_group = vdo + '_' + f11 + '_' + f12
    v_file = f21 + '.' + m
    return v_folder + '/' + v_group + '/' + v_file

starttime = time.time()
print("Start Analysing and Grouping!")
all_sum = []
shape_1_fn_a = []
shape_1_fn_v = []
shape_2_fn_a = []
shape_2_fn_v = []
shape_3_fn_a = []
shape_3_fn_v = []
shape_4_fn_a = []
shape_4_fn_v = []
shape_5_fn_a = []
shape_5_fn_v = []

d_group = ""
d_file = ""
d_path = ""

all_attri = set()

for i in range(10000):
    d_path, d_group, d_file = d_proceed_to_next(d_path, d_group, d_file)
    
    with open(d_path, "r") as f:
        data = json.load(f)
    pro = data['object_property']
    sum = 0

    for one_obj in pro:
        one_p = one_obj['mass']
        shape_num = one_p
        sum += shape_num

        
        all_attri.add(one_p)
    all_sum.append(sum)


    if sum == 7:
        shape_1_fn_a.append(d_path)
        v_path = d_to_v(d_path)
        shape_1_fn_v.append(v_path)
    elif sum == 8:
        shape_2_fn_a.append(d_path)
        v_path = d_to_v(d_path)
        shape_2_fn_v.append(v_path)
    elif sum == 9:
        shape_3_fn_a.append(d_path)
        v_path = d_to_v(d_path)
        shape_3_fn_v.append(v_path)    

    

tally = [0,0,0,0,0]

for i in range(len(all_sum)):
    val = 0
    if all_sum[i] == 7:
        val = 0
    elif all_sum[i] == 8:
        val = 1
    elif all_sum[i] == 9:
        val = 2


    tally[val] += 1
    
print("The property we partition is MASS")
print("If the data is in group 1, then your totoal mass is 7")
print("If the data is in group 2, then your totoal mass is 8")
print("If the data is in group 3, then your totoal mass is 9")
print(tally)

# The Partition Starts
print("Start Partitioning!")
for i in range(len(shape_1_fn_a)):
    shutil.copy(shape_1_fn_a[i], "mass7/target_annotation/annotation_" + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".json")
    shutil.copy(shape_1_fn_v[i], "mass7/target/video_"  + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".mp4")

for i in range(len(shape_2_fn_a)):
    shutil.copy(shape_2_fn_a[i], "mass8/target_annotation/annotation_" + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".json")
    shutil.copy(shape_2_fn_v[i], "mass8/target/video_"  + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".mp4")

for i in range(len(shape_3_fn_a)):
    shutil.copy(shape_3_fn_a[i], "mass9/target_annotation/annotation_" + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".json")
    shutil.copy(shape_3_fn_v[i], "mass9/target/video_"  + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".mp4")

endtime = time.time()
print("Done! The time taken is", endtime - starttime, "seconds")