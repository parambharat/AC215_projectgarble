**Train Data  Distribution**
-  30 sentences, 1554 words and 7150 characters per row are the mean values and they are  close to the median values.
- Standard deviations are  small, but not too small.
- We observe that the maximum number of sentences (2827) and chars (more than 382791) are far away from the mean values, indicating that there are some registers with values out of range or outliers.

**Train Data Summary Distribution**

The distribution of words and sentences are far from mean value and the standard deviation is   low.
Most summaries are composed by 2 sentence and the number of words is very close to 14
The number of chars are mostly between 7035 and 7045.
There are few records with large values. Outliers is not a problem, we can remove them.

**Data Visualization**

The count of rows with outliers values is a large number, we can consider removing them but it does not look a great deal. The count of words looks like right skewed distribution, 75% of rows in the range 199 words, 1 sentences and the count of char is a right skewed distribution. Complete data distribution is right skewed.