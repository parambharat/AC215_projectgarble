**Train Data  Distribution**
-  39 sentences, 691 words and 3341 characters per row are the mean values and they are  close to the median values.
- Standard deviations are  small, but not too small.
- We observe that the maximum number of sentences (399) and chars (more than 13680) are far away from the mean values, indicating that there are some registers with values out of range or outliers.

**Train Data Summary Distribution**

The distribution of words and sentences are close to mean value and the standard deviation is relatively  low.
Most summaries are composed by 3 sentence and the number of words is very close to 51
The number of chars are mostly between 240 and 250.
There are few records with large values. Outliers is not a problem, we can remove them.

**Data Visualization**

The count of rows with outliers values is a large number, we can consider removing them but it does not look a great deal. The count of words looks like normal distribution, 75% of rows in the range 60 words, 4 sentences and the count of char is a normal distribution. Complete data distribution is right skewed.