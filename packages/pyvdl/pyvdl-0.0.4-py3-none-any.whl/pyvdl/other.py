import os
from .libs import *
class obj:
    def __init__(self):
        self.color = (255, 255, 255)
    def render(self, x, y):
        pass
    def abs_(self, i, j):
        return abs(complex(i, j))
    def dot(self, p1, p2):
        sqrt = lambda n : n ** 0.5
        return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def save(name, img):
    try:
        cv2.imwrite(name, np.array(img))
    except cv2.error as e:
        raise pyvdl_error(f'{e}')
class animation:
    def __init__(self):
        self.size = (500, 500)
        self.form = lambda x : x
        self.t = 5
        self.obj_ = circle()
    def render(self):
        width, heigth = self.size
        for i in range(self.t):
            o = i - self.t / 2
            cp = render(self.obj_, width, heigth, self.form(o), o)
            save(f'cp{i}.png', cp)
    def video(self, filename):
        out = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'DIVX'),30,self.size)
        for i in range(self.t):
            img = cv2.imread(f'cp{i}.png')
            os.system(f'del cp{i}.png >nul')
            out.write(img)
        out.release()
def render(obj_, width, heigth, x=0, y=0):
    p = []
    for i in range(width):
        p.append([])
        for j in range(heigth):
            r = obj_.render(i - width / 2 + x, j - heigth / 2 + y)
            if r:
                p[len(p)-1].append(obj_.color)
            else:
                p[len(p)-1].append((0, 0, 0))
    return p
# stantart obj
class circle(obj):
    def __init__(self, r=10):
        super().__init__()
        self.color = (255, 255, 255)
        self.r = r
    def render(self, x, y):
        return 0 > self.abs_(x, y) - self.r > -2
# exeption
def font(ttf_path, font_size=224, encoding="utf-8", b="A"):
    font = ImageFont.truetype(ttf_path, 224, encoding='utf-8')
    W, H = font_size, font_size
    image = Image.new("RGB",(W,H),"black")
    draw = ImageDraw.Draw(image)
    offset_w,offset_h = font.getoffset("A")
    w,h = draw.textsize(b,font = font)
    pos = ((W - w - offset_w) / 2,(H - h - offset_h) / 2)
    draw.text(pos,b,"white",font = font)
    print(type(image))
    image.save(f"{b}.png")
    return np.array(Image.open(f'{b}.png'))
class pyvdl_error(Exception):
    def __init__(self, f, *args):
        super().__init__(*args)
        self.f = f
    def __str__(self):
        s: list = "◜◝-◟◞|"
        out = ''
        out += s[0]
        out += s[2] * len(self.f)
        out += s[1] + "\n" + "                             " + s[5]
        out += self.f + " "
        out += s[5]
        out += "\n" + "                             "
        out += s[3] + s[2] * len(self.f) + s[4]
        return out