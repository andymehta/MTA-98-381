#Udemy test 1: Q25 and Q35 in addition to below

#Capsule 17
#Two list variables with same value returns false for identity check and true for comparison check
#In all other cases (string, int etc.), two diff variables with same value returns true and true 

def identity_test():
	x= ['1','2'];
	y= ['1','2'];
	identity_result= x is y;
	comparison_result = x==y;
	print("list identity result:" + str(identity_result));
	print ("list comparison_result: "+ str(comparison_result));


	x= "Anand";
	y= "Anand";
	identity_result= x is y;
	comparison_result = x==y;
	print("string identity result:" + str(identity_result));
	print ("string comparison_result: "+ str(comparison_result));


	x= (2,4);
	y= (2,4);
	identity_result= x is y;
	comparison_result = x==y;
	print("tuple identity result:" + str(identity_result));
	print ("tuple comparison_result: "+ str(comparison_result));

	x= 2;
	y= 2;
	identity_result= x is y;
	comparison_result = x==y;
	print("int identity result:" + str(identity_result));
	print ("int comparison_result: "+ str(comparison_result));

#Capsule 16
#For Empty String, Empty List,Empty tuple,Empty set,Empty dict and range(0) arguments
#  bool() function returns False.

def boolean_test():
	a=bool([False])
	b=bool(0.5)
	c=bool("")
	d=bool(' ')
	print (a);
	print (b);
	print (c);
	print (d);


def main():
	identity_test();
	boolean_test();

if __name__== '__main__':
	main();