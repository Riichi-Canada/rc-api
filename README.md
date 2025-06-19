# Riichi Canada API
API that will be used to access data from the Riichi Canada players and events database, to be used (mostly) by the
web ranking platform which will soon be available at riichi.ca.

---

# Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Riichi-Canada/rc-api.git
   cd rc-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **On Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **On Linux / macOS:**
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```
   
---
