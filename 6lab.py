# 6.	Реализация алгоритма рекомендательной системы.

dictScore = {"роман":[3,5,5,2,5],"комедия":[5,3,5,3,3,3], "драмма":[2,5,4], "детектив":[2,4,2,4,5], "фантастика":[5,3,4,2,3,2]}
averageLine = [3.4,3.75,4.75,2.25,3.75,3.5]
dictSIM = {"роман":[-0.4,1.25,0.25,-0.25,1.25],"комедия":[1.6,-0.75,0.25,0.75,-0.75,-0.5], "драмма":[-1.4,0.25,0.5], "детектив":[-1.4,0.25,-0.25,0.25,1.5], "фантастика":[1.6,-0.75,-0.75,-0.25,-0.75,-1.5]}
prod = -1.116415 #[-2.00704,0.17578125,-0.01171875,-0.01171875,0.17578125,0.5625]

rootSIM=1
for key in dictSIM:
    a=0
    for i in dictSIM[key]:a+=(i**2)
    rootSIM=rootSIM*(a**(1/2))
wSIM = prod/rootSIM
# print(wSIM)

ruj = dictScore["роман"]
rj = []
for key in dictScore:
    count=0
    summ=0
    for i in dictScore[key]: 
        count+=1
        summ+=i
    rj.append(summ/count)
# print(ruj,rj)
sim=0
for i in range(5):
    sim+=wSIM*(rj[i]-ruj[i])
    # print(wSIM*(rj[i]-ruj[i]))
# print(sim)
sim = sim/wSIM
rui=rj[0]+sim
print("Вероятное значение - ", rui)
