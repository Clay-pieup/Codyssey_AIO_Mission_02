"""퀴즈 게임 전체를 관리하는 QuizGame 클래스"""

from quiz import Quiz, make_default_quizzes

MENU_MIN = 1      # 메뉴 번호 최솟값
MENU_MAX = 5      # 메뉴 번호 최댓값
LINE = "=" * 40   # 구분선


def read_number(prompt, min_value, max_value):
    """min_value~max_value 사이의 정수를 받을 때까지 다시 묻고, 그 정수를 돌려준다."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print(f"입력이 비어 있습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue
        try:
            number = int(text)
        except ValueError:
            print(f"잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue
        if number < min_value or number > max_value:
            print(f"잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue
        return number


class QuizGame:
    """퀴즈 목록과 최고 점수를 가지고, 메뉴에서 고른 기능을 실행한다."""

    def __init__(self):
        self.quizzes = make_default_quizzes()  # 퀴즈 목록 (Quiz 인스턴스들의 list)
        self.best_score = None                 # 최고 점수 (아직 안 풀었으면 None)

    def show_menu(self):
        """메뉴 화면을 출력한다."""
        print(LINE)
        print("  나만의 퀴즈 게임 (Python·Git 기초)")
        print(LINE)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print(LINE)

    def play_quiz(self):
        """저장된 퀴즈를 차례로 출제하고, 맞힌 개수와 점수를 보여 준다."""
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        correct_count = 0
        print(f"퀴즈를 시작합니다! (총 {total}문제)")

        for number, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            quiz.display(number)
            print()
            user_answer = read_number("정답 입력: ", 1, Quiz.CHOICE_COUNT)
            if quiz.is_correct(user_answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        score = round(correct_count / total * 100)
        print(LINE)
        print(f"결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
        print(LINE)

    def run(self):
        """메뉴를 보여 주고 번호를 받아 기능을 실행한다. 5(종료)를 고를 때까지 반복한다."""
        while True:
            self.show_menu()
            choice = read_number("선택: ", MENU_MIN, MENU_MAX)
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                print("퀴즈 추가는 준비 중입니다.")
            elif choice == 3:
                print("퀴즈 목록은 준비 중입니다.")
            elif choice == 4:
                print("점수 확인은 준비 중입니다.")
            else:
                print("프로그램을 종료합니다.")
                break
