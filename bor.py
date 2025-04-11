import matplotlib.pyplot as plt
x = []
y_bolt = []
y_ostermelo = []
palack = 0
palackok_szama = 0
for i in range(50):
    bolti_ar = palack*3
    ostermelo_ar = palack*2.40+18
    kulonbseg = bolti_ar-ostermelo_ar
    if kulonbseg == 0:
        palackok_szama=palack
    x.append(palack)
    y_bolt.append(bolti_ar)
    y_ostermelo.append(ostermelo_ar)
    palack += 1

print(palackok_szama, "palack felett már érdemes az őstermelőtől vásárolni!")
plt.title('Vásárlás!')
plt.xlabel('Palackok száma')
plt.ylabel('Kiadás')
plt.plot(x,y_bolt,'r_',label='Bolt')
plt.plot(x, y_ostermelo,'g-', label ='Őstermelő')
plt.legend()
plt.show()