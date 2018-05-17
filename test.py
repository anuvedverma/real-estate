import zillow
import numpy as np


ZILLOW_API_KEY = 'X1-ZWz1gevn1g1l3f_91vx7'
api = zillow.ValuationApi()

address = "3400 Pacific Ave., Marina Del Rey, CA"
postal_code = "90292"

data = api.GetSearchResults(ZILLOW_API_KEY, address, postal_code)

print(data.get_dict())


# property_value = 249900
# closing_costs = 3000
# pct_down_payment = 0.32
# rehab_costs = 5000
# down_payment = property_value * pct_down_payment
# total_investment = down_payment + closing_costs + rehab_costs


# interest_rate = 0.04745
# loan_term = 30
# principal = property_value - down_payment

# monthly_income = {
# 	'rental_income': 2000,
# 	# 'airbnb_income': 1500
# }

# monthly_expenses = {
# 	'property_tax': property_value * (0.1 / 12),
# 	'insurance': 200,
# 	'utilities': 100,
# 	'hoa': 700,
# 	'repairs': 100,
# 	'vacancy': 200,
# 	'property_manager': monthly_income['rental_income'] * 0.1,
# 	'mortgage': abs(np.pmt(interest_rate / 12, loan_term * 12, principal))
# }

# monthly_cash_flow = sum(monthly_income.values()) - sum(monthly_expenses.values())

# roi = (monthly_cash_flow * 12) / total_investment

# print 'Monthly Income: $', round(sum(monthly_income.values()), 2)
# print 'Monthly Expenses: $', round(sum(monthly_expenses.values()), 2)
# print 'Monthly Cash Flow: $', round(monthly_cash_flow, 2)
# print 'ROI: ', round(roi * 100, 2), '%'
