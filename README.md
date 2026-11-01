# Social Media Hashtag Analysis using Hadoop MapReduce

## Project Overview

This project implements a distributed Social Media Hashtag Analysis system using Python, Apache Hadoop, Hadoop Streaming, and HDFS.

The objective is to analyze social media posts and calculate the frequency of hashtags using the MapReduce programming model.

Python scripts implement the Mapper, Combiner, and Reducer, while Hadoop manages distributed processing, partitioning, shuffling, sorting, and execution.

## Technologies Used

- Python 3
- Apache Hadoop 3.3.6
- Hadoop MapReduce
- Hadoop Streaming
- HDFS
- Ubuntu Linux

## Project Architecture

Social Media Posts
       |
       v
      HDFS
       |
       v
     Mapper
       |
       v
     Combiner
       |
       v
 Default Partitioner
       |
       v
  Shuffle and Sort
       |
       v
     Reducer
       |
       v
 Final Hashtag Frequency

## Input Dataset

The input dataset contains sample social media posts with hashtags.

Example:

    P1001 rahul #python #hadoop #bigdata
    P1002 priya #python #spark
    P1003 amit #hadoop #spark #bigdata
    P1004 neha #python #bigdata

## MapReduce Components

### 1. Mapper (mapper.py)

- Reads social media posts from standard input.
- Extracts hashtags using Python regular expressions.
- Converts hashtags to lowercase.
- Emits each hashtag with a count of 1.

Example:

    #python    1
    #hadoop    1
    #bigdata   1

### 2. Combiner (combiner.py)

- Performs local aggregation of Mapper output.
- Groups identical hashtags within a Mapper's output.
- Calculates partial hashtag frequencies.
- Reduces intermediate data transferred during the shuffle phase.

### 3. Partitioner

Hadoop's default HashPartitioner assigns intermediate keys to Reducers based on their hash values.

All identical keys are assigned to the same Reducer.

### 4. Shuffle and Sort

- Transfers Mapper output to Reducers.
- Groups identical hashtag keys.
- Sorts intermediate keys before reduction.

### 5. Reducer (reducer.py)

- Receives grouped hashtag counts.
- Calculates final hashtag frequencies.
- Writes the results to HDFS.

## Execution Workflow

1. Created the social media input dataset.
2. Uploaded the dataset to HDFS.
3. Implemented Mapper, Combiner, and Reducer using Python.
4. Tested the Python scripts locally.
5. Executed the MapReduce job using Hadoop Streaming.
6. Retrieved final hashtag frequencies from HDFS.
7. Verified successful execution through YARN.

## Hadoop Streaming Execution

The Hadoop Streaming JAR allows Python scripts to work with Hadoop MapReduce through standard input and output.

The job was executed using:

    hadoop jar hadoop-streaming-3.3.6.jar \
    -input /user/soumit/social_media/input/social_posts.txt \
    -output /user/soumit/social_media/output \
    -mapper mapper.py \
    -combiner combiner.py \
    -reducer reducer.py \
    -file mapper.py \
    -file combiner.py \
    -file reducer.py

## Final Output

The MapReduce job generated the following hashtag frequencies:

| Hashtag | Frequency |
|---------|-----------|
| #bigdata | 3 |
| #hadoop | 2 |
| #python | 3 |
| #spark | 2 |

## Execution Results

The Hadoop job completed successfully.

- Map Input Records: 4
- Map Output Records: 10
- Combiner Input Records: 10
- Combiner Output Records: 8
- Reduce Input Groups: 4
- Reduce Output Records: 4
- Map Tasks: 2
- Reduce Tasks: 1
- Failed Shuffles: 0
- YARN Final Status: SUCCEEDED

## Project Structure

    Social-Media-Hashtag-Analysis/
    |
    |-- input/
    |   |-- social_posts.txt
    |
    |-- mapper.py
    |-- combiner.py
    |-- reducer.py
    |-- README.md
    |
    |-- screenshots/

## Key Learnings

- Understanding the Hadoop MapReduce architecture.
- Implementing Python-based Hadoop Streaming jobs.
- Working with HDFS for distributed data storage.
- Understanding Mapper, Combiner, and Reducer.
- Learning default partitioning and shuffle/sort operations.
- Executing and monitoring MapReduce jobs using YARN.

## Conclusion

This project demonstrates how Hadoop MapReduce and Python Hadoop Streaming can process social media data to identify hashtag frequencies.
