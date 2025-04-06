import streamlit as st
import pandas as pd
import json
import io

library_file = "data/library.json"
def load_json_data():
    try:
        with open(library_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_to_json(data):
    with open(library_file, "w") as file:
        json.dump(data, file, indent=4)

def upload_csv():
    upload_file = st.file_uploader("Upload CSV", type=["csv"])
    if upload_file is not None:
        df = pd.read_csv(upload_file)
        st.write("CSV Data Preview:")
        st.dataframe(df)

        json_data = load_json_data()

        # convert dataframe to a list of dictionary to append a json file
        new_data = df.to_dict(orient="records")
        json_data.extend(new_data)

        save_to_json(json_data)

        st.success("Data imported successfully!")
        return df
    return None

def upload_excel():
    upload_file = st.file_uploader("Upload CSV", type=["xlsx"])
    if upload_file is not None:
        df = pd.read_excel(upload_file)
        st.write("Excel Data Preview:")
        st.dataframe(df)

        json_data = load_json_data()

        # convert dataframe to a list of dictionary to append a json file
        new_data = df.to_dict(orient="records")
        json_data.extend(new_data)

        save_to_json(json_data)

        st.success("Data imported successfully!")
        return df
    return None
        
def render_import_export():
    st.title("Import/Export Data")

    # option choose
    file_type = st.selectbox("Choose file type", ["CSV", "Excel"])

    if file_type == "CSV":
        df = upload_csv()

    if file_type == "Excel":
        df = upload_excel()
        
        # Export button
    export_datas = st.selectbox("Export Data", ["Excel", "CSV"])

    if export_datas == "Excel":
        if st.button("Export to Excel"):
            json_data = load_json_data()
            df = pd.DataFrame(json_data)
            
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="Library")
            buffer.seek(0)

            # Provide the file for download using Streamlit's download button
            st.download_button(
                label="Download Excel file",
                data=buffer,
                file_name="library.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            st.success("Data exported successfully!")

    elif export_datas == "CSV":
        if st.button("Export to CSV"):
            json_data = load_json_data()
            df = pd.DataFrame(json_data)
            
            # Saving to a CSV string buffer for download
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)

            # Provide the file for download using Streamlit's download button
            st.download_button(
                label="Download CSV file",
                data=csv_buffer.getvalue(),
                file_name="library.csv",
                mime="text/csv"
            )
            st.success("Data exported successfully!")