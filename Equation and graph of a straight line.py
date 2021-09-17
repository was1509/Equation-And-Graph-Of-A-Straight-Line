#!/usr/bin/env python
# coding: utf-8

# In[18]:


from matplotlib import pyplot as plt


# In[ ]:


x_one = float(input("X One : "))
y_one = float(input("Y One : "))
x_two = float(input("X Two : "))
y_two = float(input("Y Two : "))
if x_one == x_two:
    print("Equation: x = {}".format(x_one))
    mylist = [x_one,x_two]
    mylist2 = [y_one,y_two]
    plt.plot(mylist , mylist2, 'o')
    plt.plot(mylist , mylist2)
    plt.ylabel("Y Axis")
    plt.xlabel("X Axis")
    plt.title("Graph of x = {}".format(x_one))
    plt.grid()
elif y_two == y_one:
    c = y_one
    print("Equation: y = {}".format(c))
    x_li = [x_one , x_two]
    y_li = [y_one , y_two]
    plt.plot(x_li , y_li , 'o')
    plt.plot(x_li , y_li)
    plt.ylabel('Y Axis')
    plt.xlabel('X Axis')
    plt.title("Graph of y = {}".format(c))
    plt.grid()
else:
    grad = (y_two - y_one) / (x_two - x_one)
    constant = y_one - (grad * x_one)
    if constant > 0:
        print("Equation: y = {}x + {}".format(round(grad,2) , round(constant,2)))
        x_li = [x_one , x_two]
        y_li = [y_one , y_two]
        plt.plot(x_li , y_li, 'o')
        plt.plot(x_li , y_li)
        plt.ylabel("Y Axis")
        plt.xlabel("X Axis")
        plt.title("Graph of y = {}x + {}".format(round(grad,2) , round(constant,2)))
        plt.grid()
    elif constant < 0:
        print("Equation: y = {}x - {}".format(round(grad,2) , round(abs(constant),2)))
        x_li = [x_one , x_two]
        y_li = [y_one , y_two]
        plt.plot(x_li , y_li, 'o')
        plt.plot(x_li , y_li)
        plt.ylabel("Y Axis")
        plt.xlabel("X Axis")
        plt.title("Graph of y = {}x - {}".format(round(grad,2) , round(abs(constant),2)))
        plt.grid()
    elif constant == 0:
        print("Equation: y = {}x".format(grad))
        x_li = [x_one , x_two]
        y_li = [y_one , y_two]
        plt.plot(x_li , y_li, 'o')
        plt.plot(x_li , y_li)
        plt.ylabel("Y Axis")
        plt.xlabel("X Axis")
        plt.title("Graph of y = {}x".format(grad))
        plt.grid()


# In[ ]:




