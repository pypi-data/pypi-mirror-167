# utf-8
import requests
import json
from tqdm import tqdm
import itertools
from terminaltables import AsciiTable
import os
import argparse
import numpy as np
from faster_coco_eval.faster_coco_eval import COCO, COCOeval_faster
from pycocotools.cocoeval import COCOeval

from lvt_eval.utils import *
from lvt_eval.tools.coco_error_analyze import coco_error_analysis
from lvt_eval.tools.cal_pred_error import cal_per_image_prediction_boxes_error, cal_image_prediction_error_rate
from lvt_eval.tools.cal_new_ap import cal_new_ap
from lvt_eval.tools.cal_precision_and_recall import cal_precision_and_recall
from lvt_eval.utils.read_gt_img import read_gt_img

import copy
import logging
logging.basicConfig(format='%(asctime)s [%(pathname)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

total_results = dict()

class StudioJsonEvaluation:
    def __init__(self):
        pass

    def save_predbox(self, config, json_result):
        prediction = []
        category = config.get('label')
        for cat in category:
            cat_pred = cat["prediction"]
            cat_id = cat['id']
            for i in json_result:
                if i["status"] == True:
                    continue
                else:
                    bbox_list = len(i["bbox_list"])
                    for b in range(bbox_list):
                        
                        if i["bbox_list"][b]["status"] == False:    # bbox的status为false，才会报警，故取该框
                            if isinstance(i["bbox_list"][b]["label"], str): # bbox的label为str格式
                                label = i["bbox_list"][b]["label"]
                            elif isinstance(i["bbox_list"][b]["label"], list): # bbox的label为list格式
                                label = i["bbox_list"][b]["label"][0]
                            if cat_pred == label:
                                image = int(i["id"])
                                score = 0
                                if isinstance(i["bbox_list"][b]["conf"], float): # bbox的conf为float格式
                                    score = i["bbox_list"][b]["conf"]
                                elif isinstance(i["bbox_list"][b]["conf"], list): # bbox的conf为list格式
                                    score = i["bbox_list"][b]["conf"][0]
                                bbox = i["bbox_list"][b]["bbox"]
                                x1, y1, x2, y2 = bbox[0], bbox[1], bbox[2], bbox[3]
                                box = [x1, y1, x2 - x1, y2 - y1]
                                pred = {
                                    "image_id": image,
                                    "category_id": cat_id,
                                    "bbox": box,  # xywh
                                    "score": score
                                }
                                prediction.append(pred)
                            if isinstance(label, int):
                                image = int(i["id"])
                                bbox, score =  i["bbox_list"][b]["bbox"], i["bbox_list"][b]["conf"]
                                x1, y1, x2, y2 = bbox[0], bbox[1], bbox[2], bbox[3]
                                box = [x1, y1, x2 - x1, y2 - y1]
                                pred = {
                                    "image_id": image,
                                    "category_id": cat_id,
                                    "bbox": box, 
                                    "score": score[0]
                                }
                                prediction.append(pred)
        logging.info("prediction save done.")
        return prediction

    def get_perbox(self, urls, res_id, aiport="http://192.1.2.238:8998/vql/v1/serving/process", includeCoincideRatio_name="person",
                includeCoincideRatio_ratio=0.95,
                includeCoincideRatio_threshold="0.1", excludeCoincideRatio=[], classesThreshold=0.3,
                displayAllBboxes=False, displayScore=True, boxEnlargeSize=3.2, bigModelQueryPositive=[],
                bigModelQueryNegative=[], bigModelExcludeCoincideRatio=[], bigModelIncludeCoincideRatio=[]):
        logging.info("success start get_perbox")
        src = []
        plaod = {
            "taskId": "123",
            # "schedulingCenter": {
            #     "linker_ai_debug_flag": "debug_mode_activate"
            # },  # debug使用的
            "schedulingCenter": {"checkServingDto": {"url": "CiSUryUCfphXUERWvkfhEOF8ox+P7GFhUEgIty9KQZIY7QUfRlwSS8EqBaB7uhfKUmjCHYRftXu+\n9o0wIXXmGQ=="}},
            "tasks": [],
            "src": src,
            "dest": [
                {
                    "linkage": {
                        "bucketName": "omeye",
                        "password": "",
                        "url": "http://192.1.2.249:8082/webdav/",
                        "username": ""
                    },
                    "destType": "webdav",
                    "kwargs": {}
                }
            ],
            "callback": "123",
            "kwargs": {}
        }
        
        for id, url in enumerate(tqdm(urls)):
            src_info = {
                "imageId": id + res_id,
                "data": url,
                "selectedRegions": [],
                "videoValidation": "346",
                "abilityCode": "target_detection",
                "eventTime": "2021-11-23 15:19:45",
                "kwargs": {
                    "startTime": "00:00:00",
                    "interval": 15,
                    "endTime": "23:59:00",
                    "isStart": False,
                    "isEnd": False,
                    "includeCoincideRatio": [
                        {
                            "name": includeCoincideRatio_name,
                            "ratio": includeCoincideRatio_ratio,
                            "threshold": includeCoincideRatio_threshold
                        }
                    ],
                    "excludeCoincideRatio": excludeCoincideRatio,
                    "classesThreshold": classesThreshold,
                    "displayAllBboxes": displayAllBboxes,
                    "displayScore": displayScore,
                    "boxEnlargeSize": boxEnlargeSize,
                    "bigModelQueryPositive": bigModelQueryPositive,
                    "bigModelQueryNegative": bigModelQueryNegative,
                    "bigModelExcludeCoincideRatio": bigModelExcludeCoincideRatio,
                    "bigModelIncludeCoincideRatio": bigModelIncludeCoincideRatio
                },
                "videoId": "1780",
                "srcType": "url"
            }
            src.append(src_info)
        save_json(plaod, "./prediction_dirs/plaod.json")
        
        result = requests.post(aiport, data=json.dumps(plaod)).text
        json_result = json.loads(result)
        logging.info("success end get_perbox")
        return json_result

    def get_groundtruth(self, raw_data, config, download_image=True): # 从studio_json中提取coco格式的groundtruth
        gt = {
            "info": {},
            "licenses": {},
            "images": list,
            "annotations": list,
            "categories": list
        }
        images = []
        annotations = []
        categories = []
        data = raw_data
        label = config.get('label')
        k = 0
        # add categories
        for ll in label:
            obj_mapping = ll["objectLabel"]
            at_mapping = ll["attrLabel"]
            lab_id = ll["id"]
            
            if isinstance(obj_mapping, list): # 若objectLabel包含多个目标
                if at_mapping == '':  # attrLabel没有包含任何属性
                    cat = {
                        "supercategory": str(obj_mapping),
                        "id": lab_id,
                        "name": str(obj_mapping),
                    } 
                elif isinstance(at_mapping, list): # attrLabel包含多个属性
                    cat = {
                    "supercategory": str(obj_mapping) + '-' + str(at_mapping),
                    "id": lab_id,
                    "name": str(obj_mapping) + '-' + str(at_mapping),
                    }
                else:
                    cat = {
                    "supercategory": str(obj_mapping) + '-' + at_mapping,
                    "id": lab_id,
                    "name": str(obj_mapping) + '-' + at_mapping,
                }
            elif isinstance(obj_mapping, str): # 若objectLabel包含单个目标
                if at_mapping == '': # attrLabel没有包含任何属性
                    cat = {
                        "supercategory": obj_mapping,
                        "id": lab_id,
                        "name": obj_mapping,
                    }
                elif isinstance(at_mapping, list): # attrLabel包含多个属性
                    cat = {
                        "supercategory": obj_mapping + '-' + str(at_mapping),
                        "id": lab_id,
                        "name": obj_mapping + '-' + str(at_mapping),
                    }
                else:
                    cat = {
                        "supercategory": obj_mapping + '-' + at_mapping,
                        "id": lab_id,
                        "name": obj_mapping + '-' + at_mapping,
                    }
            categories.append(cat)
        
        image_id_mapping = {}
        # add images
        for i in tqdm(data):
            if i["marked"] in [1, 2, 3]:
                img = {
                    "license": 0,
                    "file_name": i["url"],
                    "coco_url": i["url"],
                    "height": i["height"],
                    "width": i["width"],
                    "depth": 3,
                    "id": i["id"]
                }
                images.append(img)
                if download_image == True:
                    download_img(i['url'])  # 下载图片
                image_id_mapping[i["id"]] = i['url'].split('/')[-1]
                
                # add annotations
                for l in label:                    
                    object_mapping = l["objectLabel"]
                    attr_mapping = l["attrLabel"]
                    label_id = l["id"]
                    # for obj in object_mapping:
                    for j in i["markData"]:
                        if j["objLabel"][0]["name"] in object_mapping and attr_mapping != []:  
                            attr_len = len(j["attrLabel"])
                            if attr_len != 0:
                                for a in range(attr_len):
                                    if j["attrLabel"][a]["name"] in attr_mapping:
                                        x1, y1 = j["mouseFrom"]["x"], j["mouseFrom"]["y"]
                                        x2, y2 = j["mouseTo"]["x"], j["mouseTo"]["y"]
                                        w, h = x2 - x1, y2 - y1
                                        bbox = [x1, y1, w, h]
                                        ann = {
                                            "segmentation": [[]],
                                            "image_id": i["id"],
                                            "bbox": bbox,
                                            "category_id": label_id,
                                            "id": k,
                                            "iscrowd": 0,
                                            "area": w * h
                                        }
                                        annotations.append(ann)
                                        k += 1
                        elif j["objLabel"][0]["name"] in object_mapping and attr_mapping == []:  
                            x1, y1 = j["mouseFrom"]["x"], j["mouseFrom"]["y"]
                            x2, y2 = j["mouseTo"]["x"], j["mouseTo"]["y"]
                            w, h = x2 - x1, y2 - y1
                            bbox = [x1, y1, w, h]
                            ann = {
                                "segmentation": [[]],
                                "image_id": i["id"],
                                "bbox": bbox,
                                "category_id": label_id,
                                "id": k,
                                "iscrowd": 0,
                                "area": w * h
                            }
                            annotations.append(ann)
                            k += 1

                
        gt["images"] = images
        gt["annotations"] = annotations
        gt["categories"] = categories
        
        save_json(image_id_mapping, 'mapping_dirs/studio_image_id_mapping.json')
        logging.info("Save groundtruth done.")
        return gt

    def studio_cal_map(self, gt_data, pred_data, classes, threshold, faster_coco_api=True):

        if faster_coco_api == True:
            anno = COCO(gt_data)
            pred = anno.loadRes(pred_data)  
            eval = COCOeval_faster(anno, pred, 'bbox')
        else:
            anno = COCO(gt_data)
            pred = anno.loadRes(pred_data)
            eval = COCOeval(anno, pred, 'bbox')

        img_ids = anno.getImgIds()
        img_len = len(img_ids) # 图片的数量
        eval.evaluate()
        eval.accumulate()
        eval.summarize()
        metrics = ["AP", "AP50", "AP75", "APs", "APm", "APl", "AR_50_95_all_1", "AR_50_95_all_10", "AR_50_95_all_100", "ARs", "ARm", "ARl", "AR50", "AR75"]
        results = {
            metric: float(eval.stats[idx] if eval.stats[idx] >= 0 else "nan")
            for idx, metric in enumerate(metrics)
        }
        precisions = eval.eval['precision']
        recalls = eval.eval['recall']
        # from https://github.com/facebookresearch/detectron2/
        # precision: (iou, recall, cls, area range, max dets)
        results_per_category_ap = []
        results_per_category_ar = []
        results_per_category_iou50_95 = []
        results_per_category_iou50 = []
        res_item = []
        class_num = len(classes)
        
        for idx, catId in enumerate(range(class_num)):
            name = classes[idx]
            precision = precisions[:, :, idx, 0, -1]
            precision_50 = precisions[0, :, idx, 0, -1]
            precision = precision[precision > -1]

            recall = recalls[ :, idx, 0, -1]
            recall_50 = recalls[0, idx, 0, -1]
            recall = recall[recall > -1]

            if precision.size:
                ap = np.mean(precision)
                ap_50 = np.mean(precision_50)
                rec = np.mean(recall)
                rec_50 = np.mean(recall_50)
                false = 1 - rec
                false_50 = 1 - rec_50
            else:
                ap = float('nan')
                ap_50 = float('nan')
                rec = float('nan')
                rec_50 = float('nan')
                false = 1 - rec
                false_50 = 1 - rec_50
            res_item = [f'{name}', f'{float(ap):0.3f}',f'{float(rec):0.3f}', f'{float(false):0.3f}']
            results_per_category_iou50_95.append(res_item)
            res_item_50 = [f'{name}', f'{float(ap_50):0.3f}', f'{float(rec_50):0.3f}',  f'{float(false_50):0.3f}']
            results_per_category_iou50.append(res_item_50)
            results_per_category_ap.append(("{}".format(name), float(ap)))
            results_per_category_ar.append(("{}".format(name), float(rec)))

        item_num = len(res_item)
        num_columns = min(8, len(results_per_category_iou50_95) * item_num)
        results_flatten = list(
            itertools.chain(*results_per_category_iou50_95))
        headers = ['category', 'AP', 'AR', 'FalseRate'] * (num_columns // item_num)
        results_2d = itertools.zip_longest(*[
            results_flatten[i::num_columns]
            for i in range(num_columns)
        ])
        table_data = [headers]
        table_data += [result for result in results_2d]
        table = AsciiTable(table_data)
        logging.info("置信度取: {}".format(threshold))
        logging.info("IOU阈值取0.5-0.95的预测结果平均值:")
        logging.info('\n' + table.table)

        num_columns_50 = min(8, len(results_per_category_iou50) * item_num)
        results_flatten_50 = list(
            itertools.chain(*results_per_category_iou50))
        iou_ = int(eval.params.iouThrs[0] * 100)
        headers_50 = ['category', 'AP{}'.format(iou_),'AR{}'.format(iou_), 'FalseRate{}'.format(iou_)] * (num_columns_50 // item_num)
        results_2d_50 = itertools.zip_longest(*[
            results_flatten_50[i::num_columns_50]
            for i in range(num_columns_50)
        ])

        table_data_50 = [headers_50]
        table_data_50 += [result for result in results_2d_50]
        table_50 = AsciiTable(table_data_50)
        logging.info("IOU阈值大于0.5的预测结果平均值:")
        logging.info('\n' + table_50.table)

        # a_precision = np.mean(precisions[:, :, :, 0, -1])

        results.update({"AP-" + name: ap for name, ap in results_per_category_ap})
        results.update({"AR-" + name: ar for name, ar in results_per_category_ar})
        return img_len, results


    def indicator(self, config_path, thresholds = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]):
        config = load_json(config_path)
        aiport = config.get('aiport')
        data_path = config.get('rawdata')
        download = config.get('download')
        drawbox = config.get('draw')
        raw_prediction_path = config.get('raw_prediction_path')
        save_gt_path = config.get('save_gt_coco')
        save_pred_path = config.get('save_pred_path')
        faster_coco_api = config.get('faster_coco_api')

        # thresholds = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8] 
        urls, rawdata = get_pic_urls(data_path)
        len_urls = len(urls)
        l_labels = config.get('label')
        Classes, names_list, fin_res = [], [], []
        names = {}
        bak_id, res_id = 0, 0


        for c in range(len(l_labels)):
            if isinstance(config.get('label')[c]['objectLabel'], str): # 单个目标
                if config.get('label')[c]["attrLabel"] == '':
                    Classes.append(config.get('label')[c]["objectLabel"])
                    names[config.get('label')[c]["id"]] = config.get('label')[c]["prediction"]
                elif isinstance(config.get('label')[c]["attrLabel"], list):
                    Classes.append(config.get('label')[c]["objectLabel"] + '-' + str(config.get('label')[c]["attrLabel"]))
                    names[config.get('label')[c]["id"]] = config.get('label')[c]["prediction"]
                else:
                    Classes.append(config.get('label')[c]["objectLabel"] + '-' + config.get('label')[c]["attrLabel"])
                    names[config.get('label')[c]["id"]] = config.get('label')[c]["prediction"]
            elif isinstance(config.get('label')[c]['objectLabel'], list):  # 多个目标
                if config.get('label')[c]["attrLabel"] == '':
                    Classes.append(str(config.get('label')[c]["objectLabel"]))
                    names[config.get('label')[c]["id"]] = config.get('label')[c]["prediction"]
                elif isinstance(config.get('label')[c]["attrLabel"], list):
                    Classes.append(str(config.get('label')[c]["objectLabel"]) + '-' + str(config.get('label')[c]["attrLabel"]))
                    names[config.get('label')[c]["id"]] = config.get('label')[c]["prediction"]
                else:
                    Classes.append(str(config.get('label')[c]["objectLabel"]) + '-' + config.get('label')[c]["attrLabel"])
                    names[config.get('label')[c]["id"]] = config.get('label')[c]["prediction"]

        if os.path.exists(raw_prediction_path):
            pred_bak = load_json(raw_prediction_path)
            bak_id = int(pred_bak[-1]["id"])
            fin_res = pred_bak
            res_id = bak_id + 1
        if len_urls != res_id:
            # --------------调用aiport-------start
            logging.info("已经有{}张图片被检测过，从{}开始进行检测".format(bak_id, res_id))
            for imgs in chunks(urls, 100, 100, bak_id):
                if imgs:
                    res = self.get_perbox(imgs, res_id, aiport, classesThreshold=thresholds[0])["results"]["1780"]
                    fin_res += res
                    res_id += 100
                    save_json(fin_res, raw_prediction_path) # --------------保存aiport输出的结果
            # --------------调用aiport-------end

        fin_res = load_json(raw_prediction_path)
        pred_data = self.save_predbox(config, fin_res)
        save_json(pred_data, save_pred_path)
        gt_data = self.get_groundtruth(rawdata, config, download_image=download)  # 下载图片 download_image=True
        save_json(gt_data, save_gt_path)
        
        nc = len(names)
        for n in range(nc):
            names_list.append(names[n])
        
        _, _, _, img_ids = get_classes_and_imgs(save_gt_path)
        metrics = []

        for threshold in thresholds:
            this_metric = {"threshold": threshold, "metrics": {}}
            logging.info("+-----------------------------------------------------------------------------------+")
            logging.info('threshold = {}'.format(threshold))
            if gt_data["annotations"] == [] and len(pred_data) == 0:
                logging.info('The model accuracy is 100%, AP = 1.0, AR = 1.0')
                this_metric["metrics"] = {"AP_star": 1, "AP": 1, "AP50": 1, "AP75": 1, "APs": 1, "APm": 1, "APl": 1,"AR_50_95_all_1": 1,
                                          "AR_50_95_all_10": 1, "AR_50_95_all_100": 1, "ARs": 1, "ARm": 1, "ARl": 1, "AR50": 1, "AR75": 1}

            elif gt_data["annotations"] == [] and pred_data:
                a_precision = 1
                pred_false_boxes = matched_pred_boxes = pred_data
                all_imgs_set = img_ids
                unmatch_pred_img = check_predictions(pred_data)
                new_ap = cal_new_ap(a_precision, pred_data, pred_false_boxes, unmatch_pred_img, all_imgs_set, matched_pred_boxes)
                this_metric["metrics"] = {"AP_star": new_ap, "AP": None, "AP50": None, "AP75": None, "APs": None,
                                          "APm": None, "APl": None, "AR_50_95_all_1": None, "AR_50_95_all_10": None,
                                          "AR_50_95_all_100": None, "ARs": None, "ARm": None, "ARl": None, "AR50": None, "AR75": None}

            elif gt_data["annotations"] != [] and pred_data:
                matched_pred_boxes, pred_false_boxes, unmatch_pred_img, matched_pred_imgs, all_imgs_set = check_json(pred_data, gt_data, threshold)
                draw_box(gt_data, matched_pred_boxes, data_path.rsplit('/',2)[-1].split('.')[0], threshold, draw=drawbox) # draw=True 画框

                if matched_pred_boxes == [] and pred_false_boxes == []:
                    a_precision = 1
                    this_metric["metrics"] = {"AP": 1, "AP50": None, "AP75": None, "APs": None,
                                              "APm": None, "APl": None, "AR_50_95_all_1": None, "AR_50_95_all_10": None,
                                              "AR_50_95_all_100": None, "ARs": None, "ARm": None, "ARl": None, "AR50": None, "AR75": None}

                elif matched_pred_boxes or (matched_pred_boxes and pred_false_boxes):
                    img_len, a_metrics = self.studio_cal_map(gt_data, matched_pred_boxes, Classes, threshold, faster_coco_api)
                    a_precision = a_metrics["AP"]
                    image_error_rate = cal_image_prediction_error_rate(matched_pred_boxes, pred_false_boxes, gt_data, img_len, threshold, Classes)
                    pr_results = cal_precision_and_recall(gt_data, matched_pred_boxes, names, nc)
                    merge_results = merge_bbox(gt_data, matched_pred_boxes)
                    coco_error_analysis(merge_results, save_dir='./insect')
                    if pred_false_boxes:
                        prediction_boxes_error = cal_per_image_prediction_boxes_error(pred_false_boxes, img_len, threshold)
                    this_metric["metrics"] = copy.deepcopy(a_metrics)


                elif pred_false_boxes and unmatch_pred_img and not matched_pred_boxes:
                    img_len = read_gt_img(gt_data)
                    prediction_boxes_error = cal_per_image_prediction_boxes_error(pred_false_boxes, img_len, threshold)
                    a_precision = 1
                    this_metric["metrics"] = {"AP": 1, "AP50": None, "AP75": None, "APs": None,
                                              "APm": None, "APl": None, "AR_50_95_all_1": None, "AR_50_95_all_10": None,
                                              "AR_50_95_all_100": None, "ARs": None, "ARm": None, "ARl": None, "AR50": None, "AR75": None}

                new_ap = cal_new_ap(a_precision, pred_data, pred_false_boxes, unmatch_pred_img, all_imgs_set, matched_pred_boxes, matched_pred_imgs)
                this_metric["metrics"].update({"AP_star": new_ap})
            metrics.append(this_metric)
        return metrics


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start evaluation.')
    parser.add_argument('--config', type=str, help='config path', default='config/config_fire.json')
    args = parser.parse_args()

    config_path = args.config
    studio_eval = StudioJsonEvaluation()
    studio_eval.indicator(config_path)
