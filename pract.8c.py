def read_file(filename,number):
               myfile=open(filename)
               for line in myfile.readlines()[-number:]:
                   print(line)

num=int(input("Enter the number of last lines to print"))
read_file('ample.txt',num)
