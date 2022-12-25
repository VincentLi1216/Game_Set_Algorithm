import cv2
import numpy as np

# #設定圖片路徑
# input_path = []
# output_path = []
# for i in range(1,4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             for l in range(1, 4):
#                 in_path = "draw_rect_folder/unmarked_imgs/" + str(i) + str(j) + str(k) + str(l) + ".jpg"
#                 input_path.append(in_path)
#                 out_path = "draw_rect_folder/marked_imgs/" + str(i) + str(j) + str(k) + str(l) + "M.jpg"
#                 output_path.append(out_path)
#
#
#
# def draw_rect():
#     for i in range(81):
#         #讀入圖片、設定大小、仿射座標
#         original_img = cv2.imread(input_path[i])
#         nr,nc = original_img.shape[:2]
#         original_coor = np.float32([[0,0],[346,0],[346,533]])
#         resized_coor = np.float32([[10,10],[336,10],[336, 523]])
#
#         #仿射
#         T = cv2.getAffineTransform(original_coor,resized_coor)
#         transform_img = cv2.warpAffine(original_img,T,(nc,nr))
#
#         #畫邊框
#         final_img = cv2.rectangle(transform_img, (0, 0), (346, 533), (3,127,252), 20)
#
#         #儲存照片
#         cv2.imwrite(output_path[i], final_img)