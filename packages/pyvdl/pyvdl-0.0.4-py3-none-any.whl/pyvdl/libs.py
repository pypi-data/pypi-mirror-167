try:
    import matplotlib.pyplot as plt
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
    import numpy as np
    import cv2
except ImportError as e:
    import os
    os.system("python3 -m pip install matplotlib numpy opencv-python numba")
    raise e