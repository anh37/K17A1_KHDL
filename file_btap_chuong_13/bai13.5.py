import csv
# đọc tệp tin csv 
def read_csv():
    name_file =  input('nhập tên file csv vào đây :') # điển part1.csv
    f = open(name_file)
    list=[]
    for i in csv.reader(f):
        # in ra list 
        list.append(i) 
        # ghi ra theo từng dongg
        print(i)
    f.close()
    return list
print(read_csv())



