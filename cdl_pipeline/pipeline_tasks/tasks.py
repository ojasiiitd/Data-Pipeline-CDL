from cdl_pipeline import logger

# sample
# {'ID': 0 , 'Name': 60 , 'Age': 20 , 'Gender': 20 , 'Email': 60 , 'Join_Date': 20 , 'Last_Login': 20}
def missingValues(df , thresh_dict):
    logger.info("Accessed missingValues task inside pre-processing framework.")

    results = {}
    
    for col, thresh in thresh_dict.items():
        if col not in df.columns:
            logger.error(f"Column '{col}' not found!")
            raise ValueError(f"Column '{col}' not found!")
        
        total_values = len(df)
        missing_values = df[col].isnull().sum()
        missing_percentage = (missing_values / total_values) * 100
        
        results[col] = "False" if missing_percentage > thresh else "True" 

    return results

# sample
# ["ID", "Name", "Age", "Gender", "Email", "Join_Date", "Last_Login"]
def duplicateValues(df , columns):
    logger.info("Accessed duplicateValues task inside pre-processing framework.")
    
    results = {}
    
    row_duplicates = df[df.duplicated()].shape[0]
    results['row_duplicates'] = int(row_duplicates)
    
    column_duplicates = {}
    for col in columns:
        if col not in df.columns:
            logger.error(f"Column '{col}' not found!")
            raise ValueError(f"Column '{col}' not found!")
        
        duplicate_count = df[col].duplicated().sum()
        column_duplicates[col] = int(duplicate_count)
    
    results['column_duplicates'] = column_duplicates

    return results
