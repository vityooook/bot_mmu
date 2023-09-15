import datetime
date = '2023.09.02'
data_clear = datetime.datetime.strptime(date, '%Y.%m.%d')

print(data_clear)