
from turtle import *
color('yellow', 'blue')
begin_fill()
while True:
        forward(200)
        left(220)
        if abs(pos()) < 1:
            break
end_fill()
done()