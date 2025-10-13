import csv
import random
import os

CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'quotes.csv'))

def get_random_csv_row(csv_path=CSV_PATH):
    """
    指定したCSVファイルからランダムに1行（リスト型）を抽出して返す関数。
    :param csv_path: CSVファイルのパス
    :return: ランダムな1行（リスト型） or None（ファイルが空/存在しない場合）
    """
    if not os.path.exists(csv_path):
        return "WTF"
    with open(csv_path, encoding='utf-8') as f:
        reader = list(csv.reader(f))
        if not reader:
            return "hmm"
        return random.choice(reader)
