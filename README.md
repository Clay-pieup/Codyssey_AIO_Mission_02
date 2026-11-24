# Mission 02 · 나만의 퀴즈 게임 (Python & Git 기초)
> 한 줄 요약: 터미널에서 메뉴를 골라 퀴즈를 풀고·추가하고·목록과 최고 점수를 보는 파이썬 콘솔 게임. 데이터는 `state.json`에 저장돼 껐다 켜도 남는다.

> [!NOTE]
> 코디세이 AI 올인원 1기 · 2주차 · 상태: 진행 중

## 프로젝트 개요
- Python 클래스 2개(`Quiz`, `QuizGame`)로 퀴즈 게임을 만들고, 퀴즈와 최고 점수를 `state.json`에 저장한다.
- Git으로 기능마다 커밋하고, 작업 브랜치를 만들어 합치고, clone·pull까지 직접 해 본다.
- **퀴즈 주제: Python·Git 기초** — 이번 미션에서 배우는 내용이라 게임을 만들면서 복습이 되고, 동료평가·시험 준비에도 쓸 수 있어서 골랐다 → [설계 결정](LEARNING.md#6-퀴즈-주제는-pythongit-기초)

## 실행 방법
Python 3.10 이상, 외부 라이브러리 없음. 개발 환경: Windows PowerShell · Cursor(VSCode 기반 편집기) · Python 3.14.7 · Git 2.54.0 → [환경 스크린샷](docs/screenshots/env.png)
```powershell
python main.py
```

## 기능 목록
| 메뉴 | 기능 | 실행 화면 |
|---|---|---|
| 1 퀴즈 풀기 | 문제를 무작위 순서로 출제(보너스) → 정답/오답 표시 → `결과: 8문제 중 3문제 정답! (38점)` → 최고 점수와 비교·갱신·저장 | [play](docs/screenshots/play.png) · [score](docs/screenshots/score.png) |
| 2 퀴즈 추가 | 문제·선택지 4개·정답 번호(1~4) 입력 → 바로 저장 | [add_quiz](docs/screenshots/add_quiz.png) |
| 3 퀴즈 목록 | 번호와 문제 글만 표시 (정답은 숨김), 0개면 안내 | [add_quiz](docs/screenshots/add_quiz.png) |
| 4 점수 확인 | `최고 점수: 100점`, 아직 안 풀었으면 안내 | [score](docs/screenshots/score.png) |
| 5 종료 | 저장 후 종료 | [menu](docs/screenshots/menu.png) |
| 공통 | 공백·`abc`·범위 밖 숫자·빈 Enter → 안내 후 다시 입력 / Ctrl+C·입력 끊김 → 저장 후 안전 종료 / `state.json` 없음·손상 → 기본 퀴즈로 시작 | [검증 기록](LEARNING.md#u8--검증실행-화면) |

## 파일 구조
```text
Codyssey_AIO_Mission_02/
├─ main.py          실행 시작점: QuizGame을 만들고 run()
├─ quiz.py          Quiz 클래스(문제 1개) + 기본 퀴즈 6개
├─ quiz_game.py     QuizGame 클래스(메뉴·풀기·추가·목록·점수·저장/불러오기) + 입력 검사 함수
├─ README.md        이 문서
├─ LEARNING.md      설계 결정·코드 해설·수행 로그·배운 점·용어 사전
├─ .gitignore       올리지 않을 파일 목록 (state.json, 명세, __pycache__ 등)
├─ docs/screenshots 개발 환경·실행 화면 캡처
└─ state.json       실행하면 생기는 저장 파일 (저장소에는 없음)
```

## 데이터 파일 (`state.json`)
- 경로: 프로젝트 맨 위 폴더의 `state.json` (UTF-8). 처음 실행하면 기본 퀴즈로 시작하고, 종료·퀴즈 추가·최고 점수 갱신 때 저장된다.
- 역할: 퀴즈 목록과 최고 점수를 저장해 껐다 켜도 남게 한다. 개인 플레이 기록이라 저장소에는 올리지 않는다(`.gitignore`).
- 파일이 깨져 있으면 안내 후 기본 퀴즈로 복구한다 → [설계 결정](LEARNING.md#15-statejson은-dict로-바꿔-json으로-저장한다)

| 키 | 자료형 | 뜻 |
|---|---|---|
| `quizzes` | list | 퀴즈 목록. 각 항목은 `question`(문제, str) · `choices`(선택지 4개, list) · `answer`(정답 번호 1~4, int) |
| `best_score` | int 또는 null | 최고 점수(100점 만점). 아직 안 풀었으면 null |

## 체크리스트
**필수 (완료 13/15)** — 1~11 기능·코드는 모두 ✅ ([수행 로그](LEARNING.md#수행-로그))
| # | 항목 | 상태 | 증거·해설 |
|---|---|---|---|
| 1~5 | 저장소 · 메뉴 · 입력/예외 처리 · Quiz 클래스 · 기본 퀴즈 6개 | ✅ 완료 | [U1](LEARNING.md#u1--저장소-초기-설정) · [U2](LEARNING.md#u2--quiz-클래스기본-퀴즈) · [U3](LEARNING.md#u3--메뉴입력-검증) · [U5](LEARNING.md#u5--statejson-저장불러오기) |
| 6 | 퀴즈 풀기 + 브랜치 병합 | ✅ 완료 | [U4](LEARNING.md#u4--퀴즈-풀기브랜치-병합) (`feature/play-quiz` → main) |
| 7~9 | 퀴즈 추가 · 목록 · 점수 확인 | ✅ 완료 | [U6](LEARNING.md#u6--퀴즈-추가목록) · [U7](LEARNING.md#u7--최고-점수) |
| 10~11 | QuizGame 클래스 · `state.json` 저장/불러오기 | ✅ 완료 | [클래스 구조](LEARNING.md#23-quizgame은-기능마다-메서드-하나) · [U7](LEARNING.md#u7--최고-점수) |
| 12 | README 필수 항목 (개요·주제 이유·실행·기능·파일 구조·데이터 파일) | ✅ 완료 | 이 문서 |
| 13 | clone·pull 실습 | ⬜ 대기 | — |
| 14 | Git 작업 기록 (커밋 10개+, 명령 7종) | 🔶 진행중 | 커밋 10개 이상 ✔ (19개), 명령 5/7 (pull·clone은 13번에서) |
| 15 | 개발 환경·실행 화면 증거 | ✅ 완료 | [env](docs/screenshots/env.png) · [menu](docs/screenshots/menu.png) · [play](docs/screenshots/play.png) · [add_quiz](docs/screenshots/add_quiz.png) · [score](docs/screenshots/score.png) |

**보너스 (완료 1/5)** — 1 랜덤 출제 ✅ ([설계 결정](LEARNING.md#25-보너스는-랜덤-출제-하나만-복사본을-섞는다)) · 2 문제 수 선택 · 3 힌트 · 4 퀴즈 삭제 · 5 점수 히스토리는 하지 않음

## 진행 기록
### 2026-11-24 · 주중 세션
- 추가: Quiz 클래스·기본 퀴즈 6문제 → 메뉴·입력 검사 → 퀴즈 풀기(`feature/play-quiz` 브랜치 병합) → `state.json` 저장·불러오기·예외 처리 → 퀴즈 추가·목록 → 최고 점수
- 추가: 보너스 랜덤 출제 · 실행 화면 스크린샷 4장 / 변경: README에 기능 목록·파일 구조 추가

<details><summary>이전 기록</summary>

### 2026-11-23 · 주중 세션
- 추가: 저장소 뼈대(README, LEARNING, .gitignore) · 첫 커밋과 GitHub push · 개발 환경 스크린샷
</details>

## 더 보기
- [학습 기록](LEARNING.md) — 설계 결정 · 핵심 코드 해설 · 수행 로그 · 배운 점 · 용어 사전
- 발표 슬라이드 (마지막 단계에서 추가)
