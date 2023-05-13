import json

def read_as_list(filename):
    iris_file=open(filename,'r')
    iris_list=iris_file.readlines()
    print('\nList Data:')
    for line in iris_list:
        print(line)
    iris_file.close()
    return iris_list

def read_as_dict(filename):
    iris_file=open(filename,'r')
    iris_dict=json.load(iris_file)
    print("\nDictionary Data: ")
    for line in iris_dict:
        print(line)
    iris_file.close()
    return iris_dict

def read_details(data_dict):
    print("\nAll flowers whose species is setosa")
    for i in data_dict:			      
        if (i['species']=='setosa'):
            print(i)

def area_species(dict_data):
    print("\nMinimum petal area and maximum sepal area")
    species_list = ( i['species'] for i in dict_data )           # species names
    species_list = list(set(species_list))
    for i in species_list:
        sepal_area = []                #list to store sepal and petal area
        petal_area = []
        for j in dict_data:
            if(j['species']==i):
                sepal_area.append(j['sepalLength']*j['sepalWidth'])
                petal_area.append(j['petalLength']*j['petalWidth'])
        print()
        print(i.capitalize())
        #print minimum and maximum areas
        print("Minimum Petal Area : ",round(min(petal_area),2))
        print("Maximum Sepal Area : ",round(max(sepal_area),2))

def sort(data):
    for i in data:
        total_area = (i['sepalLength']*i['sepalWidth'])+(i['petalLength']*i['petalWidth'])
        i.update({'totalArea':round(total_area,2)})
    data=sorted(data,key=lambda x:x['totalArea'])
    print("\nSorted List :")
    for i in data:
        print(i)

list_data = read_as_list('iris.json')
dict_data = read_as_dict('iris.json')
read_details(dict_data)
area_species(dict_data)
sort(dict_data)