import fnmatch
import os

dirpath = "data"
count = len(fnmatch.filter(os.listdir(dirpath), '*.json'))
print(count)

with open("count.txt", "w") as f:
    f.write(str(count))