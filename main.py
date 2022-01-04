# This is the main execution program

from CheckFace import CheckFace
from Cammera import Cammera


def main():
    faceChecker = CheckFace()
    # cammera = Cammera()
    # photo_path = cammera.takePhoto()
    photo_path = "images/tom_fake.jpg"
    pass_trip = faceChecker.analyceImage(photo_path)
    if(pass_trip):
        faceChecker.checkFamous(photo_path)


if __name__ == "__main__":
    main()
