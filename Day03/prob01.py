
months = ['dec', 'oct', 'aug', 'sep', 'jan', 'may', 'feb',
'jul', 'nov', 'mar', 'apr', 'jun']

# sort the above list according to the clendar

print(f"months :{months}")

print("-" * 60)
from calendar import month_abbr
print(list(month_abbr))

print("-" * 60)
res = sorted(months, key=list(map(lambda x : x.lower(), list(month_abbr))).index)
print(f"Sorted Months :{res}")
