# # get file list

# import os
# filepath = '/Users/adrian/TIPS/t2s/ASL_Citizen/videos'
# with open("output.txt","w", encoding='utf-8') as file:
#     for files in os.listdir(filepath):
#         file.write(files.split("-")[-1])
#         file.write('\n')

# compare file name 
with open("/Users/adrian/Desktop/master/labwork/dataset/Result/ASL_Citizen_output.txt", 'r', encoding='utf-8') as file1:
    file1_lines = [line.split('.')[0].strip().lower() for line in file1.readlines()]
with open("/Users/adrian/Desktop/master/labwork/dataset/Result/SignBank_output.txt", 'r', encoding='utf-8') as file2,open("/Users/adrian/Desktop/output.txt", 'w', encoding='utf-8') as output:
    written_lines = set()
    for line in file2:
            content = line.split('.')[0].strip().lower()
            if content not in file1_lines and content not in written_lines:
                output.write(line)
                written_lines.add(content)

# # calculate the number of mp4
# with open("/Users/adrian/Desktop/master/labwork/dataset/Result/output2.txt", 'r', encoding='utf-8') as file:
#     file_lines = [line.split() for line in file.readlines()]
#     print(len(file_lines))