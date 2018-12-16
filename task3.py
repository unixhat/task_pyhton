import os, sys

os.chdir("/Users/heriyanto/Downloads")
print("sekerip ada dih",os.getcwd())
list = os.listdir()
jumlah_file = len(list)
print("jumlah file dan folder",jumlah_file)
print("isi dalemannya bang: %s"%os.listdir(os.getcwd()))

for filename in os.listdir("."):
    os.rename(filename, filename[:-9] + '1')


print("isi dalemannya bang: %s"%os.listdir(os.getcwd()))
