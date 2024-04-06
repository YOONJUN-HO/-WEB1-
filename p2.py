import os
j=2

def replace_string_in_files(start_num, end_num, original_str):
    for i in range(start_num, end_num + 1):
        filename = f"{i}.html"
        with open(filename, 'r', encoding='utf-8') as file:
            file_contents = file.read()
        
        # 파일명에서 확장자를 제외한 부분을 추출
        file_basename = os.path.splitext(filename)[0]
        
        # 문자열 치환
        new_contents = file_contents.replace(original_str, f'<img src="{file_basename}.png" width="50%">')
        print("original_str : {}", original_str)
        # 변경된 내용을 파일에 쓰기
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(new_contents)
        global j
        j+=1
        print(j)
        original_str = f'<img src="{j}.jpg" width="50%">'
        print(f"{filename} 파일에서 문자열을 치환했습니다.")


# 치환할 문자열 정의
original_str = f'<img src="{j}.jpg" width="50%">'

# 시작 번호와 끝 번호 지정
start_num = 2
end_num = 19
# 파일 내 문자열 치환 함수 호출
replace_string_in_files(start_num, end_num, original_str)
