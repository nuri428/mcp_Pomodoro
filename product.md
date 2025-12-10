# 포모도로 타이머 프로젝트 (Pomodoro Timer - Local/MCP Integrated)

## 1. 프로젝트 개요
본 프로젝트는 로컬 환경에서 동작하는 포모도로 타이머 애플리케이션을 개발하는 것을 목표로 한다.
1차 버전은 CLI 중심의 경량 타이머이며, 이후 MCP를 통해 ChatGPT, LangGraph 등과 연동 가능한 구조를 가진다.

---

## 2. 1차 버전 목표 (MVP)
필수 기능:
1) 포커스 시간, 휴식 시간, 반복 횟수를 설정하여 자동 루프 실행
2) 현재 상태(Focus/Break/Finished)와 남은 시간 출력
3) OS별 로컬 알림 지원
4) CLI 또는 config.json을 통한 설정 입력
5) 중단, 일시정지(Optional)

---

## 3. 2차 버전 목표 (확장 계획)
- MCP 기반 외부 제어 기능 추가
- ChatGPT가 Pomodoro 시작/정지/상태 조회 가능
- 새벽 시간 경고 같은 “시간 기반 자동 노티” 기능 확장
- Google Calendar 연동 (Focus Time 자동 기록)
- 멀티 플랫폼 UI 확장 (Windows Tray, macOS Menubar, Linux Indicator)

---

## 4. 추천 디렉토리 구조
project-root/
├─ pomodoro/
│   ├─ timer.py         # 핵심 타이머 로직
│   ├─ notifier.py      # 알림 처리
│   ├─ config.py        # 설정 로딩
│   └─ utils.py
│
├─ cli.py               # CLI 엔트리 포인트
├─ config.json.example
├─ README.md
└─ requirements.txt

---

## 5. 동작 흐름
1) 설정 로딩
2) PomodoroTimer 객체 생성
3) 다음과 같은 순서로 반복:

Focus 시작 → 알림 → Focus 카운트다운  
Break 시작 → 알림 → Break 카운트다운  

전체 반복 종료 후 “세션 완료” 알림.

---

## 6. Timer 기능 명세
- 초 단위 카운트다운
- 남은 시간 실시간 출력
- KeyboardInterrupt 발생 시 안전 종료

---

## 7. Notification 구현
OS별 구현 방식:
- macOS: osascript
- Windows: win10toast
- Linux: notify-send

notifier.py 내부에서 OS 감지 후 자동 선택.

---

## 8. 기술 스택
- Python 3.10+
- cross-platform notification 라이브러리(Optional)
- MCP 연동을 고려한 모듈화 구조

---

## 9. 개발 우선순위
1) CLI 파라미터 파싱
2) Timer 클래스 구현
3) Notifier 구현
4) 실행 루프 개발
5) 예외 처리 및 종료 처리

---

## 10. 향후 개선 아이디어
- 일일 생산성 로그 기록
- 앱 차단 기능 (Deep Focus Mode)
- Slack/Discord/Webhook 알림
- 다음날 리포트 자동 생성
- Pomodoro 진행도 시각화

---

## 11. 라이센스
MIT License 권장

---

## 12. 요약
본 프로젝트는 간단한 포모도로 타이머를 기반으로 시작하여,
향후 MCP 기반 AI 도구 생태계로 확장하기 위한 구조적 기반을 제공하는 것을 목표로 한다.