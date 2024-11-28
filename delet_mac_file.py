import os
import glob

# python F:\Download\delet_mac_file.py

def delete_hidden_files(root_dir):
    # root_dir과 하위 디렉토리에서 '._*' 패턴에 맞는 모든 파일 찾기
    for filepath in glob.glob(os.path.join(root_dir, '**', '._*'), recursive=True):
        try:
            os.remove(filepath)  # 파일 삭제
            print(f"Deleted: {filepath}")
        except Exception as e:
            print(f"Failed to delete {filepath}: {e}")

# 삭제할 파일들이 있는 디렉토리 경로 설정
user_input =  r"D:\\사진\2024"
delete_hidden_files(user_input)
