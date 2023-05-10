'''number_of_files = int(input("How many files you want to sort in the memory? Keep in mind that one file size is 12 and the total memory capacity is 20  "))
memory_size = 20
a_file_size = 12
total_files_size = memory_size * number_of_files

if (total_files_size <= memory_size ):
    print ("You can sort your files")
else:
    print ("You can't sort that much of files in memory because they are big in size ")'''
    

number_of_files = int(input("number of files "))
size_memory = int(input("memory capacity? "))
size_file = int(input("size of a file "))
total_files_size = int(size_file * number_of_files)
if(total_files_size  <= size_memory):
    print ("Numbers of file: ", number_of_files)
    print ( "Memory capacity: " , size_memory)
    print (" total size of files", total_files_size)
    print (" Your memory size is good enough for your total files size")
else:
    print ("Numbers of file: ",number_of_files)
    print("Memory capacity: " , size_memory)
    print(" total size of files", total_files_size)
    print (" Your memory size is smaller than your total files size")
