letter = "Hey My Name is {1} and I am from {0}"
country = "India"
name = "Vinayak"
# This a basic way to represnt string formatting



# This Is called as F-String
print(letter.format(country, name))
print(f"Hey My Name is {name} and I am from {country}")
# Its syntax is print(string_name.format(format1, format2))
# and remeber to use print(f" string_value{format1}")

print(f"Hey My Name is {{name}} and I am from {{country}}")
# to print {} we do double {{}} this
