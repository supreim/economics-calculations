from economics_calculations import eco_calc


calc = eco_calc()
mu = calc.marginal_utility([0,100,200,300],[0,1,2,3])
mu_price_ratio = calc.marginal_price_ratio(mu, [1,2,3,4])

print(mu)
print(mu_price_ratio)
