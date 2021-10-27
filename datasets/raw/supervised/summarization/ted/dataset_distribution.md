**Train Data  Distribution**
-  93 sentences, 1759 words and 7443 characters per row are the mean values and they are  close to the median values.
- Standard deviations are  small, but not too small.
- We observe that the maximum number of sentences (461) and chars (more than 806) are far away from the mean values, indicating that there are some registers with values out of range or outliers.

**Train Data Summary Distribution**

The distribution of words and sentences are close to the mean value and the standard deviation is relatively small.
Most summaries are composed by 4 sentence and the number of words is very close to 64
The number of chars are mostly between 320 and 330.
There are few records with large values. Outliers is not a problem, we can remove them.

**Data Visualization**

The count of rows with outliers values is a small number, we can consider removing them but it does not look a great deal. The count of words looks like noraml distribution, 75% of rows in the range 78 words, 5 sentences and the count of char is a normal distribution. We do not identify weird examples or data distributions.