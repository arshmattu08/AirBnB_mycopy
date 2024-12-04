def clean_property_type(df):
    
    def categorize_property_type(property_type):
        
        property_type = str(property_type).lower()  # Ensure it's a string and lowercase
        if property_type.startswith('entire'):
            return 'Entire Space'
        elif 'private' in property_type:
            return 'Private Small Space'
        elif 'shared' in property_type:
            return 'Shared Space'
        else:
            return 'Other'

    # Apply the nested function to the 'property_type' column of the DataFrame
    df['property_category'] = df['property_type'].apply(categorize_property_type)
    
    return df
