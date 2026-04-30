import streamlit as st
from sklearn.cluster import KMeans

st.title("K-Means Clustering")

if "data" in st.session_state:
    df = st.session_state["data"]

    columns = df.columns.tolist()
    selected_columns = st.multiselect("Select Features", columns)

    if len(selected_columns) >= 2:
        X = df[selected_columns]

        k = st.slider("Number of Clusters (K)", 2, 10, 3)

        model = KMeans(n_clusters=k, random_state=42)
        df["Cluster"] = model.fit_predict(X)

        st.session_state["clustered_data"] = df

        st.success("Clustering Completed!")
        st.write(df.head())

    else:
        st.warning("Select at least 2 columns")

else:
    st.error("Please upload dataset first")