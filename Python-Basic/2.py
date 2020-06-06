bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])

print("\n\n")


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("benze")
print(motorcycles)

motorcycles.insert(0,"ford")
print(motorcycles)

del motorcycles[0]
print(motorcycles)


popped_motercycles = motorcycles.pop(1)
print(motorcycles)
print(popped_motercycles)

motorcycles.remove("ducati")
print(motorcycles)

motorcycles.sort()
print(motorcycles)

motorcycles.sort(reverse=True)
print(motorcycles)

print(sorted(motorcycles))
print(motorcycles)

i=len(motorcycles)
print(i)
