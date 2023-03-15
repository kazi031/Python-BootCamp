data = [53,76,25,98,56,42,69,81];

copy_data = data[:];
len = len(copy_data);
for i in range(len):
    for j in range(0,len-i-1):
        if copy_data[j] > copy_data[j+1]:
            copy_data[j],copy_data[j+1] = copy_data[j+1],copy_data[j];
            
            
print(copy_data);

print(sorted(data));

