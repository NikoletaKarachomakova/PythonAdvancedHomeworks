countries = input().split(", ")
capitals =  input().split(", ")

dict = {country: capital for country, capital in zip(countries, capitals)}

[print(f"{key} -> {value}") for key, value in dict.items()]