
#Capsule1: (20) is class <int>. (20,) is class <tuple>. {} is class <dict>  
def datatype_check():
	l=[10,(20),(20,), (20,30,40), {30},{},{},[40,50]]
	count=0
	for i in range(len(l)):
		print(type(l[i]));
		if type(l[i])==list:
			count+=1
		elif type(l[i])==tuple:
			count+=2
		elif type(l[i])==set:
			count+=3
		elif type(l[i])==dict:
			count+=4
		else:
			count+=5
	print(count)


#Capsule2: in operator does not check for case sensitivity when checking string membership
def membership_check():
		print ('is' in 'This IS a fake news!');


#Capsule3: A unique way to iterate over a dictionary keys using for loop and without using dict functions 
def sample(value):
    sum1=0
    for i in value:
        if i%2!=0:
            sum1+=value[i]
        else:
            sum1-=i
    print(sum1)
dict1={1:2,2:4,3:6,5:8}
sample(dict1)


def main():
	datatype_check();
	membership_check();

if __name__ == '__main__':
	main();