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


def main():
    """Run some tests."""

    test_texel()


if __name__ == "__main__":
    main()
