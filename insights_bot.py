# insights_bot.py

import os
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOpenAI

# 2. Load your sales data
df = pd.read_csv("sales_data.csv")

# 3. Set up GPT-4 agent with LangChain
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)

# 4. Ask questions
while True:
    query = input("\nAsk a question about your data (type 'exit' to quit): ")
    if query.lower() == "exit":
        break
    response = agent.invoke(query)
    print("\n🧠 Insight:", response)
