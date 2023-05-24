import pandas as pd


#let's try with list
'''
lst = [[New York,Male,4125000], [New York,Female,4300000],[Los Angeles,Male,1985000],[Los Angeles,Female,2070000],[Chicago,Male,1350000],[Chicago,Female,1400000],[Houston,Male,1100000],[Houston,Female,1120000],[Phoenix,Male,800000],[Phoenix,Female,810000],[Philadelphia,Male,750000],[Philadelphia,Female,770000]]
res= pd.DataFrame(lst, Columns=["City", "Gender", "Population"])
res
#print("")
'''
#,"Chicago","Chicago","Houston","Houston","Phoenix","Phoneix","Philadelphia"
dic = {"City": ["NewYork","NewYork","Los Angels", "Los Angels"],
       "Gender":["Male","Female","Male","Female"],
       "Population":[410000,540000,670000,980000]}
res= pd.DataFrame(dic)
res

'''
If res["Population"].max()== dic.population[i]
dic.Population()
'''
temp = res["Population"].max()
for i in dic["Population"]:
  if temp ==i:
    print()
  #if Gender[i]=="Male" and Population[i]==res["Population"].max():

print("City with most male population", res["Population"].max())
