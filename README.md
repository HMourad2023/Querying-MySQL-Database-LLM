### Interact with MySQL Database Using Open-Source LLMs
**Description :**  

The interact_with_MySQL project allows users to interact with a MySQL database using natural language instead of writing complex SQL queries.  
The goal is to simplify data access and make interactions more intuitive for users who are not experienced with SQL.

This project uses Streamlit for the user interface, MySQL-connector for connecting to MySQL, and Groq for API integration and natural language processing (LLMs).

**Features :**  

- Connect to a MySQL database.
- Execute SQL queries via natural language.
- Interactive user interface with Streamlit.
- Integration with the Groq API for natural language model management. 

**Data :**
- Airline Delays :
    - Airline Delays for December 2019 and 2020
    - kaggle link : [https://www.kaggle.com/datasets/eugeniyosetrov/airline-delays?select=airline_delay.csv]

**Technologies :**  

- Python 3.10
- Streamlit
- MySQL-connector-Python
- Groq API
- Conda (for virtual environment management)
- Git
- dotenv-python
- Pandas
- PyYaml
- fpdf  

**Prerequisites :**  

Before starting, ensure you have installed:

- Python 3.10 or higher
- Conda
- Git  

**Installation :**  

**Step 1: Clone the Repository :**  

Clone the repository to your machine:

```bash
git clone https://github.com/HMourad2023/Querying-MySQL-Database-LLM.git
```
Navigate to the project directory:

```bash
cd Querying-MySQL-Database-LLM
```  

**Step 2: Create a Virtual Environment :**  

Create a virtual environment with Conda:

```bash
conda create --name llm python=3.10 -y
```
Activate the virtual environment:

```bash
conda activate llm
```  

**Step 3: Install Dependencies :**  

Upgrade pip and install the required libraries:
```bash
python -m pip install --upgrade pip
```
```bash
pip install streamlit mysql-connector-python dotenv-python groq fpfd pyyaml pandas
```  

**Step 4: Create the Project Structure :**  

Create the template.py file:

```bash
echo. >template.py
```
Run the template.py file:

```bash
python template.py
```

