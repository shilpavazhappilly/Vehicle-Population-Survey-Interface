import operations
import data
import operations3
import operations4

ans ='y'
print("\t\t**************** Welcome To Vehicle Population Census*********************")
while(ans=='y'or ans=='Y'):
    option = input(" Choose the options below:\n 1. Display Vehicle Population of ther Year 2010 \n 2. Mean Of Population in 6 year Plan for selected fuel\n 3.Display the Years in which populationincreased by 15% than prevois year\n 4.Display difference between Petrol-Electric and Petrol-CNG vechile Plot \n 5. Bar Chert on Vechicle Popution of petrol cng and Petrol eletric\n")
    if (option == '1'):
        operations.printdata_2010()
    elif (option == '2'):
        operations.meanpop()
    elif(option =='3'):
        operations3.incr_pop()
    elif(option =='4'):
        operations4.line_plot()

    elif(option=='5'):
        operations4.bar_plot()
    else:
        exit()



    ans= input("Want to Continue (y/n):")
