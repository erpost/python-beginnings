numbers = ['2.23', '.1233', '1', '4.223', '6.2']

for x in numbers:
    print('{0: >#001.12f}'. format(float(x)))
    print('{0: #1.12f}'.format(float(x)))

print()

v=10.4
print('% 6.2f' % v)
print('% 12.1f' % v)
print('%012.1f' % v)
