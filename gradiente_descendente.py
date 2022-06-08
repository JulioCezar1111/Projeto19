# -*- coding: utf-8 -*-
"""Gradiente_Descendente.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Et3yBubNYsHe8SaOOdafb5VtoiH2tSoM

## **RECEITA DE TREINAMENTO PARA O torch**
 1 - DESIGN DO MODELO (INPUT, OUTPUT, FORWARD PASS)

 2 - DEFINIÇAO DA FUNÇÃO DE CUSTO E OTIMIZADOR

 3 - LOOP DE TREINAMENTO:

  FORWARD PASS: CALCULAR A PREDIÇÃO E O CUSTO

  BACKWARPASS: CALCULAR OS GRADIENTES
  
  ATUALIZAR OS PESOS

# **Importar Bibliotecas**
"""

import torch 
import time
import torch.nn as nn
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from torch.autograd import variable

"""# **Preparação da DATA**"""

x_numpy, y_numpy = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=1)

x = torch.from_numpy(x_numpy.astype(np.float32)) # Converte
y = torch.from_numpy(y_numpy.astype(np.float32))
y = y.view(y.shape[0], 1) # alterando a dimensão

print(x.shape)
print(y.shape)

plt.plot(x_numpy, y_numpy, 'ro')

"""# **DEFINIÇÃO DE MODELO**"""

input_size = 1 # dados de entrada
output_size = 1 # dados de saida
model = nn.Linear(input_size, output_size) # Criar o modelo

"""# **DEFINIÇÃO DA FUNÇAO DE CUSTO E OTIMIZADOR**"""

learning_rate = 0.01 # Normaliza o passo
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate) # Criar o otimizador
print(model.parameters())

"""# **LOOP DE TREINAMENTO**"""

num_epochs = 1000 # interação que ira fazer para achar os valores dos parametros
contador_custo = []
epochs_ = []
for epoch in range(num_epochs):
  #forward pass and loos
  y_hat = model(x) # cria o modelo (começo aleatorio)
  loss = criterion(y_hat, y) # fazer o calculo do custo
  contador_custo.append(loss.detach().numpy()) # lista para monitorar a queda e intensidade 
  epochs_.append(range(num_epochs))
  
  #backward pass (calcular gradientes)
  loss.backward() # Faz os calculos das derivadas parciais

  #update (atualizar os pesos)
  optimizer.step() # atualiza os pesos

  if (epoch <= 10): # condição para mostrar em 10 em 10
    print('Epoch: ', epoch) # quantas vezes ele fez os calculos
    print('Custo: {:.20f}'.format(loss.item())) # o custo atual
    print('Coeficientes: ')
    print('m: {:.20f}'.format(model.weight.data.detach().item()))
    print('m (gradiente): {:.20f}'.format(model.weight.grad.detach().item()))
    print('b: {:.20f}'.format(model.bias.data.detach().item()))
    print('b (gradiente): {:.20f}'.format(model.bias.grad.detach().item()))
    #for p in model.parameters():
    #  print('{:.2f}'.format(p.data.detach().item()))
    #  print('{:.2f}'.format(p.grad.detach().item()))

    #plotar grafico
    previsao_final = y_hat.detach().numpy()
    plt.plot(x_numpy, y_numpy, 'ro') 
    plt.plot(x_numpy, previsao_final, 'b')
    plt.show()
    time.sleep(1)

  if (epoch >= 990):
    print('Epoch: ', epoch) # quantas vezes ele fez os calculos
    print('Custo: {:.20f}'.format(loss.item())) # o custo atual
    print('Coeficientes: ')
    print('m: {:.20f}'.format(model.weight.data.detach().item()))
    print('m (gradiente): {:.20f}'.format(model.weight.grad.detach().item()))
    print('b: {:.20f}'.format(model.bias.data.detach().item()))
    print('b (gradiente): {:.20f}'.format(model.bias.grad.detach().item()))
    previsao_final = y_hat.detach().numpy()
    plt.plot(x_numpy, y_numpy, 'ro') 
    plt.plot(x_numpy, previsao_final, 'b')
    plt.show()
    time.sleep(1)

  #limpar o otimizador
  optimizer.zero_grad()

"""# **PLOTANDO O GRÁFICO DA FUNÇÃO DE CUSTO**"""

print("GRÁFICO DA FUNÇÃO DE CUSTO")
plt.plot(contador_custo, 'r')
plt.show()