class eco_calc():
    def __init__(self):
        self.MU = []
        self.MU_price_ratio = []
    def marginal_utility(self,T_MU,QUANT):
        #print('The formula for Marginal Utility is: (change in total MU / change in quantity)') 
        MU = []
        count = 0
        for i,value in enumerate(QUANT):
            if value == 0: 
                MU.append('--')
                count -= 1
            else:
                try:
                    MU.append((T_MU[count+1] - T_MU[count])/(QUANT[count+1]-QUANT[count]))
                except:
                    print('How did I get an index error?')
            count += 1
        self.MU = MU
        return MU
    def marginal_price_ratio(self,MU,prices):
        mu_price_ratio = []
        for mu,price in zip(MU, prices):
            if type(mu) is not str:
                mu_price_ratio.append(round(mu/price,1))
            else:
                mu_price_ratio.append('--')
        return mu_price_ratio

     


