# Dataset Card Spotify Dataset

## Dataset Description

- **Homepage:** [Spotiyfy Home](https://podcastsdataset.byspotify.com)
- **Repository:** [Spotify Dataset](https://podcastsdataset.byspotify.com)

- **Point of Contact:** [Rosie Jones, Ben Carterette, Ann Clifton, Maria Eskevich, Gareth JF Jones, Jussi Karlgren, Aasish Pappu, Sravana Reddy, and Yongze Yu. "TREC 2020 Podcasts Track Overview." In the Twenty-Ninth Text REtrieval Conference Proceedings (TREC 2020). NIST Special Publication 1266. Ellen M. Voorhees and Angela Ellis (editors). 2021.
 ]()

### Dataset Summary

The podcast dataset contains about 100k podcasts filtered to contain only documents which the creator tags as being in the English language, as well as by a language filter applied to the creator-provided title and description. We expect that there will be a small amount of multilingual content that may have slipped through these filters.

Episodes were sampled from both professional and amateur podcasts including episodes produced in a studio with dedicated equipment by trained professionals, as well as episodes self-published from a phone app — these vary in quality depending on professionalism and equipment of the creator.

The episodes represent a wide range of:

Audio quality: we can expect professionally produced podcasts to have high audio quality, but there is significant variability in the amateur podcasts. We have included a basic popularity filter to remove most podcasts that are defective or noisy.
Topics: the episodes represent a wide range of topics, both coarse- and fine-grained. These include lifestyle and culture, storytelling, sports and recreation, news, health, documentary, and commentary.
Structural formats: podcasts are structured in a number of different ways. These include scripted and unscripted monologues, interviews, conversations, debate, and included clips of other non-speech audio material.



Each of the 100,000 episodes in the dataset includes an audio file, a text transcript, and some associated metadata.

Note that the data do not include listening data or other user or usage-related data.

The main data are separated into three top-level directories:
 
 
one for transcripts, one for RSS files, and one for audio data.
Since the audio files are vastly larger than the metadata, and not all researchers will choose to work on the audio data, we make these available for separate download.
The metadata can be found in a single csv file in the top-level directory.
In addition there are various annotations for the podcast data in separate directories. 
 
 
Audio directory:
 
OGG format available for separate download
Median duration of an episode ~ 31.6 minutes
Estimated size: ~2 TB for entire audio data set
 
 
Metadata:
 
Extracted basic metadata file in TSV format with fields: show_uri, show_name, show_description, publisher, language, rss_link, episode_uri, episode_name, episode_description, duration
 
Subdirectory for the episode RSS header files:
 
~1000 words with additional fields of potential interest, not necessarily aligned for every episode: channel, title, description, author, link, copyright, language, image
Estimated size: 145MB total for entire RSS set when compressed. 
 

Subdirectory for transcripts: 
 
JSON format
Average length is just under 6000 words, ranging from a small number of extremely short episodes to up to 45,000 words. Two-thirds of the transcripts are between about 1,000 and about 10,000 words in length; about 1% or 1,000 episodes are very short trailers to advertise other content. 
Estimated size: 12GB for entire transcript set.

Subdirectory for OpenSmile audio features 

eGeMAPS low level acoustic descriptors and functionals computed for overlapping 1.01s windows (75GB) saved in HDF5 format.

Subdirectory for Yamnet audio events 

1024-dimensional embedding vectors for overlapping 0.96s segments for the podcasts (400GB) and Yamnet event class scores (60GB), saved in HDF5 format.
 

### Supported Tasks and Model Measurement

The dataset can be used to train a model for Extractive and Abstractive summarization, which consists, select key sentences and phrases from the document and combine them into shorter forms and Abstractive summarization tries to understand the main content of the document and then explain them in clear natural language. Success on this task is typically measured by [Rouge Score](https://en.wikipedia.org/wiki/ROUGE_(metric)).

### Languages

Datasets are limited to English as the primary language. 

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

dataset splits into Train, Validation and Test datasets

|                            | Tain   | Valid | Test |
| -----                      | ------ | ----- | ---- |
| Input Sentences            |  6465664   |    811702    |    808169  |
| Average Sentence Length    |    82    |   82    |  82    |

## Dataset Creation

### Source Data

Tetadata and content of published podcast episodes


#### Who are the source language producers?

The previous Spoken Document Retrieval task at TREC: https://pdfs.semanticscholar.org/57ee/3a15088f2db36e07e3972e5dd9598b5284af.pdf

## Considerations for Using the Data

### Social Impact of Dataset

Contact the organizers: podcasts-challenge-organizers@spotify.com

#### Final Dataset

**Final dataset has below structure**

```
{"document": ["CHITTAGONG, Bangladesh: Roshen Silva joined the run fest in Chittagong to score his maiden Test century as Sri Lanka took a 99-run lead in the first Test against Bangladesh on Saturday (Feb 3).", "The visitors reached 612-4 at lunch on the fourth day as they eased past Bangladesh's first innings total of 513 at the Zahur Ahmed Chowdhury Stadium.", "Silva made 109 off 230 balls before he became the only batsman to be dismissed in the first session of the day after Sri Lanka resumed on 504-3.", "He was Sri Lanka's third centurion in the innings after Kusal Mendis and Dhananjaya de Silva, who made 196 and 173 runs respectively.", "Off-spinner Mehedi Hasan ended Silva's impressive innings as the right-hander edged a low delivery to wicketkeeper Liton Das.", "Silva shared a 135-run stand with skipper Dinesh Chandimal for the fourth wicket and hit 6 fours and a six.", "Advertisement", "Advertisement", "Chandimal closed in on his 11 Test century and fifth against Bangladesh to remain unbeaten on 87 at the break.", "Wicketkeeper-batsman Niroshan Dickwella was accompanying him at the crease with 29 not out.", "Bangladesh had the chance to dismiss Chandimal on 79 but Liton dropped a catch down the leg side off Mehedi.", "The off-spinner himself was at fault a few overs later when he could not get his hand onto an edge offered by Dickwella off Taijul Islam as the ball raced for four.", "Dickwella made Bangladesh pay for the miss as he hit the next two balls also for four with his last boundary taking Sri Lanka past 600 runs.", "Sri Lanka will now look to consolidate their lead to press for victory on a wearing pitch that has started showing encouraging signs for their spinners."], "summary": ["Cricket: Silva hits maiden ton as Sri Lanka build lead"]}
```


## Additional Information

### Licensing Information

[License](https://docs.google.com/forms/d/e/1FAIpQLSca2WJ45uamUWJ-C5HxHe7a9M1FuiSQPqukTjL8o-vthbQtnA/viewform) 

### Citation Information

```
100,000 Podcasts: A Spoken English Document Corpus” by Ann Clifton, Sravana Reddy, Yongze Yu, Aasish Pappu, Rezvaneh Rezapour, Hamed Bonab, Maria Eskevich, Gareth Jones, Jussi Karlgren, Ben Carterette, and Rosie Jones, COLING 2020
https://www.aclweb.org/anthology/2020.coling-main.519/

Bibtex:

@inproceedings{clifton-etal- 2020-100000,
    title = "100,000 Podcasts: A Spoken {E}nglish Document Corpus",
    author = "Clifton, Ann  and
      Reddy, Sravana  and
      Yu, Yongze  and
      Pappu, Aasish  and
      Rezapour, Rezvaneh  and
      Bonab, Hamed  and
      Eskevich, Maria  and
      Jones, Gareth  and
      Karlgren, Jussi  and
      Carterette, Ben  and
      Jones, Rosie",
    booktitle = "Proceedings of the 28th International Conference on Computational Linguistics",
    month = dec,
    year = "2020",
    address = "Barcelona, Spain (Online)",
    publisher = "International Committee on Computational Linguistics",
    url = "https://www.aclweb.org/ anthology/2020.coling-main.519 ",
    pages = "5903--5917",
    abstract = "Podcasts are a large and growing repository of spoken audio. As an audio format, podcasts are more varied in style and production type than broadcast news, contain more genres than typically studied in video data, and are more varied in style and format than previous corpora of conversations. When transcribed with automatic speech recognition they represent a noisy but fascinating collection of documents which can be studied through the lens of natural language processing, information retrieval, and linguistics. Paired with the audio files, they are also a resource for speech processing and the study of paralinguistic, sociolinguistic, and acoustic aspects of the domain. We introduce the Spotify Podcast Dataset, a new corpus of 100,000 podcasts. We demonstrate the complexity of the domain with a case study of two tasks: (1) passage search and (2) summarization. This is orders of magnitude larger than previous speech corpora used for search and summarization. Our results show that the size and variability of this corpus opens up new avenues for research.",
}
 
```


### Contributions

Thanks to [Ann Clifton, Sravana Reddy, Yongze Yu, Aasish Pappu, Rezvaneh Rezapour, Hamed Bonab, Maria Eskevich, Gareth Jones, Jussi Karlgren, Ben Carterette, and Rosie Jones, COLING 2020]()