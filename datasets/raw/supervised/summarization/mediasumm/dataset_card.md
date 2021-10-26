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
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Social Impact of Dataset](#social-impact-of-dataset)
    - [Discussion of Biases](#discussion-of-biases)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [Mediasum ummary Home](https://arxiv.org/abs/2103.06410)
- **Repository:** [Mediasum GitHub](https://github.com/zcgzcgzcg1/MediaSum)
- **Paper:** [MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization](https://arxiv.org/abs/2103.06410)
- **Point of Contact:** [Chenguang Zhu]()

### Dataset Summary

MediaSum, a large-scale media interview dataset consisting of 463.6K transcripts with abstractive summaries. To create this dataset, we collect interview transcripts from NPR and CNN and employ the overview and topic descriptions as summaries. Compared with existing public corpora for dialogue summarization, our dataset is an order of magnitude larger and contains complex multi-party conversations from multiple domains. We conduct statistical analysis to demonstrate the unique positional bias exhibited in the transcripts of televised and radioed interviews. We also show that MediaSum can be used in transfer learning to improve a model's performance on other dialogue summarization tasks.

### Supported Tasks and Model Measurement

 The dataset can be used to train a model for Extractive and Abstractive summarization, which consists, select key sentences and phrases from the document and combine them into shorter forms and Abstractive summarization tries to understand the main content of the document and then explain them in clear natural language. Success on this task is typically measured by [Rouge Score](https://en.wikipedia.org/wiki/ROUGE_(metric)).

### Languages

The dataset is in english.

## Dataset Structure

### Data Instances



```
{
  "id": "NPR-11",
  "program": "Day to Day",
  "date": "2008-06-10",
  "url": "https://www.npr.org/templates/story/story.php?storyId=91356794",
  "title": "Researchers Find Discriminating Plants",
  "summary": "The \"sea rocket\" shows preferential treatment to plants that are its kin. Evolutionary plant ecologist Susan Dudley of McMaster University in Ontario discusses her discovery.",
  "utt": [
    "This is Day to Day.  I'm Madeleine Brand.",
    "And I'm Alex Cohen.",
    "Coming up, the question of who wrote a famous religious poem turns into a very unchristian battle.",
    "First, remember the 1970s?  People talked to their houseplants, played them classical music. They were convinced plants were sensuous beings and there was that 1979 movie, \"The Secret Life of Plants.\"",
    "Only a few daring individuals, from the scientific establishment, have come forward with offers to replicate his experiments, or test his results. The great majority are content simply to condemn his efforts without taking the trouble to investigate their validity.",
    ...
    "OK. Thank you.",
    "That's Susan Dudley. She's an associate professor of biology at McMaster University in Hamilt on Ontario. She discovered that there is a social life of plants."
  ],
  "speaker": [
    "MADELEINE BRAND, host",
    "ALEX COHEN, host",
    "ALEX COHEN, host",
    "MADELEINE BRAND, host",
    "Unidentified Male",    
    ..."
    Professor SUSAN DUDLEY (Biology, McMaster University)",
    "MADELEINE BRAND, host"
  ]
}
```

### Data Fields

- `id`: document id
- `program`: "Day to Day",
- `date`: Date,
- `url`:  URL,
- `title`: Title of the document
- `summary`: Summary of the document
- `utt`: Text of the document

### Data Splits
dataset splits into Train, Validation and Test datasets


|                            | Tain   | Valid | Test |
| -----                      | ------ | ----- | ---- |
| Input Sentences            |   13320852     |   292756    |    305636  |
| Average Sentence Length    |      30  |   29    |   30   |

## Dataset Creation

### Curation Rationale

[N/A]

### Source Data

 publicly available transcripts data from the media sources

#### Initial Data Collection and Normalization

[N/A]

#### Who are the source language producers?

publicly available transcripts.

### Annotations

[N/A]
#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

As media and guests may have biased views, the transcripts and summaries will likely contain them. The content of the transcripts and summaries only reflect the views of the media and guests, and should be viewed with discretion.

If efforts were made to anonymize the data, describe the anonymization process.

## Considerations for Using the Data

### Social Impact of Dataset

Please discuss some of the ways you believe the use of this dataset will impact society.

The statement should include both positive outlooks, such as outlining how technologies developed through its use may improve people's lives, and discuss the accompanying risks. These risks may range from making important decisions more opaque to people who are affected by the technology, to reinforcing existing harmful biases (whose specifics should be discussed in the next section), among other considerations.

Also describe in this section if the proposed dataset contains a low-resource or under-represented language. If this is the case or if this task has any impact on underserved communities, please elaborate here.

### Discussion of Biases

As media and guests may have biased views, the transcripts and summaries will likely contain them. The content of the transcripts and summaries only reflect the views of the media and guests, and should be viewed with discretion.

### Other Known Limitations

[N/A]

## Additional Information

### Dataset Curators

[N/A]

### Licensing Information

North American Chapter of the Association for Computational Linguistics (NAACL), Mexico City, Mexico, 2021

### Citation Information

```
@article{zhu2021mediasum,
  title={MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization},
  author={Zhu, Chenguang and Liu, Yang and Mei, Jie and Zeng, Michael},
  journal={arXiv preprint arXiv:2103.06410},
  year={2021}
}
```



### Contributions

Thanks to Chenguang Zhu*, Yang Liu*, Jie Mei and Michael Zeng (*: Equal contribution)