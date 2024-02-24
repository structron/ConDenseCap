import json

def read_result_from_json(json_path):
    # read result from json file
    # json_path: path to json file
    # return: [bbox, ...]

    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def confidence_filter(bboxes, confidence_threshold=0.5):
    # filter bboxes by confidence score
    # bboxes: [[x1, y1, x2, y2, score], ...]
    # return: [[x1, y1, x2, y2, score], ...]

    filtered_bboxes = []
    for bbox in bboxes:
        if bbox['score'] > confidence_threshold:
            filtered_bboxes.append(bbox)

    return filtered_bboxes

def main():

    json_path = './result.json'
    result = read_result_from_json(json_path)

    for k, v in result.items():
        result[k] = confidence_filter(v)

    with open('./filtered_result.json' , 'w') as f:
        json.dump(result, f, indent=4)

if __name__ == '__main__':
    main()