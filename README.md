# ComphyPartition
This repo contains code to partition the physical reasoning benchmark dataset: Comphy, with respect to physical properties

The dataset we use are the: ComPhy: Compositional Physical Reasoning of Objects and Events from Videos by
Zhenfang Chen, Kexin Yi, Yunzhu Li, Mingyu Ding, Antonio Torralba, Joshua B. Tenenbaum, Chuang Gan
The link is https://comphyreasoning.github.io/

Reference is: 4.Chen, Z., Yi, K., Li, Y., Ding, M., Torralba, A., Tenenbaum, J. B., & Gan, C. (2022). ComPhy: Compositional Physical Reasoning of Objects and Events from Videos. arXiv preprint arXiv:2205.01089.

Instructions of generating subsets:
1. Download original comphy training dataset at (https://comphyreasoning.github.io/) and download the Training and Validation Videos and Training and Validation Videos Annotation under the 
2. Unzip target, target_annotation(from COMPHY) and empty_change_name(from the repo) and Put the target, target_annotation, empty_change_name, and all the python script in the same folder
3. Duplicate the empty_change_name and rename them to the characteristic you want to partition, I will use material as a example: copy empty_change_name two times and rename it two material1, material2
4. Run the corresponding python file. Using material as an example, we can run python material.py
5. After the return message has been printed successfully (it might takes several minutes), the partition based on one physical property has been done.

Explanations for each characteristics:
Charge:
charge0: all object has no charge
charge1: some object has positive or negative charge

Number:
numberx while x from 1 to 3: all video in numberx has (x+2) type of materials in total
e.g. number2 contains all videos contains 4 objects in total

Color:
Colorx while x from 1 to 5: all video in colorx has x type of colors in total

Material:
materialx while x from 1 to 2: all video in materialx has x type of materials in total

Shape:
shapex while x from 1 to 2: all video in shapex has x type of shapes in total

Mass:
mass7: the total mass for all object in a video is 7
mass8: the total mass for all object in a video is 8
mass9: the total mass for all object in a video is 9

Friction:
friction1: the total friction for all object in a video is 0
friction2: the total friction for all object in a video is between 0 and 0.1
friction3: the total friction for all object in a video is greater than 0.1

Restitution:
rest1: the total restitution for all object in a video is between 0 and 3
rest2: the total restitution for all object in a video is greater than 3

