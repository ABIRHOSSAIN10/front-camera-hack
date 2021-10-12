import os

user_input = ("site/Front.came1/")

directory = os.listdir(user_input)

searchString = ("cam")

for line in directory:

    if searchString in line:

        lop=line

        print(line)

        os.system("cd site/Front.came1 && mv "+line+" /sdcard")

print('photo saved to your sdcard')   
