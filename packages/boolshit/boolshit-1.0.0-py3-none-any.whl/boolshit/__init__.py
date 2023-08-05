#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Consider this project as a practical joke, and academic curiosity, a piece
tangible eccentricity. A work of art if you will. With that out of the way;

Are you bored of the normal static booleans!? Order now and get the newfangled
Maybe! It exists in a superposition of True and False so you will never know
what you are getting! How exciting!

When will your while loops end? How fuzzy can your boolean logic get? Will
your assert statement fail or pass!? WILL YOU DIVIDE BY ZERO OR ONE!?!
------------------------------------------------------------------------------
As for the motivations behind this act of absurdity? Curiosity and learning.

Curiosity, which Maybe killed the cat. Exercise, that May-be was on the
subject of tedium. Madness, to which there Maybe was a method.
------------------------------------------------------------------------------
Usage: from boolshit import Maybe

>>> while Maybe: print("Loop is still running!")
...
Loop is still running!
Loop is still running!
Loop is still running!
>>>
>>> Maybe == Maybe; Maybe == Maybe
True
False
>>>
>>> 1/Maybe; 1/Maybe
1.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/mnt/c/Users/user/Desktop/maybe.py", line 127, in __rtruediv__
    def __rmul__(_self, other): return other*rnd() # x * M
ZeroDivisionError: division by zero
>>>
------------------------------------------------------------------------------
Maybe is a singleton instance of the maybe class. Maybe can be used in any
context that supports the classical, boring, booleans True and False.
The value of the singleton exists in a superposition of True and False. It
shall randomly collapse to either one of them upon being observed either
directly or indirectly. The only time Maybe will not collapse to boolean
is when it is not operator on. This happens only with plain "Maybe" by
itself when not in interactive prompt and with assignment ie. "x = Maybe".

This means that Maybe can be assigned as is and it will be both True and
False until the assigned variable is coerced to some other type. In
essence this means that you can but Maybe into any imaginable context
and it will behave exactly as True or False, depending on your luck.

Maybe obeys the limitations of a singleton pattern. "Maybe is Maybe" will
always be True, while "Maybe == Maybe" is determined on observation.

Below is a list of some example contexts that will accept Maybe, Both
left hand and right hand operations will work as one might expect.

bool(Maybe); +Maybe; -Maybe; ~Maybe; abs(Maybe); repr(Maybe); str(Maybe);
int(Maybe); float(Maybe); math.ceil(Maybe); math.floor(Maybe);
math.trunc(Maybe); Maybe + x; Maybe * x; Maybe ** x; Maybe >> x;
Maybe << x; Maybe % x; Maybe / x; Maybe // x; Maybe - x;
oct,bin,hex(Maybe), [1,2,3][Maybe]; round(Maybe); format(Maybe);
Maybe & x; Maybe | x; Maybe ^ x; Maybe < x; Maybe <= x; Maybe == x
Maybe != x; Maybe >= x; Maybe > x; divmod(Maybe, x)

Technical jargon: bool can not be subclassed with reasonable effort, so
maybe is a subclass of int as is bool. Maybe achieves the compatibility by
defining a counterpart to every method and attribute of booleans. While
strictly not bool, maybe is a bool in the practical sense. It acts like a
duck, it quacks like a duck, and thus it is a duck.
"""

from .maybe import Maybe

__version__ = "1.0.0"
__license__ = "The Unlicense"
__copyright__ = "Public Domain"
__author__ = "Markus Hirsimäki"
