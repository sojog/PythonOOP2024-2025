
import pycountry
print(len(pycountry.countries))

# Pentru a itera prin tari
country_codes = []
for country in pycountry.countries:
    country_codes.append(country.alpha_2)

print(country_codes)

germany = pycountry.countries.get(alpha_2='DE')
print(germany)

