" 2.1_ JSON to TXT file Converter """

import json
import glob

data_list = []
text_str = ""
li = []
new_list = []

# Read Json File in the folder
for f in glob.glob("*.json"):
    with open(f, ) as infile:
        data_list.append(json.load(infile))
print(data_list)
print(len(data_list))
# print(type(data_list))

for element in data_list:
    # print(element)
    # print(type(element))
    t = list(element.items())
    # print(f" .... {t}")
    # print(type(t))
    # print(' '.join(str(e) for e in t))

    N = [item for sublist in t for item in sublist]
    # print(N)
    # print(type(N))
    # Z = print(*N, sep=" ")
    # print(type(Z))
    # l = print(",".join(N))
    # print(type(l))
    s = " ".join(N)
    li = li + [s]
print(li)

# Write to txt file
Converted_Txt_file = "NEW Converted json File file2.txt"
with open(Converted_Txt_file, 'w') as filehandle:
    for j in li:
        filehandle.write('%s\n' % j)
