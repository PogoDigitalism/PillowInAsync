class Config:
    """
    You will have to tweak these settings a lot until they match with your base template (IMAGE_FILE).

    These standard settings are not configured for the template 'example.png' either.
    """

    IMAGE_GEN = {
        'CONSTANTS': {
                    'OFFER': {
                        'SPACING': 315, # Horizontal spacing between images
                        'X': 125,
                        'Y': 75,
                        'ROBUX': (450, 60), # (X,Y) tuple
                        'VALUE': (450, 70),
                        'ROBUX_RGBA': (55, 100, 226, 255), # (R,G,B,A) text colour tuple
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

        'IMAGE_FILE': 'example.png', # serves as a template
        'SIZE': (1450, 600), # template size
        'FONT': 'segoeuib.ttf',
        'FONT_SIZE': 40,
    }
