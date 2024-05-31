# KBC Game

## Overview

This project is a simple implementation of the popular Indian television quiz show "Kaun Banega Crorepati" (KBC) using Python. The game features a 50-50 lifeline, which can be used once during the game. If an incorrect answer is given after using the lifeline, the game terminates.

## Features

- A series of multiple-choice questions.
- One-time use 50-50 lifeline that eliminates two incorrect options.
- Automatic game termination upon an incorrect answer after using the lifeline.

## Requirements

- Python 3.x

## How to Play

1. The game starts with a welcome message.
2. Each question is displayed one by one with four answer options.
3. The player can choose to use the 50-50 lifeline by typing `yes` when prompted.
   - If the lifeline is used, two incorrect options will be removed, and the player will be prompted to choose between the remaining two options.
   - The lifeline can only be used once during the game.
4. If the player chooses the correct answer, a congratulatory message is displayed, and the game proceeds to the next question.
5. If the player provides an incorrect answer after using the 50-50 lifeline, the game terminates with a message indicating the incorrect answer.

## Code Structure

The code consists of the following main parts:

- **Question List (`q_l`)**: A list of questions.
- **Options List (`o_l`)**: A list of lists containing answer options for each question.
- **Correct Answers List (`s_l`)**: A list of correct answers (indexed from 1 to 4).
- **50-50 Options List (`o_50_50`)**: A list of lists containing the two remaining options after using the 50-50 lifeline.
- **50-50 Correct Answers List (`s_50_50_l`)**: A list of correct answers (indexed from 1 to 2) after using the 50-50 lifeline.

## Example Questions and Options

1. **Question**: Tomato is a vegetable or fruit?
   - Options: Red color, Fruit, Vegetable, Flower
   - Correct Answer: Fruit

2. **Question**: What is the capital of India?
   - Options: Patna, Bhopal, Delhi, Itanagar
   - Correct Answer: Delhi

3. **Question**: NG me kon sa course karaya jata hai?
   - Options: Software Engineering, Counseling, Tourism, Agriculture
   - Correct Answer: Software Engineering

4. **Question**: When did COVID come to India?
   - Options: 2021, 2018, 2020, 2019
   - Correct Answer: 2020

## Usage

To run the game, simply execute the script using Python:

```sh
python3 kbc_game.py
