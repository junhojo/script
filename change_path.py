import os
import re
# 아이폰 폴더링
# 변경할 폴더 경로
folder_path = '/Users/jojunho/Desktop/0815_backup'

# 폴더 내의 모든 파일 및 폴더 이름 가져오기
print(f"폴더 경로: {folder_path}")
print("파일 및 폴더 이름을 분석하고 변경하는 중...\n")

# 정규 표현식 패턴 (날짜와 관련된 부분을 찾는 패턴)
date_pattern = re.compile(r"(.*?),?\s*(\d{4})\s*년\s*(\d{1,2})\s*월\s*(\d{1,2})\s*일")
# date_pattern = re.compile(r"(.*?), (\d{4})년 (\d{1,2})월 (\d{1,2})일")
# date_pattern = re.compile(r"(.*?), (\d{4})년 (\d{1,2})월 (\d{1,2})일")
# date_pattern = re.compile(r"(.*?),?\s*(\d{4})\s*년\s*(\d{1,2})\s*월\s*(\d{1,2})\s*일")

# 폴더 경로 내의 파일 및 폴더 이름 순회
for folder_name in os.listdir(folder_path):
    folder_full_path = os.path.join(folder_path, folder_name)

    # 폴더일 경우에만 처리
    if os.path.isdir(folder_full_path):
        print(f"폴더 이름: {folder_name}")

        # 폴더 이름에서 날짜 패턴 찾기
        match = date_pattern.search(folder_name)
        if match:
            x = match.group(1).strip() if match.group(1) else ""
            y = match.group(2)  # 년도
            m = match.group(3).zfill(2)  # 월 (두 자리 숫자로 변환)
            d = match.group(4).zfill(2)  # 일 (두 자리 숫자로 변환)

            # 새로운 폴더 이름 생성 (m + d + "_" + x)
            new_folder_name = f"{m}{d}_{x}" if x else f"{m}{d}_"

            # 년도별 하위 폴더 경로 생성 (폴더가 없으면 생성)
            year_folder_path = os.path.join(folder_path, y)
            if not os.path.exists(year_folder_path):
                os.makedirs(year_folder_path)
                print(f"'{year_folder_path}' 폴더를 생성했습니다.")

            # 새로 생성된 년도별 하위 폴더 경로 내에 새로운 폴더 이름으로 경로 설정
            new_folder_full_path = os.path.join(year_folder_path, new_folder_name)

            # 폴더 이름 변경 및 이동
            os.rename(folder_full_path, new_folder_full_path)
            print(f"'{folder_name}' → '{new_folder_full_path}'로 이동 및 이름이 변경되었습니다.\n")
        else:
            print(f"날짜 패턴을 찾을 수 없습니다: {folder_name}\n")
