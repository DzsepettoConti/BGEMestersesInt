import matplotlib.pyplot as plt
x = []
y = []
I1 = 1
I2 = 2

w1 = 0.21
w2 = 0.35
w3 = 0.19
w4 = 0.38
w5 = 0.55
w6 = 0.79
w7 = 0.24
w8 = 0.83
w9 = 0.21
w10 = 0.47
w11 = 0.62
w12 = 0.31
w13 = 0.3
w14 = 0.54
w15 = 0.34
w16 = 0.67


a = 0.001
O1 = 2
O2 = 1

for i in range(100000):
    H1 = I1 *w1 + I2 *w2
    H2 = I1 *w3 + I2 *w4
    H3 = I1 *w5 + I2 *w6
    H4 = I1 *w7 + I2 *w8

    O_calc_1 = H1 *w9 + H2 *w10 + H3 *w11 +H4 *w12
    O_calc_2 = H1 *w13 + H2 *w14 + H3 *w15 + H4 *w16
    print("iteráció: ", i+1)
    print("Elvárt output1:",O1," eredmény otuput1: ", O_calc_1)
    print("Elvárt output2:",O2," eredmény otuput2: ", O_calc_2)

    hiba = 0.5* (O1-O_calc_1)*(O1-O_calc_1)
    hiba = hiba + 0.5* (O2-O_calc_2)*(O2-O_calc_2)
    hiba = hiba/2
    print("Hiba mértéke: ", hiba)

    w1 = w1-a*(hiba/w1)
    w2 = w2-a*(hiba/w2)
    w3 = w3-a*(hiba/w3)
    w4 = w4-a*(hiba/w4)
    w5 = w5-a*(hiba/w5)
    w6 = w6-a*(hiba/w6)
    w7 = w7-a*(hiba/w7)
    w8 = w8-a*(hiba/w8)
    x.append(i+1)
    y.append(hiba)
plt.title('Backpropagation')
plt.xlabel('Iterációk száma')
plt.ylabel('Hiba mértéke')
plt.plot(x,y,'r-', label ='hibák')
plt.legend()
plt.show()