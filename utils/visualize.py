import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.patches import Rectangle

def visualize_result(image_file_path, result):

    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)

    assert isinstance(result, list)

    img = Image.open(image_file_path)
    plt.imshow(img)
    ax = plt.gca()
    for r in result:
        ax.add_patch(Rectangle((r['box'][0], r['box'][1]),
                               r['box'][2]-r['box'][0],
                               r['box'][3]-r['box'][1],
                               fill=False,
                               edgecolor='red',
                               linewidth=3))
        ax.text(r['box'][0], r['box'][1], r['cap'], style='italic', bbox={'facecolor':'white', 'alpha':0.7, 'pad':10})
    fig = plt.gcf()
    plt.tick_params(labelbottom='off', labelleft='off')
    plt.show()

def visualize_densecap_results(image_file_path, result):
    # draw the bounding boxes on the image and draw the caption text outside the image with an arrow pointing to the box
    # result is a list of dictionaries, each dictionary has the following keys:
    # 'box': [x1, y1, x2, y2]
    # 'cap': caption string
    # 'score': score of the caption
    # 'box_score': score of the bounding box
    # 'box_feat': feature vector of the bounding box
    # 'cap_feat': feature vector of the caption
    # 'cap_len': length of the caption
    # 'cap_id': caption id

    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)

    assert isinstance(result, list)
    
    img = Image.open(image_file_path)
    plt.imshow(img)
    ax = plt.gca()
    for r in result:
        ax.add_patch(Rectangle((r['box'][0], r['box'][1]),
                               r['box'][2]-r['box'][0],
                               r['box'][3]-r['box'][1],
                               fill=False,
                               edgecolor='red',
                               linewidth=3))
        ax.text(r['box'][0], r['box'][1], r['cap'], style='italic', bbox={'facecolor':'white', 'alpha':0.7, 'pad':10})

    