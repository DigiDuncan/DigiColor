import re

from digicolor.lib.utils import AttrDict

default_colors = {
    "BLACK": 0x000000,
    "RED": 0x800000,
    "GREEN": 0x008000,
    "YELLOW": 0x808000,
    "BLUE": 0x000080,
    "MAGENTA": 0x800080,
    "CYAN": 0x008080,
    "LIGHT_GRAY": 0xc0c0c0,
    "DARK_GRAY": 0x808080,
    "LIGHT_RED": 0xff0000,
    "LIGHT_GREEN": 0x00ff00,
    "LIGHT_YELLOW": 0xffff00,
    "LIGHT_BLUE": 0x0000ff,
    "LIGHT_MAGENTA": 0xff00ff,
    "LIGHT_CYAN": 0x00ffff,
    "WHITE": 0xffffff,
    "GREY_0": 0x000000,
    "NAVY_BLUE": 0x00005f,
    "DARK_BLUE": 0x000087,
    "BLUE_3A": 0x0000af,
    "BLUE_3B": 0x0000d7,
    "BLUE_1": 0x0000ff,
    "DARK_GREEN": 0x005f00,
    "DEEP_SKY_BLUE_4A": 0x005f5f,
    "DEEP_SKY_BLUE_4B": 0x005f87,
    "DEEP_SKY_BLUE_4C": 0x005faf,
    "DODGER_BLUE_3": 0x005fd7,
    "DODGER_BLUE_2": 0x005fff,
    "GREEN_4": 0x008700,
    "SPRING_GREEN_4": 0x00875f,
    "TURQUOISE_4": 0x008787,
    "DEEP_SKY_BLUE_3A": 0x0087af,
    "DEEP_SKY_BLUE_3B": 0x0087d7,
    "DODGER_BLUE_1": 0x0087ff,
    "GREEN_3A": 0x00af00,
    "SPRING_GREEN_3A": 0x00af5f,
    "DARK_CYAN": 0x00af87,
    "LIGHT_SEA_GREEN": 0x00afaf,
    "DEEP_SKY_BLUE_2": 0x00afd7,
    "DEEP_SKY_BLUE_1": 0x00afff,
    "GREEN_3B": 0x00d700,
    "SPRING_GREEN_3B": 0x00d75f,
    "SPRING_GREEN_2A": 0x00d787,
    "CYAN_3": 0x00d7af,
    "DARK_TURQUOISE": 0x00d7d7,
    "TURQUOISE_2": 0x00d7ff,
    "GREEN_1": 0x00ff00,
    "SPRING_GREEN_2B": 0x00ff5f,
    "SPRING_GREEN_1": 0x00ff87,
    "MEDIUM_SPRING_GREEN": 0x00ffaf,
    "CYAN_2": 0x00ffd7,
    "CYAN_1": 0x00ffff,
    "DARK_RED_1": 0x5f0000,
    "DEEP_PINK_4A": 0x5f005f,
    "PURPLE_4A": 0x5f0087,
    "PURPLE_4B": 0x5f00af,
    "PURPLE_3": 0x5f00d7,
    "BLUE_VIOLET": 0x5f00ff,
    "ORANGE_4A": 0x5f5f00,
    "GREY_37": 0x5f5f5f,
    "MEDIUM_PURPLE_4": 0x5f5f87,
    "SLATE_BLUE_3A": 0x5f5faf,
    "SLATE_BLUE_3B": 0x5f5fd7,
    "ROYAL_BLUE_1": 0x5f5fff,
    "CHARTREUSE_4": 0x5f8700,
    "DARK_SEA_GREEN_4A": 0x5f875f,
    "PALE_TURQUOISE_4": 0x5f8787,
    "STEEL_BLUE": 0x5f87af,
    "STEEL_BLUE_3": 0x5f87d7,
    "CORNFLOWER_BLUE": 0x5f87ff,
    "CHARTREUSE_3A": 0x5faf00,
    "DARK_SEA_GREEN_4B": 0x5faf5f,
    "CADET_BLUE_2": 0x5faf87,
    "CADET_BLUE_1": 0x5fafaf,
    "SKY_BLUE_3": 0x5fafd7,
    "STEEL_BLUE_1A": 0x5fafff,
    "CHARTREUSE_3B": 0x5fd700,
    "PALE_GREEN_3A": 0x5fd75f,
    "SEA_GREEN_3": 0x5fd787,
    "AQUAMARINE_3": 0x5fd7af,
    "MEDIUM_TURQUOISE": 0x5fd7d7,
    "STEEL_BLUE_1B": 0x5fd7ff,
    "CHARTREUSE_2A": 0x5fff00,
    "SEA_GREEN_2": 0x5fff5f,
    "SEA_GREEN_1A": 0x5fff87,
    "SEA_GREEN_1B": 0x5fffaf,
    "AQUAMARINE_1A": 0x5fffd7,
    "DARK_SLATE_GRAY_2": 0x5fffff,
    "DARK_RED_2": 0x870000,
    "DEEP_PINK_4B": 0x87005f,
    "DARK_MAGENTA_1": 0x870087,
    "DARK_MAGENTA_2": 0x8700af,
    "DARK_VIOLET_1A": 0x8700d7,
    "PURPLE_1A": 0x8700ff,
    "ORANGE_4B": 0x875f00,
    "LIGHT_PINK_4": 0x875f5f,
    "PLUM_4": 0x875f87,
    "MEDIUM_PURPLE_3A": 0x875faf,
    "MEDIUM_PURPLE_3B": 0x875fd7,
    "SLATE_BLUE_1": 0x875fff,
    "YELLOW_4A": 0x878700,
    "WHEAT_4": 0x87875f,
    "GREY_53": 0x878787,
    "LIGHT_SLATE_GREY": 0x8787af,
    "MEDIUM_PURPLE": 0x8787d7,
    "LIGHT_SLATE_BLUE": 0x8787ff,
    "YELLOW_4B": 0x87af00,
    "DARK_OLIVE_GREEN_3A": 0x87af5f,
    "DARK_GREEN_SEA": 0x87af87,
    "LIGHT_SKY_BLUE_3A": 0x87afaf,
    "LIGHT_SKY_BLUE_3B": 0x87afd7,
    "SKY_BLUE_2": 0x87afff,
    "CHARTREUSE_2B": 0x87d700,
    "DARK_OLIVE_GREEN_3B": 0x87d75f,
    "PALE_GREEN_3B": 0x87d787,
    "DARK_SEA_GREEN_3A": 0x87d7af,
    "DARK_SLATE_GRAY_3": 0x87d7d7,
    "SKY_BLUE_1": 0x87d7ff,
    "CHARTREUSE_1": 0x87ff00,
    "LIGHT_GREEN_2": 0x87ff5f,
    "LIGHT_GREEN_3": 0x87ff87,
    "PALE_GREEN_1A": 0x87ffaf,
    "AQUAMARINE_1B": 0x87ffd7,
    "DARK_SLATE_GRAY_1": 0x87ffff,
    "RED_3A": 0xaf0000,
    "DEEP_PINK_4C": 0xaf005f,
    "MEDIUM_VIOLET_RED": 0xaf0087,
    "MAGENTA_3A": 0xaf00af,
    "DARK_VIOLET_1B": 0xaf00d7,
    "PURPLE_1B": 0xaf00ff,
    "DARK_ORANGE_3A": 0xaf5f00,
    "INDIAN_RED_1A": 0xaf5f5f,
    "HOT_PINK_3A": 0xaf5f87,
    "MEDIUM_ORCHID_3": 0xaf5faf,
    "MEDIUM_ORCHID": 0xaf5fd7,
    "MEDIUM_PURPLE_2A": 0xaf5fff,
    "DARK_GOLDENROD": 0xaf8700,
    "LIGHT_SALMON_3A": 0xaf875f,
    "ROSY_BROWN": 0xaf8787,
    "GREY_63": 0xaf87af,
    "MEDIUM_PURPLE_2B": 0xaf87d7,
    "MEDIUM_PURPLE_1": 0xaf87ff,
    "GOLD_3A": 0xafaf00,
    "DARK_KHAKI": 0xafaf5f,
    "NAVAJO_WHITE_3": 0xafaf87,
    "GREY_69": 0xafafaf,
    "LIGHT_STEEL_BLUE_3": 0xafafd7,
    "LIGHT_STEEL_BLUE": 0xafafff,
    "YELLOW_3A": 0xafd700,
    "DARK_OLIVE_GREEN_3": 0xafd75f,
    "DARK_SEA_GREEN_3B": 0xafd787,
    "DARK_SEA_GREEN_2": 0xafd7af,
    "LIGHT_CYAN_3": 0xafd7d7,
    "LIGHT_SKY_BLUE_1": 0xafd7ff,
    "GREEN_YELLOW": 0xafff00,
    "DARK_OLIVE_GREEN_2": 0xafff5f,
    "PALE_GREEN_1B": 0xafff87,
    "DARK_SEA_GREEN_5B": 0xafffaf,
    "DARK_SEA_GREEN_5A": 0xafffd7,
    "PALE_TURQUOISE_1": 0xafffff,
    "RED_3B": 0xd70000,
    "DEEP_PINK_3A": 0xd7005f,
    "DEEP_PINK_3B": 0xd70087,
    "MAGENTA_3B": 0xd700af,
    "MAGENTA_3C": 0xd700d7,
    "MAGENTA_2A": 0xd700ff,
    "DARK_ORANGE_3B": 0xd75f00,
    "INDIAN_RED_1B": 0xd75f5f,
    "HOT_PINK_3B": 0xd75f87,
    "HOT_PINK_2": 0xd75faf,
    "ORCHID": 0xd75fd7,
    "MEDIUM_ORCHID_1A": 0xd75fff,
    "ORANGE_3": 0xd78700,
    "LIGHT_SALMON_3B": 0xd7875f,
    "LIGHT_PINK_3": 0xd78787,
    "PINK_3": 0xd787af,
    "PLUM_3": 0xd787d7,
    "VIOLET": 0xd787ff,
    "GOLD_3B": 0xd7af00,
    "LIGHT_GOLDENROD_3": 0xd7af5f,
    "TAN": 0xd7af87,
    "MISTY_ROSE_3": 0xd7afaf,
    "THISTLE_3": 0xd7afd7,
    "PLUM_2": 0xd7afff,
    "YELLOW_3B": 0xd7d700,
    "KHAKI_3": 0xd7d75f,
    "LIGHT_GOLDENROD_2A": 0xd7d787,
    "LIGHT_YELLOW_3": 0xd7d7af,
    "GREY_84": 0xd7d7d7,
    "LIGHT_STEEL_BLUE_1": 0xd7d7ff,
    "YELLOW_2": 0xd7ff00,
    "DARK_OLIVE_GREEN_1A": 0xd7ff5f,
    "DARK_OLIVE_GREEN_1B": 0xd7ff87,
    "DARK_SEA_GREEN_1": 0xd7ffaf,
    "HONEYDEW_2": 0xd7ffd7,
    "LIGHT_CYAN_1": 0xd7ffff,
    "RED_1": 0xff0000,
    "DEEP_PINK_2": 0xff005f,
    "DEEP_PINK_1A": 0xff0087,
    "DEEP_PINK_1B": 0xff00af,
    "MAGENTA_2B": 0xff00d7,
    "MAGENTA_1": 0xff00ff,
    "ORANGE_RED_1": 0xff5f00,
    "INDIAN_RED_1C": 0xff5f5f,
    "INDIAN_RED_1D": 0xff5f87,
    "HOT_PINK_1A": 0xff5faf,
    "HOT_PINK_1B": 0xff5fd7,
    "MEDIUM_ORCHID_1B": 0xff5fff,
    "DARK_ORANGE": 0xff8700,
    "SALMON_1": 0xff875f,
    "LIGHT_CORAL": 0xff8787,
    "PALE_VIOLET_RED_1": 0xff87af,
    "ORCHID_2": 0xff87d7,
    "ORCHID_1": 0xff87ff,
    "ORANGE_1": 0xffaf00,
    "SANDY_BROWN": 0xffaf5f,
    "LIGHT_SALMON_1": 0xffaf87,
    "LIGHT_PINK_1": 0xffafaf,
    "PINK_1": 0xffafd7,
    "PLUM_1": 0xffafff,
    "GOLD_1": 0xffd700,
    "LIGHT_GOLDENROD_2B": 0xffd75f,
    "LIGHT_GOLDENROD_2C": 0xffd787,
    "NAVAJO_WHITE_1": 0xffd7af,
    "MISTY_ROSE1": 0xffd7d7,
    "THISTLE_1": 0xffd7ff,
    "YELLOW_1": 0xffff00,
    "LIGHT_GOLDENROD_1": 0xffff5f,
    "KHAKI_1": 0xffff87,
    "WHEAT_1": 0xffffaf,
    "CORNSILK_1": 0xffffd7,
    "GREY_100": 0xffffff,
    "GREY_3": 0x080808,
    "GREY_7": 0x121212,
    "GREY_11": 0x1c1c1c,
    "GREY_15": 0x262626,
    "GREY_19": 0x303030,
    "GREY_23": 0x3a3a3a,
    "GREY_27": 0x444444,
    "GREY_30": 0x4e4e4e,
    "GREY_35": 0x585858,
    "GREY_39": 0x626262,
    "GREY_42": 0x6c6c6c,
    "GREY_46": 0x767676,
    "GREY_50": 0x808080,
    "GREY_54": 0x8a8a8a,
    "GREY_58": 0x949494,
    "GREY_62": 0x9e9e9e,
    "GREY_66": 0xa8a8a8,
    "GREY_70": 0xb2b2b2,
    "GREY_74": 0xbcbcbc,
    "GREY_78": 0xc6c6c6,
    "GREY_82": 0xd0d0d0,
    "GREY_85": 0xdadada,
    "GREY_89": 0xe4e4e4,
    "GREY_93": 0xeeeeee
}


def hexToTuple(h: int):
    if not 0x0 <= h <= 0xFFFFFF:
        raise ValueError("Input must be a 6-digit hex value.")
    return (h >> 16) & 0xFF, (h >> 8) & 0xFF, h & 0xFF


def sanitizeName(n: str):
    return n.upper().replace(" ", "_")


class Color:
    """
    An object representing a color.
    """
    colors_by_name = dict()
    colors_by_id = dict()

    def __init__(self, colorid: int, name: str, value: int):
        """
        Create a Color object and add it to the global registry of colors.

        Example:
        > Color(colorid = 256, name = "RED", value = 0xFF0000)

        colorid and name must be unique for each Color.
        """
        self._colorid = colorid
        self._name = sanitizeName(name)
        self._value = value

        if self.colorid in self.colors_by_id:
            raise ValueError(f"Color ID ({self.colorid}) already in use.")

        if self.name in self.colors_by_name:
            raise ValueError(f"Color name ({self.name}) already in use.")

        if not 0x0 <= self.value <= 0xFFFFFF:
            raise ValueError("Color value must be a 6-digit hex value.")

        self.colors_by_name[name] = self
        self.colors_by_id[colorid] = self

    @property
    def rgb(self):
        """
        Return a 3-Tuple representing the R, G, and B values of the Color respectively, values 0-255 inclusive.
        """
        return hexToTuple(self.value)

    @property
    def prettyName(self):
        """
        Returns a String that is the colors name value, but formatted to look nice in output.
        """
        name = self.name
        name = name.replace("_", " ").title()
        match = re.search(name, r"(.*)(\d.*)")
        if match:
            name = match.group(1) + " " + match.group(2).upper()
        return name

    @property
    def value(self):
        """
        Returns an int representing the value of this Color, between 0x000000 and 0xFFFFFF, inclusive.
        """
        return self._value

    @property
    def name(self):
        """
        Returns the canonical name of this Color.
        """
        return self._name

    @property
    def id(self):
        """
        Returns the canonical ID of this Color.
        """
        return self._colorid

    def remove(self):
        """
        Removes a color from the global registry of colors.
        """
        del self.colors_by_id[self.colorid]
        del self.colors_by_name[self.name]

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value

    def __hex__(self):
        return hex(self.value)

    def __repr__(self):
        return (f"Color(colorid = {self.colorid}, name = {self.name!r}, value = {hex(self.value)})")

    @classmethod
    def fromID(cls, colorid: int):
        """
        Return a Color based on its canonical ID in the global registry of colors.
        """
        return cls.colors_by_id[colorid]

    @classmethod
    def fromName(cls, name: str):
        """
        Return a Color based on its canonical name in the global registry of colors.
        """
        return cls.colors_by_name[name]


def loadDefaultColors():
    for colorid, (name, value) in enumerate(default_colors.items()):
        Color(colorid, name, value)

    return AttrDict(Color.colors_by_name)


"""
Is an AttrDict of a default, 256-color pattlete (based on https://jonasjacek.github.io/colors/)
"""
colors = loadDefaultColors()
