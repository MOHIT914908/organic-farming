def main():  #main function defination 
    fullname = input("enter your name : ")      #take name from the user and store it in the variable fullname
    Age = int(input("enter your age : "))       #take age from the user and store it in the variable Age
    assert Age >=0 , "Age must be a positive whole  number" #assertion to check if the age is positive whole number 
    shoesize = float(input("enter your shoe size : "))      #take shoe size from the user and store it in the variable shoesize
    assert shoesize >0 , "shoe size must be a positive number"  #assertion to check if the shoe size is positive number
    
    #print the name age and shoesize of the person 
    print("Name of the person is : ",fullname)
    print("Age of the person is : ",Age)
    print("Shoe size of the person is : ",shoesize)
    
#check if the py file is run as script or module 
if __name__ == "__main__":
    main()  #call the main function
    
    