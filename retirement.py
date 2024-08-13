'''
Savings Competition Simulator

Requires:
    - game file
    - strategy file (Unique to the student)
'''

## -- IMPORTS -- ##
import matplotlib.pyplot as plt
import statistics

from gamefile import *
from aaron_wong_1 import strategy

# Set random seed (if needed)
# numpy.random.seed(100)

## -- RUN SIMULATIONS -- ##
sims = [simulation() for _ in range(num_sims)]

for count, deposit in enumerate(annual_investment):
    age = count + start_age
    
    for sim in sims:
        sim.age = age
        sim.decisions(deposit, strategy)
        sim.market()
        sim.make_report()

totals = [ sim.calculate_portfolio_value() for sim in sims ]

## -- SCORING -- ##

counts = [
    sum([total < 100000 for total in totals]), # Below $100,000
    sum([total < 200000 for total in totals]), # Below $200,000
    sum([total > 500000 for total in totals]), # Above $500,000
    sum([total > 750000 for total in totals]), # Above $750,000
    sum([total > 1000000 for total in totals]), # Above $1,000,000
    sum([total > 2000000 for total in totals]), # Above $2,000,000
    sum([total > 3000000 for total in totals]), # Above $3,000,000
    sum([total > 4000000 for total in totals]), # Above $4,000,000
    sum([total > 5000000 for total in totals]), # Above $5,000,000
    ]

values = [
    -500, # Below $100,000
    -100, # Below $200,000
    10, # Above $500,000
    10, # Above $750,000
    10, # Above $1,000,000
    5, # Above $2,000,000
    5, # Above $3,000,000
    5, # Above $4,000,000
    5, # Above $5,000,000
    ]

total_score = sum( [counts[i] * values[i] for i in range(len(counts))] )

print('''
-- Final Scoring --
# below $100,000: {}
# below $200,000: {}
# above $500,000: {}
# above $750,000: {}
# above $1,000,000: {}
# above $2,000,000: {}
# above $3,000,000: {}
# above $4,000,000: {}
# above $5,000,000: {}

Median Value: {}
Mean Value: {}
SD: {}
Score: {}'''.format(*counts, statistics.median(totals), statistics.mean(totals), statistics.stdev(totals), total_score))

adjusted_totals = [ total if total < 5000000 else 5000000 for total in totals]
plt.hist(adjusted_totals, bins = [i * 50000 for i in range(101)])
plt.show()

'''
for count, sim in enumerate(sims[0:100]):
    plt.plot(sim.portfolio_value)
plt.show()
'''