# 同一のヘッダーを持つCSVファイルを読み込み、統合する処理（修正版）
import os
import pandas as pd
# 現在の実行ディレクトリを取得
current_directory = os.getcwd()

# 現在の実行ディレクトリ内のCSVファイルを取得
csv_files_current_dir = [f for f in os.listdir(current_directory) if f.endswith('.csv')]

# リストが空でない場合のみ処理を実行
if csv_files_current_dir:
    # リストの最初のCSVファイルを読み込み、ヘッダーを取得
    reference_df_current_dir = pd.read_csv(os.path.join(current_directory, csv_files_current_dir[0]))
    headers_current_dir = reference_df_current_dir.columns.tolist()

    # 新規のCSVファイルの準備
    merged_v6_df = pd.DataFrame(columns=['Filename'] + headers_current_dir)

    # 各CSVファイルを読み込み、先頭のカラムにそのファイル名を追加して統合
    for csv_file in csv_files_current_dir:
        df = pd.read_csv(os.path.join(current_directory, csv_file))
        df.insert(0, "Filename", csv_file)
        merged_v6_df = pd.concat([merged_v6_df, df], ignore_index=True)
# 統合されたデータを現在のディレクトリにCSVファイルとして保存
    merged_v6_df.to_csv(os.path.join(current_directory, "merged_result.csv"), index=False)
    result = merged_v6_df
else:
    result = "現在のディレクトリにCSVファイルは存在しません。"

result
