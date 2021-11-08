# Dataset Card Xsum Dataset

## Dataset Description

- **Homepage:** [XSum Home)](https://huggingface.co/datasets/xsum)
- **Repository:** [Xsum Github](https://github.com/huggingface/datasets/blob/master/datasets/xsum)


### Dataset Summary

The Extreme Summarization (XSum) dataset is a dataset for evaluation of abstractive single-document summarization systems. The goal is to create a short, one-sentence new summary answering the question “What is the article about?”. The dataset consists of 226,711 news articles accompanied with a one-sentence summary. The articles are collected from BBC articles (2010 to 2017) and cover a wide variety of domains (e.g., News, Politics, Sports, Weather, Business, Technology, Science, Health, Family, Education, Entertainment and Arts). The official random split contains 204,045 (90%), 11,332 (5%) and 11,334 (5) documents in training, validation and test sets, respectively.

### Supported Tasks and Leaderboards

Extractive and Abstractive Summarization: The dataset can be used to train a model for Extractive and Abstractive summarization, which consists, select key sentences and phrases from the document and combine them into shorter forms and Abstractive summarization tries to understand the main content of the document and then explain them in clear natural language. Success on this task is typically measured by [Rouge Score](https://en.wikipedia.org/wiki/ROUGE_(metric)).


### Languages

The dataset is in English.

## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 245.38 MB
- **Size of the generated dataset:** 507.60 MB
- **Total amount of disk used:** 752.98 MB

An example of 'validation' looks as follows.
```
{
    "document": "some-body",
    "id": "29750031",
    "summary": "some-sentence"
}
```

### Data Fields

he data fields are the same among all splits.

#### default
- `document`: a `string` feature.
- `summary`: a `string` feature.
- `id`: a `string` feature.

### Data Splits

| name  |train |validation|test |
|-------|-----:|---------:|----:|
|default|204045|     11332|11334|


## Dataset Creation

### Source Data

#### Final Data

**Final dataset has below structure**
```
{"document": ["CHITTAGONG, Bangladesh: Roshen Silva joined the run fest in Chittagong to score his maiden Test century as Sri Lanka took a 99-run lead in the first Test against Bangladesh on Saturday (Feb 3).", "The visitors reached 612-4 at lunch on the fourth day as they eased past Bangladesh's first innings total of 513 at the Zahur Ahmed Chowdhury Stadium.", "Silva made 109 off 230 balls before he became the only batsman to be dismissed in the first session of the day after Sri Lanka resumed on 504-3.", "He was Sri Lanka's third centurion in the innings after Kusal Mendis and Dhananjaya de Silva, who made 196 and 173 runs respectively.", "Off-spinner Mehedi Hasan ended Silva's impressive innings as the right-hander edged a low delivery to wicketkeeper Liton Das.", "Silva shared a 135-run stand with skipper Dinesh Chandimal for the fourth wicket and hit 6 fours and a six.", "Advertisement", "Advertisement", "Chandimal closed in on his 11 Test century and fifth against Bangladesh to remain unbeaten on 87 at the break.", "Wicketkeeper-batsman Niroshan Dickwella was accompanying him at the crease with 29 not out.", "Bangladesh had the chance to dismiss Chandimal on 79 but Liton dropped a catch down the leg side off Mehedi.", "The off-spinner himself was at fault a few overs later when he could not get his hand onto an edge offered by Dickwella off Taijul Islam as the ball raced for four.", "Dickwella made Bangladesh pay for the miss as he hit the next two balls also for four with his last boundary taking Sri Lanka past 600 runs.", "Sri Lanka will now look to consolidate their lead to press for victory on a wearing pitch that has started showing encouraging signs for their spinners."], "summary": ["Cricket: Silva hits maiden ton as Sri Lanka build lead"]}
```

### Citation Information


```
@article{Narayan2018DontGM,
  title={Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization},
  author={Shashi Narayan and Shay B. Cohen and Mirella Lapata},
  journal={ArXiv},
  year={2018},
  volume={abs/1808.08745}
}  
```

### Contributions

Thanks to [@thomwolf](https://github.com/thomwolf), [@lewtun](https://github.com/lewtun), [@mariamabarham](https://github.com/mariamabarham), [@jbragg](https://github.com/jbragg), [@lhoestq](https://github.com/lhoestq), [@patrickvonplaten](https://github.com/patrickvonplaten) for adding this dataset.