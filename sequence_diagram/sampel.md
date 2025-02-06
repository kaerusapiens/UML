```mermaid
sequenceDiagram
    participant User
    participant System
    participant Database

    User->>System: 요청 보내기
    activate System

    alt 데이터 유효함
        System->>Database: 데이터 검색
        activate Database
        Database-->>System: 데이터 반환
        deactivate Database
    else 데이터 없음
        System->>User: 오류 메시지 반환
    end

    opt 재시도 로직
        loop 최대 3회
            System->>System: 데이터 재시도
        end
    end

    critical 중요 작업 실행
        System->>Database: 중요한 데이터 업데이트
    end

    alt 예외 발생 여부
        System->>Database: 트랜잭션 시작
        Database-->>System: 성공
    else 오류 발생
        System->>User: 오류 메시지 반환
    end

    break 조건 충족 시 중단
        System->>User: 프로세스 중단
    end

    deactivate System
```
* alt (조건 분기): if-else 문과 비슷한 구조.
* opt (옵션 블록): 실행할 수도 있고 안 할 수도 있는 블록.
* loop (반복문): 특정 횟수만큼 반복 실행.
* critical (중요 블록): 반드시 실행되어야 하는 중요 작업.
* try-catch: 예외 처리 패턴.
* break: 특정 조건에서 중단하는 흐름.
* activation/deactivation: 활성화 및 비활성화 표현.