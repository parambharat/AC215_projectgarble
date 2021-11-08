

# Dataset Card CC News Dataset

## Dataset Description

- **Homepage:** [CC News Homepage](https://huggingface.co/datasets/cc_news)
- **Repository:** [CC News Github](https://github.com/huggingface/datasets/tree/master/datasets/cc_news)
- **Paper:** [https://huggingface.co/datasets/cc_news]()
- **Point of Contact:** [Vladimir Blagojevic](dovlex@gmail.com)

### Dataset Summary

CC-News dataset contains news articles from news sites all over the world. The data is available on AWS S3 in the Common Crawl bucket at /crawl-data/CC-NEWS/. This version of the dataset has been prepared using [news-please](https://github.com/fhamborg/news-please) - an integrated web crawler and information extractor for news.
It contains 708241 English language news articles published between Jan 2017 and December 2019. It represents a small portion of the English language subset of the CC-News dataset.

### Supported Tasks and Model Mesaurement

The dataset can be used to train a model for Extractive and Abstractive summarization and Success on this task is typically measured by [Rouge Score](https://en.wikipedia.org/wiki/ROUGE_(metric)).


### Languages

The text in the dataset is in the English language.


## Dataset Structure

### Data Instances

Dataset instance contains an article itself and the relevant article fields. An example from the Cc-New train set looks as follows:

```
{
  'date': '2017-08-14 00:00:00',
  'description': '"The spirit of Green Day has always been about rising above oppression."',
  'domain': '1041jackfm.cbslocal.com',
  'image_url': 'https://cbs1041jackfm.files.wordpress.com/2017/08/billie-joe-armstrong-theo-wargo-getty-images.jpg?w=946',
  'text': 'By Abby Hassler\nGreen Day’s Billie Joe Armstrong has always been outspoken about his political beliefs. Following 
  the tragedy in Charlottesville, Virgina, over the weekend, Armstrong felt the need to speak out against the white supremacists 
  who caused much of the violence.\nRelated: Billie Joe Armstrong Wins #TBT with Childhood Studio Photo\n“My heart feels heavy. 
  I feel like what happened in Charlottesville goes beyond the point of anger,” Armstrong wrote on Facebook. “It makes me sad 
  and desperate. shocked. I f—— hate racism more than anything.”\n“The spirit of Green Day has always been about rising above 
  oppression. and sticking up for what you believe in and singing it at the top of your lungs,” Armstrong continued. 
  “We grew up fearing nuclear holocaust because of the cold war. those days are feeling way too relevant these days. 
  these issues are our ugly past.. and now it’s coming to haunt us. always resist these doomsday politicians. and in the 
  words of our punk forefathers .. Nazi punks f— off.”',
  'title': 'Green Day’s Billie Joe Armstrong Rails Against White Nationalists',
  'url': 'http://1041jackfm.cbslocal.com/2017/08/14/billie-joe-armstrong-white-nationalists/'
}
```



### Data Fields

- `date`: date of publication
- `description`: description or a summary of the article
- `domain`: source domain of the article (i.e. www.nytimes.com)
- `image_url`: URL of the article's image
- `text`: the actual article text in raw form
- `title`: title of the article
- `url`: article URL, the original URL where it was scraped. 


### Data Splits

CC-News dataset has only the training set, i.e. it has to be loaded with `train` split specified:
`cc_news = load_dataset('cc_news', split="train")`
for this project,  the train dataset is divided into train,
validation and test.

|                            | Tain   | Valid | Test |
| -----                      | ------ | ----- | ---- |
| Input Sentences            |  12738627      |   1613599    |  1584099    |
| Average Sentence Length    |     22   |   22    | 22     |

## Dataset Creation

CC-News has been mostly used for language model training.

### Source Data


#### Initial Data Collection and Normalization

CC-News dataset has been proposed, created, and maintained by Sebastian Nagel. 
The data is publicly available on AWS S3 Common Crawl bucket at /crawl-data/CC-NEWS/. 
This version of the dataset has been prepared using [news-please](https://github.com/fhamborg/news-please) - an 
integrated web crawler and information extractor for news.  
It contains 708241 English language news articles published between Jan 2017 and December 2019.
Although news-please tags each news article with an appropriate language tag, these tags are somewhat unreliable. 
To strictly isolate English language articles an additional check has been performed using 
[Spacy langdetect pipeline](https://spacy.io/universe/project/spacy-langdetect).   
We selected articles with text fields scores of 80% probability or more of being English.
There are no strict guarantees that each article has all the relevant fields. For example, 527595 
articles have a valid description field. All articles have what appears to be a valid image URL, 
but they have not been verified.

#### Who are the source language producers?

The news websites throughout the World.


### Personal and Sensitive Information

State whether the dataset uses identity categories and, if so, how the information is used. Describe where this information comes from (i.e. self-reporting, collecting from profiles, inferring, etc.). See [Larson 2017](https://www.aclweb.org/anthology/W17-1601.pdf) for using identity categories as a variables, particularly gender. State whether the data is linked to individuals and whether those individuals can be identified in the dataset, either directly or indirectly (i.e., in combination with other data).

State whether the dataset contains other data that might be considered sensitive (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history).  

If efforts were made to anonymize the data, describe the anonymization process.

## Considerations for Using the Data
As one can imagine, data contains contemporary public figures or individuals who appeared in the news.

### Social Impact of Dataset

The purpose of this dataset is to help language model researchers develop better language models.


### Final Data

**Final dataset has below structure**

```
{"document": ["CHITTAGONG, Bangladesh: Roshen Silva joined the run fest in Chittagong to score his maiden Test century as Sri Lanka took a 99-run lead in the first Test against Bangladesh on Saturday (Feb 3).", "The visitors reached 612-4 at lunch on the fourth day as they eased past Bangladesh's first innings total of 513 at the Zahur Ahmed Chowdhury Stadium.", "Silva made 109 off 230 balls before he became the only batsman to be dismissed in the first session of the day after Sri Lanka resumed on 504-3.", "He was Sri Lanka's third centurion in the innings after Kusal Mendis and Dhananjaya de Silva, who made 196 and 173 runs respectively.", "Off-spinner Mehedi Hasan ended Silva's impressive innings as the right-hander edged a low delivery to wicketkeeper Liton Das.", "Silva shared a 135-run stand with skipper Dinesh Chandimal for the fourth wicket and hit 6 fours and a six.", "Advertisement", "Advertisement", "Chandimal closed in on his 11 Test century and fifth against Bangladesh to remain unbeaten on 87 at the break.", "Wicketkeeper-batsman Niroshan Dickwella was accompanying him at the crease with 29 not out.", "Bangladesh had the chance to dismiss Chandimal on 79 but Liton dropped a catch down the leg side off Mehedi.", "The off-spinner himself was at fault a few overs later when he could not get his hand onto an edge offered by Dickwella off Taijul Islam as the ball raced for four.", "Dickwella made Bangladesh pay for the miss as he hit the next two balls also for four with his last boundary taking Sri Lanka past 600 runs.", "Sri Lanka will now look to consolidate their lead to press for victory on a wearing pitch that has started showing encouraging signs for their spinners."], "summary": ["Cricket: Silva hits maiden ton as Sri Lanka build lead"]}
```

