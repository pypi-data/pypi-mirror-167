# coding: utf-8
import argparse
import numpy as np
from lvt_eval.utils.general import load_json
from faster_coco_eval.faster_coco_eval import COCO, COCOeval_faster
from lvt_eval.utils.merge_bbox import merge_bbox
from lvt_eval.tools.coco_error_analyze import coco_error_analysis
from lvt_eval.tools.cal_pred_error import cal_per_image_prediction_boxes_error, cal_image_prediction_error_rate
from lvt_eval.tools.cal_new_ap import cal_new_ap
from lvt_eval.tools.cal_precision_and_recall import cal_precision_and_recall
from lvt_eval.utils.check_predictions import check_predictions, check_json
from lvt_eval.utils.get_classes_and_imgs import get_classes_and_imgs

import logging
import copy
logging.basicConfig(format='%(asctime)s [%(pathname)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

total_results = dict()

class FasterCocoJsonEvaluation:
    def __init__(self, gt_json, pred_json):
        self.gt_json = gt_json
        self.pred_json = pred_json
    
    def indicator(self, thresholds =[0.0]):
        # thresholds = [0.0, 0.1]

        # pred_data = load_json(self.pred_json)
        # gt_data = load_json(self.gt_json) 
        pred_data = load_json(self.pred_json) if type(self.pred_json) == str else self.pred_json
        gt_data = load_json(self.gt_json) if type(self.gt_json) == str else self.gt_json


        names, classes, img_len, img_ids = get_classes_and_imgs(self.gt_json) # names: dict(), classes: list()
        nc = len(names)
        metrics = []
        for threshold in thresholds:
            this_metric = {"threshold": threshold, "metrics": {}, "category": []}
            logging.info("+-----------------------------------------------------------------------------------+") 
            logging.info('threshold = {}'.format(threshold))
            if gt_data["annotations"] == [] and len(pred_data) == 0:
                logging.info('The model accuracy is 100%, AP = 1.0, AR = 1.0')
                this_metric["metrics"] = {"AP_star": 1, "AP": 1, "AP50": 1, "AP75": 1, "APs": 1, "APm": 1, "APl": 1,"AR_50_95_all_1": 1, 
                                          "AR_50_95_all_10": 1, "AR_50_95_all_100": 1, "ARs": 1, "ARm": 1, "ARl": 1, "AR50": 1, "AR75": 1}
                this_metric["category"] = []

            elif gt_data["annotations"] == [] and pred_data:
                a_precision = 1
                pred_false_boxes = matched_pred_boxes = pred_data
                all_imgs_set = img_ids
                unmatch_pred_img = check_predictions(pred_data)
                new_ap = cal_new_ap(a_precision, pred_data, pred_false_boxes, unmatch_pred_img, all_imgs_set, matched_pred_boxes)
                this_metric["metrics"] = {"AP_star": new_ap, "AP": None, "AP50": None, "AP75": None, "APs": None,
                                          "APm": None, "APl": None, "AR_50_95_all_1": None, "AR_50_95_all_10": None, 
                                          "AR_50_95_all_100": None, "ARs": None, "ARm": None, "ARl": None, "AR50": None, "AR75": None}
                this_metric["category"] = []

            elif gt_data["annotations"] != [] and pred_data:           
                matched_pred_boxes, pred_false_boxes, unmatch_pred_img, matched_pred_imgs, all_imgs_set = check_json(pred_data, gt_data, threshold)

                if matched_pred_boxes == [] and pred_false_boxes == []:
                    a_precision = 1
                    this_metric["metrics"] = {"AP": 1, "AP50": None, "AP75": None, "APs": None,
                                              "APm": None, "APl": None, "AR_50_95_all_1": None, "AR_50_95_all_10": None, 
                                              "AR_50_95_all_100": None, "ARs": None, "ARm": None, "ARl": None, "AR50": None, "AR75": None}
                    this_metric["category"] = []
                elif matched_pred_boxes or (matched_pred_boxes and pred_false_boxes):
                    image_error_rate = cal_image_prediction_error_rate(matched_pred_boxes, pred_false_boxes, gt_data, img_len, threshold, classes)  
                    a_metrics, cate = self.cal_map(gt_data, matched_pred_boxes)
                    a_precision = a_metrics["AP"]
                    
                    pr_results = cal_precision_and_recall(gt_data, matched_pred_boxes, names, nc)
                    merge_results = merge_bbox(gt_data, matched_pred_boxes)
                    coco_error_analysis(merge_results, save_dir='./insect')
                    if pred_false_boxes:
                        prediction_boxes_error = cal_per_image_prediction_boxes_error(pred_false_boxes, img_len, threshold)
                    this_metric["metrics"] = copy.deepcopy(a_metrics)
                    this_metric["category"] = copy.deepcopy(cate)

                elif pred_false_boxes and unmatch_pred_img and not matched_pred_boxes:
                    prediction_boxes_error = cal_per_image_prediction_boxes_error(pred_false_boxes, img_len, threshold)
                    a_precision = 1
                    this_metric["metrics"] = {"AP": 1, "AP50": None, "AP75": None, "APs": None,
                                              "APm": None, "APl": None, "AR_50_95_all_1": None, "AR_50_95_all_10": None, 
                                              "AR_50_95_all_100": None, "ARs": None, "ARm": None, "ARl": None, "AR50": None, "AR75": None}
                    this_metric["category"] = []

                new_ap = cal_new_ap(a_precision, pred_data, pred_false_boxes, unmatch_pred_img, all_imgs_set, matched_pred_boxes, matched_pred_imgs)
                this_metric["metrics"].update({"AP_star": new_ap})
            metrics.append(this_metric)
        return metrics


    def cal_map(self, gt_data, pred_data):
    
        anno = COCO(gt_data)
        pred = anno.loadRes(pred_data)
        
        eval = COCOeval_faster(anno, pred, 'bbox')
        eval.evaluate()
        eval.accumulate()
        eval.summarize()
        metrics = ["AP", "AP50", "AP75", "APs", "APm", "APl", "AR_50_95_all_1", "AR_50_95_all_10", "AR_50_95_all_100", "ARs", "ARm", "ARl", "AR50", "AR75"]
        results = {
            metric: float(eval.stats[idx] if eval.stats[idx] >= 0 else "nan")
            for idx, metric in enumerate(metrics)
        }
        precisions = eval.eval["precision"]
        recalls = eval.eval["recall"]
        results_per_category_ap = []
        results_per_category_ar = []
        cats = list(eval.cocoGt.cats.values())
        class_names = [c["name"] for c in sorted(cats, key=lambda x: x["id"])]
        for idx, name in enumerate(class_names):
            # area range index 0: all area ranges
            # max dets index -1: typically 100 per image

            # AP per category
            precision = precisions[:, :, idx, 0, -1]
            precision = precision[precision > -1]
            precision_50 = precisions[0, :, idx, 0, -1]
            precision_75 = precisions[5, :, idx, 0, -1]
            ap = np.mean(precision) if precision.size else float("nan")
            ap_50 = np.mean(precision_50) if precision.size else float("nan")
            ap_75 = np.mean(precision_75) if precision.size else float("nan")
            
            results_per_category_ap.append(("{}".format(name), float(ap)))
            results_per_category_ap.append(("{}".format('50-' + name), float(ap_50)))
            results_per_category_ap.append(("{}".format('75-' + name), float(ap_75)))

            # AR per category
            recall = recalls[:, idx, 0, -1]
            recall = recall[recall > -1]
            ar = np.mean(recall) if recall.size else float("nan")
            results_per_category_ar.append(("{}".format(name), float(ar)))

        # for idx, name in enumerate(class_names):
        #     # area range index 0: all area ranges
        #     # max dets index -1: typically 100 per image
        #     recall = recalls[:, idx, 0, -1]
        #     recall = recall[recall > -1]
        #     ar = np.mean(recall) if recall.size else float("nan")
        #     results_per_category.append(("{}".format(name), float(ar * 100)))
        results.update({"AP-" + name: ap for name, ap in results_per_category_ap})
        results.update({"AR-" + name: ar for name, ar in results_per_category_ar})
        return results, class_names

        # precisions = eval.eval['precision']
        # a_precision = np.mean(precisions[:, :, :, 0, -1])
        #
        # return a_precision

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Start evaluation.')
    parser.add_argument('--gt_json', type=str, help='groundtruth absolute path', default='')
    parser.add_argument('--pred_json', type=str, help='prediction absolute path', default='')
    args = parser.parse_args()

    groundtruth_json = args.gt_json
    prediction_json = args.pred_json

    eval = FasterCocoJsonEvaluation(groundtruth_json, prediction_json)
    eval.indicator()
