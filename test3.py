import os.path;

#revise question number 5 (q5()) and question number 17 (q17()) from MTA 98-381 kindle book

def q16():
    file_name = "input.txt"
    with open(file_name, 'r') as file_object:
        if (os.path.isfile(file_name)):
            return file_object.read();
        else:
            return None; 

#Capsule 11
# Note the eof character in python
def q17():
    with open("inventory.txt.txt", 'r') as inventory:
        eof = False;
        while not eof:
            line = inventory.read();
            if line != '':
                if line != '\n':
                    print (line);
            else:
                eof = True;
                inventory.close();


def q18():
    print ("What is your name");
    name = input();
    print (name);



#Capsule 12
# Note the steps to convert a float entered through terminal. direct conversion of int  to string results in valueerror 
# when input entered is float

def q5():
    input_val = int(float(input("Enter any value: ")));
    print (input_val);

def main():
    #print ("output:" + str(q16()));
    q17();
    #q18();
    #q5();

if __name__ == '__main__':
    main();