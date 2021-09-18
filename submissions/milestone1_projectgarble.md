# Project Proposal: Speech Information Explorer and Summarizer
 
## Team
 - **Joseph Kim**: <josephkim@g.harvard.edu>
 - **Malla Reddy Adaboina**: <maa0192@g.harvard.edu>
 - **Ramanathan P**: <rap940@g.harvard.edu>
 
## Background
Spoken communication is a natural way to share ideas, thoughts and opinions. Today, a lot of this information is recorded and shared as audio data - lectures, talks, podcasts, interviews, political speeches, court proceedings, meetings, conferences, etc. Audio data however, can be computationally expensive to index, catalog, search and retrieve. Extracting the essence is crucial to distilling knowledge from spoken documents to make them searchable and reviewable. Transcribing the speech provides one solution to this problem by converting audio into computationally inexpensive and familiar text data.

Large pre-trained language models have recently revolutionized the field of natural language processing. Using large datasets of documents scraped from the internet, these models create deep contextualized representations of text. State of the art models using these representations show promising results in crucial language understanding tasks such as text classification, entity recognition, question answering and summarization.

Automatic speech summarization is a well studied method of spoken document understanding. Unlike written text, spoken language is riddled with repetitions, dis-fluencies, and fragmentations. Additionally, transcriptions are often long, erroneous, and lack punctuation, sentence segmentation and clarity. It’s crucial to solve these issues to develop a spoken document retrieval and summarization system. Commonly employed techniques include topic identification, topic segmentation, entity recognition, keyword/phrase identification, emotion classification, and summarization.
 
## Problem Definition
There is an abundance of text material available on the internet. Much of this text, however, provides more information than is needed. It is very difficult for human beings to manually summarize large documents of text. Therefore, a twofold problem is encountered. Searching for relevant documents through an overwhelming number of documents available, and absorbing a large quantity of relevant information. The goal of automatic text summarization is condensing the source text into a shorter version preserving its information content and overall meaning. A good summary system should reflect the diverse topics of the document while keeping redundancy to a minimum.

The problem that we wish to solve is similar to the challenge laid out in [2021 Trec Podcasts Task](https://trecpodcasts.github.io/). Our primary goal is to develop a set of tools that aid in assisted note taking for lecture talks and lectures. Therefore, we restrict the scope of this work to monologue documents with single speakers.

## Proposed Solution
We propose using state-of-art NLP models and techniques to do automatic speech summarization of transcripts. We plan to try two different summarization methods: extractive and abstractive. Extractive summarization methods select key sentences and phrases from the document and combine them into shorter forms. Abstractive summarization tries to understand the main content of the document and then explain them in clear natural language.

For the abstractive summarization method, we intend to follow the method outlined in this [paper](https://arxiv.org/abs/2004.02016) and model the data using a pre-trained hierarchical network. We’ll use their strategy of pre-training with news broadcast data and fine-tuning on talk descriptions to train our models for this task.

To achieve extractive summarization, we intend to perform sentence segmentation and topic segmentation by jointly training the hierarchical encoder for sentence tagging tasks. We wish to also explore entity extraction and keyphrase extraction and sentence selection methods to generate extractive summaries. 
 
## Components
- A large corpora of unlabelled spoken data for self-supervised pre-training tasks.
  - [OpenSubtitles Dataset](https://huggingface.co/datasets/viewer/?dataset=open_subtitles)
  - [Gutenberg Dialogue Dataset](https://github.com/ricsinaruto/gutenberg-dialog)
  - All text from the corpora that is annotated with summaries below.

- A large corpora of transcripts data along with summaries.
  - [Spotify podcast datset](https://podcastsdataset.byspotify.com)
  - Conversation Summaries:
    - [samsum](https://huggingface.co/datasets/samsum)
  - Broadcast News Datasets
    - [cc_news](https://huggingface.co/datasets/viewer/?dataset=cc_news) 
    - [cnn_dailymail](https://huggingface.co/datasets/viewer/?dataset=cnn_dailymail)
    - [xsum](https://huggingface.co/datasets/viewer/?dataset=xsum)
    - [MediaSum](https://github.com/zcgzcgzcg1/MediaSum)
    - [Cable TV News](https://tvnews.stanford.edu/data)
    - [Ted Talks](https://www.kaggle.com/thegupta/ted-talk)
    - Tools for text processing and analysis like Spacy, Gensim etc.
    - Pre-trained models available via tensorflow, HuggingFace and pytorch libraries.
 
## High-Level Stages
 - collect, and parse datasets for both pre-training and fine-tuning tasks.
 - perform basic EDA on the dataset using distributed compute techniques.
 - create cloud infrastructure for development and training
 - develop baseline model and define metrics
 - pre-train hierarchical encoder model for using self-supervised learning.
 - fine-tune document encoder for sentence selection and topic segmentation.
 - fine-tune sentence encoder for entity and key phrase extraction
 - fine-tune hierarchical model for summary generation.
 - measure and evaluate performance of models on a held-out test set.
 - deploy a quantized model on cloud infrastructure using docker and kubernetes.  
 
## References
 - [1].Edmundson, H.: New methods in automatic extracting. J. Assoc. Comput. Mach. 16(2), 264–285 (1969)
 - [2].Lloret, E., Palomar, M.: Text summarisation in progress: a literature review. Artif. Intell. Rev. 37(1), 1–41 (2011)
 - [3].Mani, I., Maybury, M.T.: Advances in Automatic Text Summarization. MIT, Cambridge (1999)
 - [4].Turner, J., Charniak, E.: Supervised and Unsupervised Learning for Sentence Compression. In: ACL, Michigan, Ann Arbor, USA. ACL, Stroudsburg, USA (2005)
 - [5].G PadmaPriya and K Duraiswamy. An approach for text summarization using deep learning algorithms. J Comput Sci, 10:1–9, 2014.
