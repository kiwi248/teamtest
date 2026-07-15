r"""01_simple_chat_project의 실행 시작점입니다.

실행 위치:
    C:\aidev\01_python-git-foundation

실행 명령:
    python .\02_python-advanced\04_project-structure\01_simple_chat_project\main.py

이 파일의 역할:
    1. 예제 질문을 준비합니다.
    2. services.py의 함수로 질문과 답변 데이터를 만듭니다.
    3. 만들어진 결과를 화면에 출력합니다.

중요:
    이 예제는 프로젝트 구조를 익히기 위한 첫 단계입니다.
    그래서 JSON 저장, 빈 질문 검증, 예외 처리는 아직 넣지 않습니다.
"""

from app.services import create_chat_message


def main() -> None:
    while True:
        question = input("궁금한 점을 입력하세요 (종료하려면 'q' 입력): ")
        if question.lower() == "q":
            print("프로그램을 종료합니다.")
            break
        print(f"질문: {question}")
        print("LLM이 처리 중입니다......")
        message = create_chat_message(question)
        print()
        print("\n질문:")
        print(message.question)
        print("\n답변:")
        print(message.answer)
        print("\n사용 모델:")
        print(message.model)
        print("-" * 40)  # 구분선 출력


main()
