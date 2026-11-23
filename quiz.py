"""퀴즈 한 문제를 나타내는 Quiz 클래스"""


class Quiz:
    """문제 1개 = 문제 글 + 선택지 4개 + 정답 번호"""

    CHOICE_COUNT = 4  # 선택지 개수 (명세: 4개가 기본)

    def __init__(self, question, choices, answer):
        if len(choices) != Quiz.CHOICE_COUNT:
            raise ValueError("선택지는 4개여야 합니다.")
        if answer < 1 or answer > Quiz.CHOICE_COUNT:
            raise ValueError("정답 번호는 1~4 사이여야 합니다.")

        self.question = question  # 문제 글 (str)
        self.choices = choices    # 선택지 4개 (list)
        self.answer = answer      # 정답 번호 1~4 (int)

    def display(self, number):
        """문제 번호, 문제 글, 선택지 1~4를 화면에 보여 준다."""
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답이면 True, 아니면 False를 돌려준다."""
        return user_answer == self.answer


if __name__ == "__main__":
    # 이 파일만 따로 실행했을 때의 자체 점검 (python quiz.py)
    sample = Quiz(
        "Python에서 화면에 글자를 출력하는 함수는?",
        ["input", "print", "len", "type"],
        2,
    )
    sample.display(1)
    print()
    print("2번을 골랐을 때:", sample.is_correct(2))
    print("3번을 골랐을 때:", sample.is_correct(3))
