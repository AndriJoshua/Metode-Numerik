import matplotlib.pyplot as plt

#Untuk Menggambar garisnya
#gambar untuk membuat garis horizontal
x_horizontal = []
y_horizontal = []



custom_x_ticks = []
custom_y_ticks = []

for i in range(-10,11):
    x_horizontal.append(i)
    y_horizontal.append(0)

for i in range(-10,11):
    custom_x_ticks.append(i)
    custom_y_ticks.append(i)
    
#gambar untuk membuat garis vertikal
x_vertikal = []
y_vertikal = []

for i in range(-10,11):
    x_vertikal.append(0)
    y_vertikal.append(i)


x = []
y = []
x_sementara = -10
y_sementara = -10

for i in range (0,100):
    x.append(x_sementara)
    y_sementara = x_sementara ** 2 + 1
    x_sementara += 0.2
    y.append(y_sementara)
    
    


plt.plot(x, y, marker="", label="Grafik")
plt.plot(x_horizontal,y_horizontal,marker ="",label="Garis Horizontal",color="k")
plt.plot(x_vertikal,y_vertikal,marker="",label="Gari`s Vertikal",color = "k")

plt.xlim(min(custom_x_ticks), max(custom_x_ticks))
plt.ylim(min(custom_y_ticks), max(custom_y_ticks))
plt.xticks(custom_x_ticks)
plt.yticks(custom_y_ticks)

plt.title("Grafik")
plt.xlabel("X")
plt.ylabel("Y")




plt.show()
