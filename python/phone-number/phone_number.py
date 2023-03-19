import re

class PhoneNumber:
    def __init__(self, number):

        phoneRegex = re.compile(r'''(
            ( \+\d\s* | \d\s* )? # country code
            ( [2-9]{1}\d{2} | \([2-9]{1}\d{2}\) ) # area code
            ( \s | - | \. )*  # separator
            ( [2-9]{1}\d{2} ) # exchange code
            ( \s | - | \. )*  # separator
            ( \d{4} )         # subscriber number
            )''', re.VERBOSE)

        num = phoneRegex.findall(number)
        if not num:
            raise ValueError("Number is not correctly formatted")

        _, country_code, area, _, exch_code, _, subs_num = num[0]
        if country_code and country_code.strip('+ ') != '1':
            raise ValueError("Incorrect country code")
        self.area_code = area.strip('()')
        self.number = self.area_code + exch_code + subs_num

    def pretty(self):
        return f'({self.area_code})-{self.number[3:6]}-{self.number[6:]}'

