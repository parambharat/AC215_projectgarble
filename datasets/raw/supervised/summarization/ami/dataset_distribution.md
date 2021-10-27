**Train Data  Distribution**
-  830 sentences, 6177 words and 7443 characters per row are the mean values and they are  close to the median values.
- We observe that the maximum number of sentences (2154) and chars (more than 13157.00) are far away from the mean values, indicating that there are some registers with values out of range or outliers.

**Train Data Summary Distribution**

The distribution of words and sentences are not far from mean value and the standard deviation is relatively  low.
Most summaries are composed by 142 sentence and the number of words is very close to 1964
The number of chars are mostly between 7440 and 7450.
There are few records with large values. Outliers is not a problem, we can remove them.


**Data Visualization**

The count of rows with outliers values is a small number, we can consider removing them but it does not look a great deal. The count of words looks like noraml distribution, 75% of rows in the range 8010 words, 1092 sentences and the count of char is a normal distribution. We do not identify weird examples or data distributions.
