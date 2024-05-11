# Chatbot com Google Gemini Pro e Tkinter

Este projeto cria um chatbot simples utilizando o modelo de linguagem **Gemini Pro do Google** e a biblioteca gráfica **Tkinter** para a interface.

## Funcionalidades

- Interface gráfica similar ao chat do Google AI Studio.
- Envio de mensagens com botão "Enviar" ou tecla "Enter".
- Exibição das mensagens do usuário e do chatbot em cores distintas.
- Fundo escuro para uma experiência visual mais agradável.

## Pré-requisitos

- Python 3.x
- Biblioteca google-generativeai
- Biblioteca tkinter
- Chave de API do Google Generative AI

## Instalação

Instale as bibliotecas:

```bash
pip install google-generativeai tkinter
```

Obtenha sua chave de API:

1. Acesse https://developers.google.com/generativeai e crie um projeto.
2. Ative a API do Google Generative AI.
3. Crie uma chave de API e copie-a.
4. Substitua SUA_API_KEY no código Python pela sua chave de API.

## Execução

Salve o código Python em um arquivo (ex: chatbot.py).

Execute o arquivo:

```bash
python chatbot.py
```

## Personalização

Você pode personalizar a aparência do chatbot alterando as cores, fontes e tamanhos no código. Explore os parâmetros `generation_config` e `safety_settings` para ajustar o comportamento do modelo Gemini Pro.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Observação

O uso da API do Google Generative AI pode estar sujeito a custos, dependendo do seu plano e uso.
```
Espero que isso ajude! Se você precisar de mais assistência, sinta-se à vontade para perguntar.
