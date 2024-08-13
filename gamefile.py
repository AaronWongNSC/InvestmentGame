## -- IMPORTS -- ##
import numpy.random

## -- GAME PARAMETERS -- ##

# General Parameters
start_age = 25
end_age = 75
num_sims = 1000
annual_investment = [ 2000 for _ in range(end_age - start_age) ]

# Savings Account
savings_growth_rate= 0.03
savings_sd = 0.01

# Low Risk Account
low_risk_market_growth_rate = 0.07
low_risk_market_sd = 0.07

# High Risk Account
high_risk_market_growth_rate = 0.10
high_risk_market_sd = 0.25

## -- SIMULATION CLASS -- ##
class simulation():
    def __init__(self):
        self.savings_account = [0]
        self.low_risk_account = [0]
        self.high_risk_account = [0]
        self.portfolio_value = [0]
        self.savings_change = [0]
        self.low_risk_market_change = [0]
        self.high_risk_market_change = [0]
        self.age = 0
        self.report = ''
        
    def decisions(self, deposit, strategy):
        # Make market decisions
        new_savings, new_low, new_high = strategy(self.age, self.portfolio_value[-1] + deposit)

        # Check for cheating
        if abs((new_savings + new_low + new_high) - (self.portfolio_value[-1] + deposit)) > 0.001:
            print('----------')
            print('VALUE MISMATCH AT INVESTMENT:')
            print('Age: {}'.format(self.age))
            print('Input portfolio: {}'.format(self.portfolio_value[-1] + deposit))
            print('Savings: {}'.format(new_savings))
            print('Low: {}'.format(new_low))
            print('High: {}'.format(new_high))
            print('Sum: {}'.format(new_savings + new_low + new_high))
            print('----------')
            return

        # Adjust Portfolio
        self.savings_account.append(new_savings)
        self.low_risk_account.append(new_low)
        self.high_risk_account.append(new_high)

    def market(self):
        # Simulate savings account
        self.savings_change.append(numpy.random.normal(savings_growth_rate, savings_sd))
        self.savings_account[-1] = self.savings_account[-1] * (1 + self.savings_change[-1])
        
        # Simulate low risk market
        self.low_risk_market_change.append(numpy.random.normal(low_risk_market_growth_rate, low_risk_market_sd))
        self.low_risk_account[-1] = self.low_risk_account[-1] * (1 + self.low_risk_market_change[-1])
        
        # Simulate high risk market
        self.high_risk_market_change.append(numpy.random.normal(high_risk_market_growth_rate, high_risk_market_sd))
        self.high_risk_account[-1] = self.high_risk_account[-1] * (1 + self.high_risk_market_change[-1])

        # Calculate the total value of the portfolio
        self.portfolio_value.append(self.calculate_portfolio_value())
    
    def calculate_portfolio_value(self):
        return self.savings_account[-1] + self.low_risk_account[-1] + self.high_risk_account[-1]
    
    def make_report(self):
        self.report += '''
----- Report Age {} -----

Market Conditions:
* Low Risk Market Change: {}
* High Risk Market Change: {}

Portfolio:
* Savings: {}
* Low Risk Investment: {}
* High Risk Investment: {}
* Total Value: {}

'''.format(self.age,
           self.low_risk_market_change[-1], self.high_risk_market_change[-1],
           self.savings_account[-1], self.low_risk_account[-1], self.high_risk_account[-1], self.portfolio_value[-1])

    def show_report(self):
        print(self.report)
        
    def show_graph(self):
        import matplotlib.pyplot as plt
        plt.plot(self.portfolio_value)
        plt.ylim(0,1500000)
        plt.show()
