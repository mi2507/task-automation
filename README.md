# Task Automation with Python 🧠⚙️

Automating repetitive tasks using Python, Pandas and PyAutoGUI.

This project simulates the process of registering products through a desktop interface by reading data from a CSV file and automating keyboard/mouse interactions.

## 🗂 Project structure

automacao_tarefas

├── cadastro_produtos.py # Main automation script

├── pegar_posicao.py # Tool to get screen coordinates

├── produtos.csv # Sample CSV with 20 products

└── produtos2.csv # Full CSV with 200+ product


## 🛠 How it works

- Uses `pandas` to read product data from a CSV file.
  
- Uses `pyautogui` to fill out a product registration form automatically.
  
- Includes a helper script to get screen positions before automation.

## ▶️ To run

1. Make sure the product registration screen is open and ready.
2. Run the script:

```bash
python cadastro_produtos.py
```
Sit back and watch the automation!


