import os
import shutil
if os.name == 'nt':
    import string
    from ctypes import windll

sectorsize = 1048576 #default value change it if you want

def get_driveswin(): 
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

def clearscreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def select_partition(drivelist):
    print("Select partition that you want to image:")
    for i in range(0, len(drivelist)):
        used_space = round(get_used_space(drivelist[i]) / 1024 / 1024 / 1024, 3) #convert to GB with 3 decimal digits 
        print(str(i) + ". [" + drivelist[i]  + ":/ ]" + " Disk Usage = " + str(used_space) + " GB")
    partition = input("Partition:")
    if int(partition) > len(drivelist) - 1:
        print("Invalid Value... Please try again.")
        select_partition(drivelist)
    return drivelist[int(partition)]

def get_outputfile():
    print("Insert your output file. It's recommended to put on another partition")
    path = input("Absolute Path: ")
    return path

def get_used_space(partition):
    return shutil.disk_usage(partition + ":/")[1]

def read_and_write(partition, path):
    partition_usage = get_used_space(partition)
    partitionletter = str(r"\\.\"" + partition + ":").replace('"', "")
    try:
        f = open(partitionletter, "rb")
    except PermissionError:
        print("You need admin permission to image the disk")
    w = open(path, "wb")
    i = 0 
    while True:
        if w.write(f.read(sectorsize)) == 0:
            break
        i = i + sectorsize
        percentage = round((i / partition_usage) * 100, 3)
        print("Imaging.." + str(percentage))
    f.close()
    w.close()

if __name__ == '__main__':
    drivelist = get_driveswin()
    partition = select_partition(drivelist)
    path = get_outputfile()
    print("Starting imaging to " + path + " ...")
    read_and_write(partition, path)
