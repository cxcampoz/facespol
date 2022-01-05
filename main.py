# This is the main execution program

from CheckFace import CheckFace
from Cammera import Cammera
from SearchData import SearchData
from credential import Credential


def main():
    faceChecker = CheckFace()
    searcher = SearchData()
    credentialMaker = Credential()
    # cammera = Cammera()
    # photo_path = cammera.takePhoto()
    photo_path = "images/tom_smile.jpg"
    data = faceChecker.analyceImage(photo_path)

    person = faceChecker.checkFamous(photo_path)
    personData = searcher.testAPI(person)
    credentialMaker.createCredential(photo_path, personData, data[1])
    # if(data[0]):
    #     person = faceChecker.checkFamous(photo_path)
    #     personData = searcher.testAPI(person)
    #     credentialMaker.createCredential(photo_path, personData, data[1])


if __name__ == "__main__":
    main()
