import streamlit as st
import pandas as pd
import json
import io
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

library_file = "data/library.json"

def load_json_data():
    try:
        with open(library_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        st.error("Error reading library data. Starting with empty library.")
        return []

def save_to_json(data):
    try:
        with open(library_file, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        st.error(f"Error saving data: {str(e)}")

def upload_csv():
    upload_file = st.file_uploader("Upload CSV", type=["csv"])
    if upload_file is not None:
        try:
            df = pd.read_csv(upload_file)
            st.write("CSV Data Preview:")
            st.dataframe(df)

            json_data = load_json_data()
            new_data = df.to_dict(orient="records")
            json_data.extend(new_data)
            save_to_json(json_data)

            st.success("Data imported successfully!")
            return df
        except Exception as e:
            st.error(f"Error processing CSV: {str(e)}")
    return None

def upload_excel():
    upload_file = st.file_uploader("Upload Excel", type=["xlsx"])
    if upload_file is not None:
        try:
            df = pd.read_excel(upload_file)
            st.write("Excel Data Preview:")
            st.dataframe(df)

            json_data = load_json_data()
            new_data = df.to_dict(orient="records")
            json_data.extend(new_data)
            save_to_json(json_data)

            st.success("Data imported successfully!")
            return df
        except Exception as e:
            st.error(f"Error processing Excel: {str(e)}")
    return None
        
def render_import_export():
    st.title("Import/Export Data")

    file_type = st.selectbox("Choose file type", ["CSV", "Excel"])

    if file_type == "CSV":
        df = upload_csv()
    elif file_type == "Excel":
        df = upload_excel()
        
    # Export section
    st.markdown("---")
    st.subheader("Export Data")
    export_datas = st.selectbox("Export Format", ["Excel", "CSV"])

    if export_datas == "Excel":
        if st.button("Export to Excel"):
            try:
                json_data = load_json_data()
                if not json_data:
                    st.warning("No data available to export")
                    return
                
                df = pd.DataFrame(json_data)
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False, sheet_name="Library")
                buffer.seek(0)

                st.download_button(
                    label="Download Excel file",
                    data=buffer,
                    file_name="library.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                st.success("Data exported successfully!")
            except Exception as e:
                st.error(f"Error exporting to Excel: {str(e)}")

    elif export_datas == "CSV":
        if st.button("Export to CSV"):
            try:
                json_data = load_json_data()
                if not json_data:
                    st.warning("No data available to export")
                    return
                    
                df = pd.DataFrame(json_data)
                csv_buffer = io.StringIO()
                df.to_csv(csv_buffer, index=False)
                csv_buffer.seek(0)

                st.download_button(
                    label="Download CSV file",
                    data=csv_buffer.getvalue(),
                    file_name="library.csv",
                    mime="text/csv"
                )
                st.success("Data exported successfully!")
            except Exception as e:
                st.error(f"Error exporting to CSV: {str(e)}")