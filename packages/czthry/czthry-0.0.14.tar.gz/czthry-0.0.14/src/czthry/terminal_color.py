'''
在命令行输出文本，可以着色
单字母的方法是前景色
双字母的方法是背景色
rgbw 红 绿 蓝 白
cmyk 青 品红 黄 黑
rvs 反转

    msg = 'hello, world'
    color_msg = Color(msg).r().cc().string
    print(color_msg)

'''
class Color(object):
    _esc = '\033'
    _reset = _esc + '[0m'
    _c = _esc + '[36m%s' + _reset
    _m = _esc + '[35m%s' + _reset
    _y = _esc + '[33m%s' + _reset
    _k = _esc + '[30m%s' + _reset
    _r = _esc + '[31m%s' + _reset
    _g = _esc + '[32m%s' + _reset
    _b = _esc + '[34m%s' + _reset
    _w = _esc + '[37m%s' + _reset

    _b_c = _esc + '[46m%s' + _reset
    _b_m = _esc + '[45m%s' + _reset
    _b_y = _esc + '[43m%s' + _reset
    _b_k = _esc + '[40m%s' + _reset
    _b_r = _esc + '[41m%s' + _reset
    _b_g = _esc + '[42m%s' + _reset
    _b_b = _esc + '[44m%s' + _reset
    _b_w = _esc + '[47m%s' + _reset

    _rvs = _esc + '[7m%s' + _reset


    def __init__(self, arg):
        self.string = arg

    def r(self):
        self.string = Color._r % self.string
        return self
    def g(self):
        self.string = Color._g % self.string
        return self
    def b(self):
        self.string = Color._b % self.string
        return self
    def w(self):
        self.string = Color._w % self.string
        return self
    def c(self):
        self.string = Color._c % self.string
        return self
    def m(self):
        self.string = Color._m % self.string
        return self
    def y(self):
        self.string = Color._y % self.string
        return self
    def k(self):
        self.string = Color._k % self.string
        return self
    def rr(self):
        self.string = Color._b_r % self.string
        return self
    def gg(self):
        self.string = Color._b_g % self.string
        return self
    def bb(self):
        self.string = Color._b_b % self.string
        return self
    def ww(self):
        self.string = Color._b_w % self.string
        return self
    def cc(self):
        self.string = Color._b_c % self.string
        return self
    def mm(self):
        self.string = Color._b_m % self.string
        return self
    def yy(self):
        self.string = Color._b_y % self.string
        return self
    def kk(self):
        self.string = Color._b_k % self.string
        return self
    def rvs(self):
        self.string = Color._rvs % self.string
        return self

if __name__ == '__main__':
    s = 'hello'
    ss = Color(s).r().cc().string
    print(Color(s).c().string)
    print(Color(s).y().cc().string)
    print(Color(s).y().cc().rvs().string)
