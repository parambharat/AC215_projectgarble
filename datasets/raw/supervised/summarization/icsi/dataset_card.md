# Dataset Card ICSI Data

## Dataset Description

- **Homepage:** [ICSI Home](http://www1.icsi.berkeley.edu/Speech/mr/)
- **Repository:** [ICSI download](https://groups.inf.ed.ac.uk/ami/icsi/download/)


### Dataset Summary

The ICSI Meeting Corpus is an audio data set consisting of about 70 hours of meeting recordings. More information can be found at the ICSI web site. To access the data, follow the directions given on the download page.

The audio was recorded on close-talking microphones - and available as either separate SPH files or a single mixed WAV file. Also available is orthographic transcription, and manual annotation of dialog acts and speech quality. Some third party annotations may also be made available here.

All of the signals and transcription, and some of the annotations, have been released publicly under the Creative Commons Attribution 4.0 International Licence (CC BY 4.0).

The collection includes 922 speech files, for a total of approximately 72 hours of Meeting Room speech. The speech is structured as one subdirectory per meeting, containing wavefiles for each channel (and possible .blp file, specifying any censored intervals).

The audio was collected at a 48 kHZ sample-rate, downsampled on the fly to 16 kHz. Audio files for each meeting are provided as separate time-synchronous recordings for each channel, encoded as 16-bit linear (big-endian) wavefiles, shorten-compressed in NIST SPHERE format.

The meetings were simultaneously recorded using close-talking microphones for each speaker (generally head-mounted, but early meetings contain some lapel microphones), as well as six table-top microphones: four high-quality omnidirectional PZM microphones arrayed down the center of the conference table, and two inexpensive microphone elements mounted on a mock PDA. All meetings were recorded in the same instrumented meeting room.

In addition to recording the meetings themselves, the participants were also asked to read digit strings, similar to those found in TIDIGITS, at the start or end of the meeting. This small-vocabulary read-speech component of the recordings -- using the same meeting room, speakers, and microphones -- provides a valuable supplement to the natural conversational data, allowing a factorization of the speech challenges offered by the corpus. For all but a dozen of the meetings included in the corpus, at least some of the participants read digit strings; for the great majority of meetings, all participants did. The digit readings are included as part of the wavefiles for the meeting as a whole and are fully transcribed as part of the associated transcripts.

There are a total of 53 unique speakers in the corpus. Meetings involved anywhere from three to 10 participants, averaging six. The corpus contains a significant proportion of non-native English speakers, varying in fluency from nearly-native to challenging-to-transcribe.

### Supported Tasks and Model measurement

Extractive and Abstractive Summarization: The dataset can be used to train a model for Extractive and Abstractive summarization, which consists, select key sentences and phrases from the document and combine them into shorter forms and Abstractive summarization tries to understand the main content of the document and then explain them in clear natural language. Success on this task is typically measured by [Rouge Score](https://en.wikipedia.org/wiki/ROUGE_(metric)).


### Languages

The dataset is available in english language

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

- `item1` = Description

- `item2` = Summary

### Data Splits
dataset split into Train, Validation and Test data sets

  For example:


|                            | Tain   | Valid | Test |
| -----                      | ------ | ----- | ---- |
| Input Sentences            |  35773      |  11650     |  5909    |
| Average Sentence Length    |    882    |    970   |  984    |

## Dataset Creation

### Curation Rationale

What need motivated the creation of this dataset? What are some of the reasons underlying the major choices involved in putting it together?

### Source Data

This section describes the source data (e.g. news text and headlines, social media posts, translated sentences,...)

#### Initial Data Collection and Normalization

Describe the data collection process. Describe any criteria for data selection or filtering. List any key words or search terms used. If possible, include runtime information for the collection process.

If data was collected from other pre-existing datasets, link to source here and to their [Hugging Face version](https://huggingface.co/datasets/dataset_name).

If the data was modified or normalized after being collected (e.g. if the data is word-tokenized), describe the process and the tools used.

#### Who are the source language producers?

State whether the data was produced by humans or machine generated. Describe the people or systems who originally created the data.

If available, include self-reported demographic or identity information for the source data creators, but avoid inferring this information. Instead state that this information is unknown. See [Larson 2017](https://www.aclweb.org/anthology/W17-1601.pdf) for using identity categories as a variables, particularly gender.

Describe the conditions under which the data was created (for example, if the producers were crowdworkers, state what platform was used, or if the data was found, what website the data was found on). If compensation was provided, include that information here.

Describe other people represented or mentioned in the data. Where possible, link to references for the information.

### Annotations

Annotations are in [NXT format](http://groups.inf.ed.ac.uk/nxt/). To use with signals downloaded below, unzip one or both of these files into the 'amicorpus' directory. Requires NXT version 1.4.4.

[ICSI core annotations](http://groups.inf.ed.ac.uk/ami/ICSICorpusAnnotations/ICSI_core_NXT.zip)v1.0 22-July-2016 (19MB): transcripts plus dialogue act coding
[ICSI core plus contributed annotations](http://groups.inf.ed.ac.uk/ami/ICSICorpusAnnotations/ICSI_plus_NXT.zip) v1.0 (53MB): all the above plus third-party annotations for topic, hotspot, summarization etc.
[ICSI original MRT format transcripts with documentation](http://groups.inf.ed.ac.uk/ami/ICSICorpusAnnotations/ICSI_plus_NXT.zip) (4MB)
To use the signals below with NXT, download the Headset mix files, and unzip them into the directory where your ICSI-metadata.xml file is. Some programs assume the wav files are directly in the Signals directory, so you may need to use soft links to use those programs with audio.

#### Final Data

**Final dataset has below structure**
```
{"document": ["CHITTAGONG, Bangladesh: Roshen Silva joined the run fest in Chittagong to score his maiden Test century as Sri Lanka took a 99-run lead in the first Test against Bangladesh on Saturday (Feb 3).", "The visitors reached 612-4 at lunch on the fourth day as they eased past Bangladesh's first innings total of 513 at the Zahur Ahmed Chowdhury Stadium.", "Silva made 109 off 230 balls before he became the only batsman to be dismissed in the first session of the day after Sri Lanka resumed on 504-3.", "He was Sri Lanka's third centurion in the innings after Kusal Mendis and Dhananjaya de Silva, who made 196 and 173 runs respectively.", "Off-spinner Mehedi Hasan ended Silva's impressive innings as the right-hander edged a low delivery to wicketkeeper Liton Das.", "Silva shared a 135-run stand with skipper Dinesh Chandimal for the fourth wicket and hit 6 fours and a six.", "Advertisement", "Advertisement", "Chandimal closed in on his 11 Test century and fifth against Bangladesh to remain unbeaten on 87 at the break.", "Wicketkeeper-batsman Niroshan Dickwella was accompanying him at the crease with 29 not out.", "Bangladesh had the chance to dismiss Chandimal on 79 but Liton dropped a catch down the leg side off Mehedi.", "The off-spinner himself was at fault a few overs later when he could not get his hand onto an edge offered by Dickwella off Taijul Islam as the ball raced for four.", "Dickwella made Bangladesh pay for the miss as he hit the next two balls also for four with his last boundary taking Sri Lanka past 600 runs.", "Sri Lanka will now look to consolidate their lead to press for victory on a wearing pitch that has started showing encouraging signs for their spinners."], "summary": ["Cricket: Silva hits maiden ton as Sri Lanka build lead"]}
```

### Other Known Limitations

If studies of the datasets have outlined other limitations of the dataset, such as annotation artifacts, please outline and cite them here.

## Additional Information

### Licensing Information

The ICSI corpus and its annotations are released under the Creative
Commons Attribution 4.0 license agreement (also called CC BY 4.0).
Use of this data implies agreement with the terms below. See also:
http://creativecommons.org/licenses/by/4.0/legalcode

### Citation Information
```
@@INPROCEEDINGS{Mccowan05theami,
    author = {I. Mccowan and G. Lathoud and M. Lincoln and A. Lisowska and W. Post and D. Reidsma and P. Wellner},
    title = {The AMI Meeting Corpus},
    booktitle = {In: Proceedings Measuring Behavior 2005, 5th International Conference on Methods and Techniques in Behavioral Research. L.P.J.J. Noldus, F. Grieco, L.W.S. Loijens and P.H. Zimmerman (Eds.), Wageningen: Noldus Information Technology},
    year = {2005}
}
```