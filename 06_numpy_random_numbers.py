import numpy as np

# RANDOM NUMBERS
rng1 = np.random.default_rng(seed = 1)

print(rng1.integers(1, 7))
print(rng1.integers(low=1, high=7, size=10))
print(rng1.integers(low=1, high=7, size=(3,2)))

rng2 = np.random.uniform(low=-1 , high=1, size=(3,2))

rng3 = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng3.shuffle(array)
print(array)

rng4 = np.random.default_rng()
fruits = np.array(['apple', 'banana', 'cherry', 'date', 'elderberry'])
fruit = rng4.choice
print(fruit)
fruits = rng4.choice(fruits, size=(3,3))
print(fruits)