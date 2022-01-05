from PIL import Image, ImageFont, ImageDraw


class Credential:

    def __init__(self):
        self.a = "a"

    def createCredential(self, imageURL, personalData, cropImage):
        img = Image.open(imageURL, 'r')
        angles_right = 210
        angles_left = -220
        im_resized = img.crop(
            (cropImage[0]+angles_left, cropImage[1]+angles_left+50, cropImage[2]+angles_right, cropImage[3]+angles_right-50))
        im_resized = im_resized.resize((238, 250))

        carnet = Image.open("images/carnet/carnet_vacio.jpg")
        title_font = ImageFont.truetype('fonts/gb.ttf', 60)
        subtitle_font = ImageFont.truetype('fonts/gl.otf', 30)

        carnet_editable = ImageDraw.Draw(carnet)

        carnet_editable.text(
            (350, 250), personalData["Nombre"], (33, 33, 33), font=title_font)
        carnet_editable.text(
            (355, 310), personalData["Carrera"], (0, 87, 155), font=subtitle_font)
        carnet_editable.text(
            (45, 470), personalData["Facultad"], (33, 33, 33), font=subtitle_font)
        carnet_editable.text(
            (50, 570), personalData["Fecha de nacimiento"], (33, 33, 33), font=subtitle_font)

        carnet.paste(im_resized, (63, 109))

        carnet.show()
