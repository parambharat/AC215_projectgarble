**Train Data  Distribution**
-  22 sentences, 396 words and 1991 characters per row are the mean values and they are  close to the median values.
- Standard deviations are  small, but not too small.
- We observe that the maximum number of sentences (3489) and chars (more than 99629) are far away from the mean values, indicating that there are some registers with values out of range or outliers.

**Train Data Summary Distribution**

The distribution of words and sentences are far from mean value and the standard deviation is relatively  high.
Most summaries are composed by 2 sentence and the number of words is very close to 29
The number of chars are mostly between 145 and 155.
There are few records with large values. Outliers is not a problem, we can remove them.

**Data Visualization**

The count of rows with outliers values is a large number, we can consider removing them but it does not look a great deal. The count of words looks like right skewed distribution, 75% of rows in the range 38 words, 2 sentences and the count of char is a right skewed distribution. Complete data distribution is right skewed.