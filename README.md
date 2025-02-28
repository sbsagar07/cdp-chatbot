# 🤖 CDP Support Agent Chatbot

A chatbot designed to answer "how-to" questions related to four Customer Data Platforms (**CDPs**): **Segment, mParticle, Lytics, and Zeotap**. It extracts relevant information from official documentation to provide step-by-step guidance.

## 🚀 Features  
✅ Answers "how-to" questions about CDPs  
✅ Retrieves information from official documentation  
✅ Handles variations in question phrasing  
✅ **Bonus**: Cross-CDP comparisons & advanced queries  

## 🛠 Tech Stack  
- **Backend**: Python  
- **Libraries**: `requests`, `beautifulsoup4`, `openai`  
- **Storage**: JSON for storing documentation data  

## 🔧 Installation & Setup  
1. **Clone the repository**  
   ```sh
   git clone https://github.com/YOUR-USERNAME/CDP-Support-Chatbot.git
   cd CDP-Support-Chatbot
   ```
2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Scraper** (fetches documentation)  
   ```sh
   python scraper.py
   ```
4. **Run the Chatbot**  
   ```sh
   python chatbot.py
   ```
   Example query:  
   ```
   How do I create an audience segment in Lytics?
   ```

## 📜 Project Structure  
```
📂 CDP-Support-Chatbot
├── scraper.py        # Scrapes documentation
├── chatbot.py        # Chatbot logic
├── cdp_docs.json     # Extracted documentation
├── requirements.txt  # Dependencies
├── README.md         # Documentation
└── .gitignore        # Ignored files
```

## 🤝 Contributing  
- Submit issues and pull requests.  
- Ensure clean, well-documented code.  

## 📜 License  
Licensed under the **MIT License**.  

📌 **Author**: [Your Name] | 📌 **GitHub**: [Your GitHub Profile Link]  

🚀 **Push to GitHub**  
```sh
git add README.md
git commit -m "Added README"
git push origin main
```
