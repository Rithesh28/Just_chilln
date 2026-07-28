from turtle import*
bgcolor("white")
pensize(2)
color("green")
left(90)
backward(100)
speed(1000000)
shape("turtle")
def tree(i):
    if i<10:
        return
    else:
        forward(i)
        color("orange")
        circle(2)
        color("brown")
        left(30)
        tree(3*i/4)
        right(60)
        tree(3*i/4)
        left(30)
        backward(i)
tree(100)
done()
                        
