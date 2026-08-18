# 🧠 LangChain SQL Agent

An AI-powered SQL Agent built using **LangChain, Groq, and SQLite**.

This project was created as a hands-on learning project to understand how LLM-powered agents can interact with databases, generate SQL queries dynamically, execute tools, and convert database results into natural-language responses.

The user does not need to write SQL queries manually. The agent understands the user's question, generates the appropriate SQL query, executes it against the SQLite database, and returns the result in a human-friendly format.

---

## 🚀 Features

- 🤖 LLM integration using Groq
- 🦜 LangChain Agent implementation
- 🔧 Custom LangChain tools
- 🗄️ SQLite database integration
- 📝 Dynamic SQL query generation
- 🔍 Natural-language database queries
- 🔗 SQL JOIN operations
- 📊 Aggregations using `COUNT`, `SUM`, `AVG`, etc.
- 📈 Sorting and filtering
- 🛡️ Read-only SQL execution
- 💬 Interactive command-line interface
- 🔐 Environment-based API key configuration

---

## 🏗️ Architecture

The application follows this flow:

```text
                    User
                     │
                     ▼
              ┌─────────────┐
              │ LangChain   │
              │   Agent     │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │     LLM     │
              │    Groq     │
              └──────┬──────┘
                     │
              Generates SQL
                     │
                     ▼
              ┌─────────────┐
              │ execute_sql │
              │    Tool     │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │   SQLite    │
              │  Database   │
              └──────┬──────┘
                     │
                 SQL Result
                     │
                     ▼
              ┌─────────────┐
              │     LLM     │
              └──────┬──────┘
                     │
                     ▼
              Natural Language
                 Response
```

---

## 🗂️ Project Structure

```text
SQLAgent/
│
├── database/
│   ├── db.py
│   ├── create_db.py
│   ├── seed_data.py
│   ├── test_db.py
│   └── shop.db
│
├── agent.py
├── config.py
├── main.py
├── prompts.py
├── tools.py
├── test.py
│
├── .env
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

### Key files

| File | Purpose |
|---|---|
| `agent.py` | Initializes the LLM and creates the LangChain agent |
| `tools.py` | Contains the SQL execution tool used by the agent |
| `prompts.py` | Defines the system instructions for the agent |
| `main.py` | Provides the interactive command-line interface |
| `database/db.py` | Handles SQLite database connections |
| `database/create_db.py` | Creates the database tables |
| `database/seed_data.py` | Inserts sample data |
| `database/test_db.py` | Tests database connectivity and data |
| `config.py` | Application configuration |
| `test.py` | Project-level testing |

---

## 🗄️ Database

The project uses **SQLite** as the database.

The database contains three tables:

### Customers

Stores customer information.

```text
id
name
email
city
```

### Products

Stores product information.

```text
id
name
category
price
stock
```

### Orders

Stores customer orders.

```text
id
customer_id
product_id
quantity
status
order_date
```

### Relationships

```text
customers
    │
    │ customer_id
    ▼
 orders
    │
    │ product_id
    ▼
products
```

This allows the agent to answer questions requiring multiple-table JOINs.

---

# 🛠️ Technologies Used

- **Python**
- **LangChain**
- **Groq**
- **SQLite**
- **SQL**
- **LangChain Tools**
- **LLM-based Agents**

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/zunaidhossain/langchain-sql-agent.git
```

Navigate into the project:

```bash
cd langchain-sql-agent
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

Using `pip`:

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

The application requires a Groq API key.

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual API key.

> ⚠️ Never commit your `.env` file or API key to GitHub.

The `.env` file is included in `.gitignore`.

---

# 🗃️ Initialize the Database

Create the SQLite database and tables:

```bash
python database/create_db.py
```

Then populate the database with sample data:

```bash
python database/seed_data.py
```

You can verify the database:

```bash
python database/test_db.py
```

---

# ▶️ Running the Application

Start the SQL Agent:

```bash
python main.py
```

You should see:

```text
============================================================
      SQL Agent
============================================================
Type 'exit' to quit.

You:
```

You can now interact with the database using natural language.

---

# 💬 Example Queries

### Basic queries

```text
How many customers do we have?
```

```text
List all customers from Delhi.
```

```text
Which products are in the Electronics category?
```

### Aggregation

```text
What is the average product price?
```

```text
How many orders have been delivered?
```

```text
Which product was ordered the most?
```

### JOIN queries

```text
Show all orders with the customer name and product name.
```

```text
Which products has Alice Johnson ordered?
```

```text
Which customers have pending orders?
```

### More complex queries

```text
Which customer spent the most money?
```

```text
Which category generated the most revenue?
```

```text
Show the top 3 customers by total spending.
```

```text
Which city generated the highest revenue from delivered orders?
```

---

# 🔍 Example

### User

```text
Which accessories were ordered the most?
```

### Agent-generated SQL

```sql
SELECT
    p.name,
    SUM(o.quantity) AS total_ordered
FROM orders o
JOIN products p
    ON p.id = o.product_id
WHERE p.category = 'Accessories'
GROUP BY p.id, p.name
ORDER BY total_ordered DESC
LIMIT 1;
```

### Agent response

```text
The Accessories product ordered the most is the
USB-C Cable with a total of 26 units ordered.
```

The important part is that the user **does not need to know or write the SQL query**.

---

# 🧩 How the Agent Works

When a user asks a question, the following process occurs:

### 1. User asks a question

```text
Which accessories were ordered the most?
```

### 2. LLM interprets the question

The agent determines that it needs information from the database.

### 3. Agent calls the SQL tool

The agent generates SQL.

### 4. SQL tool executes the query

The tool sends the query to SQLite.

### 5. SQLite returns the result

```text
USB-C Cable
26
```

### 6. LLM generates the final response

The result is converted into a natural-language answer.

---

# 🔐 Security Considerations

The SQL tool is designed for **read-only database access**.

Only `SELECT` queries are allowed.

Queries such as:

```sql
DROP TABLE customers;
```

or:

```sql
DELETE FROM customers;
```

should not be executed by the tool.

The project also keeps API credentials outside the source code using environment variables.

> This is a learning project and should not be considered production-ready database security.

---

# 🎯 Learning Objectives

This project was built to gain practical experience with:

- Integrating an LLM into a Python application
- Calling an LLM through LangChain
- Creating LangChain agents
- Understanding agent/tool interactions
- Creating custom tools
- Understanding tool calling
- Working with different message types
- Generating structured outputs
- Generating SQL dynamically using an LLM
- Connecting an agent to a real database
- Executing SQL generated by an LLM
- Handling tool execution results
- Designing prompts for reliable SQL generation
- Debugging LLM tool-calling issues

---

# 🔮 Future Improvements

Potential improvements for future versions include:

- [ ] Automatic database schema discovery
- [ ] Add a `get_schema` tool
- [ ] Support multiple databases
- [ ] Query validation before execution
- [ ] SQL query optimization
- [ ] Better error handling and query retry logic
- [ ] Conversation memory
- [ ] Streaming agent responses
- [ ] Structured SQL generation
- [ ] Web-based user interface
- [ ] Authentication and authorization
- [ ] Query logging and monitoring
- [ ] Automated test suite
- [ ] Docker support

---

# 📚 Project Purpose

This project is primarily a **learning and experimentation project** for understanding how modern LLM applications and AI agents interact with external tools and data sources.

The goal is to progressively evolve the application from a simple LLM integration into a more capable **agentic AI system**.

---

## 👨‍💻 Author

**Zunaid Hossain**

GitHub: https://github.com/zunaidhossain
