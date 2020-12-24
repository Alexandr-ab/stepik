assert abs(-42) == 42, 'Not correct'

print('Let\'s count together: {}, then {}, then {}'.format('one', 'two', 'three'))

st1 = 'one'
st2 = 'two'
st3 = 'three'

print(f'Let\'s count together: {st1}, then {st2}, then {st3}')

print(f'{2+3}')

s = 'My Name is Alex'

if 'Name' in s:
    print('Sustring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')