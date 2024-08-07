# ConDenseCap

A prototype code repository for construction image dense captioning and safety hazard identification.

```
Proactive safety hazard identification using visual–text semantic similarity
for construction safety management

https://doi.org/10.1016/j.autcon.2024.105602
```

## Requirements

- Python 3
- PyTorch 1.8.1
- torchvision 0.9.1
- spaCy
- spacy-universal-sentence-encoder
- pandas
- numpy
- PIL
- h5py
- tqdm
- nlgeval: https://github.com/Maluuba/nlg-eval

we recommend using docker to install the pytorch environment:

```bash
docker pull pytorch/pytorch:1.8.1-cuda11.1-cudnn8-devel
#or
docker pull pytorch/pytorch:1.10.0-cuda11.3-cudnn8-devel

#then

pip install spacy, pandas, [...]
```

## Data Preparation

### Image Data

Please contact the authors of the following paper to obtain the images:

```
@article{zhang2022automatic,
  title={Automatic construction site hazard identification integrating construction scene graphs with BERT based domain knowledge},
  author={Zhang, Lite and Wang, Junjie and Wang, Yanbo and Sun, Hai and Zhao, Xuebing},
  journal={Automation in Construction},
  volume={142},
  pages={104535},
  year={2022},
  publisher={Elsevier}
}
```

### Labeling Data

Please contact the authors of this paper to obtain the label files:

```
place-holder-bibtex
```

### Data Structure

In our experiments, we labelled the above dedicated dataset and named it "con_densecap". The folder structure is like this:

```
 data
    ├── con_densecap
    │   ├── images (put the images in this folder)
    │   ├── region_descriptions.json (regional captioning labeling)
    │   ├── image_data.json (image information)
    │   └── densecap_splits.json (train/val split)
    ├── VG-regions-dicts-lite.pkl (this file will be genreated by the pre-processing)
    └── VG-regions-lite.h5 (this file will be genreated by the pre-processing)
```

You can also label your own data like the following format.

```
region_descriptions.json
{
  "id": [int], Unique identifier for this image,
  "regions": [
    {
      "id": [int] Unique identifier for this region,
      "height": [int] Height of the region in pixels,
      "width": [int] Width of the region in pixels,
      "x": [int] x-coordinate of the upper-left corner of the region,
      "y": [int] y-coordinate of the upper-left corner of the region,
      "category": [string] Optional classification of the object in this box,
      "phrase": [string] Caption for this region,
    },
    ...
  ]
}
```

```
image_data.json
{
    "image_id": [int] Unique identifier for this image,
    "width": [int] Width of the image in pixels,
    "height": [int] Height of the image in pixels,
    "filename": [string] Filename of this image
  }
```

## Acknowledgement

The captioning part is based upon https://github.com/soloist97/densecap-pytorch , most modifications are made about data preprocessing and using `torch.amp` during training instead of using `nvidia apex`.
