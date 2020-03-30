import doctest

from digicolor.lib import colors

doctest.testmod(colors, extraglobs={"mycolor": colors.colors.add(colorid = 256, name = "AWESOME", value = 0x0fcdf7)})
