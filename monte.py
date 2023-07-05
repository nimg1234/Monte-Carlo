import numpy.random as random
timesteps = 30
starting_price = 600
volatility = 0.02   
max_simulations = 5000
paths=[]
m=0
while m<max_simulations:
    c=0
    ps=[]
    ps.append(starting_price)
    price=starting_price*(1+random.normal(0,volatility))
    ps.append(price)
    
    for y in range(timesteps):
        if c==29:
            break
        price=ps[c+1]*(1+random.normal(0,volatility))
        ps.append(price)
        c+=1
    paths.append(ps)
    m=m+1
final_values=[]
j=0
while j<len(paths):
    for k in paths:
        final_values.append(paths[j][-1]
        j+=1
plot_paths(paths, starting_price)
plot_final_dist(final_values)
