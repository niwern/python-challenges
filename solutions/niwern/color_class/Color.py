class Color:
    r, g, b, h, s, l = 0, 0, 0, 0, 0, 0

    def __init__(self, r=None, g=None, b=None, h=None, s=None, l=None):
        if h != None and s != None and l != None:
            self.__dict__['h'] = h
            self.__dict__['s'] = s
            self.__dict__['l'] = l
            self.hsl_to_rgb()
        elif r != None and g != None and b != None:
            self.__dict__['r'] = r
            self.__dict__['g'] = g
            self.__dict__['b'] = b
            self.rgb_to_hsl()
        else:
            raise ValueError('Missing attribute')


    def hsl_to_rgb(self):
        s_ = self.s/100.0
        l_ = self.l/100.0
        h_ = self.h/60.0

        Z = 1 - abs(h_%2 - 1)
        C = (1 - abs(2*l_  - 1))*s_
        X = C*(1 - abs(h_ % 2 - 1))
        m = l_ - C/2


        if h_ < 1:
            r_, g_, b_ = C, X, 0

        elif h_ < 2:
            r_, g_, b_ = X, C, 0

        elif h_ < 3:
            r_, g_, b_ = 0, C, X

        elif h_ < 4:
            r_, g_, b_ = 0, X, C

        elif h_ < 5:
            r_, g_, b_ = X, 0, C

        elif h_ < 6:
            r_, g_, b_ = C, 0, X

        self.__dict__['r'] = int(round((r_ + m)*255))
        self.__dict__['g'] = int(round((g_ + m)*255))
        self.__dict__['b'] = int(round((b_ + m)*255))

    def rgb_to_hsl(self):
        r = self.r/255.0
        g = self.g/255.0
        b = self.b/255.0
        M = max(r, g, b)
        m = min(r, g, b)
        C = M - m

        if C == 0:
            self.h = 0

        elif M == r:
            self.h = ((g - b)/C%6)

        elif M == g:
            self.h = ((b - r)/C + 2)

        elif M == b:
            self.h = ((r - g)/C + 4)

        self.l = 0.5*(M + m)

        if self.l == 1 or self.l == 0:
            self.s = 0

        else:
            self.s = C/(1 - abs(2*self.l - 1))

        self.s = int(100*self.s)
        self.l = int(100*self.l)
        self.h = int(60* self.h)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if key == 'r' or key == 'g' or key == 'b':
            self.rgb_to_hsl()
        elif key == 'h' or key == 's' or key == 'l':
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
