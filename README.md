# DigiColor
Makes working with colors a bit nicer.

**DigiColor** comes with a default pallete of 256 colors. If this is all you need, it's really simple to use out of the box:

```python
>>> from digicolor import colors
>>> colors.RED
```
```python
Color(colorid = 1, name = "RED", value = 0x800000)
```

You can also "search" the global registry of colors by ID or name:

```python
>>> from digicolor import Color
>>> Color.fromID(2)
```
```python
Color(colorid = 2, name = "GREEN", value = 0x008000)
```
```python
>>> Color.fromName("BLUE")
```
```python
Color(colorid = 4, name = "BLUE", value = 0x000080)
```

You can look at the entire registry by accessing `Color.registry`...
```python
>>> print(Color.registry)
```
```python
[Color(colorid = 0, name = 'BLACK', value = 0x0), Color(colorid = 1, name = 'RED', value = 0x800000), Color(colorid = 2, name = 'GREEN', value = 0x8000), ...
```
...etc.

You can create your own colors by constructing one!

```python
>>> awesomecolor = Color(colorid = 256, name = "AWESOME", value = 0x0fcdf7)

>>> print(f"""Awesome Color
... ID: {awesomecolor.colorid}
... Name: {awesomecolor.name}
... Prettified Name: {awesomecolor.prettyName}
... Value: {awesomecolor.value}
... RGB: {awesomecolor.rgb}
... """)
```
```
Awesome Color
ID: 256
Name: AWESOME
Prettified Name: Awesome
Value: 1035767
RGB: (15, 205, 247)
```

And remove colors from the global registry:

```python
>>> awesomecolor.remove()
```

You can even get the closest approximation to a given color that your registry has:

```python
>>> Color.getClosestColor(0x00AA00)
```
```python
Color(colorid = 34, name = 'GREEN_3A', value = 0x00af00)
```
```python
>>> Color.getClosestColor("00AA00")
```
```python
Color(colorid = 34, name = 'GREEN_3A', value = 0x00af00)
```
```python
>>> Color.getClosestColor((0, 170, 0))
```
```python
Color(colorid = 34, name = 'GREEN_3A', value = 0x00af00)
```
