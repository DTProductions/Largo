import cv2

def crop_measures(img, horizontal_lines, vertical_lines):
    cropped_measures = []

    height, width = img.shape[:2]

    horizontal_lines = [0] + horizontal_lines + [height]
    vertical_lines = [0] + vertical_lines + [width]

    for i, horizontal_line in enumerate(horizontal_lines):
        if i == len(horizontal_lines) - 1:
            continue

        y_start = horizontal_line
        y_end = horizontal_lines[i + 1]

        for j, vertical_line in enumerate(vertical_lines):
            if j == len(vertical_lines) - 1:
                continue

            x_start = vertical_line
            x_end = vertical_lines[j + 1]
            
            cropped_measure = img[y_start:y_end, x_start:x_end]
            cropped_measures.append(cropped_measure)
    
    return cropped_measures


img = cv2.imread("image.png")
measures = crop_measures(img, [50,100], [300, 450])

resize_factor = 1

for i, measure in enumerate(measures):
    resized_measure = cv2.resize(measure, None, fx=resize_factor, fy=resize_factor)
    cv2.imshow(f"image {i}", resized_measure)

cv2.waitKey(0)
cv2.destroyAllWindows()