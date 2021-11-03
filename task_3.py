import psutil
import os
import time
import logging

#loging config
logging.basicConfig(filename='app3.log',format='%(asctime)s - %(message)s', level=logging.DEBUG)

#test case 1 class
class test_case_1:
    #def init
    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name
    #def prep 
    def prep(self):
        logging.info("STARTING test ID: {} NAME: {}".format(self.tc_id, self.name))
        print("\nSTARTING test ID: {} NAME: {}".format(self.tc_id, self.name))
        #check memory
        memory_size = psutil.virtual_memory().total
        memory_size = memory_size/1000000
        #check if memory size is bigger or smaler than 1024 mb
        if memory_size < 1024:
            logging.info("Memory is smaller than 1024\nINTERUPTING test ID: {} NAME: {}\n".format(self.tc_id, self.name))
            print("\nMemory is smaller than 1024\nINTERUPTING test ID: {} NAME: {}\n".format(self.tc_id, self.name))
            return 0
        else: 
            logging.info("Memory is bigger than 1024")
            return 1
    #def run 
    def run(self):
        #creating random file of given size
        with open("random_file", "w") as file:
            file.truncate(1024)
            logging.info("Random file created")
            print("\nRandom file created")
    #def clean        
    def clean(self):
        #removing created file
        os.remove("random_file")
        logging.info("Random file deleted")
        print("Random file deleted\n\nTEST COMPLETED\n")
        logging.info("TEST COMPLETED\n")

#test case 2 class
class test_case_2:
    #def init
    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name
    #def prep 
    def prep(self):
        logging.info("STARTING test ID: {} NAME: {}".format(self.tc_id, self.name))
        print("\nSTARTING test ID: {} NAME: {}".format(self.tc_id, self.name))
        #getting epoch time in seconds
        epoch_time = int(time.time())
        logging.info("Epoch time: "  + str(epoch_time))
        print("\nEpoch time: "  + str(epoch_time))
        #checking if it is divisible by 2 
        if epoch_time % 2 != 0:
            logging.info("Epoch time is not divisible by 2, INTERUPTING test ID: {} NAME: {}\n".format(self.tc_id, self.name))
            print("\nEpoch time is not divisible by 2\nINTERUPTING test ID: {} NAME: {}\n".format(self.tc_id, self.name))
            return 0
        else: 
            return 1
    #def run 
    def run(self):
        #listing user home folders
        username = os.getlogin()
        logging.info(os.listdir("C:\\Users\\" + username))
        print(os.listdir("C:\\Users\\" + username))
        logging.info("TEST COMPLETED\n")
        print("\nTEST COMPLETED\n")
    #def clean 
    def clean(self):
        #doing nothing
        pass



#creating objects
test = test_case_1("1", "create_file")
test2 = test_case_2("2","list_home_directory")

#if condition is not met, interrupt the test case
if test.prep() == 1:
    test.run()
    test.clean()
#if condition is not met, interrupt the test case
if test2.prep() == 1:
    test2.run()
    test2.clean()
