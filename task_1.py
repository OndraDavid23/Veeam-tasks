import xml.etree.ElementTree as ET
import shutil



#function to copy file
def copy_file():
    #parsing xml
    tree = ET.parse("config.xml")
    root = tree.getroot()
    x = 0
    print("Enter file name you want to copy: ")
    file_input = input()
    #looping throug xml 
    for child in root:
        #checking if input match a file in xml
        if root[x].attrib["file_name"]  == file_input:
            try: 
                #try to copy from source to destination
                src = root[x].attrib["source_path"] + "\\" + root[x].attrib["file_name"]
                dest = root[x].attrib["destination_path"]
                print("\nSource folder: "  + src)
                print("Destination folder: " + dest + "\n")
                shutil.copy(src, dest)
                return print("File " + root[x].attrib["file_name"] + " was copied to " + root[x].attrib["destination_path"])
            #exceptions
            except shutil.SameFileError:
                return print("Source and destination are the same")
            except PermissionError:
                return print("Permission denied")
            except:
                return print("Destination does not exist") 
        #if file doesnt match check next file
        else:
            x =+ 1
    return print("File not found")



copy_file()
