#simulations.py

#import libraries
import numpy as np
import matplotlib.pyplot as plt

#simulation data
data = {
        'initial debt': 140000,
        'monthly interest rate': 0.05,
        'incomes': {
            'mean monthly income': 25000,
            'standard deviation montly income': 5000
            },
        'expenses': {
            'mean monthly expense': 20000,
            'standard deviation monthly expense': 6500
            }
        }

#simulation parameters
simulation_months = 12

#simulation functions
def simulate_income(data):
    return np.random.normal(data['incomes']['mean monthly income'],
                            data['incomes']['standard deviation montly income'],
                            simulation_months)

def simulate_expense(data):
    return np.random.normal(data['expenses']['mean monthly expense'],
                            data['expenses']['standard deviation monthly expense'],
                            simulation_months)

def simulate_earnings(data):
    incomes = simulate_income(data)
    expenses = simulate_expense(data)
    earnings = incomes - expenses
    return earnings

#main
if __name__ == '__main__':
    n_sims = 5
    plt.figure()
    for i in range(n_sims):
        plt.plot(simulate_earnings(data),label=f'simulation {i+1}')
    plt.legend()
    plt.show()
    