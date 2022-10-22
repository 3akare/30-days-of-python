#!/usr/bin/env python3
'''
Day 5
30 days of python
'''

new_empty_list = []
not_empty_list = [1, 2, 34, 41, 2]
print(len(not_empty_list))
print(not_empty_list[0])
print(not_empty_list[len(not_empty_list) -1])
print(not_empty_list[int(len(not_empty_list) / 2)])

mixed_data = ['David', 19, 60.9, False, 'Abuja, Nigeria']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
new_empty_list = it_companies.copy()
print(mixed_data)
print(it_companies)
print(len(it_companies))
print(it_companies[len(it_companies) - 1])
print(it_companies[0])
print(it_companies[int(len(not_empty_list) / 2)])
it_companies[4] = 'Pied Piper'
print(it_companies)
it_companies.append('IBM')
print(it_companies)
it_companies.insert(5, 'Tesla')
print(it_companies)
it_companies[0] = it_companies[0].lower()
print(it_companies)
it_companies.append('#; ')
print(it_companies)
print('IBM' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
it_companies.reverse()
print(it_companies)
del it_companies[:3]
print(it_companies)

del it_companies[-3:]
print(it_companies)


print(new_empty_list)

i = 0
while (len(new_empty_list) != 3):
    del new_empty_list[0]
    del new_empty_list[-1]
print(new_empty_list)

i = 0
while (len(new_empty_list) > 0):
    del (new_empty_list[i])
print(new_empty_list)
del new_empty_list

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

fullstack = front_end + back_end
print(front_end)
print(fullstack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
j = ages[-1]
print(f'min: {ages[0]}\nmax: {ages[-1]}')
ages.append(ages[0])
ages.append(j)
print(ages)

sum = 0
for i in ages:
    sum += i
print(f'{sum/len(ages)}')
print(max(ages) - min(ages))

print((min(ages) - sum/len(ages)) > (max(ages) - sum/len(ages)))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

list1 = []
list2 = []

k = 0
for i in countries:
    if (k < len(countries) / 2):
        list1.append(i)
    else:
        list2.append(i)
    k += 1

hello = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_three = hello[:3]
del hello[:3]
scandic_count = hello
print(scandic_count)
print(first_three)
print(len(list1))
print(len(list2))