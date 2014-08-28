#!/usr/bin/python

from bignumbers import bignumexp


def test():
  cases = {}
  cases["5  "]="thousand"
  cases["6  "]="million"
  cases["9  "]="billion"
  cases["12 "]="trillion"
  cases["15 "]="quadrillion"
  cases["18 "]="quintillion"
  cases["21 "]="sextillion"
  cases["24 "]="septillion"
  cases["27 "]="octillion"
  cases["30 "]="nonillion"
  cases["33 "]="decillion"
  cases["36 "]="undecillion"
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
      if bignumexp(int(c)) != cases[c]:
        print "Case:", c, "printed",bignumexp(int(c)),"instead of",cases[c]
    except Exception as e:
      print "Messed up on",c, e
      #import ipdb
      #ipdb.set_trace()





if __name__ == "__main__":
  test()



