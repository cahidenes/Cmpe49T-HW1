import os
import random

test_count = 6986 // 5

names = os.listdir('trainA')

for _ in range(test_count):
    random_image = random.choice(names)
    os.rename(f'trainA/{random_image}', f'testA/{random_image}')
    os.rename(f'trainB/{random_image}', f'testB/{random_image}')
    names.remove(random_image)


