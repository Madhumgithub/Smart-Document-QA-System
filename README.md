```
# Smart Document Q&A System

## Project Overview

The **Smart Document Q&A System** is a legal document query system designed to allow users to ask questions related to legal contracts and receive relevant answers. The system also integrates legal news summaries and a fact-checking component to ensure accurate legal responses. It is powered by machine learning and advanced NLP techniques.

---

## Features

- **Legal Document Querying**: Users can ask questions regarding legal contracts or documents.
- **Legal News Summarization**: Retrieves relevant legal news based on user input.
- **Fact-Checking**: Verifies the legal information against authoritative sources.
- **AI Integration**: Uses frameworks such as LangChain or Crew.ai to orchestrate AI capabilities.
- **Responsive Interface**: Designed for user-friendly interaction and seamless experience.

---

## Installation

To run the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Smart-Document-QA-System.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Smart-Document-QA-System
   ```

3. **Install the required Python packages:**

   Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **Mac/Linux:**

     ```bash
     source venv/bin/activate
     ```

   Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server:**

   ```bash
   python app.py
   ```

   The system will run on `http://127.0.0.1:5000/`.

---

## File Structure

```
Smart_Document_QA_System/
│
├── app.py                  # Main Flask application
├── templates/              # HTML templates for the chatbot UI
│   └── index.html
├── static/                 # Static files (CSS, JavaScript)
│   ├── style.css
│   └── scripts.js
├── legal_docs/             # Folder for storing legal documents (PDFs, TXT files)
│   ├── contract1.pdf
│   └── contract2.pdf
├── news_data/              # Folder for storing legal news data (JSON files)
│   ├── legal_news_1.json
│   └── legal_news_2.json
└── requirements.txt        # List of dependencies
```

---

## Usage

1. Open the web application at `http://127.0.0.1:5000/` in your browser.
2. Ask a legal question related to contracts or legal concepts.
3. The system will provide an answer, along with relevant legal news updates and fact-checking information.

### Example Questions

Here are some sample questions you can ask the bot:

- "What is a contract?"
- "What is the meaning of liability?"
- "What is intellectual property?"
- "What is negligence in law?"
- "Explain the term 'force majeure'."

---

## Contributing

If you would like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgements

- Flask for web development
- LangChain/Crew.ai for AI integration
- NLP Techniques for processing legal texts

---

## Contact

For any queries, please reach out to mp9075@srmist.edu.in.
``` 

