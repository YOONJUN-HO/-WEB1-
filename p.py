import shutil

def copy_files(filename, num_copies):
    # 파일명에서 확장자 추출
    base_filename, extension = filename.split('.')
    
    # 파일을 num_copies 만큼 복사하고 이름을 변경하여 저장
    for i in range(3, num_copies + 1):
        new_filename = f"{i}.{extension}"
        shutil.copy(filename, new_filename)
        print(f"{filename}을(를) {new_filename}로 복사했습니다.")

# 테스트를 위한 파일명과 복사할 횟수 지정
filename = "2.html"  # 복사할 파일명
num_copies = 15            # 복사할 횟수

# 파일 복사 함수 호출
copy_files(filename, num_copies)
