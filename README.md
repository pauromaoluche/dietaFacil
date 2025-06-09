
DietaFácil
==========

DietaFácil é uma API intuitiva, desenvolvida com FastAPI, projetada para simplificar o cálculo de necessidades nutricionais diárias. Com ela, usuários podem obter estimativas precisas de macronutrientes (proteínas, gorduras, carboidratos), gasto energético basal (GEB) e gasto energético total (GET), facilitando o planejamento de dietas personalizadas para diversos objetivos, como emagrecimento, hipertrofia ou manutenção de peso, lembrando que aqui trago apenas medias, para valores exatos, consulte um nutricionista.

Funcionalidades
--------------

A API DietaFácil oferece os seguintes recursos principais:

- Cálculo de Macronutrientes: Determina as quantidades ideais de proteínas, gorduras e carboidratos com base em peso, altura, idade, sexo, nível de atividade e objetivo.

- Cálculo de Proteína: Estima a necessidade de proteína diária, considerando o IMC ideal (24,9) ou o percentual de gordura.

- Cálculo de Gasto Energético Basal (GEB): Calcula as calorias mínimas que o corpo necessita para funcionar em repouso.

- Cálculo de Gasto Energético Total (GET): Calcula o total de calorias queimadas diariamente, levando em conta o nível de atividade física.

- Cálculo de Gordura: Determina a quantidade ideal de gorduras diárias de acordo com o objetivo (emagrecer, manter, hipertrofia) e, opcionalmente, o percentual de gordura ou estado físico.

Instalação e Uso
----------------

Para configurar e executar o DietaFácil localmente, siga os passos abaixo:

### Pré-requisitos

- Python 3.9+
- pip (gerenciador de pacotes do Python)

### Configuração

Clone o repositório:

```
git clone https://github.com/seu-usuario/dietaFacil.git
cd dietaFacil
```

Crie e ative um ambiente virtual (recomendado):

```
python -m venv venv
# No Windows:
.
env\Scripts ctivate
# No macOS/Linux:
source venv/bin/activate
```

Instale as dependências:

```
pip install -r requirements.txt
```

(Crie um arquivo requirements.txt na raiz do seu projeto se ainda não tiver um, contendo fastapi e uvicorn.)

Execute a aplicação:

```
uvicorn main:app --reload
```

A API estará disponível em http://127.0.0.1:8000. Você pode acessar a documentação interativa da API (Swagger UI) em http://127.0.0.1:8000/docs.

Endpoints da API
----------------

A API DietaFácil expõe os seguintes endpoints:

### 1. Calcular Dieta Completa

Calcula os macronutrientes para uma dieta personalizada.

- **Endpoint:** `POST /api/calcularDieta`

- **Summary:** Calcula os macronutrientes para uma dieta personalizada.

- **Description:** Este endpoint calcula os macronutrientes necessários para uma dieta personalizada com base nas informações fornecidas pelo usuário.

- **Parâmetros de Entrada (JSON Body):**

  - peso (float): Peso do usuário (kg)
  - altura (float): Altura do usuário (cm)
  - idade (int): Idade do usuário
  - sexo (str): Sexo do usuário (masculino ou feminino)
  - frequencia_atividade (str): Nível de atividade física do usuário (sedentario, moderado, ativo)
  - objetivo (str): Objetivo do usuário (emagrecer, hipertrofia ou manter_peso)
  - nivel_calorico (float): Percentual de ajuste calórico para atingir o objetivo (ex: de 0 a 50%)

- **Resposta (JSON):** Retorna os valores dos macronutrientes recomendados (proteínas, gorduras e carboidratos) em gramas e seus respectivos percentuais em relação ao total de calorias ajustadas, além do gasto basal e total de calorias.

### 2. Calcular Proteínas

Calcula a quantidade de proteínas de acordo com o IMC Ideal (24,9).

- **Endpoint:** `POST /api/calcularProteinas`

- **Summary:** Calcula a quantidade de proteínas de acordo com o IMC Ideal, 24,9.

- **Description:** Este endpoint calcula as proteínas de acordo com o IMC ideal 24,9 (padrão).

- **Parâmetros de Entrada (JSON Body):**

  - peso (float): Peso do usuário (kg)
  - altura (float): Altura do usuário (cm)
  - percentual_gordura (float, opcional): Percentual de gordura.
  - estado_fisico (int, opcional): Se não informar percentual, escolha uma opção:
    - 0: muito_magro
    - 1: magro
    - 2: normal
    - 3: sobrepeso
    - 4: obeso

- **Resposta (JSON):** Retorna o valor em gramas de proteína.

### 3. Calcular Gasto Basal

Calcula o gasto energético basal (GEB).

- **Endpoint:** `POST /api/calculoBasal`

- **Summary:** Calcula o seu gasto basal.

- **Description:** Quantidade de calorias que seu corpo precisa por dia, GEB (Gasto Energético Basal).

- **Parâmetros de Entrada (JSON Body):**

  - peso (float): Peso do usuário (kg)
  - altura (float): Altura do usuário (cm)
  - idade (int): Idade do usuário
  - sexo (int):
    - 0: masculino
    - 1: feminino

- **Resposta (JSON):** Retorna as calorias que seu corpo precisa por dia.

### 4. Calcular Gasto Energético Total

Calcula o gasto de energia total de acordo com a atividade física.

- **Endpoint:** `POST /api/gastoEnergeticoTotal`

- **Summary:** Calcula o seu Gasto de Energia Total.

- **Description:** Quantidade Gasto de Energia Total de acordo com sua atividade física.

- **Parâmetros de Entrada (JSON Body):**

  - basal (float): Seu gasto basal (obtido do endpoint /calculoBasal).
  - frequencia_atividade (int):
    - 0: Sedentário (pouca ou nenhuma atividade)
    - 1: Atleta esporádico (1-3 dias por semana)
    - 2: Ativa (3-5 dias por semana)
    - 3: Muito ativa (5-7 dias por semana)
    - 4: Muito ativa e intensa (diária, incluindo exercícios pesados)

- **Resposta (JSON):** Retorna suas calorias de acordo com sua frequência física.

### 5. Calcular Gorduras

Calcula as gorduras necessárias de acordo com o objetivo.

- **Endpoint:** `POST /api/calcularGordura`

- **Summary:** Calcula as gorduras necessárias de acordo com o objetivo.

- **Description:** Este endpoint calcula os macronutrientes necessários para uma dieta personalizada com base nas informações fornecidas pelo usuário.

- **Parâmetros de Entrada (JSON Body):**

  - peso (float): Peso do usuário (kg)
  - altura (float): Altura do usuário (cm)
  - objetivo (int):
    - 0: emagrecer
    - 1: manter
    - 2: hipertrofia
  - percentual_gordura (float, opcional): Percentual de gordura.
  - estado_fisico (int, opcional): Se não informar percentual, escolha uma opção:
    - 0: muito_magro
    - 1: magro
    - 2: normal
    - 3: sobrepeso
    - 4: obeso

- **Resposta (JSON):** Retorna o valor em gramas de gordura por dia de acordo com o objetivo.

Contribuição
------------

Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
-------

Este projeto está licenciado sob a Licença MIT.

Contato
-------

Para dúvidas ou sugestões, entre em contato:

[Seu Nome/GitHub User] - Seu E-mail
