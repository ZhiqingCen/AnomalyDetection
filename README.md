# AnomalyDetection

COMP9313 - Big Data Management, Project 1
- Term 3 2023, 25 Sep 2023 - 09 Oct 2023

- [AnomalyDetection](#anomalydetection)
  - [Anomaly detection from sensor readings (12 marks)](#anomaly-detection-from-sensor-readings-12-marks)
  - [Submission](#submission)
  - [Late submission penalty](#late-submission-penalty)
  - [Marking Criteria](#marking-criteria)

## Anomaly detection from sensor readings (12 marks)

**Background**: Anomaly detection aims to examine specific data points and detect rare occurrences that seem suspicious because they're different from the established pattern of behaviors. Anomaly detection is a crucial technique in various industries and domains where detecting unusual patterns or behaviors can lead to significant benefits, such as preventing fraud, ensuring safety, optimizing processes, and saving costs.

**Problem Definition**: You are given a dataset of sensor readings collected over time. Each record in the dataset consists of a station name where the sensor is located, a date, and a numerical sensor reading value reporting the humidity. A sample input file has been provided. Your task is to utilize MRJob to detect anomalies from the readings for each sensor based on the following steps:
- For each sensor, calculate the daily average humidity (daily average for short).
- For each sensor, calculate the overall average humidity (overall average for short)
- For each sensor on each day, calculate the gap between the daily and the overall average.
- Report all the readings such that the gap between the daily average and the overall average for that sensor on that day is larger than a given threshold $T$. 

**Output Format**: The output should contain three fields: the station name, the date, and the gap, in the format of `<the station name>\t<the date>,<the gap>`. The result should be sorted by the station name alphabetically first and then by the date in descending order. Given the sample input file and the threshold $T=20$, the result should be like:

~~~txt
"Foster Weather Station"	"2015-06-09.27.82352941176471"
"Foster Weather Station"	"2015-05-25,23.82352941176471"
"Oak Street Weather Station"	"2015-06-12,20.07692307692308"
"Oak Street Weather Station"	"2015-06-09.23.42307692307692"
"Oak Street Weather Station"	"2015-05-25.22.92307692307692"
~~~

One more test case is provided as well, and the value of $T$ is set to 30.

**Code Format**: The code template has been provided. Your code should take three parameters: the input file, the output folder on HDFS, and the threshold value $T$. We will also use more than 1 reducer to test your code. Assuming $T=20$ and using 2 reducers, you need to use the command below to run your code:

~~~console
$ python3 project1.py -r hadoop input -o hdfs_output --jobconf myjob.settings.tau=20 --jobconf mapreduce.job.reduces=2
~~~

Note: You can access the value of $T$ in your program like `tau = jobconf_from_env('myjob.settings.tau')`, and you need to `import jobconf_from_env` by `from mrjob.compat import jobconf_from_env` (see the code template). 

## Submission

Deadline: **Monday 9th October 11:59:59 PM**

If you need an extension, please apply for a special consideration via “myUNSW” first. You can submit multiple times before the due date and we will only mark your final submission. To prove successful submission, please take a screenshot as the assignment submission instructions show and keep it to yourself. If you have any problems with submissions, please email siqing.li@unsw.edu.au or yi.xu10@student.unsw.edu.au. 

## Late submission penalty

5% reduction of your marks for up to 5 days, submissions delayed for over 5 days will be rejected.

## Marking Criteria

- You must complete this assignment based on MRjob and Hadoop. Submissions only contain regular Python techniques will be marked as 0.
- You cannot simply emit all key-value pairs from mappers and buffer them in memory on reducers to do the task, and such a method will receive no more than 4 marks
- Submissions that cannot be compiled and run on Hadoop on the Ed environment will receive no more than 4. 
- Submissions can be compiled on ED and run on Hadoop. => +4
- All the gap values in the output are correct. =>+1
- The order in the output is correct. =>+1 (Note: You only need to guarantee the order within each reducer output)
- The output format is correct. => +1
- Submissions correctly implement the combiner or in-mapper combing. => +1
- Submissions correctly implement order inversion (i.e., using special keys). => +1
- Submissions correctly implement secondary sort. => +1
- Submissions can produce the correct result using one MRStep. => +1
- Submissions can produce the correct result with multiple reducers. => +1 (Note: You do not need to include 'mapreduce.job.reduces' in JOBCONF since the number of reducers will be received from the command)
