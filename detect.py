import cv2 as cv
import sys

def main():
    img_path = "data/screenshots/screenshot1.png"

    img = cv.imread(img_path)

    if img is None:
        print(f"Failed to load {img_path}")
        sys.exit(1)

    print(f"img loaded: {img.shape}")

    cv.imshow("screenshot", img)
    cv.waitKey(0)
    cv.destroyAllWindows

if __name__ == "__main__":
    main()