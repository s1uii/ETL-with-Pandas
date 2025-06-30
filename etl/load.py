import pandas as pd
from sqlalchemy import create_engine

def load_to_postgres(df, table_name, db_url):
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f" تم تحميل البيانات إلى الجدول: {table_name}")
    except Exception as e:
        print(f" خطأ في التحميل: {e}")

