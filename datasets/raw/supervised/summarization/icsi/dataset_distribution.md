**Train Data  Distribution**
-  872 sentences, 11993 words and 45582 characters per row are the mean values and they are  close to the median values.
- Standard deviations are  small, but not too small.
- We observe that the maximum number of sentences (2258) and chars (more than 99034) are far away from the mean values, indicating that there are some registers with values out of range or outliers.

**Train Data Summary Distribution**

The distribution of words and sentences are far from mean value and the standard deviation is relatively  high.
Most summaries are composed by 73 sentence and the number of words is very close to 1335
The number of chars are mostly between 5125 and 5135.
There are few records with large values. Outliers is not a problem, we can remove them.

**Data Visualization**

The count of rows with outliers values is a large number, we can consider removing them but it does not look a great deal. The count of words looks like normal distribution, 75% of rows in the range 2239 words, 121 sentences and the count of char is a normal distribution.