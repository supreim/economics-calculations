class eco_calc():
    def __init__(self):
        pass
    def marginal_utility(self,T_MU,QUANT):
        print('The formula for Marginal Utility is: (change in total MU / change in quantity)') 
        count = 0
        MU = []
        for i in range(len(T_MU)-1):
            if count == 0: 
                MU.append('--')
                count += count + 1
            MU.append(T_MU[i+1] - T_MU[i])
        print(MU)


if __name__ == "__main__":
    calc = eco_calc()
    calc.marginal_utility([0,100,300,300],[0,1,2,3])

    


