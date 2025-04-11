import matplotlib.pyplot as plt

x = []
y = []
ido = 0.1
legnagyobb_magassag = 0
magassag = 0.5*ido*ido+2.5*ido
max_magassag = magassag
max_ido = ido
x.append(ido)
y.append(magassag)
while magassag > 0:
    ido = ido+0.1
    magassag = -0.5*ido*ido+2.5*ido
    x.append(ido)
    y.append(magassag)
    if magassag > max_magassag:
        max_magassag = magassag
        max_ido = ido

print("A golyo repülési magassága", max_magassag, "méternél a legnagyobb",max_ido, "mp után")
print("A golyó kilövés után", ido, "mp elteltével esett le.")
plt.xlabel("mp")
plt.ylabel("méter")
plt.plot(x, y, 'b-', label = 'repülési magasság')
plt.legend()
plt.show()