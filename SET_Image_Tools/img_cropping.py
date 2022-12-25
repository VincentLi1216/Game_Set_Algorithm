import cv2
import numpy as np

def crop_img():

    #設定原始圖片九個起始座標
    x_positions = [282, 836, 1391, 1946, 282, 836, 1391, 1946, 282, 836, 1391, 1946]
    y_positions = [111, 111,  111,  111, 476, 476,  476,  476, 841, 841,  841,  841]

    #設定原始圖片名稱
    image_names = ["IMG_D806A242A11F-1.jpeg"]

    #設定裁切區域的長度與寬度
    w = 533
    h = 346


    # 裁切區域的 x 與 y 座標（左上角）
    for n in range(len(image_names)):
        #讀取照片
        input_path = "img_cropping_folder/sorce_imgs/" + image_names[n]
        original_img = cv2.imread(input_path)

        for i in range(12):
            # 裁切圖片
            crop_img = original_img[y_positions[i]:y_positions[i] + h, x_positions[i]:x_positions[i] + w]
            final_img = np.rot90(crop_img)

            #儲存照片
            output_path = "img_cropping_folder/save_place_" + str(n+1) + "/" + str(n+1) + "_" + str(i+1) + ".jpg"
            cv2.imwrite(output_path, final_img)
            # cv2.imshow("finished", final_img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()




