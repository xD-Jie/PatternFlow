# -*- coding: utf-8 -*-
# Author: Antoine DELPLACE
import numpy as np
import imageio

import vif


##Driver script
if __name__ == "__main__":
    img = imageio.imread("../../../lena_ref.bmp").astype(np.float32)
    img2 = imageio.imread("../../../lena_gauss_noise.bmp").astype(np.float32)
    img3 = imageio.imread("../../../lena_low_pass_filter.bmp").astype(np.float32)
    img4 = imageio.imread("../../../lena_jpeg.jpg", as_gray=True).astype(np.float32)

    print("Nearest")
    print(vif.pbvif(img, img))
    print(vif.pbvif(img, img2))
    print(vif.pbvif(img, img3))
    print(vif.pbvif(img, img4))

    print("Symmetric")
    print(vif.pbvif(img, img, mode="symmetric"))
    print(vif.pbvif(img, img2, mode="symmetric"))
    print(vif.pbvif(img, img3, mode="symmetric"))
    print(vif.pbvif(img, img4, mode="symmetric"))

    print("Constant")
    print(vif.pbvif(img, img, mode="constant"))
    print(vif.pbvif(img, img2, mode="constant"))
    print(vif.pbvif(img, img3, mode="constant"))
    print(vif.pbvif(img, img4, mode="constant"))
