import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="🧹 Sweep Your Data – Fast, Easy, Efficient!", layout="wide")
st.title("🧹 Sweep Your Data – Fast, Easy, Efficient!")
st.write("🚀 Welcome to Data Sweeper! Upload your CSV or Excel files and clean or convert them effortlessly.")

uploaded_files = st.file_uploader("Upload files (CSV or Excel)", type=["csv", "xlsx"], accept_multiple_files=True)


# Check if openpyxl is available
try:
    import openpyxl
    excel_engine = 'openpyxl'
except ImportError:
    st.warning("⚠️ 'openpyxl' is missing. Excel files won't be processed. Install it using: `pip install openpyxl`")
    excel_engine = None

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        try:
            # Read CSV or Excel files
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                if excel_engine:
                    df = pd.read_excel(file, engine=excel_engine)
                else:
                    st.error(f"❌ Unable to process {file.name} - 'openpyxl' is required.")
                    continue
            else:
                st.error(f"❌ Invalid file type: {file_ext}")
                continue

            # Display details about the file
            st.write(f"**File Name:** {file.name}")
            st.write(f"**File Size:** {file.getbuffer().nbytes / 1024:.2f} KB")

            # Show preview of the dataframe
            st.write("🔍 **Preview the Head of the Dataframe**")
            st.dataframe(df.head())

            # Data cleaning options
            st.subheader("🗑️ Data cleaning options")
            if st.checkbox(f"Clean data for {file.name}"):
                col1, col2 = st.columns(2)

                with col1:
                    if st.button(f"Remove duplicates from {file.name}"):
                        df.drop_duplicates(inplace=True)
                        st.write("✅ Duplicates removed")

                with col2:
                    if st.button(f"Fill missing values for {file.name}"):
                        numeric_cols = df.select_dtypes(include=["number"]).columns
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.write("✅ Missing values filled")

            # Choose specific columns to keep or convert
            st.subheader("🎯 Select columns to convert")
            columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
            df = df[columns]

            # Create some visualizations
            if st.checkbox("📈 Data Visualizations", key=f"viz_{file.name}"):
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

            # Convert the file
            st.subheader("🔁 File conversion options")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

            if st.button(f"🔄 Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                elif conversion_type == "Excel":
                    if excel_engine:
                        df.to_excel(buffer, index=False, engine=excel_engine)
                        file_name = file.name.replace(file_ext, ".xlsx")
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    else:
                        st.error("❌ Cannot convert to Excel - 'openpyxl' is required.")
                        continue

                buffer.seek(0)


                # Download Button
                st.download_button(
                    label=f"⬇️ Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )

        except Exception as e:
            st.error(f"🚨 Error processing {file.name}: {e}")

st.success("🥳 All files processed successfully!")
