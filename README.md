# 🎮 Unbeatable Tic-Tac-Toe AI

A classic command-line Tic-Tac-Toe game written in Python, featuring an unbeatable AI opponent. The AI is powered by the **Minimax algorithm** and optimized using **Alpha-Beta Pruning** to make highly efficient and perfect decisions.

## ✨ Features
- **Unbeatable AI:** The AI calculates every possible move. You can either draw or lose, but you can never win!
- **Optimized Performance:** Uses Alpha-Beta pruning to reduce the number of nodes evaluated by the Minimax algorithm, making the AI's decision-making instant.
- **Interactive Gameplay:** Play directly in your terminal or in cloud environments like Google Colab.
- **Zero External Dependencies:** Built entirely using Python's standard library (only the built-in `math` module is required).

## 🚀 How to Run in Google Colab (Quickest Way)
Since this game takes user input interactively, you can easily play it right in your browser using Google Colab without installing anything.

1. Go to [Google Colab](https://colab.research.google.com/) and click on **New Notebook**.
2. Copy the entire Python code of this game.
3. Paste the code into the first code cell of your new Colab notebook.
4. Click the **Play button** (▶️) on the left side of the cell or press `Shift + Enter` to run it.
5. The game will start in the output area just below the cell. Enter your row and column numbers (0, 1, or 2) when prompted to make your move!

## 💻 How to Run Locally
If you prefer to run it on your own machine, follow these steps:

1. Make sure you have [Python](https://www.python.org/downloads/) installed on your system.
2. Clone this repository or download the Python script (e.g., `tictactoe.py`).
3. Open your terminal or command prompt and navigate to the folder where the file is saved.
4. Run the following command:
   ```bash
   python tictactoe.py

# 🗺️ Graph Traversal: BFS & DFS in Python

This project is a simple Python implementation of two foundational graph traversal algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. To make the concepts easy to visualize, the graph represents a small network of connected cities in Pakistan.

## ⚙️ How it Works

*   **The Graph:** The cities and their connections (edges) are defined using a Python dictionary (`graph`), where each key is a city and its value is a list of connected neighboring cities.
*   **BFS (Breadth-First Search):** This algorithm explores the graph level-by-level, visiting all immediate neighbors of a node before moving deeper. It is implemented using a Queue (`collections.deque`), which follows the First-In-First-Out (FIFO) principle.
*   **DFS (Depth-First Search):** This algorithm explores as far as possible along a single path until it hits a dead end, then backtracks to explore other branches. In this script, it is implemented elegantly using **Recursion**.

## 🚀 How to Run

1.  Make sure you have Python installed on your system.
2.  Save the code into a new Python file (e.g., `graph_search.py`).
3.  Open your terminal or command prompt, navigate to the folder where the file is saved, and run the following command:
    ```bash
    python graph_search.py
    ```
4.  The terminal will print the exact traversal sequences for both BFS and DFS starting from 'Karachi'.

## 💡 Output Example
When you run the script, you will see the traversal paths printed sequentially like this:

**BFS starting from Karachi:**
`Karachi -> Lahore -> Faisalabad -> Islamabad -> Multan -> Peshawar -> Quetta ->`

**DFS starting from Karachi:**
`Karachi -> Lahore -> Islamabad -> Peshawar -> Quetta -> Multan -> Faisalabad ->`
