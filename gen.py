# Synchronous image generator example
# make sure to read async_example.py to understand how to asynchronously generate images with Pillow 

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import discord
from config import Config
import requests

def _IMGtoFILE(IMG: Image) -> discord.File:
    with BytesIO() as image_binary:
        IMG.save(image_binary, 'PNG')
        image_binary.seek(0)

        return discord.File(fp=image_binary, filename='ad.png')

def _URLtoIMG(URL: str) -> Image:
    REQUEST = requests.get(URL)
    BYTES_CONTENT = REQUEST.content
    
    return Image.open(BytesIO(BYTES_CONTENT))

def GenerateImage(AD_IMG_DATA: dict[str, list[list[int], int, int]]) -> discord.File:
    """
    As Pillow is synchronous, you want to run this in a seperate thread. Use multithreading for this!
    
    AD_IMG_DATA EXAMPLE: {'OFFER': [[sshf_url, sshf_url, pv_url, skotn_url], robux], 'REQUEST': [[cwhp_url], robux]}
    """
  
    IMG_CONFIG = Config.IMAGE_GEN

    IMG_SIZE = IMG_CONFIG['SIZE']
    IMG_FONT = ImageFont.truetype(IMG_CONFIG['FONT'], IMG_CONFIG['FONT_SIZE'])
    IMG_CONSTANTS = IMG_CONFIG['CONSTANTS']
    IMG_TEMPLATE = Image.open(IMG_CONFIG['IMAGE_FILE'])

    main = IMG_TEMPLATE.resize(IMG_SIZE, Image.Resampling.LANCZOS)

    # Add images to template
    for side in AD_IMG_DATA:
        for i, asset_url in enumerate(AD_IMG_DATA[side][0]):
            img = _URLtoIMG(asset_url)
            img_position = (IMG_CONSTANTS[side]['X'] + (i * IMG_CONSTANTS[side]['SPACING']), IMG_CONSTANTS[side]['Y'])

            main.paste(img, img_position, img)

    # Add text to template
    draw = ImageDraw.Draw(main)
    for side in AD_IMG_DATA:
        value_text = str(AD_IMG_DATA[side][2])
        draw.text(IMG_CONSTANTS[side]['VALUE'], value_text, font=IMG_FONT, align="left", fill=IMG_CONSTANTS[side]['VALUE_RGBA'])

        robux_text = f'{AD_IMG_DATA[side][1]} Robux'
        draw.text(IMG_CONSTANTS[side]['ROBUX'], robux_text, font=IMG_FONT, align="left", fill=IMG_CONSTANTS[side]['ROBUX_RGBA'])

    return _IMGtoFILE(main)
