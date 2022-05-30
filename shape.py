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
all_shape_diff = []
shape_1_fn_a = []
shape_1_fn_v = []
shape_2_fn_a = []
shape_2_fn_v = []
shape_3_fn_a = []
shape_3_fn_v = []


d_group = ""
d_file = ""
d_path = ""


all_attri = set()
for i in range(1000):
    d_path, d_group, d_file = d_proceed_to_next(d_path, d_group, d_file)
    
    with open(d_path, "r") as f:
        data = json.load(f)
    pro = data['object_property']
    shape = set()
    for one_obj in pro:
        shape_num = one_obj['shape']
        shape.add(one_obj['shape'])
        all_attri.add(one_obj['shape'])


    
    if len(shape) == 1:
        shape_1_fn_a.append(d_path)
        v_path = d_to_v(d_path)
        shape_1_fn_v.append(v_path)

    if len(shape) == 2:
        shape_2_fn_a.append(d_path)
        v_path = d_to_v(d_path)
        shape_2_fn_v.append(v_path)

    if len(shape) == 3:
        shape_3_fn_a.append(d_path)
        v_path = d_to_v(d_path)
        shape_3_fn_v.append(v_path)

    all_shape_diff.append(len(shape))
# print(all_attri)

tally = [0,0,0,0,0]
index_1 = []
index_2 = []
index_3 = []
for i in range(len(all_shape_diff)):
    val = all_shape_diff[i]-1
    if val == 0:
        index_1.append(i)
    elif val == 1:
        index_2.append(i)
    elif val == 2:
        index_3.append(i)
    tally[val] += 1
    
print("The property we partition is SHAPE")
print(tally)
#print(shape_1_fn_a)
#print(shape_1_fn_v)

# The Partition Starts
print("Start Partitioning!")
for i in range(len(shape_1_fn_a)):
    #print("shape1/target_annotation/annotation_" + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".json")
    shutil.copy(shape_1_fn_a[i], "shape1/target_annotation/annotation_" + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".json")
    shutil.copy(shape_1_fn_v[i], "shape1/target/video_"  + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".mp4")

for i in range(len(shape_2_fn_a)):
    #print("shape2/target_annotation/annotation_" + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".json")
    shutil.copy(shape_2_fn_a[i], "shape2/target_annotation/annotation_" + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".json")
    shutil.copy(shape_2_fn_v[i], "shape2/target/video_"  + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".mp4")

for i in range(len(shape_3_fn_a)):
    #print("shape3/target_annotation/annotation_" + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".json")
    shutil.copy(shape_3_fn_a[i], "shape3/target_annotation/annotation_" + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".json")
    shutil.copy(shape_3_fn_v[i], "shape3/target/video_"  + folder_index(i) + '_' + folder_index_next(i) + '/' + convert_num(i) + ".mp4")

endtime = time.time()
print("Done! The time taken is", endtime - starttime, "seconds")