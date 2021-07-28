import data

####### Menu option 1
def printdata_2010():
    mycols = ['Fuel Type','2010']
    print(data.pop_data[mycols])
#printdata_2010()
####################################
######### Menu Option 2
def meanpop():

    ft = input("Select Fuel Type From Below:\n 1. Diesel \n 2. Diesel-Electric\n 3. Electric\n 4. Petrol\n 5. Petrol-CNG\n 6. Petrol-Electric 7. Petrol-Electric (Plug-In)\n")
    if (ft == '1'):
        diesel = data.pop_data[data.pop_data["Fuel Type"]== "Diesel"] # selecting data of given fuel type
        print(diesel)
        mean1 =diesel.iloc[:,[1,2,3,4,5,6] ].mean(axis =1) # finding mean of frst 6 years
        print("The mean vehicle population from (2006-2011)of Diesel: "+str(mean1))
        print("The year(s) and the vehicle population in that period which exceed the mean found above is/are: ")
        for i in range(1,7):
            for year, value in diesel.iterrows(): #iterating through the row of selected fuel

                subset = value[i]>mean1
                if (subset.bool() == True): #returns a boolean value

                    print(value.index[i] ,value[i])
    elif (ft=='2'):
        diesel_ele = data.pop_data[data.pop_data["Fuel Type"]== "Diesel-Electric"]
        print(diesel_ele)
        mean1 =diesel_ele.iloc[:,[1,2,3,4,5,6] ].mean(axis =1)
        print("The mean vehicle population from (2006-2011)of Diesel- Electric: "+str(mean1))
        print("The year(s) and the vehicle population in that period which exceed the mean found above is/are: ")
        for i in range(1,7):
            for year, value in diesel_ele.iterrows():

                subset = value[i]>mean1
                if (subset.bool() == True):

                    print(value.index[i] ,value[i])
    elif(ft=='3'):
        electric = data.pop_data[data.pop_data["Fuel Type"]== "Electric"]
        print(electric)
        mean1 =electric.iloc[:,[1,2,3,4,5,6] ].mean(axis =1)
        print("The mean vehicle population from (2006-2011)of Electric: "+str(mean1))
        print("The year(s) and the vehicle population in that period which exceed the mean found above is/are: ")
        for i in range(1,7):
            for year, value in electric.iterrows():

                subset = value[i]>mean1
                if (subset.bool() == True):

                    print(value.index[i] ,value[i])
    elif(ft=='4'):
        petrol = data.pop_data[data.pop_data["Fuel Type"]== "Petrol"]
        print(petrol)
        mean1 =petrol.iloc[:,[1,2,3,4,5,6] ].mean(axis =1)
        print("The mean vehicle population from (2006-2011)of Electric: "+str(mean1))
        print("The year(s) and the vehicle population in that period which exceed the mean found above is/are: ")
        for i in range(1,7):
            for year, value in petrol.iterrows():

                subset = value[i]>mean1
                if (subset.bool() == True):

                    print(value.index[i] ,value[i])
    elif(ft =='5'):
            petrol_cng = data.pop_data[data.pop_data["Fuel Type"]== "Petrol-CNG"]
            print(petrol_cng)
            mean1 =petrol_cng.iloc[:,[1,2,3,4,5,6] ].mean(axis =1)
            print("The mean vehicle population from (2006-2011)of Electric: "+str(mean1))
            print("The year(s) and the vehicle population in that period which exceed the mean found above is/are: ")
            for i in range(1,7):
                for year, value in petrol_cng.iterrows():

                    subset = value[i]>mean1
                    if (subset.bool() == True):

                        print(value.index[i] ,value[i])

    elif(ft=='6'):
            petrol_ele = data.pop_data[data.pop_data["Fuel Type"]== "Petrol-Electric"]
            print(petrol_ele)
            mean1 =petrol_ele.iloc[:,[1,2,3,4,5,6] ].mean(axis =1)
            print("The mean vehicle population from (2006-2011)of Electric: "+str(mean1))
            print("The year(s) and the vehicle population in that period which exceed the mean found above is/are: ")
            for i in range(1,7):
                for year, value in petrol_ele.iterrows():

                    subset = value[i]>mean1
                    if (subset.bool() == True):

                        print(value.index[i] ,value[i])
    elif(ft == '7'):
            petrol_elep = data.pop_data[data.pop_data["Fuel Type"]== "Petrol-Electric (Plug-In)"]
            print(petrol_elep)
            mean1 =petrol_elep.iloc[:,[1,2,3,4,5,6] ].mean(axis =1)
            print("The mean vehicle population from (2006-2011)of Electric: "+str(mean1))
            print("The year(s) and the vehicle population in that period which exceed the mean found above is/are: ")
            for i in range(1,7):
                for year, value in petrol_elep.iterrows():

                    subset = value[i]>mean1
                    if (subset.bool() == True):

                        print(value.index[i] ,value[i])
