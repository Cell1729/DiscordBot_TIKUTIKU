# csvファイルをsqlite3に変換する関数
import pandas as pd
from sqlalchemy import create_engine
import os

def import_quotes_csv_to_db(csv_path, db_path):
    # CSVを読み込む
    df = pd.read_csv(csv_path, header=None, names=["id", "quote", "url"])
    # DBエンジン作成
    engine = create_engine(f"sqlite:///{db_path}")
    # quotesテーブルに追加
    df.to_sql("quotes", engine, if_exists="append", index=False)

if __name__ == "__main__":
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'quotes.csv'))
    db_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models'))
    db_path = os.path.join(db_dir, 'db.sqlite3')
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    if not os.path.exists(csv_path):
        print(f"{csv_path} が見つかりません。パスを確認してください。")
    else:
        import_quotes_csv_to_db(csv_path, db_path)
        print("Import completed.")