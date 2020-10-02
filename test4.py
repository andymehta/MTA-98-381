import time; 
import random;
import sys;

#Capsule 13
#  import time as t is invalid. 

# Capsule 14
#localtime() method returns a current_time object which encapsulates day, month year and time of the day

def time_functions():
    #sleep function from time module
    current_time = time.localtime();
    hour = current_time.tm_hour;
    minute = current_time.tm_min;
    mday = current_time.tm_mday;
    year = current_time.tm_year;
    month = current_time.tm_mon;
    second = current_time.tm_sec;

    time_string = "Current time is {0} hrs and {1} min. and {2} seconds on {3}th day of the month {4} in the year {5}";
    time_string = time_string.format(hour, minute, second, mday, month, year);
    print (time_string);

    print ("hmm.......let me sleep!!!");
    time.sleep(10);
    print ("I am ready now! ha ha ha");


#Capsule 15
# randint       x <= n <= y (int) 
# random        0 <= n <= 1 (float)
# randrange     x <= n < y 
# sample        return a slice with randomly selected values from a given sequence. 
#               Length of slice is equal to given int argument (2nd argument) 
# choice        return a random value from the given sequence

# A sequence can be a range, a list, a tuple or a string

def random_functions():
    i = random.randint(1,20);
    print (f"Your lucky number today: {i}");

    j = random.random();
    print (f"I will give you a float random number now {int(j*10)}"); 

    k = random.randrange(1,21,1);
    print (f"I will now give you one more chance (randrange)  {k}");

    sequence = range(1,21);
    val = random.sample(sequence, 3);
    print (f"Random lucky numbers today are : {val}"); 

    if (i in val) or (j*10 in val) or (k in val):
        print("Congratulations! it's your lucky day ...");

    chosen_val = random.choice(val);
    print (f"If you chose: {chosen_val} you have won bumper prize")


#Capsule 16
# see the creation of list from a range. Also range is a class of its own class<range>
def lists_and_ranges():
    sequence = range(1,21);
    val = random.sample(sequence, 3);
    print (f"Random lucky numbers today are : {val}"); 
    print (type(sequence));

    lst = [i for i in range(1,21)];
    print (type(lst));


#eval(args) evaluates the argument passed like a normal python code 

def eval_function():
    x = 5; 
    y = 10;
    val = input("Enter an expression for x and y:");
    print (f"Evaluation of {val} is: ", eval(val));


def cmd_line_args_func():
    try:
        print(f"1st argument: {sys.argv[1]}");
    except:
        print("Argument not provided");
    else:
        print("argument provided. thank you");
    finally:
        print("in finally block for cleanup");


def main():
    #time_functions();
    #random_functions();
    eval_function();



if __name__ == '__main__':
    main();
