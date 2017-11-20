import re
p = re.compile('[0-9]{1,9}')
p1 = re.compile('[0-9]{1,9}.[0-9]{1,9}')
text = '1st member and 2nd member are visiting 105th visitor. There are 2 ballons, 158 balls, Rs.158965.9873, shell 345.987 in the shed.' 
newtext = p1.sub('0', p.sub('0',text))
print (newtext)
