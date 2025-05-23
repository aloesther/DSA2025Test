# -*- coding: utf-8 -*-
"""DSA2025Test.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mVCIxq0ReToU58b_U10FNcDhx5u6O-Vb
"""

# Initialize Otter
import otter
grader = otter.Notebook("DSA2025Test.ipynb")

"""# DSA 2025 Summer School Admittance Check

Thanks for your interest in attending DSA 2025 Ibadan, Nigeria. To attend the summer school you have to have some level of basic Python proficiency. Completing the following notebook should ensure you have the right kind of background to benefit maximally from the Summer School. See you in Ibadan!

## Instructions
1. Complete each function according to the provided specifications
2. Run all cells to verify your solutions
3. All tests must pass to generate a submission
4. Save your work before submitting
"""

# Run these once ... To be on a safe side
!pip install nose
!pip install otter-grader
import IPython
from IPython import get_ipython
# Import the good stuff
import pandas as pd
import numpy as np
import math
from nose.tools import assert_equal
import otter
from collections import Counter
# Assuming your tests are in a directory called "tests"
# Create the directory if it doesn't exist
import os
if not os.path.exists("tests"):
    os.makedirs("tests")

grader = otter.Notebook("DSA2025Test.ipynb", tests_dir= "tests")

"""<!-- BEGIN QUESTION -->

**Question 1:**
Write a Python function to return a tuple of even and odd numbers

1.   List item
2.   List item

given an integer input.</br>
Example: For input 10, the output should be ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]).
"""

def even_odd_numbers(n):
    """
    Returns a tuple of even and odd numbers up to n.

    Args:
        n (int): The upper limit.

    Returns:
        tuple: A tuple of two lists: (evens, odds).
    """
    evens = [i for i in range(1, n + 1) if i % 2 == 0]
    odds = [i for i in range(1, n + 1) if i % 2 != 0]

    """
    Returns a tuple containing a list of even numbers and a list of odd numbers up to n (inclusive).
    """
    return (evens, odds)
# Example usage:
print(even_odd_numbers(10))

grader.check("q1")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 2: Create a dictionary to store the frequency of each word in the paragraph provided.**</br>
Example: For the paragraph "Data science is fun. Data science is useful.", the output should be {'Data': 2, 'science': 2, 'is': 2, 'fun': 1, 'useful': 1}.
"""

grader.check("q2")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 3: Extract the values from the dictionary above into a list and sort them in descending order.**</br>
Example: For the dictionary {'a': 3, 'b': 1, 'c': 2}, the output should be [3, 2, 1]
"""

def extract_and_sort_values(dictionary):
    """
    Extracts and sorts dictionary values in descending order.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        list: A list of sorted values in descending order.
    """
    value_list = [num for num in dictionary.values()]
    sorted_list = sorted(value_list, reverse=True)
    return sorted_list

    # Example dictionary
example_dict = {'a': 3, 'b': 1, 'c': 2}

# Expected output: [3, 2, 1]
print(extract_and_sort_values(example_dict))

grader.check("q3")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 4: Merge the two lists (from Questions 3 and 4) into a dictionary where the keys are the sorted keys and the values are the sorted values.**</br>
Example: For lists ['a', 'b', 'c'] and [3, 2, 1], the output should be {'a': 3, 'b': 2, 'c': 1}
"""

def merge_lists_to_dict(dictionary):  # Changed to accept a dictionary
    """
    Merges dictionary keys and sorted values into a new dictionary.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: A dictionary with sorted keys and values paired.
    """
    keys = sorted(dictionary.keys())
    values = sorted(dictionary.values(), reverse=True)
    return dict(zip(keys, values))

# Example usage:
print(merge_lists_to_dict(example_dict))  # Call with the dictionary

grader.check("q4")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 5:Write a function least_common_multiple that takes two inputs a and b and returns the least common multiple of the two numbers.**</br>
Example: For input (4, 6), the output should be 12
"""

def least_common_multiple(a, b):
    """
    Returns the least common multiple of two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: The LCM of a and b.
    """
    multiple = a * b
    # Use the greatest common divisor function from the maths module
    greatest_common_divisor = math.gcd(a,b)

    # Using floor division in order to get a integer output
    lcm = multiple // greatest_common_divisor
    return lcm

grader.check("q5")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 6:Write a function get_nearest_farthest that takes in a point of interest (x, y) and a list of points [(x1, y1), (x2, y2), ...] and returns the indices of the nearest and farthest points from the point of interest.** </br>
Example: For pt = (0, 0) and points = [(1, 1), (3, 3), (-1, -1)], the output should be (0, 1)
"""

def get_nearest_farthest(pt, points):

    """
    Returns the indices of the nearest and farthest points from a point of interest.

    Args:
        pt (tuple): The point of interest (x, y).
        points (list): List of points [(x1, y1), (x2, y2), ...].

    Returns:
        tuple: Indices of the nearest and farthest points.
    """
    distances = []
    for point in points:
        dist = abs(np.array(pt) - np.array(point))
        dist_magnitude = np.sum(dist)
        distances.append(dist_magnitude)

    nearest_point = min(distances)
    farthest_point = max(distances)

    return (distances.index(nearest_point), distances.index(farthest_point))

grader.check("q6")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 7:Write a function filter_divisible to return a list of numbers between 0 and a number N that are not perfectly divisible by q.** </br>

> Hint: If N is negative, use N = 20.

Example: For N = 10 and q = 2, the output should be [1, 3, 5, 7, 9]
"""

def filter_divisible(N, q):
    """
    Returns a list of numbers between 0 and N that are not divisible by q.

    Args:
        N (int): The upper limit.
        q (int): The divisor.

    Returns:
        list: A list of non-divisible numbers.
    """
    non_divisible_nums = []
    for i in range(N+1):
        if i % q != 0:
            non_divisible_nums.append(i)

    return non_divisible_nums

grader.check("q7")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 8: Write a function flatten_and_unique that takes in a list of lists and outputs a sorted list of unique elements from all sublists.**
"""

def flatten_and_unique(list_of_lists):
    """
    Flattens a list of lists and returns a sorted list of unique elements.

    Args:
        list_of_lists (list): A list of lists.

    Returns:
        list: A sorted list of unique elements.
    """
    all_elements = []
    for sublist in list_of_lists:
        for element in sublist:
            all_elements.append(element)
    unique_elements = set(all_elements)
    unique_list = list(unique_elements)
    return sorted(unique_list)

grader.check("q8")

"""<!-- END QUESTION -->

**The Extra Mile!**

Download the dataset Nigeria Food Prices (9.9M)

> https://data.humdata.org/dataset/wfp-food-prices-for-nigeria

<!-- BEGIN QUESTION -->

**Question 9: Create a new column date_new from the date column, converting it to a datetime format.**
"""

import pandas as pd

# Load the dataset
file_path = '/content/wfp_food_prices_nga.csv'  # Replace with the actual file path
df = pd.read_csv(file_path,skiprows=[1])
df = df.drop(index=2)
df = df.reset_index(drop=True)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

def create_date_new(df):
    """
    Creates a new column `date_new` from the `date` column, converting it to a datetime format.

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        pd.DataFrame: The dataframe with the new `date_new` column.
    """
    df['date_new'] = pd.to_datetime(df["date"])

    return df

grader.check("q9")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 10:Split the dataframe into two separate dataframes based on the category column: one for cereals and tubers and another for pulses and nuts**
"""

def split_dataframes(df):
    """
    Splits the dataframe into two separate dataframes based on the `category` column.

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        tuple: A tuple of two dataframes: (cereals_df, pulses_df).
    """
    cereals_df = df[df.category == "cereals and tubers"]
    pulses_df = df[df.category == "pulses and nuts"]

    return (cereals_df, pulses_df)

grader.check("q10")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 11:Calculate the mean, median, and mode of the price and usdprice columns for each category**
"""

def calculate_price_stats(df):
    """
    Calculates the mean, median, and mode of the `price` and `usdprice` columns for each `category`.

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        tuple: A tuple of two dataframes: (price_stats, usdprice_stats).

    """

    price_stats = pd.DataFrame(data = {"mean" : df["price"].mean(), "median":df["price"].median(), "mode":df["price"].mode()})
    usdprice_stats = pd.DataFrame(data = {"mean" : df["usdprice"].mean(), "median":df["usdprice"].median(), "mode":df["usdprice"].mode()})
    return (price_stats, usdprice_stats)

grader.check("q11")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 12:Merge the two dataframes (from Question 11) back into one dataframe and save it as `merged_data.csv`.**
"""

def merge_dataframes(cereals_df, pulses_df):
    """
    Merges the two dataframes back into one dataframe and saves it as `merged_data.csv`.

    Args:
        cereals_df (pd.DataFrame): The cereals and tubers dataframe.
        pulses_df (pd.DataFrame): The pulses and nuts dataframe.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    merged_df = pd.concat([cereals_df, pulses_df])
    return merged_df.reset_index(drop=True)

grader.check("q12")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 13:Open the `merged_data.csv` file and select only the `date_new`, `market`, `commodity`, `price`, and `usdprice` columns**
"""

def select_columns():
    """
    Opens the `merged_data.csv` file and selects only the `date_new`, `market`, `commodity`, `price`, and `usdprice` columns.

    Returns:
        pd.DataFrame: The dataframe with selected columns.
    """
    data = pd.read_csv('merged_data.csv', usecols=["date_new", "market", "commodity", "price", "usdprice"])

    return data

grader.check("q13")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 14:Group the data by `admin1` (state) and calculate the average `price` and `usdprice` for each state**
"""

def calculate_state_avg_prices(df):
    """
    Groups the data by `admin1` (state) and calculates the average `price` and `usdprice` for each state.

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        pd.DataFrame: The dataframe with average prices by state.
    """
    grouped_by_state = df.groupby("admin1")[["price", "usdprice"]].mean()

    return grouped_by_state

grader.check("q14")

"""<!-- END QUESTION -->

<!-- BEGIN QUESTION -->

**Question 15:Identify the top 5 markets with the highest average `usdprice` for `Rice (imported)`.**
"""

def identify_top_markets(df):
    """
    Identifies the top 5 markets with the highest average `usdprice` for `Rice (imported)`.

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        pd.Series: A series with the top 5 markets and their average `usdprice`.
    """
    rice = df[df.commodity == "Rice (imported)"]
    grouped_df = rice.groupby(by="market")["usdprice"].mean().sort_values(ascending=False)
    top_5_markets = grouped_df.head(5)
    return top_5_markets

grader.check("q15")

"""<!-- END QUESTION -->

---

To double-check your work, the cell below will rerun all of the autograder tests.
"""

grader.check_all()

"""## Submission

Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit. **Please save before exporting!**

Complete each function according to the provided specifications. Make sure all tests pass.
"""

# Save your notebook first, then run this cell to export your submission.
grader.export(run_tests=True)