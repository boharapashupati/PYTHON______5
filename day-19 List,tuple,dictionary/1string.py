

# capitalize  : capitalize() function ले string को पहिलो अक्षरलाई ठूला अक्षर (uppercase) बनाउँछ,
# अनि बाँकी सबै अक्षरलाई सानो अक्षर (lowercase) मा परिवर्तन गर्छ।
# Example:

name = "pASHUPATI"
print(name.capitalize())
# Output: Pashupati

# lower      : lower() function ले string का सबै अक्षरलाई सानो अक्षर (lowercase) मा परिवर्तन गर्छ।

city = "KATHMANDU"
print(city.lower())
# Output: kathmandu

# upper      : upper() function ले string का सबै अक्षरलाई ठूला अक्षर (uppercase) मा परिवर्तन गर्छ।
country = "nepal"
print(country.upper())
# Output: NEPAL

# title      : title() function ले string का प्रत्येक शब्दको पहिलो अक्षरलाई ठूला अक्षर (uppercase) मा परिवर्तन गर्छ।
book_title = "RICH DAD POOR DAD"
print(book_title.title())
# Output: Rich Dad Poor Dad

# swapcase   : swapcase() function ले string का ठूला अक्षरलाई सानो अक्षर (lowercase) मा र साना अक्षरलाई ठूला अक्षर (uppercase) मा परिवर्तन गर्छ।

sentence = "i miss you Daddy"
word = "I MISS YOU mummy"
print(sentence.swapcase())  # Output: I MISS YOU dADDY
print(word.swapcase())  # Output: i miss you MUMMY

print(sentence.swapcase() + " | " + word.swapcase()) 
# Output: I MISS YOU dADDY | i miss you MUMMY  



#  confused strip method    *

# strip      : strip() function ले string को सुरुवात र अन्त्यका whitespace (जस्तै space, tab, newline) लाई हटाउँछ।

text = "                                                                                     Hello, World!   "
print(text.strip())
# Output: Hello, World!

# lstrip     : lstrip() function ले string को सुरुवातका whitespace लाई मात्र हटाउँछ।  *
 
country_name = "                                                   Nepal             "
print(country_name.lstrip())
# Output: Nepal

# rstrip     : rstrip() function ले string को अन्त्यका whitespace लाई मात्र हटाउँछ।  *
state_name = "  Jhapa             "
print(state_name.rstrip())
# Output: Jhapa


# split      : split() function ले string लाई एक वा धेरै delimiters (जस्तै space, comma) को आधारमा टुक्रा टुक्रा पार्छ र एउटा list मा परिणत गर्छ।
sentence = "Hello, World! How are you?"
print(sentence.split())  # Default delimiter is space
# Output: ['Hello,', 'World!', 'How', 'are', 'you?']



# split(',') : split() function लाई comma (,) delimiter को आधारमा टुक्रा टुक्रा पार्न पनि प्रयोग गर्न सकिन्छ।
csv_data = "name,age,city"
print(csv_data.split(','))  # Splitting by comma
# Output: ['name', 'age', 'city']

# join       : join() function ले list का elements लाई एक string मा परिणत गर्छ, जसमा delimiter को रूपमा प्रयोग गरिन्छ।
words = ['Hello', 'World', 'Python']
delimiter = ' '
print(delimiter.join(words))
# Output: Hello World Python

#     : replace() function ले string मा कुनै substring लाई अर्को substring सँग परिवर्तन गर्छ।   *
text = "Hello, bipna!"
print(text.replace("python ","sita"))
# Output: Hello, bipna!

# find       : find() function ले string मा कुनै substring को पहिलो occurrence को index फिर्ता गर्छ। यदि substring भेटिएन भने -1 फिर्ता गर्छ।
text = "Hello, World!"
index = text.find("python")
print(index)  # Output: 7



