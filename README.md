# 📊 GenBI Insight Copilot

An AI-powered business intelligence assistant that enables users to explore, analyze, and forecast CSV-based business data using natural language queries.

---

## 🚀 Project Highlights
- Built with **Streamlit**, **LangChain**, **OpenAI**, and **Prophet**
- Upload any CSV file and ask **natural language questions** about your data
- Integrated **forecasting** with Prophet to predict future revenue trends
- Designed a clean and intuitive interface for business users

---

## 🔧 Features
- **AI Chat Interface**: Ask questions like:
  - "What is the average revenue?"
  - "Show revenue trend by month."
  - "What is the highest revenue recorded and when?"
  - "Which product generated the most profit?"
  - "Compare revenue between Q1 and Q2."
  - "What is the total sales this year?"
  - "List top 5 performing regions."
  - "Show monthly growth rate."
  - "Predict future revenue for next 30 days."
  - "Which category saw the most decline in sales?""What is the average revenue?" or "Show revenue trend by month."
- **Forecasting**: Select days to forecast and visualize future performance
- **Memory**: Chat history preserved during session
- **Export**: Download charts/data 
- **Power BI Compatible**: Designed to integrate with existing BI tools

---

## 📂 Sample Results

| Screenshot | Description |
|-----------|-------------|
| ![Revenue Over Time](https://github.com/yukthika-muppaneni/genbi_insight_copilot/blob/main/Revenue%20Over%20Time.png.png) | Chart for the question "What is the average revenue?" |
| ![Revenue Forcast](https://github.com/yukthika-muppaneni/genbi_insight_copilot/blob/main/Revenue%20Forecast.png.png) | Revenue forecast for "What is the average revenue?" |
| ![Forecast Chart](https://github.com/yukthika-muppaneni/genbi_insight_copilot/blob/main/Forecast%20Chart.png.png) | Forecast chart for "What is the average revenue?" |
| ![Insight 1](https://github.com/yukthika-muppaneni/genbi_insight_copilot/blob/main/Chart%20Insight%201.png.png) | Chat interface answering "What is the average revenue?" |
| ![Insight 2](https://github.com/yukthika-muppaneni/genbi_insight_copilot/blob/main/Chart%20Insight%202.png.png) | KPI cards displaying total, average, and max revenue |
| ![Insight 3](https://github.com/yukthika-muppaneni/genbi_insight_copilot/blob/main/Chart%20Insight%203.png.png) | Prophet forecast results table for 14 days |
| ![Insight 4](https://github.com/yukthika-muppaneni/genbi_insight_copilot/blob/main/Chart%20Insight%204.png.png) | Insight and forecast export buttons with smooth layout |
| ![Insight 5](https://github.com/yukthika-muppaneni/genbi_insight_copilot/blob/main/Chart%20Insight%205.png.png) | Forecast chart visualizing revenue projection |

---

## 🛠️ Tech Stack
- `Python`
- `Streamlit`
- `LangChain`
- `OpenAI API`
- `Prophet`
- `Pandas`
- `Matplotlib`

---

## 📂 Project Structure
```
├── insights_bot.py          # Console-based agent
├── streamlit_app.py         # Streamlit web app
├── sales_data.csv           # Sample dataset
├── requirements.txt         # All dependencies
```

---

## 🧪 How to Run Locally
```bash
# Clone the repo
https://github.com/yukthika-muppaneni/genbi_insight_copilot.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

---

## 🙋‍♀️ Author
**Yukthika Muppaneni**  
📧 yukmuppaneni07@gmail.com  
🌐 [Portfolio](https://yukmuppaneni07.wixsite.com/my-site-4)  
🔗 [LinkedIn](https://www.linkedin.com/in/yukthika-muppaneni-397b21213)

---

## 🌟 Acknowledgements
Special thanks to open-source contributors in the LangChain, Streamlit, and Prophet communities for enabling innovation through AI-powered tools.

---

