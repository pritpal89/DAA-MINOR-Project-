import tkinter as tk
from tkinter import simpledialog, messagebox

def knapsack(weights, values, capacity, items):
    n = len(weights)
    dp = [0] * (capacity + 1)
    chosen_items = []
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            if dp[w - weights[i]] + values[i] > dp[w]:
                dp[w] = dp[w - weights[i]] + values[i]
    
    w = capacity
    for i in range(n - 1, -1, -1):
        if w >= weights[i] and dp[w] == dp[w - weights[i]] + values[i]:
            chosen_items.append(items[i])
            w -= weights[i]
    
    return f"Maximum Profit: {dp[capacity]}\nItems to include: {', '.join(chosen_items)}"

def get_input():
    n = simpledialog.askinteger("Input", "Number of items:", minvalue=1)
    items, weights, values = [], [], []
    
    for i in range(n):
        items.append(simpledialog.askstring("Input", f"Name of item {i+1}:"))
        weights.append(simpledialog.askinteger("Input", f"Weight of {items[-1]}:", minvalue=1))
        values.append(simpledialog.askinteger("Input", f"Value of {items[-1]}:", minvalue=1))
    
    capacity = simpledialog.askinteger("Input", "Knapsack capacity:", minvalue=1)
    result = knapsack(weights, values, capacity, items)
    messagebox.showinfo("Result", result)

root = tk.Tk()
root.withdraw()
get_input()
