# PerceptionVisualization
Implementation for "Perception Visualization: Seeing Through the Eyes of a DNN".

## Running
1. In order to run these scripts you need to place the PASCAL VOC dataset in a folder called `./datasets/`. If you also want to use the default configuration please create folders `./models` and `./images`


2. We need to train the classifier, but first we need to setup the dataset from the raw PASCAL VOC form. run 'create_classifier_dataset.py' for this purpose.

2. You can now train the model using one of the training scripts, we recommend `voc_decoder_dsim.py`


3. With results from the training, we can create the dataset needed to train the decoder (from the embeddings generated by the model). Firstly run `create_decoder_dataset.py`.

3. Now train the decoder with `train_decoder_ssim_from_pretrained.py`


4. Now you can run and generate explanations using `test_decoder.py`

## Citing

If you use this in your work, please use this citation:

```
@article{giulivi2022perception,
  title={Perception Visualization: Seeing Through the Eyes of a DNN},
  author={Giulivi, Loris and Carman, Mark James and Boracchi, Giacomo},
  journal={arXiv preprint arXiv:2204.09920},
  year={2022}
}
```
