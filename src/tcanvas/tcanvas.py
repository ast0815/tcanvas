"""Text-based canvases.

Colours
-------

Colours can be specified as a single character string, or as a tuple of RGB
values. Tuples of floats are assumed to be in the 0.0-1.0 range, tuples of ints
in the 0-255 range. Strings map to the default terminal colours like this:

====== ====================
String Colour
====== ====================
0      Default fg/bg colour
k      black
r      red
g      green
y      yellow
b      blue
m      magenta
c      cyan
w      white
K      bright black
R      bright red
G      bright green
Y      bright yellow
B      bright blue
M      bright magenta
C      bright cyan
W      bright white

"""

import click


class Texel(object):
    """One character on the screen.

    Parameters
    ----------

    character : str
        The character to be displayed
    fg_color, bg_color : str or tuple
        Forground and background colours.
    bold, underline, cross, blink : bool
        Set special text effects

    """

    def __init__(
        self,
        character="",
        fg_color="0",
        bg_color="0",
        bold=False,
        faint=False,
        italic=False,
        underline=False,
        cross=False,
        blink=False,
        inverse=False,
        overline=False,
    ):
        self.character = character
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.bold = bold
        self.faint = faint
        self.italic = italic
        self.underline = underline
        self.blink = blink
        self.inverse = inverse
        self.cross = cross
        self.overline = overline

    @staticmethod
    def ansi_color_code(color, bg=False):
        """Return the ANSI colour code for the given colour."""

        # String to default terminal colours
        subs = {
            "k": 30,
            "r": 31,
            "g": 32,
            "y": 33,
            "b": 34,
            "m": 35,
            "c": 36,
            "w": 37,
            "0": 39,  # Reset to default
            "K": 90,
            "R": 91,
            "G": 92,
            "Y": 93,
            "B": 94,
            "M": 95,
            "C": 96,
            "W": 97,
        }
        if color in subs:
            if bg:
                return "%d;" % (subs[color] + 10,)
            else:
                return "%d;" % (subs[color],)

        # Other wise this probably a tuple of rgb values
        if isinstance(color[0], float):
            # Translate 0.0-1.0 floats to 0-255 ints
            color = tuple(int(x * 255) for x in color)
        if bg:
            return "48;2;%d;%d;%d;" % color
        else:
            return "38;2;%d;%d;%d;" % color

    def render(self):
        """Return the ANSI sequence representing the Texel."""

        ansi = "\033["
        ansi += self.ansi_color_code(self.fg_color, bg=False)
        ansi += self.ansi_color_code(self.bg_color, bg=True)
        if self.bold:
            ansi += "1;"
        if self.faint:
            ansi += "2;"
        if self.italic:
            ansi += "3;"
        if self.underline:
            ansi += "4;"
        if self.blink:
            ansi += "5;"
        if self.inverse:
            ansi += "7;"
        if self.cross:
            ansi += "9;"
        if self.overline:
            ansi += "53;"
        ansi = ansi[:-1]  # Remove last ";"
        ansi += "m"
        if len(self.character) > 0:
            ansi += self.character  # The actual character to print
        else:
            ansi += " "
        # Finally reset everything
        ansi += "\033[0m"

        return ansi


class TCanvas(object):
    """A basic canvas.

    Parameters
    ----------

    columns, rows : int or None
        The size of the canvas. Defaults to current terminal size.
    """

    def __init__(self, columns=None, rows=None):
        term_width, term_height = click.get_terminal_size()
        if columns is None:
            self._columns = term_width
        else:
            self._columns = columns
        if rows is None:
            self._rows = term_height
        else:
            self._rows = rows

        self.clear_buffer()

    def get_size(self):
        """Return the number of columns and rows."""
        return self._columns, self._rows

    def clear():
        """Clear the canvas."""
        self._buffer = []
        nrow, ncol = self.get_size()
        for row in range(nrow):
            self._buffer.append([])
            for column in range(ncol):
                self._buffer[-1].append(Texel())
