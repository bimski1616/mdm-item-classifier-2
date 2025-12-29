import streamlit as st
import pandas as pd

from classifier import classify_item

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="MDM Item Description Classifier",
    layout="wide"
)

st.title("MDM Item Description Classifier")
st.write("Upload CSV dengan kolom **item_description** untuk klasifikasi otomatis.")

# =========================
# FILE UPLOADER
# =========================
uploaded_file = st.file_uploader(
    "Upload file CSV",
    type=["csv"]
)

# =========================
# MAIN PROCESS
# =========================
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if "item_description" not in df.columns:
        st.error("CSV harus memiliki kolom 'item_description'")
    else:
        st.info("Memproses klasifikasi...")

        result = df["item_description"].apply(classify_item)
        df_result = pd.concat([df, result.apply(pd.Series)], axis=1)

        st.success("Klasifikasi selesai")

        # =========================
        # PREVIEW
        # =========================
        st.subheader("Preview Result")
        st.dataframe(df_result.head(20), use_container_width=True)

        # =========================
        # DOWNLOAD
        # =========================
        csv_output = df_result.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Hasil Klasifikasi",
            data=csv_output,
            file_name="mdm_classified_output.csv",
            mime="text/csv"
        )
