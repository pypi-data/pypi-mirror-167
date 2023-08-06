
from tqdm import tqdm
import os
import cv2
import json
import numpy as np
import logging
# from plotbbox import plotBBox
logging.root.setLevel("INFO")
logging.debug("Запись.")

def draw_groundtruth(gt_info, root_dir, output_dir, mapping):
    for i in tqdm(gt_info['annotations']):
        im_path = os.path.join(root_dir, "download_images", mapping[str(i['image_id'])])
        gt_output_img = os.path.join(root_dir, output_dir, mapping[str(i['image_id'])])

        if not os.path.exists(gt_output_img):
            
            gt_out = cv2.imdecode(np.fromfile(im_path, dtype=np.uint8), cv2.IMREAD_COLOR)  # rgb
            if gt_out is None:
                continue

            r,g,b = cv2.split(gt_out)
            gt_out = cv2.merge([r,g,b]) 
            
        else: 
            gt_out = cv2.imdecode(np.fromfile(gt_output_img, dtype=np.uint8), cv2.IMREAD_COLOR)  # rgb
            
            if gt_out is None:
                continue
            r,g,b = cv2.split(gt_out)
            gt_out = cv2.merge([r,g,b]) 

        x, y, w, h = i["bbox"]
        x, y, w, h = int(x), int(y), int(w), int(h)
        x2, y2 = x + w, y + h
        # plotBBox(gt_out, x, y, x2, y2, color=(0, 0, 255), thickness=2) # red 
        cv2.rectangle(gt_out, (x, y), (x2, y2), (0, 0, 255), thickness=2) # red 
        cv2.imencode('.jpg', gt_out)[1].tofile(gt_output_img)

    logging.info("Groundtruth done.")

def draw_predictions(pred_info, root_dir, output_dir, mapping):
    for p in tqdm(pred_info):
        img_path = os.path.join(root_dir, "download_images", mapping[str(p['image_id'])])
        pred_output_img = os.path.join(root_dir, output_dir, mapping[str(p['image_id'])])
        
        score = p["score"]
        category = p['category_id']
        if not os.path.exists(pred_output_img):
            pred_out = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)  # rgb
            if pred_out is None:
                continue
            r,g,b = cv2.split(pred_out)
            pred_out = cv2.merge([r,g,b]) 
        else: 
            pred_out = cv2.imdecode(np.fromfile(pred_output_img, dtype=np.uint8), cv2.IMREAD_COLOR)  # rgb
            if pred_out is None:
                continue
            r,g,b = cv2.split(pred_out)
            pred_out = cv2.merge([r,g,b]) 
        
        x, y, w, h = p["bbox"]
        x, y, w, h = int(x), int(y), int(w), int(h)
        x2, y2 = x + w, y + h
        if float(score) >= 0.00:
            cv2.rectangle(pred_out, (x, y), (x2, y2), (0, 255, 0), thickness=2) # green
            cv2.putText(pred_out, "{:.3f} {}".format(score, category),(x + 5, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,127,0), 2)
        cv2.imencode('.jpg', pred_out)[1].tofile(pred_output_img)

    logging.info("Prediction done.")

def draw_box(gt_data, pred_data, filename, threshold, draw=True):
    if draw == True:
        gt_info = gt_data
        mapping = json.load(open('mapping_dirs/studio_image_id_mapping.json'))
        output_dir = os.path.join("draw_images_output", filename, str([threshold]))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        # draw groundtruth
        root_dir = os.getcwd()
        draw_groundtruth(gt_info, root_dir, output_dir, mapping)
        
        # draw predictions
        pred_info = pred_data
        draw_predictions(pred_info, root_dir, output_dir, mapping)

if __name__ == "__main__":
    gt_data = json.load(open("/home/liaojiajia/download/yh_coco_groundtruth.json"))
    pred_data = json.load(open("/home/liaojiajia/download/0823/yh_pred_v2.json"))
    clas = ['person']
    threshold = [0.0]
    draw_box(gt_data, pred_data, clas, threshold)