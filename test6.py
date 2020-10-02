# Capsule x: A single except block can catch multiple exceptions
# except (ZeroDivisionError, TypeError) as e:

def multi_exceptions_in_single_except_block():
    x = 5;
    #y = 0;
    try:
        z= x/y;
    except (ZeroDivisionError, NameError) as e:
        print (e);
    finally:
        print("Thanks for trying out...");

def main():
    multi_exceptions_in_single_except_block();


if __name__ == '__main__':
    main();