# 'key' : 'value'
# keys are unique
convert_month={
    'jan' : 'january',
    'feb' : 'febraury',
    'mar' : 1
}
print(convert_month['mar'])
print(convert_month.get('jan'))
print(convert_month.get('april','the value is not exist'))
print(convert_month.get('april'))
print(convert_month.keys())
print(convert_month.values())

