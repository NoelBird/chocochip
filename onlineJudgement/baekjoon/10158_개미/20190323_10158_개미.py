w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

dis_x = t - (t // (w*2))*(w*2)
dis_y = t - (t // (h*2))*(h*2)
if w - x-dis_x >=0:
    x += dis_x
else:
    x = 2*w -x-dis_x
if h - y-dis_y >=0:
    y += dis_y
else:
    y = 2*h -y - dis_y
print("%d %d" % (abs(x), abs(y)))