from_line = "From louis@media.berkely.edu Fri Jan 8 2020 18:20:40"
print("\n",from_line, "\n")

split_line = from_line.split(" ")
print(split_line)
print(split_line[1], "\n")

email = split_line[1]
split_email = email.split("@")
print(split_email, "\n")

organization = split_email[1]
print(organization)
