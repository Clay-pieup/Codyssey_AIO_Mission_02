# Mission 02 학습 기록

[README로 돌아가기](README.md)

## 목차
- [설계 결정](#설계-결정)
- [핵심 코드 해설](#핵심-코드-해설)
- [수행 로그](#수행-로그)
- [시행착오](#시행착오)
- [배운 점](#배운-점)
- [용어 사전](#용어-사전)

## 설계 결정

### 1. 브랜치는 main + 작업 브랜치 1개
- 맥락: 명세가 'main 말고 다른 브랜치에서 퀴즈 풀기 기능을 만든 뒤 main에 합치기'를 요구한다.
- 결정: 평소에는 `main`에서 작업하고, 퀴즈 풀기 단위(U4)만 작업 브랜치에서 만든 뒤 `main`에 병합한다.
- 결과: 얻은 것: 브랜치 생성·병합을 한 번 제대로 경험하고 기록이 `git log --graph`에 남는다. / 포기한 것: 모든 기능을 브랜치로 나누는 실무식 흐름 (혼자 하는 작은 과제라 생략).

### 2. 커밋과 push는 내가 터미널에서 직접 한다
- 맥락: 명세가 Git 명령 7종(init·add·commit·push·pull·checkout·clone)을 각각 한 번 이상 쓰라고 한다.
- 결정: AI는 파일 초안과 명령을 안내하고, 명령은 내가 PowerShell에서 직접 친다.
- 결과: 얻은 것: 명령마다 무엇이 바뀌는지 눈으로 확인하고 설명할 수 있다. / 포기한 것: 속도 (명령을 하나씩 직접 입력해야 한다).

### 3. 저장소에 올리지 않는 파일을 `.gitignore`로 막는다
- 맥락: 공개 저장소라 누구나 본다. 코디세이 교육자료(명세)와 작업 메모, 파이썬 임시 파일은 올리면 안 되거나 필요 없다.
- 결정: `.gitignore`에 작업 기준 파일(CLAUDE.md), 명세(`*.pdf`, `Mission_*.md`), `__pycache__/`, `.env`를 적는다.
- 결과: 얻은 것: `git add .`을 해도 실수로 올라가지 않는다. / 포기한 것: 없음. 다만 `docs/` 안에 둘 슬라이드 PDF는 예외로 열어 둔다.

### 4. 편집기는 Cursor를 쓴다
- 맥락: 명세의 개발 환경 스크린샷 예시는 VSCode다. Mission 01부터 Cursor를 쓰고 있다.
- 결정: Cursor를 그대로 쓰고 README에 'VSCode 기반 편집기'라고 적는다.
- 결과: 얻은 것: 익숙한 화면에서 터미널·파일 목록·Git 표시를 함께 본다. / 포기한 것: 명세 예시와 똑같은 화면 (기능은 같다).

### 5. 파일은 클래스별로 나눈다
- 맥락: 명세가 클래스 2개 이상으로 역할을 나누고, README에 파일 구조를 설명하라고 한다.
- 결정: `quiz.py`(문제 1개) · `quiz_game.py`(게임 전체, U3부터) · `main.py`(실행 시작점)로 나눈다.
- 결과: 얻은 것: 파일 이름만 봐도 역할이 보이고, 평가에서 구조를 설명하기 쉽다. / 포기한 것: 파일이 하나일 때보다 `import`(다른 파일 불러오기)를 하나 더 알아야 한다.

### 6. 퀴즈 주제는 Python·Git 기초
- 맥락: 내가 고른 주제로 퀴즈 5개 이상을 만들어야 하고, README에 선정 이유를 적어야 한다.
- 결정: 이번 미션에서 배우는 Python·Git 기초로 6문제를 만든다.
- 결과: 얻은 것: 게임을 만들면서 동시에 복습이 되고, 동료평가·금요일 시험 준비에도 쓸 수 있다. / 포기한 것: 일상 상식 주제보다 재미는 덜할 수 있다.

### 7. Quiz는 만들 때 바로 검사하고, 정답은 번호(int)로 저장한다
- 맥락: 선택지가 4개가 아니거나 정답 번호가 이상하면 게임 중에 엉뚱한 채점이 일어난다.
- 결정: `__init__`에서 선택지 개수와 정답 범위(1~4)를 검사해 틀리면 `ValueError`를 일으킨다. 정답은 명세 권장대로 1~4 번호로 저장한다.
- 결과: 얻은 것: 잘못된 문제는 처음부터 만들어지지 않는다. 나중에 `state.json`이 망가졌는지 알아내는 데에도 쓴다(U5). / 포기한 것: 선택지를 3개나 5개로 바꾸려면 코드를 고쳐야 한다.

### 8. 기본 퀴즈는 변수가 아니라 함수로 만든다
- 맥락: 퀴즈를 추가하거나 파일이 망가졌을 때 기본 퀴즈로 되돌려야 한다.
- 결정: `make_default_quizzes()`를 부를 때마다 새 목록을 만들어 돌려준다.
- 결과: 얻은 것: 언제 불러도 오염되지 않은 깨끗한 6문제를 받는다. / 포기한 것: 부를 때마다 새로 만드는 아주 작은 비용 (6문제라 무시할 수준).

### 9. 숫자 입력 검사는 함수 하나(`read_number`)로 모으고, 클래스 밖에 둔다
- 맥락: 메뉴 번호(1~5), 정답 입력(1~4), 퀴즈 추가 때 정답 번호(1~4) 모두 '정해진 범위의 숫자'를 받아야 한다. 명세는 공백·문자·범위 밖·빈 입력을 모두 처리하라고 한다.
- 결정: `read_number(prompt, min_value, max_value)` 하나를 범위만 바꿔 다시 쓴다. 게임 정보(`self`)를 쓰지 않으므로 QuizGame 밖의 함수로 둔다.
- 결과: 얻은 것: 같은 검사를 여러 번 쓰지 않고, 고칠 때 한 곳만 고친다. / 포기한 것: 문자 입력(문제 글 등)은 따로 검사해야 한다 (U6).

### 10. 최고 점수는 `None`으로 시작한다
- 맥락: 0점과 '아직 한 번도 안 풀었음'은 다르다. 명세는 '아직 퀴즈를 풀지 않은 경우'를 처리하라고 한다.
- 결정: `self.best_score = None`으로 시작한다.
- 결과: 얻은 것: U7에서 `None`이면 '아직 풀지 않았습니다'를 보여 줄 수 있다. / 포기한 것: 점수를 비교할 때 `None`인지 먼저 확인해야 한다.

### 11. 메뉴 흐름을 먼저 완성하고, 기능은 '준비 중'으로 둔다
- 맥락: 명세는 '메뉴 기능 완성 후 커밋'을 요구하고, 기능마다 따로 커밋해야 한다.
- 결정: 1~4는 '준비 중입니다'만 출력하고, U4~U7에서 하나씩 채운다.
- 결과: 얻은 것: 메뉴·입력 검사를 먼저 시험하고 커밋할 수 있다. / 포기한 것: 이 단계에서는 게임을 실제로 할 수 없다.

### 12. 작업 브랜치는 `feature/play-quiz`, 병합은 `--no-ff`
- 맥락: 명세가 main 외 브랜치에서 퀴즈 풀기를 만들고 main에 병합하라고 하며, `git log --oneline --graph` 스크린샷을 증거로 낸다.
- 결정: 실무에서 많이 쓰는 `feature/기능이름` 형식으로 브랜치를 만들고, `git merge --no-ff`로 병합 커밋을 남긴다.
- 결과: 얻은 것: 그래프에 갈라졌다 합쳐진 모양이 그대로 남는다. 그냥 `git merge`면 빨리 감기(fast-forward)로 한 줄이 되어 증거가 약해진다. / 포기한 것: 옵션 하나(`--no-ff`)를 더 설명할 수 있어야 한다.

### 13. 퀴즈 풀기는 만들어 둔 부품을 다시 쓴다
- 맥락: 문제 출력·채점·입력 검사는 U2·U3에서 이미 만들었다.
- 결정: `quiz.display()`, `quiz.is_correct()`, `read_number(…, 1, 4)`를 그대로 쓰고, 순서대로 묻고 맞힌 수를 세는 흐름만 새로 만든다. 퀴즈가 0개면 맨 앞에서 `return`한다.
- 결과: 얻은 것: 새 코드가 짧고, 입력 검사 규칙이 메뉴와 정답 입력에서 똑같다. 0개일 때 점수 계산의 0으로 나누기 오류를 막는다. / 포기한 것: 없음.

### 14. 점수는 `round(맞힌 수 / 전체 * 100)`
- 맥락: 처음에는 `correct_count * 100 // total`(몫 나눗셈, 소수점 버림)로 썼지만, 내가 `//`를 설명하기 어려웠다.
- 결정: '맞힌 비율에 100을 곱하고 반올림'으로 바꿨다. 평가에서 생활 감각으로 설명할 수 있는 방식을 골랐다.
- 결과: 얻은 것: 5/6 → 83점, 4/6 → 67점처럼 익숙한 반올림 점수. / 포기한 것: 정확히 .5인 경우 파이썬 `round`는 가까운 짝수로 간다(12.5 → 12). 6문제에서는 생기지 않는다.

## 핵심 코드 해설

<details><summary><code>quiz.py</code> — Quiz 클래스와 기본 퀴즈</summary>

| 코드 | 설명 |
|---|---|
| `class Quiz:` | Quiz라는 설계도(클래스)를 만든다. 이 틀로 찍어 낸 문제 하나하나가 인스턴스(객체)다 |
| `CHOICE_COUNT = 4` | 모든 문제가 같이 쓰는 값(클래스 변수). 숫자 4를 한 곳에서 관리한다 |
| `def __init__(self, question, choices, answer):` | 문제를 새로 만들 때 자동으로 한 번 실행되는 준비 메서드. 괄호 안은 재료(매개변수) |
| `if len(choices) != Quiz.CHOICE_COUNT: raise ValueError(…)` | 선택지가 4개가 아니면 오류를 일으켜 잘못된 문제를 막는다 |
| `if answer < 1 or answer > Quiz.CHOICE_COUNT: raise ValueError(…)` | 정답 번호가 1~4 밖이면 막는다 |
| `self.question = question` 외 2줄 | 받은 재료를 이 문제의 속성으로 저장한다. `self`는 '지금 만들어지는 바로 이 문제' |
| `def display(self, number):` | 문제 번호·문제 글·선택지를 보여 주는 메서드 |
| `for index, choice in enumerate(self.choices, start=1):` | 선택지를 하나씩 꺼내며 1부터 번호를 붙인다 |
| `print(f"{index}. {choice}")` | f-string으로 번호와 선택지를 끼워 넣어 출력한다 → `2. print` |
| `def is_correct(self, user_answer): return user_answer == self.answer` | 고른 번호와 이 문제의 정답을 비교한 결과(True/False)를 돌려준다 |
| `def make_default_quizzes(): return [Quiz(…), …]` | 기본 퀴즈 6개를 Quiz 인스턴스로 만들어 list로 돌려준다 |
| `if __name__ == "__main__":` | `python quiz.py`로 이 파일을 직접 실행할 때만 아래 자체 점검을 돌린다 |

자료형 연결: 문제 글 `str`, 선택지 `list`, 정답 `int`, `is_correct`의 결과 `bool`. `dict`는 U5에서 `state.json` 저장에 쓴다.
</details>

<details><summary><code>quiz_game.py</code> — 입력 검사 함수와 QuizGame 클래스</summary>

| 코드 | 설명 |
|---|---|
| `from quiz import make_default_quizzes` | `quiz.py`의 기본 퀴즈 함수를 불러온다 (import) |
| `MENU_MIN = 1`, `MENU_MAX = 5`, `LINE = "=" * 40` | 자주 쓰는 값에 이름을 붙인다. `"=" * 40`은 `=`를 40번 이어 붙인 구분선 |
| `def read_number(prompt, min_value, max_value):` | 묻는 글과 허용 범위를 받아, 올바른 정수를 돌려주는 함수 |
| `while True:` | 올바른 숫자가 들어올 때까지 반복한다. 몇 번 틀릴지 모르므로 `for`가 아니라 `while` |
| `text = input(prompt).strip()` | 키보드 입력을 글자로 받고 앞뒤 공백을 지운다 (`" 1 "` → `"1"`) |
| `if text == "": … continue` | 빈 입력이면 안내하고 반복의 처음으로 돌아가 다시 묻는다 |
| `try: number = int(text)` / `except ValueError:` | 정수로 바꿔 보고, `abc`처럼 바꿀 수 없으면 멈추지 않고 안내 후 다시 묻는다 |
| `if number < min_value or number > max_value: … continue` | 범위 밖(9, 0)이면 안내 후 다시 묻는다 |
| `return number` | 세 검사를 모두 통과한 숫자만 돌려주고 함수를 끝낸다 |
| `self.quizzes = make_default_quizzes()` | 게임이 가진 퀴즈 목록 (Quiz 인스턴스들의 list) |
| `self.best_score = None` | 최고 점수. 아직 안 풀었으면 값 없음(None) |
| `def show_menu(self):` | 메뉴 화면을 출력하는 메서드 |
| `choice = read_number("선택: ", MENU_MIN, MENU_MAX)` | 1~5 중 올바른 번호를 `choice` 변수에 담는다 |
| `if choice == 1: … elif … else:` | 번호에 따라 다른 기능을 실행한다. 위에서부터 처음 맞는 하나만 실행 |
| `else: … break` | 남은 번호는 5(종료)뿐. `break`로 메뉴 반복을 빠져나가 프로그램이 끝난다 |
| `from quiz import Quiz, make_default_quizzes` | 정답 범위(1~4)를 `Quiz.CHOICE_COUNT`에서 가져오려고 Quiz도 불러온다 (U4) |
| `def play_quiz(self):` | 퀴즈 풀기 메서드 (U4) |
| `if len(self.quizzes) == 0: … return` | 퀴즈가 없으면 안내하고 바로 메뉴로 돌아간다 |
| `total = len(self.quizzes)` / `correct_count = 0` | 전체 문제 수와 맞힌 개수를 담을 변수 |
| `for number, quiz in enumerate(self.quizzes, start=1):` | 문제 수가 정해져 있으니 `for`로 하나씩 꺼내며 1부터 번호를 붙인다 |
| `quiz.display(number)` | 이 문제를 화면에 보여 준다 (self는 이 quiz) |
| `user_answer = read_number("정답 입력: ", 1, Quiz.CHOICE_COUNT)` | U3의 입력 검사를 범위 1~4로 다시 쓴다 |
| `if quiz.is_correct(user_answer): … correct_count += 1` | 맞으면 '정답입니다!'를 출력하고 맞힌 수를 1 늘린다 |
| `else: print(f"오답입니다. 정답은 {quiz.answer}번입니다.")` | 틀리면 정답 번호를 알려 준다 |
| `score = round(correct_count / total * 100)` | 맞힌 비율 × 100을 반올림해 100점 만점 점수로 만든다 |
| `if choice == 1: self.play_quiz()` | 메뉴 1번이 퀴즈 풀기를 부른다 |
</details>

<details><summary><code>main.py</code> — 실행 시작점</summary>

| 코드 | 설명 |
|---|---|
| `from quiz_game import QuizGame` | `quiz_game.py`의 QuizGame 클래스를 불러온다 |
| `game = QuizGame()` | 게임 하나를 만들어 `game` 변수에 담는다 (`__init__`이 자동 실행되어 기본 퀴즈를 준비) |
| `game.run()` | 메뉴 반복을 시작한다 |
| `if __name__ == "__main__": main()` | `python main.py`로 실행할 때만 게임을 시작한다 |
</details>

## 수행 로그

### U1 · 저장소 초기 설정
2026-11-23 · Windows PowerShell (Cursor 터미널)

```text
PS> python --version              → Python 3.14.7
PS> git --version                 → git version 2.54.0.windows.1
PS> git config --global user.name → Clay-pieup
PS> git config --global user.email → (GitHub noreply 주소, 공개 저장소라 생략)
PS> git init -b main              → Initialized empty Git repository in …/Codyssey_AIO_Mission_02/.git/
PS> git add .                     → 경고 3줄: LF will be replaced by CRLF (줄바꿈 방식 안내, 내용 변화 없음)
PS> git status
On branch main
No commits yet
Changes to be committed:
        new file:   .gitignore
        new file:   LEARNING.md
        new file:   README.md
  → CLAUDE.md와 명세 파일은 목록에 없음 (.gitignore가 막음)
PS> git commit -m "Docs: 저장소 뼈대 추가 - README·LEARNING·.gitignore로 Mission 02 시작 준비"
PS> git remote add origin https://github.com/Clay-pieup/Codyssey_AIO_Mission_02.git
PS> git push -u origin main
PS> git log --oneline             → 00265db Docs: 저장소 뼈대 추가 - …
```
- GitHub: Public 저장소에서 README가 보이는 것을 확인했다. GitHub 쪽 main 기록(`origin/main`)도 `00265db`이다.
- 개발 환경 스크린샷: [env.png](docs/screenshots/env.png) (Python·Git 버전, 사용자 이름, 원격 주소. 이메일은 처음부터 출력하지 않음)
- 명령 7종 진행: init · add · commit · push (4/7)

### U2 · Quiz 클래스·기본 퀴즈
2026-11-24 · Windows PowerShell (Cursor 터미널)

```text
PS> python quiz.py
[문제 1]
Python에서 화면에 글자를 출력하는 함수는?

1. input
2. print
3. len
4. type

2번을 골랐을 때: True
3번을 골랐을 때: False

기본 퀴즈 6개
[1] True와 False 두 값만 가지는 자료형은?
[2] 여러 값을 순서대로 담고, 0번부터 번호로 꺼내 쓰는 자료형은?
[3] 조건이 참인 동안 계속 반복할 때 쓰는 문법은?
[4] 클래스로 객체를 만들 때 자동으로 실행되는 메서드는?
[5] 내 컴퓨터의 커밋을 GitHub 원격 저장소로 올리는 Git 명령은?
[6] 새 브랜치를 만들면서 그 브랜치로 바로 옮겨 가는 명령은?
PS> git log --oneline
e5de3a4 Feat: 기본 퀴즈 데이터 추가 - Python·Git 기초 6문제를 Quiz 인스턴스로 생성
2905631 Feat: Quiz 클래스 작성 - 문제·선택지 4개·정답 번호 저장, 출력·정답 확인 메서드
eba0801 Docs: U1 기록 - 개발 환경 스크린샷·수행 로그·체크리스트 갱신
00265db Docs: 저장소 뼈대 추가 - README·LEARNING·.gitignore로 Mission 02 시작 준비
```
- 잘못된 문제 검사 (AI가 실행해 확인): 선택지 3개 → `ValueError: 선택지는 4개여야 합니다.` / 정답 0·5 → `ValueError: 정답 번호는 1~4 사이여야 합니다.`
- 기본 퀴즈 정답: 1 bool(3) · 2 list(4) · 3 while(3) · 4 `__init__`(2) · 5 git push(3) · 6 git checkout -b(1). 번호를 섞어 같은 번호가 계속 답이 되지 않게 했다.
- 기능 단위 커밋: Quiz 클래스와 기본 퀴즈를 커밋 2개로 나눴다 (`git add quiz.py`로 파일 하나만 담음).

### U3 · 메뉴·입력 검증
2026-11-24 · Windows PowerShell (Cursor 터미널) · `python main.py`

| 입력 | 결과 |
|---|---|
| ` 1 ` (앞뒤 공백) | 퀴즈 풀기는 준비 중입니다. → 메뉴 다시 출력 |
| `abc` | 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요. |
| `9` | 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요. |
| (그냥 Enter) | 입력이 비어 있습니다. 1-5 사이의 숫자를 입력하세요. |
| `0` | 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요. |
| `4` | 점수 확인은 준비 중입니다. |
| `5` | 프로그램을 종료합니다. → PowerShell로 돌아옴 |

```text
PS> git log --oneline
e4b5ab5 Feat: 메뉴와 입력 검증 구현 - QuizGame 뼈대, 1~5 메뉴, 공백·문자·범위·빈 입력 재입력
```
- 아직 Ctrl+C를 누르면 Traceback(오류 안내문)이 나오며 꺼진다 → U5에서 처리한다.

### U4 · 퀴즈 풀기·브랜치 병합
2026-11-24 · Windows PowerShell (Cursor 터미널)

```text
PS> git checkout -b feature/play-quiz     → Switched to a new branch 'feature/play-quiz'
PS> python main.py                        → 1 선택 후 6문제 풀기
퀴즈를 시작합니다! (총 6문제)
정답 입력: 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.   (5, abc 입력)
정답 입력: 오답입니다. 정답은 3번입니다.
결과: 6문제 중 5문제 정답! (83점)
PS> python -c "from quiz_game import QuizGame; g = QuizGame(); g.quizzes = []; g.play_quiz()"
등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.
PS> git commit -m "Feat: 퀴즈 풀기 기능 구현 - …"       → 61b7629 (feature/play-quiz)
PS> git push -u origin feature/play-quiz                  → GitHub에 브랜치도 올라감
PS> git checkout main
PS> git merge --no-ff feature/play-quiz -m "Merge: feature/play-quiz - 퀴즈 풀기 기능을 main에 병합"
Merge made by the 'ort' strategy.
PS> git push
PS> git log --oneline --graph --all
*   a820a38 (HEAD -> main, origin/main) Merge: feature/play-quiz - 퀴즈 풀기 기능을 main에 병합
|\
| * 61b7629 (origin/feature/play-quiz, feature/play-quiz) Feat: 퀴즈 풀기 기능 구현 - …
* | 514ec8b Docs: U3 기록 - …
|/
* e4b5ab5 Feat: 메뉴와 입력 검증 구현 - …
```
- 그래프에서 `feature/play-quiz`가 갈라졌다가 병합 커밋 `a820a38`에서 main과 합쳐진 것을 확인했다.
- 명령 7종 진행: init · add · commit · push · checkout (5/7)

## 시행착오

### 1. U3 문서 커밋을 빠뜨리고 브랜치를 만들었다
- 문제: `git checkout -b feature/play-quiz` 뒤 `git status`에 `modified: LEARNING.md / README.md`가 빨갛게 남았다.
- 원인: U3 문서를 커밋하지 않은 채 브랜치를 옮겼다. 커밋하지 않은 변경은 어느 브랜치에도 속하지 않아 따라온다.
- 해결: `git checkout main` → 문서만 커밋·push → `git checkout feature/play-quiz`로 돌아왔다. 덕분에 main과 작업 브랜치가 실제로 갈라져 병합 그래프가 더 분명해졌다.

### 2. AI가 PC에 보낸 파일이 한 번 반영되지 않았다
- 문제: 점수 계산 줄을 바꾼 `quiz_game.py`를 보냈는데 PC 파일은 예전 그대로였다.
- 원인: 파일을 만든 직후 바로 보내서 예전 내용이 전달됐다 (전송 시점 문제).
- 해결: PC 파일의 지문(md5)을 비교해 발견하고 다시 보냈다. 앞으로도 보낼 때마다 지문을 확인한다.

## 배운 점
- U2: `self`는 클래스(틀)가 아니라 메서드를 부른 '바로 그 문제'다. `q2.is_correct(2)`면 q2의 정답과 비교한다. 처음엔 틀렸다가 붕어빵 비유로 이해했다.
- U3: 반복 안의 세 단어를 구분했다. 처음에 `continue`와 `break`를 반대로 알았고, 다시 묻는 것을 `return`으로 착각했다가 한 줄씩 따라가며 고쳤다.

  | 상황 | 실행되는 것 | 뜻 |
  |---|---|---|
  | 틀린 입력 | `continue` | 반복의 처음으로 돌아가 다시 묻기 (회전목마 다음 바퀴) |
  | 올바른 입력 | `return number` | 함수를 끝내고 숫자를 돌려주기 |
  | 5 선택 | `break` | 메뉴 반복을 끝내기 (회전목마에서 내림) |
- U4: 브랜치는 원본 공책(main)을 복사한 연습장이다. 연습장에서 만들고 잘 되면 main에 합친다. 커밋하지 않은 변경은 브랜치를 옮겨도 따라온다.
- U4: 파이썬 `round(값)`은 엑셀 `ROUND(값, 0)`과 같다 (정수로 반올림). 처음에는 엑셀 `ROUND(값, 2)`처럼 생각해 66.67을 골랐다. `//`(소수점 버림)도 헷갈려서 점수 계산을 `round`로 바꿨다.
- U1: `add`는 '담기', `commit`은 '사진 찍기', `push`는 'GitHub로 올리기'다. 커밋 전에 `git status`로 무엇이 담겼는지 보면 비밀 파일이 올라가는 사고를 막을 수 있다.

### 과제 목표, 내 말로
- Git이 필요한 이유: 파일이 언제 어떻게 바뀌었는지 기록해 두고, 되돌리거나 비교하려고 쓴다.
- add / commit / push: add는 기록할 파일을 담기, commit은 담은 것을 기록 한 장으로 남기기, push는 그 기록을 GitHub로 올리기.
- `__init__`: 클래스로 객체를 만드는 순간 자동으로 불리는 준비 메서드.
- `self`: 메서드를 부른 바로 그 객체. `q1.display(1)`이면 q1.
- 속성 / 메서드: 속성은 객체가 기억하는 정보(question, answer), 메서드는 객체가 하는 행동(display, is_correct).
- `for` vs `while`: 횟수가 정해진 목록을 차례로 돌 때는 `for`(선택지 4개 출력), 몇 번 반복할지 모를 때는 `while`(올바른 입력이 들어올 때까지).
- `try/except`: 오류가 날 수 있는 일(`int("abc")`)을 try에서 해 보고, 오류가 나면 except에서 받아 프로그램이 멈추지 않게 한다.
- `if/elif/else`: 메뉴 번호에 따라 다른 기능으로 길을 나눈다. 위에서부터 처음 맞는 하나만 실행된다.
- 함수의 매개변수·반환값: `read_number("선택: ", 1, 5)`는 묻는 글과 범위를 재료로 받고, 검사를 통과한 숫자를 `return`으로 돌려준다.
- 브랜치 생성·병합: `git checkout -b 이름`으로 연습장(브랜치)을 만들어 옮겨 가고, 작업 후 `git checkout main`으로 돌아와 `git merge --no-ff 이름`으로 합친다.

## 용어 사전
- **Git**: 파일이 언제 어떻게 바뀌었는지 사진첩처럼 차곡차곡 기록해 주는 프로그램. 예전 상태로 되돌리거나 비교할 수 있다.
- **GitHub**: Git 기록을 인터넷에 올려 두고 다른 사람과 같이 보는 웹사이트.
- **저장소(repository)**: Git이 기록을 관리하는 폴더 하나. 내 컴퓨터에 있으면 로컬 저장소, GitHub에 있으면 원격 저장소.
- **`.gitignore`**: "이 파일은 기록하지 마"라고 Git에게 알려 주는 목록 파일.
- **스테이징(add)**: 사진을 찍기 전에 찍을 물건을 상 위에 올려 두는 단계. 실제 기록은 commit에서 남는다.
- **커밋(commit)**: 지금 파일 상태를 기록 한 장으로 남기는 것. 이름표(커밋 메시지)를 붙인다.
- **커밋 번호(해시)**: `00265db`처럼 기록마다 붙는 고유 번호. 겹치지 않는다.
- **push**: 내 컴퓨터의 기록을 GitHub로 올리는 것.
- **remote / origin**: remote는 인터넷 저장소 주소, origin은 그 주소의 기본 별명.
- **origin/main**: 내 컴퓨터가 기억하는 'GitHub 쪽 main의 마지막 기록'. 내 main과 번호가 같으면 push가 끝난 것이다.
- **LF / CRLF**: 줄바꿈을 나타내는 숨은 표시. 리눅스는 LF, 윈도우는 CRLF를 쓴다.
- **PowerShell**: 윈도우에서 글자로 명령을 입력하는 창(터미널).
- **modified / new file**: `git status`에서 modified는 '이미 기록된 파일이 바뀜', new file은 '처음 기록되는 파일'.
- **클래스 / 인스턴스(객체)**: 클래스는 붕어빵 틀(설계도), 인스턴스는 그 틀로 찍어 낸 붕어빵 하나하나(실제 문제).
- **`__init__`**: 인스턴스를 새로 만들 때 자동으로 한 번 실행되는 준비 메서드.
- **`self`**: 메서드를 부른 바로 그 인스턴스.
- **속성(attribute) / 메서드(method)**: 속성은 객체가 기억하는 정보, 메서드는 객체가 할 수 있는 행동.
- **함수(def)**: 자주 쓰는 일을 묶어 이름을 붙인 것. 부르면 일을 하고 결과를 돌려준다.
- **매개변수 / 반환값**: 함수에 넣어 주는 재료 / 함수가 `return`으로 돌려주는 결과.
- **`raise ValueError`**: "값이 잘못됐다"는 오류를 일부러 일으켜 잘못된 데이터를 막는 것.
- **f-string**: `f"…{변수}…"`처럼 글자 안에 변수 값을 끼워 넣는 방법.
- **`enumerate`**: 목록에서 항목을 꺼낼 때 순서 번호도 같이 붙여 주는 함수.
- **`__pycache__`**: 파이썬이 실행 속도를 높이려고 저절로 만드는 임시 폴더. 저장소에는 올리지 않는다.
- **Feat / Docs**: 커밋 메시지 머리말. Feat는 새 기능, Docs는 문서 작업.
- **import**: 다른 파일의 함수·클래스를 불러와 쓰는 것. 이웃집 공구를 빌려 오는 것과 비슷하다.
- **변수**: 값에 붙이는 이름표. `choice = 3`이면 3에 choice라는 이름표가 붙는다.
- **`input` / `.strip()`**: input은 키보드로 친 글자를 받고, strip은 앞뒤 공백을 지운다.
- **`int()`**: 글자를 정수로 바꾼다. `"3"` → 3. 숫자가 아닌 글자는 ValueError.
- **`try` / `except`**: try 안에서 오류가 나면 멈추지 않고 except 아래를 실행하는 안전망.
- **`continue` / `break` / `return`**: 다음 바퀴로 / 반복에서 내림 / 함수를 끝내고 값을 돌려줌.
- **`None`**: '아직 값이 없음'을 뜻하는 특별한 값. 0과 다르다.
- **`if` / `elif` / `else`**: 조건에 따라 길을 나눈다. 위에서부터 처음 맞는 하나만 간다.
- **Traceback**: 프로그램이 오류로 멈출 때 나오는 오류 경로 안내문.
- **브랜치(branch)**: 원본(main)을 건드리지 않고 따로 작업하는 갈래. 원본 공책을 복사한 연습장.
- **checkout**: 다른 브랜치로 옮겨 가는 명령. `-b`를 붙이면 새로 만들면서 옮겨 간다.
- **merge(병합)**: 다른 브랜치의 작업을 지금 브랜치에 합치는 것.
- **fast-forward / `--no-ff`**: 빨리 감기는 갈래 없이 한 줄로 이어 붙이는 병합, `--no-ff`는 '합쳤다'는 병합 커밋을 꼭 남기라는 옵션.
- **병합 커밋**: 두 갈래를 합쳤다는 기록. 그래프에서 두 선이 만나는 점.
- **작업 중인 변경(working tree)**: 고쳤지만 아직 커밋하지 않은 상태. 브랜치를 옮겨도 따라온다.
- **`--graph --all`**: 기록을 갈래 그림으로, 모든 브랜치를 함께 보여 달라는 옵션.
- **`round()`**: 반올림 함수. 숫자만 넣으면 정수로, `round(값, 2)`처럼 자릿수를 넣으면 그 자리까지.
- **`/` 와 `//`**: `/`는 보통 나눗셈(7 / 2 = 3.5), `//`는 소수점 아래를 버리는 몫 나눗셈(7 // 2 = 3).
- **`+=`**: `a += 1`은 `a = a + 1`의 줄임말 (1 늘리기).
- **`python -c "…"`**: 파일 없이 따옴표 안의 짧은 코드를 바로 실행.
