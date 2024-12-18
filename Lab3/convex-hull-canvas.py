import matplotlib.pyplot as plt
import os
from scipy.spatial import ConvexHull

# Визначаємо шляхи до файлів
file_path = 'DS1.txt'
output_image_path = os.path.join(os.path.dirname(file_path), 'convex_hull_plot.png')
output_dataset_path = os.path.join(os.path.dirname(file_path), 'convex_hull_dataset.txt')

# Зчитування координатів із датасету
coordinates = []
with open(file_path, 'r') as file:
    for line in file:
        x, y = map(int, line.split())
        coordinates.append((x, y))

# Заносимо координати Х та Y в окремі масиви
x_values = [coord[0] for coord in coordinates]
y_values = [coord[1] for coord in coordinates]

# Знаходимо координати опуклої оболонки
points = [[x, y] for x, y in coordinates]
hull = ConvexHull(points)

# зберігаємо координати опуклої оболонки в Dataset
with open(output_dataset_path, 'w') as outfile:
    for vertex in hull.vertices:
        outfile.write(f"{points[vertex][0]} {points[vertex][1]}\n")

print(f"Convex hull dataset saved at: {output_dataset_path}")

# Визначаємо розмір вікна та наносимо на канвас точки
plt.figure(figsize=(9.6, 5.4))  
plt.scatter(x_values, y_values, s=1, color='black', label='Original Points')  

# наносимо на канвас опуклу оболонку
for simplex in hull.simplices:
    plt.plot([points[simplex[0]][0], points[simplex[1]][0]],
             [points[simplex[0]][1], points[simplex[1]][1]], 'b-', label='Convex Hull' if simplex[0] == hull.simplices[0][0] else "")

# Set Axes and Labels
plt.xlim(0, 960)
plt.ylim(0, 540)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Convex Hull of Dataset')
plt.legend()

# Step 6: Save and Display the Image
plt.savefig(output_image_path)
plt.show()

print(f"Image saved at: {output_image_path}")
