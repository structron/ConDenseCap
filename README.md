# (WIP) Safety Hazard Identification Using Visual–Text Semantic Similarity for Construction Safety Management

A prototype code repository for construction image dense captioning and safety hazard identification.

Yiheng Wang, Bo Xiao, Ahmed Bouferguene, Mohamed Al-Hussein

Yiheng Wang : yiheng6 [AT] ualberta [dot] ca OR yihengw [AT] hust [DOT] edu [dot] cn

If you use this code repository in your research or wish to refer to the baseline results published in this study, please cite this paper:

```
place-holder-bibtex
```

## Requirements

- Python 3
- PyTorch 1.8.1
- torchvision 0.9.1
- spaCy
- pandas
- numpy
- PIL
- h5py
- tqdm
- nlgeval: https://github.com/Maluuba/nlg-eval

## Data Preparation

### Image Dataset

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

### Dense Captioning Labeling Data

Please contact the authors of the following paper to obtain the images:

```
place-holder-bibtex
```

### Data Structure

In our experiments, we labelled the above dedicated dataset and named it "con_densecap". The folder structure is like this:

```
 data
    ├── con_densecap
    │   ├── images (put the images in this folder)
    │   ├── region_descriptions.json
    │   └── image_data.json
    ├── VG-regions-dicts-lite.pkl (this file will be genreated by the pre-processing)
    └── VG-regions-lite.h5 (this file will be genreated by the pre-processing)
```

You can also label your own data like the follwoing format.

```
region_descriptions.json
[
  {
    "image_id": 1,
    "regions": [
      {
        "id": 0,
        "image_id": 1,
        "category": "worker",
        "phrase": "the clock is green in colour",
        "x": 100,
        "y": 100,
        "width": 200,
        "height": 300
      },
      ...
    ]
  }
  ...
]
```

```
image_data.json
[
  {
    "image_id": 1,
    "filename": "00001.jpg",
    "width": 1920,
    "height": 1080
    ]
    ...
  }
  ...
]
```

## Acknowledgement

The captioning part is based upon https://github.com/soloist97/densecap-pytorch , most modifications are made about using torch.amp during training instead of using nvidia apex.
