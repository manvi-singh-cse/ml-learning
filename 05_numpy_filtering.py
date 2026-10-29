import numpy as np

# FILTERING
ages = np.array([[21, 17, 19, 20, 16, 30, 18],
                 [39, 22, 15, 85, 18, 19, 26]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]

print(teenagers)
print(adults)
print(seniors)

adults2D = np.where(ages >= 18, ages, 0)            # (condition, array, what to replace for false values)
print(adults2D)