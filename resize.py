import cv2


def crop_horizontal_lines(img, horizontal_lines):
    cropped_images = []

    height, _ = img.shape[:2]

    horizontal_lines = [0] + horizontal_lines + [height]

    for i, horizontal_line in enumerate(horizontal_lines):

        if i == len(horizontal_lines) - 1:
            continue

        y_start = horizontal_line
        y_end = horizontal_lines[i + 1]

        cropped_image = img[y_start:y_end, :]
        cropped_images.append(cropped_image)            
    
    return cropped_images


def crop_vertical_lines(img, vertical_lines):
    cropped_images = []

    _, width = img.shape[:2]

    vertical_lines = [0] + vertical_lines + [width]

    for i, vertical_line in enumerate(vertical_lines):

        if i == len(vertical_lines) - 1:
            continue

        x_start = vertical_line
        x_end = vertical_lines[i + 1]

        cropped_image = img[:, x_start:x_end]
        cropped_images.append(cropped_image)            
    
    return cropped_images


def resize_images(imgs, factor):
    resized_images = []
    for img in imgs:
        resized_image = cv2.resize(img, None, fx=factor, fy=factor)
        resized_images.append(resized_image)

    return resized_images


img = cv2.imread("image.png")

horizontal_crops = crop_horizontal_lines(img, [50, 100])

measures = []
measures += crop_vertical_lines(horizontal_crops[0], [300, 450])
measures += crop_vertical_lines(horizontal_crops[1], [300, 450])
measures += crop_vertical_lines(horizontal_crops[2], [300, 550])

print(len(measures))

resized_measures = resize_images(measures, 1.25)

for i, measure in enumerate(resized_measures):
    cv2.imshow(f"image {i}", measure)

cv2.waitKey(0)
cv2.destroyAllWindows()