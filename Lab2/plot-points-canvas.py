import matplotlib.pyplot as plt
import os

# Визначаємо шляхи до файлів
file_path = 'OGKG\Lab2\DS1.txt'
output_image_path = os.path.join(os.path.dirname(file_path), 'output_plot.png')

# Зчитування координатів із датасету
coordinates = []
with open(file_path, 'r') as file:
    for line in file:
        x, y = map(int, line.split())
        coordinates.append((x, y))

# Заносимо координати Х та Y в окремі масиви
x_values = [coord[0] for coord in coordinates]
y_values = [coord[1] for coord in coordinates]

# Визначаємо розмір вікна та наносимо на канвас точки
plt.figure(figsize=(9.6, 5.4))  
plt.scatter(x_values, y_values, s=1, color='blue')  

# Позначаємо осі на назву канвасу
plt.xlim(0, 960)
plt.ylim(0, 540)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Points from Dataset')

# Відображаємо та зберігаємо 
plt.savefig(output_image_path)
plt.show()

print(f"Image saved at: {output_image_path}")
