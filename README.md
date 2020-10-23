# Senior Data Engineer Homework

## Overview

Hello and thank you for applying to be a Senior Data Engineer here at Hinge!

As a Data Engineer, you will be tasked with loading data of various degrees of correctness, performing initial analysis of that data, and providing insight to our stakeholders. In this homework, you will be answering some questions about a dataset using Python and PostgreSQL.

## Assignment

In the folder `./dataset` is 14 files, a week's worth of data for user and marketing events. These files may contain errors as they are sourced from a somewhat unreliable provider. You will be loading these files into a PostgreSQL container.

Please perform the following:

1. Clone this repository and create a new branch.
2. Spin up a Docker container using the Dockerfile provided.
3. Write a script(s) in Python that will load that data into the PostgreSQL container.
    * The credentials for the Docker PostgreSQL are:
        ```
        username: postgres
        password: password
        ```
4. Answer the following questions (please provide the answer and the SQL used to get that answer):
    1. What is the number of unique users?
    2. Who are the marketing ad providers?
    3. Which user property is changed the most frequently?
    4. How many users were shown a Snapchat ad on July 3rd, 2019?
    5. Which ad was shown the most to users who identify as moderates?
    6. What are the top 5 ads? Explain how you arrived at that conclusion.

Please let us know when you are satisfied with your branch and when we can review it.

Your completed assignment should satisfy the following:

1. Your code must use Python to load the included datasets. Any transformations to the dataset you deem as necessary can be done via Python or SQL.
2. When provided instructions, we should be able to run your code locally and the dockerized PostreSQL instance should have the datasets loaded successfully.
3. Your repository should also contain the following files:
    1. `INSTALL.md`: instructions on how to run your code.
    2. `ANSWERS.md`: contains the answers to the dataset questions asked above.

If you have any questions at all, please reach out to us via email.
