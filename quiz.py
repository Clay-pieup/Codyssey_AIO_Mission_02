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


def make_default_quizzes():
    """기본 퀴즈 6개를 Quiz 인스턴스로 만들어 리스트로 돌려준다."""
    return [
        Quiz("True와 False 두 값만 가지는 자료형은?",
             ["int", "str", "bool", "list"], 3),
        Quiz("여러 값을 순서대로 담고, 0번부터 번호로 꺼내 쓰는 자료형은?",
             ["dict", "int", "str", "list"], 4),
        Quiz("조건이 참인 동안 계속 반복할 때 쓰는 문법은?",
             ["for", "if", "while", "def"], 3),
        Quiz("클래스로 객체를 만들 때 자동으로 실행되는 메서드는?",
             ["__main__", "__init__", "self", "print"], 2),
        Quiz("내 컴퓨터의 커밋을 GitHub 원격 저장소로 올리는 Git 명령은?",
             ["git pull", "git clone", "git push", "git init"], 3),
        Quiz("새 브랜치를 만들면서 그 브랜치로 바로 옮겨 가는 명령은?",
             ["git checkout -b 이름", "git merge 이름", "git add 이름", "git status"], 1),
    ]


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

    quizzes = make_default_quizzes()
    print()
    print(f"기본 퀴즈 {len(quizzes)}개")
    for number, quiz in enumerate(quizzes, start=1):
        print(f"[{number}] {quiz.question}")
