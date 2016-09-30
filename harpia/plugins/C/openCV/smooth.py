#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin

class Smooth(OpenCVPlugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)
        self.smooth_type = "CV_GAUSSIAN"
        self.param1 = 7
        self.param2 = 9

    # ----------------------------------------------------------------------
    def get_help(self):
        return "Aplicação de um filtro de suavização. Suaviza os contornos de objetos na imagem, borrando-os levemente."

    # ----------------------------------------------------------------------
    def generate_vars(self):
        return \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'int block$id$_int_i1 = $param1$;\n' + \
            'int block$id$_int_i2 = $param2$;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n'

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        return \
            '\nif(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'block$id$_int_i1 = (block$id$_int_i1 %2 == 0)? block$id$_int_i1 + 1 : block$id$_int_i1;\n' + \
            'block$id$_int_i2 = (block$id$_int_i2 %2 == 0)? block$id$_int_i2 + 1 : block$id$_int_i2;\n' + \
            'cvSmooth(block$id$_img_i0, block$id$_img_o0 ,$smooth_type$,block$id$_int_i1,block$id$_int_i2,0,0);\n' + \
            '}\n'

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Label": "Smooth",
            "Icon": "images/smooth.png",
            "Color": "50:125:50:150",
            "InTypes": {0: "HRP_IMAGE", 1: "HRP_INT", 2:"HRP_INT"},
            "OutTypes": {0: "HRP_IMAGE"},
            "TreeGroup": "Filters and Color Conversion"
            }
    # ----------------------------------------------------------------------
    def get_properties(self):
        return {
        "smooth_type":{"name": "Type",
                    "type": HARPIA_COMBO,
                    "value": self.smooth_type,
                    "values": ["CV_GAUSSIAN", "CV_BLUR", "CV_MEDIAN"]
                    },
        "param1":{"name": "Parameter 1",
                    "type": HARPIA_INT,
                    "value": self.param1,
                    "lower":0,
                    "upper":99,
                    "step":1
                    },
        "param2":{"name": "Parameter 2",
                    "type": HARPIA_INT,
                    "value": self.param2,
                    "lower":0,
                    "upper":99,
                    "step":1
                    }
        }

# ------------------------------------------------------------------------------
