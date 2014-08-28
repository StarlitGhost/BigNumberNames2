#!/usr/bin/python

from bignumbers import small2eng


def test():
  cases = {}
  cases["39"] = "thirty nine"
  cases["42"] = "forty two"
  cases["45"] = "forty five"
  cases["48"] = "forty eight"
  cases["51"] = "fifty one"
  cases["57"] = "fifty seven"
  cases["60"] = "sixty"
  cases["63"] = "sixty three"
  cases["66"] = "sixty six"
  cases["69"] = "sixty nine"
  cases["78"] = "seventy eight"
  cases["84"] = "eighty four"
  cases["87"] = "eighty seven"
  cases["90"] = "ninety"
  cases["93"] = "ninety three"
  cases["99"] = "ninety nine"
  cases["102"] = "one hundred two"
  cases["108"] = "one hundred eight"
  cases["123"] = "one hundred twenty three"
  cases["138"] = "one hundred thirty eight"
  cases["144"] = "one hundred forty four"
  cases["153"] = "one hundred fifty three"
  cases["168"] = "one hundred sixty eight"
  cases["186"] = "one hundred eighty six"
  cases["213"] = "two hundred thirteen"
  cases["243"] = "two hundred forty three"
  cases["261"] = "two hundred sixty one"
  cases["300"] = "three hundred"
  cases["303"] = "three hundred three"
  cases["306"] = "three hundred six"
  cases["309"] = "three hundred nine"
  cases["312"] = "three hundred twelve"
  cases["342"] = "three hundred forty two"
  cases["351"] = "three hundred fifty one"
  cases["366"] = "three hundred sixty six"
  cases["402"] = "four hundred two"
  cases["543"] = "five hundred forty three"
  cases["603"] = "six hundred three"
  cases["624"] = "six hundred twenty four"
  cases["903"] = "nine hundred three"   

  #import ipdb
  #ipdb.set_trace()
  
  keys = cases.keys()
  f = lambda x,y: int(x)-int(y)
  keys = sorted(keys, f)
  for c in keys:
    try:
      if small2eng(int(c)) != cases[c]:
        print "Case:", c, "printed",small2eng(int(c)),"instead of",cases[c]
        #print "cases[\""+str(int(c))+"\"] = \""+small2eng(int(c))+"\""
    except Exception as e:
      print "Messed up on",c, e
      #import ipdb
      #ipdb.set_trace()



if __name__ == "__main__":
  test()

