from d1p1input import heightInput

print(heightInput())

heightArray = heightInput()

previous = 199

current = 0

larger = 0

for height in heightArray:
    current = height
    diff = (current - previous)
    previous = height

    if diff > 0 :
        larger = larger + 1
        print(larger)

print(heightArray)