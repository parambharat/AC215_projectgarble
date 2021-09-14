# Project Proposal
##Speech Information Explorer and Summarizer
 
## Team Members

- Ian Davenport: <iandavenport@g.harvard.edu>
- Joseph Kim: <josephkim@g.harvard.edu>
- Malla Reddy Adaboina: <maa0192@g.harvard.edu>
- Ramanathan P: <rap940@g.harvard.edu>
 
## Problem Definition

Extract and summarize monologue audio to assist note-takers.

...
 
## Proposed Solution

Build an application that generates a Summary of Speech (Lectures, Podcasts, News Reports, and other speeches and monologues). We could leverage pre-trained models to transcribe, segment, and summarize the audio. The project would allow us to design, develop, and deploy scalable pipelines that combine speech-to-text models with summarization techniques.
 
## Project Scope
 
- Monologue Speech
- Extractive Summaries

### Level 1

Assume automatic transcript is available from an existing service
Focus on segmentation, summarization, and extraction pipelines

### Level 2
Assume only audio file is available
Focus on ASR, error correction, segmentation and summarization pipelines

## Timeline and Components
 

## Datasets and Models

### Datasets

- https://tensorflow.google.cn/datasets/catalog/tedlium?hl=zh-cn
- https://github.com/zcgzcgzcg1/MediaSum
- https://paperswithcode.com/dataset/dialogsum
- https://podcastsdataset.byspotify.com/ [Need to request access)

### Models

- Transcription – Automatic Speech Recognition: [Wav2Vec](https://huggingface.co/transformers/model_doc/wav2vec2.html#wav2vec2)
- Topic Segmentation: [TextTiling with BERT](https://arxiv.org/pdf/2106.12978.pdf)
- Key phrase Identification: [KeyBert](https://github.com/MaartenGr/KeyBERT), [BertNER](https://huggingface.co/dslim/bert-base-NER)
- Summarization:
  - [Leveraging BERT for extractive summarization of lectures](https://paperswithcode.com/paper/leveraging-bert-for-extractive-text)
  - https://arxiv.org/pdf/2004.06190.pdf