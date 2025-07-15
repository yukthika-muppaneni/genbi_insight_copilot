import streamlit as st
import pandas as pd
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from prophet import Prophet
import matplotlib.pyplot as plt

# ---- Page Setup ----
st.set_page_config(page_title="GenBI Insight Copilot", layout="wide")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---- Sidebar ----
with st.sidebar:
    st.title("🧭 Navigation")
    st.markdown("Use the main page to:")
    st.markdown("- Upload CSV")
    st.markdown("- Ask GPT questions")
    st.markdown("- Forecast revenue")

st.title("📊 GenBI Insight Copilot")
st.markdown("Ask questions about your business data using AI")

# ---- File Upload ----
uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📁 Preview of Uploaded Data")
    st.dataframe(df)

    # ---- KPIs ----
    total_revenue = df["Revenue"].sum()
    avg_revenue = df["Revenue"].mean()
    max_revenue = df["Revenue"].max()

    st.markdown("### 📌 Key Business Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
    col2.metric("📊 Average Revenue", f"${avg_revenue:,.2f}")
    col3.metric("🚀 Max Revenue", f"${max_revenue:,.2f}")

    # ---- GPT Agent Setup ----
    llm = ChatOpenAI(
        model="mistralai/mistral-7b-instruct",
        api_key="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",  # Replace with your actual OpenRouter API key
        base_url="https://openrouter.ai/api/v1"
    )

    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        allow_dangerous_code=True
    )

    # ---- GPT Chat Interface ----
        # ---- GPT Chat Interface ----
    st.subheader("💬 Ask a Question About Your Data")
    user_input = st.text_input("Type your question here:")

    if user_input:
        with st.spinner("Thinking..."):
            try:
                result = agent.invoke({"input": user_input})
                final_answer = result.get("output") or result.get("answer") or result
                st.success(f"🧠 Insight: {final_answer}")
                # Store Q&A in session state
                st.session_state.chat_history.append(
                 {"question": user_input, "answer": final_answer}
)

                    # ---- Download GPT Insight ----
                st.download_button(
                label="⬇️ Download GPT Insight",
                data=final_answer,
                file_name="insight.txt",
                mime="text/plain"
    )
            except Exception as e:
               st.error(f"❌ Error: {e}")
               if st.session_state.chat_history:
                  st.markdown("### 💬 Chat History")
                  for i, item in enumerate(reversed(st.session_state.chat_history), 1):
                      st.markdown(f"**Q{i}:** {item['question']}")
                      st.markdown(f"**A{i}:** {item['answer']}")


    # ---- Forecasting Section ----
    st.subheader("📈 Forecast Future Revenue")

    forecast_days = st.slider("Select number of days to forecast", min_value=7, max_value=60, value=14)

    if "Date" in df.columns and "Revenue" in df.columns:
        df_forecast = df[["Date", "Revenue"]].copy()
        df_forecast = df_forecast.rename(columns={"Date": "ds", "Revenue": "y"})
        df_forecast["ds"] = pd.to_datetime(df_forecast["ds"])

        model = Prophet()
        model.fit(df_forecast)

        future = model.make_future_dataframe(periods=forecast_days)
        forecast = model.predict(future)

        st.write("📅 Forecast Data:")
        st.dataframe(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(forecast_days))
            # ---- Export Forecast to CSV ----
        csv = forecast.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Forecast as CSV",
            data=csv,
            file_name='forecast_output.csv',
            mime='text/csv'
    )

        st.write("📉 Forecast Chart")
        fig = model.plot(forecast)
        st.pyplot(fig)
    else:
        st.warning("⚠️ 'Date' and 'Revenue' columns are required for forecasting.")

else:
    st.info("📤 Please upload a CSV file to begin.")
