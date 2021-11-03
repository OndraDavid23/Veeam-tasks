import hashlib

#path to input_file
input_file_path = input("\nEnter path to the input_file: ")
#path to file to check
file_to_check_path = input("Enter path to the folder where are files to check:")

#open input_file
with open(input_file_path) as f:
    #main loop through input_file
    for line in f:
        #spliting lines to list to easy acces to them
        input_file_list = line.split(" ")
        #file to check path + name of the file to check from input_file
        file_to_check = file_to_check_path + input_file_list[0]
        print("\nPath to the file: " + file_to_check )
        try:
            #opening and reading the file 
            with open(file_to_check, "rb") as file_to_check:
                file_to_check_read = file_to_check.read()
                #for md5 hash. It is the same for other hash types.
                if input_file_list[1] == "md5":
                    #read the sum of a file
                    hex_result = hashlib.md5(file_to_check_read).hexdigest()
                    #check if hash sum o file qual to value in input file
                    if input_file_list[2] == hex_result:
                        print(input_file_list[0] + " OK")
                    else:
                        print(input_file_list[0] + " FAIL")
                #for sha1 hash
                if input_file_list[1] == "sha1":
                    hex_result = hashlib.sha1(file_to_check_read).hexdigest()
                    if input_file_list[2] == hex_result:
                        print(input_file_list[0] + " OK")
                    else:
                        print(input_file_list[0] + " FAIL")
                #for sha256 hash  
                if input_file_list[1] == "sha256":
                    hex_result = hashlib.sha256(file_to_check_read).hexdigest()
                    if input_file_list[2] == hex_result:
                        print(input_file_list[0] + " OK")
                    else:
                        print(input_file_list[0] + " FAIL")
        except:
            #if input file is not in inputed file path
            print(input_file_list[0]  + " not found")        




