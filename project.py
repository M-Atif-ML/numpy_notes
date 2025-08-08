import numpy as np
import cv2

# Load image

img = cv2.imread("images.webp")

# Check if image loaded correctly
if img is None:
    print("Error: Image not found.")
    exit()

# Optional: Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Flip the RGB image
encrypted  = np.transpose(img_rgb,(0,1,2))
# Convert back to BGR for OpenCV display
encrypted_bgr = cv2.cvtColor(encrypted, cv2.COLOR_RGB2BGR)



cv2.imshow("Inc", encrypted_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
