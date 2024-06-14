# Prova 2 - M10

Nesse repositório estará a prova 2 de progmamação, do módulo 10.

## Instalação

```bash
# Clone o repositório
git clone https://github.com/cmtabr/p2-m10.git
cd p2-m10

# Crie um ambiente virtual e instale as dependências
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Execução
```bash
# Execute o programa
uvicorn app:app --host 0.0.0.0 --port 5000
```

## Execução via Docker
```bash
cd p2-m10
docker compose up --build 
```
