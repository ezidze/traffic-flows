import numpy as np
import matplotlib.pyplot as plt
import function as f


c = np.linspace( 0, 40, 41 ) #price of parking fee
x = np.linspace( 0.1, 1, 1000 )

#equilibrium region // plot

fig, ax = plt.subplots( figsize =  (12, 10) )

ax.plot(x, f.P(x,0), x, f.X( x ))

ax.set( xlabel = 'x', ylabel = 'func', title = 'Equilibrium region' )

ax.grid()

fig.savefig("Equilibrium_region.png", dpi = 400)

plt.show()

#budget calculated // plot

bal_serch = []

for i in c:

    bal_serch.append( f.balance_search(i)[-1] )

fig2, ax2 = plt.subplots( figsize =  (12, 10) )

ax2.plot( c, f.budget( np.asarray( bal_serch ) ), 'r-',

         c, f.budget_without_parking_fee( np.asarray( bal_serch ), c ), 'b-' )

ax2.set ( xlabel = 'price of parking', ylabel = 'budget', title = 'График функционала от стоимости парковки' )

ax2.legend( [ 'budget', 'budget without parking fee' ] )

ax2.grid()

plt.show()

fig2.savefig( 'budget.png', dpi = 400 )


