start = input("Топлива было: ")
end = input("Топлива осталось: ")
distance = input("Расстояние: ")

diff = int(start) - int(end)
result = diff / int(distance)

print(f"Расход на км: {result}")