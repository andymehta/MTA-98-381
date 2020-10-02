import math;
import time;

def input_to_int():
    'This is a doc string to be used by pydoc for method input_to_int()'
    marks = input("enter marks: ");
    int_marks = int(marks);
    print (int_marks);

#Capsule 4: The input received from input() method is string. Be sure to convert it in int before processing
# 'if not' syntax is valid
def room_check():
    'This is a doc string to be used by pydoc for method room_check()'

    #this is a comment which continues to the 
    # next line. Each line has to be commented with # in the beginning.     
    rooms_dict = {1:"suite", 2:"conference room"};
    room = int(input("which room? "));
    if not room in rooms_dict:
        print ("room not found");
    else:
        print (f"The room name is {rooms_dict[room]}");


def bool_type():
    'This is a doc string to be used by pydoc for method bool_type()'
    b = True;
    print (type(b));
    if type(b) is bool:
        print ("Boolean datatype is called bool in python");

#Capsule 5: int (float_val) will truncate numbers after decimal. round() function has two arguments.
#If 2nd argument is not supplied it will round to nearest integer.
def type_converter():
    'This is a doc string to be used by pydoc for method type_converter()'
    f = 4.9;
    print(f"Int val: {int(f)}");
    print (f"Rounded val: {round(f)}");

    str_val = input("Enter a float value: ");
    print (int(float(str_val)));


#Capsule 6: logical operator precedence in python is: not, and, or.
# first three operators in the order of precedence are: parenthesis/function call/attribute reference, exponentiation, unary 
# exponentiation associativity is right to left. 
def logical_operator_precedence():
    'This is a doc string to be used by pydoc for method logical_operator_precedence()'
    right_age = False;
    paid_fees = True;
    has_pass = True;

    can_enter = right_age and paid_fees or has_pass;
    print (can_enter);


#Capsule 7:
#  elif without else is valid
def elif_without_else(marks):
    'This is a doc string to be used by pydoc for method elif_without_else and it works()'
    if marks >= 90:
        return 'A';
    elif marks >= 80:
        return 'B';
    elif marks >=70:
        return 'C';
    elif marks >=60:
        return 'D';
    elif marks >=40:
        return 'P';
    elif marks >=0:
        return 'F';


#Capsule 8:
# a string can have placeholders for parameters. The actual values for these parameters can be passed by calling
# <str>.format(args) function.  
#the placeholders can contain the format in which the values need to be shown
# some formats are :08.2f, :4.1f, :.2f

def templatization(my_name, my_age):
    'Format is a method of string class. You can use to parameterize the string object'
    txt_msg = "My name is {0} and my age is {1} and i have {2:8.2f} rupees in my walet";
    rupees = 25.5123;
    formatted_msg = txt_msg.format(my_name,my_age, rupees)
    print (formatted_msg);

    txt_msg = "My name is {} and my age is {} and i have {:1.1f} rupees in my walet";
    rupees = 25.5623;
    formatted_msg = txt_msg.format(my_name,my_age, rupees)
    print (formatted_msg);



#Capsule 9
# A function can return multiple values in the form of a tuple
# a<=x<=b is a valid logical operation
# 
def multiple_val_return_fn(age):
    str_ret = "anand mehta";
    bool_ret = False;

    if 30<=age<=40:
        bool_ret = True;

    return str_ret, bool_ret;



#Capsule 10
# borrowed from C language %s prints string, %f prints float %d prints integers
# actual values are passed as tuple preceded by % sign without comma
# -sign is for left alignment with the characters boundary specified by the number after %
def ampersand_usage():
    #%s usage in strings
    name = "anand";
    surname = "mehta";
    rupees = 25.46
    print("hello %-20s your surname is %s and you have %-10.1f expressed in round is %-10d" % (name,surname, rupees, rupees));


def main():
    # Below function will work if input value is int (entered as string). It throws ValueError if input is float
    # Try with 20 and 20.5 as separate inputs
    #input_to_int();

    #why does this program doesnt produce intended output
    #check if not syntax
    #room_check();

    #bool_type();

    #round built in function (doesnt require import math). syntax: round(f, no of digits). default is 0.
    #rounds the number to the nearest integer, if no of digits to 0.
    #type_converter();

    #logical operator precedence - not, or, and
    #logical_operator_precedence();    

    #elif without else?....Is possible
    #grade = elif_without_else(40);
    #print (grade);

    #formatting strings
    templatization('anand', '39');

    #return multiple values from a function (a tuple)
    #ret_val = multiple_val_return_fn(39);
    #print (ret_val[0]);
    #print (ret_val[1]);

    #%s usage in strings
    ampersand_usage();


if __name__ == '__main__':
    main();

