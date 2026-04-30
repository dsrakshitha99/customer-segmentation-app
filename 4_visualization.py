import streamlit as st
import matplotlib.pyplot as plt

st.title("Cluster Visualization")

if "clustered_data" in st.session_state:
    df = st.session_state["clustered_data"]

    columns = df.columns.tolist()
    selected_columns = st.multiselect("Select 2 Columns", columns)

    if len(selected_columns) == 2:
        fig, ax = plt.subplots()

        ax.scatter(
            df[selected_columns[0]],
            df[selected_columns[1]],
            c=df["Cluster"]
        )

        ax.set_xlabel(selected_columns[0])
        ax.set_ylabel(selected_columns[1])
        ax.set_title("Customer Segments")

        st.pyplot(fig)

    else:
        st.warning("Select exactly 2 columns")

else:
    st.error("Perform clustering first")