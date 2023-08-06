from faster_coco_eval.faster_coco_eval import COCO

def read_gt_img(gt_data):
    anno = COCO(gt_data)
    img_ids = anno.getImgIds()
    img_len = len(img_ids)

    return img_len
