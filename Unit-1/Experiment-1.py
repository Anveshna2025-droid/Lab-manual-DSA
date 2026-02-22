# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment -1 
# Submitted to = Deepak Kaushik Sir
# <=========================================>


# Aim - Design a Stack ADT and build confidence   in LIFO behavior and constant-time operations

# Input / Output expectation
# Input: sequence of operations.
# Output: returned values (pop/peek) + final stack state + safe underflow handling.

#<=====================CODE STARTS==========================>

# Complexity of the code : All operations (Push, Pop, Peek) are O(1).

class StackADT:
    def __init__(self):
        self.data=[]
    def push(self,x):
        self.data.append(x)
    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]
    def is_empty(self):
        return len(self.data)==0
    def size(self):
        return len(self.data)
    def display(self):
        return self.data
def reversing_string(a):
    ADT= StackADT()
    for ch in a:
            ADT.push(ch)
    rev=""
    while not ADT.is_empty():
        rev += ADT.pop()
    return rev
def main():
    ADT=StackADT()
    while True:
        print("\n------STACK_ADT MENU------")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Size")
        print("6. Display Stack")
        print("7. Reversing a string")
        print("0. Exit the program")

        choice=input("Enter a number corresponding to your choice :").strip()

        if choice=="1":
            value=input("Enter value to push: ")
            ADT.push(value)
            print("Pushed : ", value)
        elif choice=="2":
            removed=ADT.pop()
            if removed is None:
                print("Underflow condition found ! Stack is empty , poping not possible")
            else:
                print("Popped:",removed)
        elif choice=="3":
            top=ADT.peek()
            if top is None:
                print("Nothing to peek!")
            else:
                print("Top element is : ",top)
        elif choice=="4":
             print("isEmpty:", ADT.is_empty())
        elif choice == "5":
             print("Size of the stack : ", ADT.size())   
        elif choice == "6":
             print("Stack (bottom -> top):", ADT.display())
        elif choice == "7":
            s = input("Enter a string to reverse: ")
            print("Reversed string:", reversing_string(s))
        elif choice == "0":
            print("Terminating the program ! See you soon ...")
            break
        else:
            print("Enter a valid choice!")
if __name__=="__main__":
    main()    
#<=====================CODE ENDS============================>
