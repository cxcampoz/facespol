import json
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.computervision._computer_vision_client import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

from msrest.authentication import CognitiveServicesCredentials
from PIL import Image, ImageDraw


class CheckFace:

    def __init__(self):
        self.credential = json.load(open('AzureCloudKeys.json'))
        self.FACE = self.credential["FACE"]
        self.VISION = self.credential["VISION"]

    def analyceImage(self, imageRoute):
        pass_trip = True
        dimentions = []
        face_client = FaceClient(
            self.FACE["ENDPOINT"], CognitiveServicesCredentials(self.FACE["API_KEY"]))

        # opens the file
        img_file = open(imageRoute, 'rb')

        response_detected_faces = face_client.face.detect_with_stream(
            image=img_file,
            detection_model='detection_01',
            recognition_model='recognition_04',
            return_face_attributes=["gender", "smile", "glasses"]
        )

        if not response_detected_faces:
            raise Exception('No face detected')

        analyce = [response_detected_faces[0].face_attributes.glasses,
                   response_detected_faces[0].face_attributes.smile, response_detected_faces[0].face_attributes.gender]

        if(analyce[0] == "noGlasses" and analyce[1] > 0.0):
            pass_trip = False

        print("\n----Analysis Results----\n")
        print("glasses: {} \n".format(analyce[0]))
        print("smile: {} \n".format(analyce[1]))
        print("gender: {} \n".format(analyce[2]))
        print("Pass: {} \n".format(pass_trip))
        print("----END----\n")

        img = Image.open(img_file)
        draw = ImageDraw.Draw(img)

        for face in response_detected_faces:
            rect = face.face_rectangle
            left = rect.left
            top = rect.top
            right = rect.width + left
            bottom = rect.height + top
            dimentions = [left, top, right, bottom]
            # draw.rectangle(((left, top), (right, bottom)),
            #                outline='green', width=5)

        # img.show()
        return [pass_trip, dimentions]

    def checkFamous(self, imageRoute):
        resultName = "none"
        computervision_client = ComputerVisionClient(
            self.VISION["ENDPOINT"], CognitiveServicesCredentials(self.VISION["API_KEY"]))

        with open(imageRoute, mode="rb") as image_stream:
            response = computervision_client.analyze_image_by_domain_in_stream(
                "celebrities", image_stream)

        if len(response.result["celebrities"]) > 0:
            resultName = response.result["celebrities"][0]["name"]
            print("name: {} ".format(resultName))

        return resultName
