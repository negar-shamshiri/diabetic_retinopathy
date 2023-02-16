#pre_processing
#pre_processing
import math
import numpy as np
from PIL import Image, ImageShow, ImageEnhance, ImageFilter
import cv2

class PreProcessing:

    def __init__(self, image):
        self.image = image

# contrast
# -----------------------------
    def controst(self, im):
        enhancer = ImageEnhance.Contrast(im)

        factor = 1.8 #increase contrast
        contrast_im = enhancer.enhance(factor)
        return contrast_im

# -----------------------------
# green channel
    def green_channel(self, contrast_im):
        green_channel = Image.Image.split(contrast_im)
        green_channel = green_channel[1]
        return green_channel

# ------------------------------
# color normalization
    def color_normalized(self, green_channel):
        def normalize(arr):
            arr = arr.astype('float')
            # Do not touch the alpha channel
            for i in range(3):
                minval = arr[...,i].min()
                maxval = arr[...,i].max()
                if minval != maxval:
                    arr[...,i] -= minval
                    arr[...,i] *= (255.0/(maxval-minval))
            return arr

        def demo_normalize(green_channel):
            arr = np.array(green_channel)
            new_img = Image.fromarray(normalize(arr).astype('uint8'))
            return new_img
            
        normalized = demo_normalize(green_channel)
        return normalized

# --------------------------------
# remove background
    def remove_back(self, normalized):
        median = normalized.filter(ImageFilter.MedianFilter(size = 29))
        sub2 = cv2.subtract(np.asarray(median),np.asarray(normalized))

        final_im2 = Image.fromarray(sub2)

        return final_im2

#-----------------------------------------
#function_call
    
    def pre_processed(self):
        
        controst_im = self.controst(self. image)
        green_channel = self.green_channel(controst_im)
        color_normalized = self.color_normalized(green_channel)
        remove_back = self.remove_back(color_normalized)
            
        return remove_back
