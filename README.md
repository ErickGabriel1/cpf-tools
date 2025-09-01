# CPF Tools

Uma ferramenta simples em **Python** para **gerar e validar números de CPF**.

## 🚀 Funcionalidades

- Gerar CPFs válidos aleatórios.
- Validar se um CPF informado é válido.
- Interface simples (CLI ou integração com bibliotecas).

## 📂 Estrutura do projeto

```
cpf-tools/
 ├─ LICENSE
 ├─ README.md
 └─ src/
    ├─ app.py
    └─ main.py
```

- `main.py` → contém as funções principais (geração e validação de CPF).  
- `app.py` → arquivo que executa o programa (ponto de entrada).  

## 🔧 Pré-requisitos

- Python 3.10 ou superior instalado na sua máquina.  
- (Opcional) Criar um ambiente virtual:  

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

## ▶️ Como usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/cpf-tools.git
cd cpf-tools/src
```

2. Execute o programa:

```bash
python app.py
```

3. Exemplos de uso:

- **Gerar CPF aleatório:**  
  O programa exibe um CPF válido gerado automaticamente.

- **Validar CPF existente:**  
  Informe um CPF e ele dirá se é válido ou inválido.

## 📜 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.