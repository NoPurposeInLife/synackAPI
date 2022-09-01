#!/usr/bin/env python3

from synack import synack
from datetime import datetime

s1 = synack()
s1.gecko = False
s1.getSessionToken()




payins = s1.getTransactions_CashIn()

payins.reverse()

for payin in payins:
    print(payin)

current_month = 0
previous_month = 0
current_year = 0
previous_year = 0
month_payins_amount = 0
total_payins = len(payins)
i = 0
j = 0

for payin in payins:
    payin_date = payin.split(",")[0]
    amount = payin.split(",")[1]
    datetime_vuln_data_resolved_at = datetime.strptime(payin_date, '%Y-%m-%d')
    current_month = datetime_vuln_data_resolved_at.month
    current_year = datetime_vuln_data_resolved_at.year
    j += 1

    if i == 0:
        previous_month = datetime_vuln_data_resolved_at.month
        previous_year = datetime_vuln_data_resolved_at.year
        i += 1

    if current_month != previous_month:
        print("Year-Month: " + str(previous_year) + "-" + str(previous_month) + " Total payin: $" + str("%.2f" % round(month_payins_amount, 2)))
        month_payins_amount = 0
        i = 0
    else:
        previous_month = datetime_vuln_data_resolved_at.month
        previous_year = datetime_vuln_data_resolved_at.year
        month_payins_amount += float(amount)

    if j == total_payins:
        print("Year-Month: " + str(current_year) + "-" + str(current_month) + " Total payin: $" + str("%.2f" % round(month_payins_amount, 2)))

