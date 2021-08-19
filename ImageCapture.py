import cv2

vid = cv2.VideoCapture(0)

img_counter = 0

while True:
    if img_counter == 11:
        break
    ret, frame = vid.read()

    cv2.imshow('frame',frame)

    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))

    img_counter += 1


if cv2.waitKey(1) & 0xFF == ord('q'):
    exit()

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
