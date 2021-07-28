import data
def incr_pop():
        ft = input("Select Fuel Type From Below:\n 1. Diesel \n 2. Diesel-Electric\n 3. Electric\n 4. Petrol\n 5. Petrol-CNG\n 6. Petrol-Electric 7. Petrol-Electric (Plug-In)\n")
        if ft =='1':
                    diesel = data.pop_data[data.pop_data["Fuel Type"]== "Diesel"] # selecting data of given fuel type
                    print(diesel)
                    print(" The years and population in which the vehicle population has increased by at least 15% over the previous year are:")
                    for i in range(2,13):
                        for year, value in diesel.iterrows():
                            incr = value[i]*0.15 + value[i]
                            subset = incr>= value[i-1]


                            if (subset == True):
                                 print( str(value.index[i]) +"-"+str(value[i]))
        if ft =='2':
                    diesel_ele = data.pop_data[data.pop_data["Fuel Type"]== "Diesel-Electric"] # selecting data of given fuel type
                    print(diesel_ele)
                    print(" The years and population in which the vehicle population has increased by at least 15% over the previous year are:")
                    for i in range(2,13):
                        for year, value in diesel_ele.iterrows():
                            incr = value[i]*0.15 + value[i]
                            subset = incr>= value[i-1]


                            if (subset == True):
                                 print( str(value.index[i]) +"-"+str(value[i]))

        if ft =='3':
                    electric = data.pop_data[data.pop_data["Fuel Type"]== "Electric"] # selecting data of given fuel type
                    print(electric)
                    print(" The years and population in which the vehicle population has increased by at least 15% over the previous year are:")
                    for i in range(2,13):
                        for year, value in electric.iterrows():
                            incr = value[i]*0.15 + value[i]
                            subset = incr>= value[i-1]


                            if (subset == True):
                                 print( str(value.index[i]) +"-"+str(value[i]))
        if ft =='4':
                    petrol = data.pop_data[data.pop_data["Fuel Type"]== "Petrol"] # selecting data of given fuel type
                    print(petrol)
                    print(" The years and population in which the vehicle population has increased by at least 15% over the previous year are:")
                    for i in range(2,13):
                        for year, value in petrol.iterrows():
                            incr = value[i]*0.15 + value[i]
                            subset = incr>= value[i-1]


                            if (subset == True):
                                 print( str(value.index[i]) +"-"+str(value[i]))
        if ft =='5':
                    petrol_cng = data.pop_data[data.pop_data["Fuel Type"]== "Petrol-CNG"] # selecting data of given fuel type
                    print(petrol_cng)
                    print(" The years and population in which the vehicle population has increased by at least 15% over the previous year are:")
                    for i in range(2,13):
                        for year, value in petrol_cng.iterrows():
                            incr = value[i]*0.15 + value[i]
                            subset = incr>= value[i-1]


                            if (subset == True):
                                 print( str(value.index[i]) +"-"+str(value[i]))

        if ft =='6':
                    petrol_ele = data.pop_data[data.pop_data["Fuel Type"]== "Petrol-Electric"] # selecting data of given fuel type
                    print(petrol_ele)
                    print(" The years and population in which the vehicle population has increased by at least 15% over the previous year are:")
                    for i in range(2,13):
                        for year, value in petrol_ele.iterrows():
                            incr = value[i]*0.15 + value[i]
                            subset = incr>= value[i-1]


                            if (subset == True):
                                 print( str(value.index[i]) +"-"+str(value[i]))
        if ft =='7':
                    petrol_elep = data.pop_data[data.pop_data["Fuel Type"]== "Petrol-Electric (Plug-In)"] # selecting data of given fuel type
                    print(petrol_elep)
                    print(" The years and population in which the vehicle population has increased by at least 15% over the previous year are:")
                    for i in range(2,13):
                        for year, value in petrol_elep.iterrows():
                            incr = value[i]*0.15 + value[i]
                            subset = incr>= value[i-1]


                            if (subset == True):
                                 print( str(value.index[i]) +"-"+str(value[i]))
