class Color:

    def __init__(self, r=None, g=None, b=None, h=None, s=None, l=None):
        if h != None and s != None and l != None:
            self._h = h
            self._s = s
            self._l = l
            self.hsl_to_rgb()
        elif r != None and g != None and b != None:
            self._r = r
            self._g = g
            self._b = b
            self.rgb_to_hsl()
        else:
            raise ValueError('Missing attribute')

    def hsl_to_rgb(self):
        s_ = self.s/100.0
        l_ = self.l/100.0
        h_ = self.h/60.0

        # z = 1 - abs(h_%2 - 1)
        c = (1 - abs(2*l_ - 1))*s_
        x = c*(1 - abs(h_%2 - 1))
        m = l_ - c/2

        if h_ < 1:
            r_, g_, b_ = c, x, 0

        elif h_ < 2:
            r_, g_, b_ = x, c, 0

        elif h_ < 3:
            r_, g_, b_ = 0, c, x

        elif h_ < 4:
            r_, g_, b_ = 0, x, c

        elif h_ < 5:
            r_, g_, b_ = x, 0, c

        else:
            r_, g_, b_ = c, 0, x

        self._r = int(round((r_ + m)*255))
        self._g = int(round((g_ + m)*255))
        self._b = int(round((b_ + m)*255))

    def rgb_to_hsl(self):
        r = self.r/255.0
        g = self.g/255.0
        b = self.b/255.0
        maximum = max(r, g, b)
        minimum = min(r, g, b)
        c = maximum - minimum

        if c == 0:
            self._h = 0

        elif maximum == r:
            self._h = ((g - b)/c%6)

        elif maximum == g:
            self._h = ((b - r)/c + 2)

        elif maximum == b:
            self._h = ((r - g)/c + 4)

        self._l = 0.5*(maximum + minimum)

        if self._l == 1 or self._l == 0:
            self._s = 0

        else:
            self._s = c/(1 - abs(2*self.l - 1))

        self._s = int(100*self._s)
        self._l = int(100*self._l)
        self._h = int(60*self._h)

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, val):
        self._r = val
        self.rgb_to_hsl()

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, val):
        self._g = val
        self.rgb_to_hsl()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, val):
        self._b = val
        self.rgb_to_hsl()

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, val):
        self._h = val
        self.hsl_to_rgb()

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, val):
        self._s = val
        self.hsl_to_rgb()

    @property
    def l(self):
        return self._l

    @l.setter
    def l(self, val):
        self._l = val
        self.hsl_to_rgb()

    def __str__(self):
        def hex(x):
            x_hex = [int(x/16), x%16]
            for i in range(2):
                if x_hex[i] < 10:
                    x_hex[i] = str(x_hex[i])
                elif x_hex[i] == 10:
                    x_hex[i] = 'a'
                elif x_hex[i] == 11:
                    x_hex[i] = 'b'
                elif x_hex[i] == 12:
                    x_hex[i] = 'c'
                elif x_hex[i] == 13:
                    x_hex[i] = 'd'
                elif x_hex[i] == 14:
                    x_hex[i] = 'e'
                elif x_hex[i] == 15:
                    x_hex[i] = 'f'
            return x_hex[0] + x_hex[1]

        return '#' + hex(self.r) + hex(self.g) + hex(self.b)
