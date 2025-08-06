import cv2
import matplotlib.pyplot as plt

# image = cv2.imread('land_cruiser.jpeg')
#
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
# plt.imshow(image_rgb)
# plt.axis('off')
# plt.show()


#Load the image
image = cv2.imread('defender.jpeg')

if image is None:
    print("Error : Image not found")
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
    crop_size = 600

    cropped_image = image[
                    center_y - crop_size // 2 : center_y + crop_size // 2,
                    center_x - crop_size // 2 : center_x + crop_size // 2,
                    ]

    plt.figure(figsize=(12, 4))

    #display the original image
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    #sisplay cropped image
    plt.subplot(1, 2, 2) #rows, columns, position of image on row
    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    plt.title('Cropped image (600 X 600 - From Center)')
    plt.axis('off')

    #show the plots
    plt.tight_layout()
    plt.show()