---
YAML tags:
- copy-paste the tags obtained with the tagging app: https://github.com/huggingface/datasets-tagging

annotations_creators:
- other
language_creators:
- other
languages:
- en-US
licenses:
- unknown
multilinguality:
- monolingual
pretty_name: 'Garble Summarization'
size_categories:
- unknown
source_datasets:
- extended|cc_news
- extended|cnn_dailymail
- extended|xsum
- extended|mediasumm
- extended|tedtalks
- extended|spotify
- extended|ami
- extended|icsi

task_categories:
- conditional-text-generation
task_ids:
- summarization
---

# Dataset Card Creation Guide

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Model Measurement](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://groups.inf.ed.ac.uk/ami/corpus/
- **Repository:** https://github.com/gcunhase/AMICorpusXML
- **Paper:** https://groups.inf.ed.ac.uk/ami/corpus/overview.shtml


### Dataset Summary

The AMI Meeting Corpus consists of 100 hours of meeting recordings. The recordings use a range of signals synchronized to a common timeline. These include close-talking and far-field microphones, individual and room-view video cameras, and output from a slide projector and an electronic whiteboard. During the meetings, the participants also have unsynchronized pens available to them that record what is written. The meetings were recorded in English using three different rooms with different acoustic properties, and include mostly non-native speakers.

  The AMI Meeting Corpus includes high quality, manually produced orthographic transcription for each individual speaker, including word-level timings that have derived by using a speech recognizer in forced alignment mode. It also contains a wide range of other annotations, not just for linguistic phenomena but also detailing behaviours in other modalities. These include dialogue acts; topic segmentation; extractive and abstractive summaries; named entities; the types of head gesture, hand gesture, and gaze direction that are most related to communicative intention; movement around the room; emotional state; and where heads are located on the video frames. The linguistically motivated annotations have been applied the most widely, and cover all of the scenario-based recordings. Other annotations are more limited, but in each case we have chosen what we consider a sensible data subset. For phenomena that are sparse in the meeting recordings, we have marked up auxiliary recordings where the behaviours are more common. These are also included in the corpus.

### Supported Tasks and Model Mesaurement


- Extractive and Abstractive Summarization: The dataset can be used to train a model for Extractive and Abstractive summarization, which consists, select key sentences and phrases from the document and combine them into shorter forms and Abstractive summarization tries to understand the main content of the document and then explain them in clear natural language. Success on this task is typically measured by [Rouge Score](https://en.wikipedia.org/wiki/ROUGE_(metric)).

### Languages

American English


## Dataset Structure

### Data Instances



```
<data>
    <items>
        <item name="item1">item1abc</item>
        <item name="item2">item2abc</item>
    </items>
</data>
```


### Data Fields

item1 = Description

item2 = Summary



### Data Splits


dataset split into Train, Validation and Test data sets

  For example:

|                            | Tain   | Valid | Test |
| -----                      | ------ | ----- | ---- |
| Input Sentences            |   78934     | 19571   | 8050      |
| Average Sentence Length    |    830    |  630     | 619     |

## Dataset Creation

Final dataset has below structure
```
{"document": ["New York (AP) \u2014 Sugar futures trading on the IntercontinentalExchange (ICE) Monday:", "(112,000 lbs.", "; cents per lb.)"], "summary": ["BC-US--Sugar, US", "BC-US--Sugar, US"]}
```
### Licensing Information

[License](http://creativecommons.org/licenses/by/4.0/legalcode)

### Citation Information


```
@INPROCEEDINGS{Mccowan05theami,
    author = {I. Mccowan and G. Lathoud and M. Lincoln and A. Lisowska and W. Post and D. Reidsma and P. Wellner},
    title = {The AMI Meeting Corpus},
    booktitle = {In: Proceedings Measuring Behavior 2005, 5th International Conference on Methods and Techniques in Behavioral Research. L.P.J.J. Noldus, F. Grieco, L.W.S. Loijens and P.H. Zimmerman (Eds.), Wageningen: Noldus Information Technology},
    year = {2005}
}
```

