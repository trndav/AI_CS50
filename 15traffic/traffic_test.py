# Not working
from traffic import IMG_HEIGHT, IMG_WIDTH, load_data

# images, labels = load_data("gtsrb-small")
images, labels = load_data("gtsrb")


for image in images:
    assert image.shape == (IMG_WIDTH, IMG_HEIGHT, 3)

print("Labels:", labels) 

# Labels range not correct
for label in labels:
    assert label in range(3)