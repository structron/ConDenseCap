import json
from tqdm import tqdm

def calculate_overlap(box1, box2):

    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(box1[0], box2[0])
    yA = max(box1[1], box2[1])
    xB = min(box1[2], box2[2])
    yB = min(box1[3], box2[3])

    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    # compute the area of both the prediction and ground-truth
    # rectangles

    box1Area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2Area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    ioi = max(interArea/box1Area, interArea/box2Area)

    # return the intersection over union value
    return ioi

def get_main_bbox(bboxes):
    # get main bbox from group bboxes if the caption of the box start with 'worker'
    # bboxes: [[x1, y1, x2, y2], ...]
    # return: [box, ...]

    main_bboxes = []
    for bbox in bboxes:
        if bbox['cap'].startswith('worker'):
            main_bboxes.append(bbox)
    
    return main_bboxes

def group_bbox(bboxes, main_bboxes, ioi_threshold=0.5):
    # group bboxes by iou with main bboxes
    # bboxes: [[x1, y1, x2, y2, score], ...]
    # return: [[group1], [group2], ...]

    groups = []
    for main_bbox in main_bboxes:
        group = []
        for bbox in bboxes:
            iou = calculate_overlap(main_bbox['box'], bbox['box'])
            if iou > ioi_threshold:
                group.append(bbox)
        groups.append(group)

    return groups

def read_result_from_json(json_path):
    # read result from json file
    # json_path: path to json file
    # return: [bbox, ...]

    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def main():
    # get main bbox from group bboxes if the caption of the box start with 'worker'
    # group bboxes by iou with main bboxes
    # write result to json file

    json_path = './filtered_result.json'
    result = read_result_from_json(json_path)

    # transform dictionary to list and move the key into a value
    result = [dict({'img': k, 'bbox': v}) for k, v in result.items()]
    
    for img in tqdm(result):
        main_bboxes = get_main_bbox(img['bbox'])
        img['bbox'] = group_bbox(img['bbox'], main_bboxes)
    with open('./processed_result.json' , 'w') as f:
        json.dump(result, f, indent=4)

if __name__ == '__main__':
    main()