class Geometry2D(object):
    """2D geometry methods."""

    def line(self, pos0, pos1, transformation=None, **kwargs):
        """Draw a line between the two positions."""

        px0, py0 = pos0
        px1, py1 = pos1
        x0, y0 = self.transform_position(pos0, transformation)
        x1, y1 = self.transform_position(pos1, transformation)

        Dx = abs(x1 - x0)
        Dy = abs(y1 - y0)
        steps = max(Dx, Dy)

        if steps == 0:
            self.set(pos0, transformation, **kwargs)
        else:
            dpx = (px1 - px0) / steps
            dpy = (py1 - py0) / steps
            x = px0
            y = py0
            self.set((x, y), transformation, **kwargs)

            for i in range(steps):
                x += dpx
                y += dpy
                self.set((x, y), transformation, **kwargs)

    def triangle(self, pos0, pos1, pos2, transformation=None, fill=True, **kwargs):
        """Draw a triangle."""

        x0, y0 = self.transform_position(pos0, transformation=transformation)
        x1, y1 = self.transform_position(pos1, transformation=transformation)
        x2, y2 = self.transform_position(pos2, transformation=transformation)

        self.line((x0, y0), (x1, y1), transformation=None, **kwargs)
        self.line((x1, y1), (x2, y2), transformation=None, **kwargs)
        self.line((x0, y0), (x2, y2), transformation=None, **kwargs)

        if fill:
            px0, py0 = pos0
            px1, py1 = pos1
            Dx = abs(x1 - x0)
            Dy = abs(y1 - y0)
            steps = max(Dx, Dy)

            # First and last step were alreday drawn above
            if steps >= 2:
                dpx = (px1 - px0) / steps
                dpy = (py1 - py0) / steps
                x = px0
                y = py0

                for i in range(steps - 1):
                    x += dpx
                    y += dpy
                    self.line((x, y), pos2, transformation, **kwargs)

    def polygon(self, vertices, transformation=None, fill=True, **kwargs):
        """Draw a polygon given by a list of vertices.

        Filling only works with convex-ish polygons.

        """

        if fill:
            # Centre position
            xc = 0.0
            yc = 0.0
            for pos in vertices:
                xc += pos[0]
                yc += pos[1]
            xc /= len(vertices)
            yc /= len(vertices)
            pos0 = vertices[-1]
            for pos1 in vertices:
                self.triangle(
                    (xc, yc), pos0, pos1, transformation=transformation, **kwargs
                )
                pos0 = pos1
        else:
            # Just draw lines
            pos0 = vertices[-1]
            for pos1 in vertices:
                self.line(pos0, pos1, transformation=transformation, **kwargs)
                pos0 = pos1

    def rectangle(self, pos0, pos1, transformation=None, fill=True, **kwargs):
        """Draw a rectangle between the given points."""

        x0, y0 = pos0
        x1, y1 = pos1
        self.polygon(
            [(x0, y0), (x0, y1), (x1, y1), (x1, y0)],
            transformation=transformation,
            fill=fill,
            **kwargs
        )
