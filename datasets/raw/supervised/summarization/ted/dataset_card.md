# Dataset Card Ted Dataset

## Dataset Description

- **Homepage:** [Ted Talk Home](https://www.kaggle.com/rounakbanik/ted-talks)
- **Repository:** [Ted Talk Download](https://www.kaggle.com/account/login?titleType=dataset-downloads&showDatasetDownloadSkip=False&messageId=datasetsWelcome&returnUrl=%2Frounakbanik%2Fted-talks%3Fresource%3Ddownload)

### Dataset Summary

These datasets contain information about all audio-video recordings of TED Talks uploaded to the official TED.com website until September 21st, 2017. The TED main dataset contains information about all talks including number of views, number of comments, descriptions, speakers and titles. The TED transcripts dataset contains the transcripts for all talks available on TED.com.

Content
There are two CSV files.

ted_main.csv - Contains data on actual TED Talk metadata and TED Talk speakers.

transcripts.csv - Contains transcript and URL information for TED Talks

Acknowledgements
The data has been scraped from the official TED Website and is available under the Creative Commons License.

Inspiration
I've always been fascinated by TED Talks and the immense diversity of content that it provides for free. I was also thoroughly inspired by a TED Talk that visually explored TED Talks stats and I was motivated to do the same thing, albeit on a much less grander scale.

Some of the questions that can be answered with this dataset:

How is each TED Talk related to every other TED Talk?
Which are the most viewed and most favorited Talks of all time? Are they mostly the same? What does this tell us?
What kind of topics attract the maximum discussion and debate (in the form of comments)?
Which months are most popular among TED and TEDx chapters?
Which themes are most popular amongst TEDsters?

### Supported Tasks and Model Measurement

**Extractive and Abstractive Summarization**: The dataset can be used to train a model for Extractive and Abstractive summarization, which consists, select key sentences and phrases from the document and combine them into shorter forms and Abstractive summarization tries to understand the main content of the document and then explain them in clear natural language. Success on this task is typically measured by [Rouge Score](https://en.wikipedia.org/wiki/ROUGE_(met

### Languages

The dataset is in English language

## Dataset Structure

### Data Instances

Provide an JSON-formatted example and brief description of a typical instance in the dataset. If available, provide a link to further examples.

```
comments	description	duration	event	film_date	languages	main_speaker	name	num_speaker	published_date	ratings	related_talks	speaker_occupation	tags	title	url	views
4553	Sir Ken Robinson makes an entertaining and profoundly moving case for creating an education system that nurtures (rather than undermines) creativity.	1164	TED2006	1140825600	60	Ken Robinson	Ken Robinson: Do schools kill creativity?	1	1151367060	[{'id': 7, 'name': 'Funny', 'count': 19645}, {'id': 1, 'name': 'Beautiful', 'count': 4573}, {'id': 9, 'name': 'Ingenious', 'count': 6073}, {'id': 3, 'name': 'Courageous', 'count': 3253}, {'id': 11, 'name': 'Longwinded', 'count': 387}, {'id': 2, 'name': 'Confusing', 'count': 242}, {'id': 8, 'name': 'Informative', 'count': 7346}, {'id': 22, 'name': 'Fascinating', 'count': 10581}, {'id': 21, 'name': 'Unconvincing', 'count': 300}, {'id': 24, 'name': 'Persuasive', 'count': 10704}, {'id': 23, 'name': 'Jaw-dropping', 'count': 4439}, {'id': 25, 'name': 'OK', 'count': 1174}, {'id': 26, 'name': 'Obnoxious', 'count': 209}, {'id': 10, 'name': 'Inspiring', 'count': 24924}]	[{'id': 865, 'hero': 'https://pe.tedcdn.com/images/ted/172559_800x600.jpg', 'speaker': 'Ken Robinson', 'title': 'Bring on the learning revolution!', 'duration': 1008, 'slug': 'sir_ken_robinson_bring_on_the_revolution', 'viewed_count': 7266103}, {'id': 1738, 'hero': 'https://pe.tedcdn.com/images/ted/de98b161ad1434910ff4b56c89de71af04b8b873_1600x1200.jpg', 'speaker': 'Ken Robinson', 'title': "How to escape education's death valley", 'duration': 1151, 'slug': 'ken_robinson_how_to_escape_education_s_death_valley', 'viewed_count': 6657572}, {'id': 2276, 'hero': 'https://pe.tedcdn.com/images/ted/3821f3728e0b755c7b9aea2e69cc093eca41abe1_2880x1620.jpg', 'speaker': 'Linda Cliatt-Wayman', 'title': 'How to fix a broken school? Lead fearlessly, love hard', 'duration': 1027, 'slug': 'linda_cliatt_wayman_how_to_fix_a_broken_school_lead_fearlessly_love_hard', 'viewed_count': 1617101}, {'id': 892, 'hero': 'https://pe.tedcdn.com/images/ted/e79958940573cc610ccb583619a54866c41ef303_2880x1620.jpg', 'speaker': 'Charles Leadbeater', 'title': 'Education innovation in the slums', 'duration': 1138, 'slug': 'charles_leadbeater_on_education', 'viewed_count': 772296}, {'id': 1232, 'hero': 'https://pe.tedcdn.com/images/ted/0e3e4e92d5ee8ae0e43962d447d3f790b31099b8_800x600.jpg', 'speaker': 'Geoff Mulgan', 'title': 'A short intro to the Studio School', 'duration': 376, 'slug': 'geoff_mulgan_a_short_intro_to_the_studio_school', 'viewed_count': 667971}, {'id': 2616, 'hero': 'https://pe.tedcdn.com/images/ted/71cde5a6fa6c717488fb55eff9eef939a9241761_2880x1620.jpg', 'speaker': 'Kandice Sumner', 'title': "How America's public schools keep kids in poverty", 'duration': 830, 'slug': 'kandice_sumner_how_america_s_public_schools_keep_kids_in_poverty', 'viewed_count': 1181333}]	Author/educator	['children', 'creativity', 'culture', 'dance', 'education', 'parenting', 'teaching']	Do schools kill creativity?	"https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity
"	47227110
```



### Data Fields

- `comments`
-	`description`	
- `duration`
- `event`
- `film_date`
- `languages`
- `main_speaker`
- `name`
- `num_speaker`
- `published_date`	
- `ratings`
- `related_talks`	
- `speaker_occupation`
- `tags`	
- `title`	
- `url`
- `views`

### Data Splits

dataset split into Train, Validation and Test datasets

|                            | Tain   | Valid | Test |
| -----                      | ------ | ----- | ---- |
| Input Sentences            |   265526     |  57254     |   55849   |
| Average Sentence Length    |     93   |  94     |   92   |

## Dataset Creation

### Source Data

Kaggle

#### Who are the source language producers?

audio-video recordings of TED Talks uploaded to the official TED.com 

### Final Data

**Final dataset has below structure**
```
{"document": ["CHITTAGONG, Bangladesh: Roshen Silva joined the run fest in Chittagong to score his maiden Test century as Sri Lanka took a 99-run lead in the first Test against Bangladesh on Saturday (Feb 3).", "The visitors reached 612-4 at lunch on the fourth day as they eased past Bangladesh's first innings total of 513 at the Zahur Ahmed Chowdhury Stadium.", "Silva made 109 off 230 balls before he became the only batsman to be dismissed in the first session of the day after Sri Lanka resumed on 504-3.", "He was Sri Lanka's third centurion in the innings after Kusal Mendis and Dhananjaya de Silva, who made 196 and 173 runs respectively.", "Off-spinner Mehedi Hasan ended Silva's impressive innings as the right-hander edged a low delivery to wicketkeeper Liton Das.", "Silva shared a 135-run stand with skipper Dinesh Chandimal for the fourth wicket and hit 6 fours and a six.", "Advertisement", "Advertisement", "Chandimal closed in on his 11 Test century and fifth against Bangladesh to remain unbeaten on 87 at the break.", "Wicketkeeper-batsman Niroshan Dickwella was accompanying him at the crease with 29 not out.", "Bangladesh had the chance to dismiss Chandimal on 79 but Liton dropped a catch down the leg side off Mehedi.", "The off-spinner himself was at fault a few overs later when he could not get his hand onto an edge offered by Dickwella off Taijul Islam as the ball raced for four.", "Dickwella made Bangladesh pay for the miss as he hit the next two balls also for four with his last boundary taking Sri Lanka past 600 runs.", "Sri Lanka will now look to consolidate their lead to press for victory on a wearing pitch that has started showing encouraging signs for their spinners."], "summary": ["Cricket: Silva hits maiden ton as Sri Lanka build lead"]}
```

### Licensing Information

Copyright (c) 2020 Vishal Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
