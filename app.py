import streamlit as st
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.anthropic import Claude

st.title("Claude Sonnet + AI Web Search")
st.caption("This app allows you to search the web using Claude Sonnet 3.5")

anthropic_api_key = st.text_input("Anthropic's Calude API key", type="password")
if anthropic_api_key:
    assistant = Assistant(
        llm=Claude(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1024,
            temperature=0.9,
            api_key=anthropic_api_key),
            tools=[DuckDuckGo()], show_tool_calls=True
        )

        #getting the query
query = st.text_input("Enter the search query", type="default")
if query:
    response = assistant.run(query, stream=False)
    st.write(response)
