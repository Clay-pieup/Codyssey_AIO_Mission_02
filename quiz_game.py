"""퀴즈 게임 전체를 관리하는 QuizGame 클래스"""

import json
import os

from quiz import Quiz, make_default_quizzes

MENU_MIN = 1      # 메뉴 번호 최솟값
MENU_MAX = 5      # 메뉴 번호 최댓값
LINE = "=" * 40   # 구분선
# 저장 파일 위치: 이 파일(quiz_game.py)이 있는 폴더(프로젝트 루트)의 state.json
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")


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


def read_text(prompt):
    """비어 있지 않은 글자를 받을 때까지 다시 묻고, 앞뒤 공백을 지운 글자를 돌려준다."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("입력이 비어 있습니다. 내용을 입력하세요.")
            continue
        return text


class QuizGame:
    """퀴즈 목록과 최고 점수를 가지고, 메뉴에서 고른 기능을 실행한다."""

    def __init__(self):
        self.quizzes = make_default_quizzes()  # 퀴즈 목록 (Quiz 인스턴스들의 list)
        self.best_score = None                 # 최고 점수 (아직 안 풀었으면 None)
        self.load_state()                      # 저장 파일이 있으면 그 내용으로 바꾼다

    def best_score_text(self):
        """최고 점수를 화면용 글자로 돌려준다. 아직 없으면 '없음'."""
        if self.best_score is None:
            return "없음"
        return f"{self.best_score}점"

    def load_state(self):
        """state.json을 읽어 퀴즈 목록과 최고 점수를 채운다. 없거나 깨졌으면 기본 퀴즈를 그대로 쓴다."""
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
            quizzes = []
            for item in data["quizzes"]:
                quizzes.append(Quiz(item["question"], item["choices"], item["answer"]))
            best_score = data["best_score"]
            if best_score is not None and not isinstance(best_score, int):
                raise ValueError("best_score는 정수 또는 null이어야 합니다.")
        except FileNotFoundError:
            print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            return
        except (ValueError, KeyError, TypeError):
            print("저장 파일(state.json)이 손상되어 기본 퀴즈로 복구합니다.")
            return
        except OSError:
            print("저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
            return

        self.quizzes = quizzes
        self.best_score = best_score
        print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score_text()})")

    def save_state(self):
        """퀴즈 목록과 최고 점수를 state.json에 UTF-8로 저장한다."""
        data = {
            "quizzes": [],
            "best_score": self.best_score,
        }
        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer,
            })
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
        except OSError:
            print("데이터 저장에 실패했습니다. (state.json을 쓸 수 없습니다)")
            return
        print("데이터를 저장했습니다.")

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

    def add_quiz(self):
        """문제·선택지 4개·정답 번호를 입력받아 새 퀴즈를 추가하고 바로 저장한다."""
        print("새로운 퀴즈를 추가합니다.")
        question = read_text("문제: ")
        choices = []
        for number in range(1, Quiz.CHOICE_COUNT + 1):
            choices.append(read_text(f"선택지 {number}: "))
        answer = read_number(f"정답 번호 (1-{Quiz.CHOICE_COUNT}): ", 1, Quiz.CHOICE_COUNT)

        self.quizzes.append(Quiz(question, choices, answer))
        print(f"퀴즈가 추가되었습니다! (총 {len(self.quizzes)}개)")
        self.save_state()

    def show_quizzes(self):
        """등록된 퀴즈의 문제 글만 번호와 함께 보여 준다 (정답은 보여 주지 않음)."""
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

    def run(self):
        """메뉴를 보여 주고 번호를 받아 기능을 실행한다. 5(종료)를 고를 때까지 반복한다.
        Ctrl+C나 입력 끊김(EOF)이 생겨도 저장하고 안전하게 끝낸다."""
        try:
            while True:
                self.show_menu()
                choice = read_number("선택: ", MENU_MIN, MENU_MAX)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quizzes()
                elif choice == 4:
                    print("점수 확인은 준비 중입니다.")
                else:
                    self.save_state()
                    print("프로그램을 종료합니다.")
                    break
        except (KeyboardInterrupt, EOFError):
            print()
            print("입력이 중단되었습니다. 저장 후 안전하게 종료합니다.")
            self.save_state()
