class Config:
    """
    You will have to tweak these settings a lot until they match with your base template (IMAGE_FILE).
    """

    IMAGE_GEN = {
        'CONSTANTS': {
                    'OFFER': {
                        'SPACING': 315,
                        'X': 125,
                        'Y': 75,
                        'ROBUX': (450, 60),
                        'VALUE': (450, 70),
                        'ROBUX_RGBA': (55, 100, 226, 255),
                        'VALUE_RGBA': (255, 255, 255, 255),
                        },        
                    'REQUEST': {
                        'SPACING': 315,
                        'X': 125,
                        'Y': 15,
                        'ROBUX': (450, 0),
                        'VALUE': (450, 10),
                        'ROBUX_RGBA': (55, 100, 226, 255),
                        'VALUE_RGBA': (255, 255, 255, 255),
                        },
                      },

        'IMAGE_FILE': 'concept2.png',
        'SIZE': (1450, 600),
        'FONT': 'segoeuib.ttf',
        'FONT_SIZE': 40,
    }
