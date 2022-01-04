import cv2
import uuid


class Cammera:

    def __init__(self):
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cv2.namedWindow("ESPOL PHOTO TOOL")

    def takePhoto(self):
        img_counter = 0
        img_individual_name = ""
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("ESPOL PHOTO TOOL", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                if img_counter > 0:
                    print("limit of pics hit, closing...")
                    break
                # SPACE pressed
                img_individual_name = "{}.png".format(
                    uuid.uuid4())
                img_name = "images/cammera_pics/{}".format(
                    img_individual_name)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

        self.cam.release()
        cv2.destroyAllWindows()
        return img_name
