"""
split_file.py
100MBを超えるファイルを100MBに分割するツール

Usage:
    python split_file.py [filepath]
    python split_file.py                 (対話式入力)
    ファイルをドラッグ＆ドロップ対応
"""

import os
import sys
import time

CHUNK_SIZE = 100 * 1024 * 1024   # 100MB = 104,857,600 bytes
MIN_SIZE   = 100 * 1024 * 1024   # 100MB = 104,857,600 bytes


def format_size(size_bytes):
    """バイト数を読みやすい単位に変換"""
    if size_bytes >= 1024 ** 3:
        return f"{size_bytes / (1024 ** 3):.2f} GB"
    elif size_bytes >= 1024 ** 2:
        return f"{size_bytes / (1024 ** 2):.2f} MB"
    elif size_bytes >= 1024:
        return f"{size_bytes / 1024:.2f} KB"
    return f"{size_bytes} bytes"


def split_file(filepath):
    """ファイルを100MBごとに分割する"""

    # --- Validate ---
    if not os.path.isfile(filepath):
        print(f"[ERROR] ファイルが見つかりません: {filepath}")
        return 1

    file_size = os.path.getsize(filepath)
    base_name = os.path.splitext(os.path.basename(filepath))[0]
    extension = os.path.splitext(filepath)[1]
    directory = os.path.dirname(filepath) or "."
    total_parts = -(-file_size // CHUNK_SIZE)  # 切り上げ除算

    # --- Info ---
    print()
    print("========================================")
    print("  File Splitter (100MB -> 100MB chunks)")
    print("========================================")
    print(f"File : {os.path.basename(filepath)}")
    print(f"Dir  : {directory}")
    print(f"Size : {file_size:,} bytes ({format_size(file_size)})")
    print()

    # --- Size check ---
    if file_size <= MIN_SIZE:
        print("ファイルサイズが 100MB 以下のため、分割不要です。")
        return 0

    print(f"分割数 : {total_parts} パーツ (各 100MB)")
    print(f"出力先 : {directory}")
    print("========================================")
    print()

    # --- Split ---
    start_time = time.time()
    total_bytes_read = 0
    part_num = 0

    with open(filepath, "rb") as reader:
        while True:
            chunk = reader.read(CHUNK_SIZE)
            if not chunk:
                break

            part_num += 1
            part_filename = f"{base_name}_part{part_num:03d}{extension}"
            part_path = os.path.join(directory, part_filename)

            with open(part_path, "wb") as writer:
                writer.write(chunk)

            total_bytes_read += len(chunk)
            pct = (total_bytes_read / file_size) * 100
            size_mb = len(chunk) / (1024 * 1024)

            print(f"  [{pct:5.1f}%] Part {part_num:03d} - {part_filename} ({size_mb:.2f} MB)")

    elapsed = time.time() - start_time

    print()
    print("========================================")
    print(f"完了: {part_num} パーツ作成 (経過時間: {elapsed:.1f} 秒)")
    print("========================================")
    return 0


def main():
    # コマンドライン引数またはドラッグ＆ドロップ
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = input("分割するファイルのパスを入力してください: ").strip().strip('"')

    result = split_file(filepath)

    input("\n続行するには Enter を押してください...")
    sys.exit(result)


if __name__ == "__main__":
    main()
