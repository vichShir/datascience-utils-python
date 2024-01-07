import re

EMAIL_PATTERN = "([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)"
PHONE_PATTERN_1 = "(\(?\d{2}\)?\s)?(\(?\d{1,2}\)?\s)?(\d{4,6}[-. ]?\d{4,5})" # +55 (11) 123456-7890
PHONE_PATTERN_2 = "(\d{10,13})" #5511234567890
PHONE_PATTERN = PHONE_PATTERN_1 + "|" + PHONE_PATTERN_2
YEAR_PATTERN = "\s19\d{2}|20\d{2}"


def find_email(txt):
  return re.findall(EMAIL_PATTERN, txt)


def find_phone(txt):
  phone_list = []
  numbers_found = re.findall(PHONE_PATTERN, txt)
  for number in numbers_found:
    number = ''.join(number)
    phone = re.sub('[\s().+-]', '', number) # Remove special characters
    phone_list.append(phone)
  return phone_list


def find_year(txt):
  return list(map(str.strip, re.findall(YEAR_PATTERN, txt)))


def remove_multiple_spaces(txt):
  return re.sub(r'\W+', ' ', txt)