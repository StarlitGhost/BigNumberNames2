import math

# See print_number at bottom of file to use program

ones_names = {
  0:'',
  1:'un',
  2:'duo',
  3:'tre',
  4:'quattuor',
  5:'quin',
  6:'se',
  7:'septe',
  8:'octo',
  9:'nove'}

tens_names = {
    0:'',
    1:'deci',
    2:'viginti',
    3:'triginta',
    4:'quadraginta',
    5:'quinquaginta',
    6:'sexaginta',
    7:'septuaginta',
    8:'octoginta',
    9:'nonaginta'}

hundreds_names = {
    0:'',
    1:'centi',
    2:'ducenti',
    3:'trecenti',
    4:'quadringenti',
    5:'quingenti',
    6:'sescenti',
    7:'septingenti',
    8:'octingenti',
    9:'nongenti'}

ones_combiners = {
  0:[],
  1:[],
  2:[],
  3:['s','x'],
  4:[],
  5:[],
  6:['s','x'],
  7:['m','n'],
  8:[],
  9:['m','n']}

tens_combiners = {
    0:[],
    1:['n'],
    2:['m','s'],
    3:['n','s'],
    4:['n','s'],
    5:['n','s'],
    6:['n'],
    7:['n'],
    8:['m','x'],
    9:[]}

hundreds_combiners = {
    0:[],
    1:['n','x'],
    2:['n'],
    3:['n','s'],
    4:['n','s'],
    5:['n','s'],
    6:['n'],
    7:['n'],
    8:['m','x'],
    9:[]}

normal_no_illion = {
    0:"thousand",
    1:"milli",
    2:"billi",
    3:"trilli",
    4:"quadrilli",
    5:"quintilli",
    6:"sextilli",
    7:"septilli",
    8:"octilli",
    9:"nonilli"}


def get_powers(n):
  """
  Returns a list where the last element in the list is how many 1000**0's fit into n,
  the second to last element is how many 1000**1's fit into n
  the third to last element is how many 1000**2 fit into n
  >>> get_powers( 603 )
  [603]
  >>> get_powers( 1002 )
  [1, 2]
  >>> get_powers( 1683 )
  [1, 683]
  >>> get_powers( 59052 )
  [59, 52]
  >>> get_powers( 3000003 )
  [3, 0, 3]
  """

  #find the largest power of 10 that fits into q
  i = int(math.floor(math.log(n,1000))) # is largest power of 1000 that fits into n
  a = 1000**i # the power itself

  # see get_powers docstring for explanation of array
  powers = [0] # stands for first 1000
  for j in range(i):
    powers.append(0)

  # find out how much of each power of 1000 fits into n
  q = n
  for i in range(len(powers)):
    num_that_fit = q / a
    powers[i] = num_that_fit
    q = q % a
    a /= 1000

  return powers


def common_letter(a,b):
  """returns a common element lists. null otherwise"""
  for i in a:
    if i in b:
      return i
  return None


def get_name(n):
  """
  Returns the name for any power of 10 from n**3 to n**999
  Refers to global variables: hundreds_names, tens_names, ones_names, normal_no_illion, ones_combiners, tens_combiners, hundreds_combiners
  """

  # do not need the conway weschler algorithm to determine the name of anything less than 10^33
  if n < 10 and n >= 0:
    return normal_no_illion[n]
  if n < 0:
    return ""

  # find the number of hundreds, tens and ones that fit into n & get the appropriate name
  q = n
  n_hundreds = q / 100
  hundreds = hundreds_names[n_hundreds] if n_hundreds > 0 else ""

  q %= 100
  n_tens = q / 10
  tens = tens_names[n_tens] if n_tens > 0 else ""

  n_ones = q % 10
  ones = ones_names[n_ones] if n_ones > 0 else ""

  # start assembling the name
  name = ones

  # find the combining letters, if any
  ones_and_tens_letter = common_letter(ones_combiners[n_ones], tens_combiners[n_tens])
  if ones_and_tens_letter != None:
    name += ones_and_tens_letter if n_ones != 3 else 's' # for special case of tre, only add 's'
  elif not tens: # can't use a common letter between ones and tens, ones and hundreds
    ones_and_hundreds_letter = common_letter(ones_combiners[n_ones], hundreds_combiners[n_hundreds])
    if ones_and_hundreds_letter != None:
      name += ones_and_hundreds_letter if n_ones != 3 else 's' # for special case of tre, only add 's'

  name += tens
  name += hundreds

  # remove any vowels at the end
  if name[-1] in ['a','e','i','o','u']:
    name = name[0:-1]

  return name


def bignumexp(n):
  """
  Returns the english name of any nth power of 10 (10^n) up to infinity
  """
  q = (n - 3)/3

  # if q is 999 or less, don't need to combine names with illi
  if q <= 999:
    name = get_name(q)
    suffix = ""
    if q > 9:
      suffix = "illion"
    elif q > 0: # between 9 and 0
        suffix = "on"
    return name + suffix

  # otherwise, we have to use the 1,000,000,000,000W ... 1000000X + 1000Y + Z algorithm
  name = ""
  powers = get_powers(q) # powers is arranged from highest to lowest
  for i in range(len(powers)):
    name += get_name(powers[i]) if powers[i] > 0 else "nilli"
    # combine each name with illi
    if i < len(powers) - 1 and name[len(name)-4:len(name)] != "illi":
      name += "illi"

  # if the last name begins with anything other than i, add illion
  # otherwise add on
  name += "on" if name[-1] == "i" else "illion"

  return name


# http://www.blog.pythonlibrary.org/2010/10/21/python-converting-numbers-to-words/
# print the name of any number less than 999

_SMALL = {
    '0' : '',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen',
    '20' : 'twenty',
    '30' : 'thirty',
    '40' : 'forty',
    '50' : 'fifty',
    '60' : 'sixty',
    '70' : 'seventy',
    '80' : 'eighty',
    '90' : 'ninety'}


def get_num(num):
    '''Get token <= 90, return '' if not matched'''
    return _SMALL.get(num, '')

 
def norm_num(num):
    """Normalize number (remove 0's prefix). Return number and string"""
    n = int(num)
    return n, str(n)

 
def small2eng(num):
    """English representation of a number <= 999"""
    n, num = norm_num(num)
    hundred = ''
    ten = ''
    if len(num) == 3: # Got hundreds
        hundred = get_num(num[0]) + ' hundred'
        num = num[1:]
        n, num = norm_num(num)
    if (n > 20) and (n != (n / 10 * 10)): # Got ones
        tens = get_num(num[0] + '0')
        ones = get_num(num[1])
        ten = tens + ' ' + ones
    else:
        ten = get_num(num)
    if hundred and ten:
        return hundred + ' ' + ten
        #return hundred + ' and ' + ten
    else: # One of the below is empty
        return hundred + ten


def split_number(n_str):
  """This takes a number and splits it into groups of 3 digits"""
  result = []

  power = 0

  while len(n_str) > 3:
    dig = n_str[-3:]
    result.append(dig[0] + dig[1] + dig[2])
    n_str = n_str[:-3]

  if len(n_str) > 0:
    result.append(n_str)

  result.reverse()

  return result


def print_number(n_str):
  """Takes a number up to infinity and prints the english name
  >>> print_number("7823479018273487912534987162938476182734589127364981273649812734689")
  seven unvigintillion eight hundred twenty three vigintillion four hundred seventy nine novendecillion eighteen octodecillion two hundred seventy three septendecillion four hundred eighty seven sedecillion nine hundred twelve quindecillion five hundred thirty four quattuordecillion nine hundred eighty seven tredecillion one hundred sixty two duodecillion nine hundred thirty eight undecillion four hundred seventy six decillion one hundred eighty two nonillion seven hundred thirty four octillion five hundred eighty nine septillion one hundred twenty seven sextillion three hundred sixty four quintillion nine hundred eighty one quadrillion two hundred seventy three trillion six hundred forty nine billion eight hundred twelve million seven hundred thirty four thousand six hundred eighty nine
  """
  groups = split_number(n_str)
  #print ",".join(groups)
  ret = []
  for i in range(len(groups)):
    if groups[i] != '000':
      power_name = bignumexp(3*(len(groups)-(i+1)))
      small_name = small2eng(groups[i])
      ret.append(small_name)
      ret.append(power_name)
      #print small_name, power_name
  return "\n".join(ret)


if __name__ == "__main__":
  print "The english name for 7823479018273487912534987162938476182734589127364981273649812734689 is"
  print print_number("7823479018273487912534987162938476182734589127364981273649812734689")

