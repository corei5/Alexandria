# Paper name: Alexandria (Need to update)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/axcell-automatic-extraction-of-results-from/scientific-results-extraction-on-pwc)]()

This repository is the official implementation of [Alexandria](paper link).

![pipeline]()

## Requirements (Need to update)

To create a [conda](https://www.anaconda.com/distribution/) environment named `Alexandria` and install requirements run:

```setup
conda env create -f environment.yml
```

Additionally, `Alexandria` requires `docker` (that can be run without `sudo`). Run `scripts/pull_docker_images.sh` to download the necessary images.

## Datasets (Need to update)
We publish the following datasets:
* [ArxivPapers](https://github.com/paperswithcode/axcell/releases/download/v1.0/arxiv-papers.csv.xz)
* [other datasets](......)


See [datasets](notebooks/datasets.ipynb) notebook for an example of how to load the datasets provided below. The [extraction](notebooks/extraction.ipynb) notebook shows how to use `Alexandria` to extract text and tables from papers.

## Evaluation (Need to update)

See the [evaluation](notebooks/evaluation.ipynb) notebook for the full example of how to evaluate Alexandria on the Arxive dataset. 

### Prompt Engineering (Need to update)

## Fine-tuning (Need to update)

* [pre-training language model](notebooks/finetuning/lm.ipynb) on the ArxivPapers dataset 

## Pre-trained Models (Need to update)

You can download pre-trained models here:

- [axcell](https://github.com/paperswithcode/axcell/releases/download/v1.0/models.tar.xz) &mdash; an archive containing the taxonomy, abbreviations, table type classifier and table segmentation model. See the [results-extraction](notebooks/results-extraction.ipynb) notebook for an example of how to load and run the models 
- [language model](https://github.com/paperswithcode/axcell/releases/download/v1.0/lm.pth.xz) &mdash; [ULMFiT](https://arxiv.org/abs/1801.06146) language model pretrained on the ArxivPapers dataset

## Results (Need to update)

Alexandria achieves the following performance:

### 


| Dataset | Macro F1 | Micro F1 |
| ---------- |---------------- | -------------- |
| [PWC Leaderboards](https://paperswithcode.com/sota/scientific-results-extraction-on-pwc)     |     XXX         |      XXX      |
| [NLP-TDMS](https://paperswithcode.com/sota/scientific-results-extraction-on-nlp-tdms-exp)    |    XXX         |      XXX       |



## License

## Todo:

1. We do all evaluations with the abstracts using Lama 3 8b, 70b and Phi 3 Mini (Also Mixtral 8*7b and Mixtral 8*22b).
2. Then we do exactly the same thing again for entire papers with a sliding window where the content is first
   a) paraphrased into simple, short sentences and at the same time, number salad and artifacts are filtered out... and
   b) then knowledge graph segments are created from these simple, short sentences. ...
4. In addition, we do a sentence embedding and a bag of words from each of these simple, paraphrased short sentences.
5. When reconstructing the original text, we can then compare how
   a) the reconstruction works directly with the knowledge graph as the only input and
   b) how the reconstruction works when you give the knowledge graph and the bag of words as input and then again c) give the knowledge graph and the bag of words as context and then reconstruct the individual sentences from the respective bag of words sentence by sentence and the reconstruction candidates with the original sentence embedding comparison and those with the highest cosine similarity are selected


## Citation
The pipeline is described in the following paper:
```bibtex

```
