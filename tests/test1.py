#!/usr/bin/env python

from bignumbers import *

def old_get_powers(n):
  #find the largest power of 10 that fits into q
  q = n
  a = 1000
  powers = []
  powers.append(0)
  while a < q:
    a *= 1000
    powers.append(0)


  # if the largest power of a doesn't divide q, divide a by 1000 & don't add an extra power
  if q / a == 0:
    a /= 1000
  else: # leave it be
    powers.append(0)


  old_q = q # ewwww old q..? that's naaaasssttttyyyyy!
  i = len(powers)-1
  #print "a is",a
  while a > 0:
    num_that_fit = q / a
    powers[i] = num_that_fit
    q = q % a
    a /= 1000
    i -= 1
    #print "a is",a
  q = old_q

  return powers

  #for p in range(len(powers)):
    #print "Can fit",powers[p],"of",pow(1000,p),"into",q

def test():
  cases = {}
  cases["39 "]="duodecillion"
  cases["42 "]="tredecillion"
  cases["45 "]="quattuordecillion"
  cases["48 "]="quindecillion"
  cases["51 "]="sedecillion"
  cases["57 "]="octodecillion"
  cases["60 "]="novendecillion"
  cases["63 "]="vigintillion"
  cases["66 "]="unvigintillion"
  cases["69 "]="duovigintillion"
  cases["78 "]="quinvigintillion"
  cases["84 "]="septemvigintillion"
  cases["87 "]="octovigintillion"
  cases["90 "]="novemvigintillion"
  cases["93 "]="trigintillion"
  cases["99 "]="duotrigintillion"
  cases["102    "]="trestrigintillion"
  cases["108    "]="quintrigintillion"
  cases["123    "]="quadragintillion"
  cases["138    "]="quinquadragintillion"
  cases["144    "]="septenquadragintillion"
  cases["153    "]="quinquagintillion"
  cases["168    "]="quinquinquagintillion"
  cases["186    "]="unsexagintillion"
  cases["213    "]="septuagintillion"
  cases["243    "]="octogintillion"
  cases["261    "]="sexoctogintillion"
  cases["300    "]="novenonagintillion"
  cases["303    "]="centillion"
  cases["306    "]="uncentillion"
  cases["309    "]="duocentillion"
  cases["312    "]="trescentillion"
  cases["342    "]="tredecicentillion"
  cases["351    "]="sedecicentillion"
  cases["366    "]="unviginticentillion"
  cases["402    "]="trestrigintacentillion"
  cases["543    "]="octogintacentillion"
  cases["603    "]="ducentillion"
  cases["624    "]="septenducentillion"
  cases["903    "]="trecentillion"
  cases["1002   "]="trestrigintatrecentillion"
  cases["1683   "]="sexagintaquingentillion"
  cases["1803   "]="sescentillion"
  cases["2421   "]="sexoctingentillion"
  cases["3000   "]="novenonagintanongentillion"
  cases["3003   "]="millinillion"
  cases["3006   "]="millimillion"
  cases["3009   "]="millibillion"
  cases["3012   "]="millitrillion"
  cases["3042   "]="millitredecillion"
  cases["3705   "]="milliquattuortrigintaducentillion"
  cases["19683  "]="sextillisexagintaquingentillion"
  cases["59052  "]="novendecillitresoctogintasescentillion"
  cases["3000003    "]="millinillinillion"

  #import ipdb
  #ipdb.set_trace()
  
  keys = cases.keys()
  f = lambda x,y: int(x)-int(y)
  keys = sorted(keys, f)
  for c in keys:
    try:
      p = get_powers(int(c))
      if get_name(int(c)) != get_name(int(c)):
        #print ">>> get_powers(",int(c), ")"
        #print get_powers(int(c))
        print "Case:", c, "should've returned", old_get_powers(int(c)), "it returned", get_powers(int(c))
    except:
      print "Messed up on",c
      #import ipdb
      #ipdb.set_trace()





if __name__ == "__main__":
  test()

