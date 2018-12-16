import os

s = "ABCD"
os.chdir("/Users/heriyanto/Downloads")
print("sekerip kerja dih",os.getcwd())

for i in range(0, len(s)):
    berih = s[i]
    os.mkdir(berih)

kura = sorted(os.listdir(os.getcwd()))
print("isi foldernyah", kura)
