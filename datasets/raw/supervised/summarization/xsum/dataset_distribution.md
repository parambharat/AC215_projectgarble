**Train Data  Distribution**
-  20 sentences, 373 words and 1828 characters per row are the mean values and they are  close to the median values.
- Standard deviations are  small.
- We observe that the maximum number of sentences (1895) and chars (more than 144825) are not far from the mean values, indicating that there are some registers with values out of range or outliers.

**Train Data Summary Distribution**

The distribution of words and sentences are not far from mean value and the standard deviation is relatively  low.
Most summaries are composed by 1 sentence and the number of words is very close to 2921
The number of chars are mostly between 100 and 110.
There are few records with large values. Outliers is not a problem, we can remove them.

**Data Visualization**

The count of rows with outliers values is not a large number, we can consider removing them but it does not look a great deal. The count of words looks like normal distribution, 75% of rows in the range 24 words, 1 sentence and the count of char is a normal distribution. Summary of Word count is also normally distributed.