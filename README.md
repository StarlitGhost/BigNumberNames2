BigNumberNames2
===============

This is the canonical implementation of the Conway-Weschler algorithm.


BigNumberNames
Print the latin name of any number up to infinity!

This is a python implementation of the Conway-Weschler algorithm. http://mrob.com/pub/math/largenum.html#conway-wechsler Along with Conway's Game of Life, Conway helped create an algorithm to produce latin names for any number up to infinity. This is an implementation of that algorithm.

How To Use
>>> from bignumbers import print_number

>>> print_number("7823479018273487912534987162938476182734589127364981273649812734689")
seven unvigintillion eight hundred twenty three vigintillion 
four hundred seventy nine novendecillion eighteen octodecillion 
two hundred seventy three septendecillion four hundred eighty 
seven sedecillion nine hundred twelve quindecillion five hundred 
thirty four quattuordecillion nine hundred eighty seven tredecillion 
one hundred sixty two duodecillion nine hundred thirty eight 
undecillion four hundred seventy six decillion one hundred eighty 
two nonillion seven hundred thirty four octillion five hundred eighty 
nine septillion one hundred twenty seven sextillion three hundred 
sixty four quintillion nine hundred eighty one quadrillion two hundred 
seventy three trillion six hundred forty nine billion eight hundred 
twelve million seven hundred thirty four thousand six hundred eighty nine
I encourage you to try this tool with numbers of to a couple hundred megabytes of digits. After that, you may run out of memory since it's not a supercomputer program. It could be one, if you so desire.

AFAIK, this is the only implementation of this algorithm.

License
The content of the site (i.e., blog posts and page content) is licensed under a Creative Commons Attribution License: you may use it, but you must give attribution.

You may feel free to reuse any part of the structure, design, and layout of this site; it is all licensed under the MIT License.

