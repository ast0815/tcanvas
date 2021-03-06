from click import echo

from tcanvas import *


def test_texel():
    echo("=====")
    echo("Texel")
    echo("=====")
    echo("Empty:   " + Texel("").render())
    echo("Default: " + Texel("D").render())
    echo("Inverse: " + Texel("I", inverse=True).render())
    echo("Colours: " + Texel("C", fg_color="r", bg_color="K").render())
    echo(
        "RGB:     "
        + Texel("R", fg_color=(0, 255, 0), bg_color=(1.0, 0.0, 1.0)).render()
    )
    echo("Bold:    " + Texel("B", bold=True).render())
    echo("Faint:   " + Texel("F", faint=True).render())
    echo("Italic:  " + Texel("I", italic=True).render())
    echo("Under:   " + Texel("U", underline=True).render())
    echo("Cross:   " + Texel("S", cross=True).render())
    echo("Blink:   " + Texel("B", blink=True).render())
    echo("Over:    " + Texel("O", overline=True).render())
    echo("Blink c.:" + Texel("B", blink=True, fg_color="b", bg_color="y").render())


def test_tcanvas():
    c = TCanvas(columns=20, rows=10, bg_color="K")
    c.text((13, 0), "=======\nTCanvas\n=======")
    c.set((0, 0), character="*")
    c.set((19, 9), character="#")
    c.line((-1, 5), (10, -2), bg_color="r")
    c.line((2, -1), (6, 4), fg_color="W", blink=True, character="x")
    c.triangle((2.6, 4.6), (6.4, 8.4), (15, 7), bg_color="c", fg_color="k")
    c.triangle((3, 5), (6, 8), (15, 7), character="t", fill=False)
    c.polygon([(10, 5), (18, 6), (19, 8), (18, 9), (12, 6)], bg_color="y", fg_color="k")
    c.polygon([(10, 5), (18, 6), (19, 8), (18, 9), (12, 6)], character="p", fill=False)
    c.rectangle((17, 3), (19, 5), character="r")
    c.show()


def main():
    """Run some tests."""

    test_texel()
    test_tcanvas()


if __name__ == "__main__":
    main()
