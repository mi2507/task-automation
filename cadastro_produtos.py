import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# Acessar o link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# Login (use suas coordenadas exatas aqui)
pyautogui.click(x=524, y=362)  # campo email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")  # coloque sua senha real
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)

# Carregar base
tabela = pd.read_csv("produtos.csv")

# Loop de cadastro
for linha in tabela.index:
    try:
        print(f"Cadastrando produto {linha + 1} de {len(tabela)}")

        # Volta o formulário para o topo da página
        pyautogui.scroll(5000)  # pode ajustar esse valor se quiser
        time.sleep(1)

        pyautogui.click(x=653, y=294)  # campo código (só funciona se estiver visível)
        pyautogui.write(str(tabela.loc[linha, "codigo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab")

        obs = tabela.loc[linha, "obs"]
        if not pd.isna(obs):
            pyautogui.write(str(obs))

        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(2)

    except Exception as e:
        print(f"Erro na linha {linha}: {e}")
        continue
