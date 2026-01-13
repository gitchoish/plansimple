# Cloudflare Pages 배포 설정

## 필수 단계:

### 1. Cloudflare 계정 생성
- https://dash.cloudflare.com/sign-up/pages 방문
- 무료 계정으로 가능

### 2. GitHub 저장소 연결
1. Cloudflare Dashboard → Pages → "계정 생성"
2. GitHub 선택 → "GitHub 연결"
3. plansimple 리포지토리 선택

### 3. 빌드 설정
- **프레임워크**: Astro
- **빌드 명령어**: `npm run build`
- **빌드 출력 디렉토리**: `dist`
- **루트 디렉토리**: `/` (또는 비워두기)

### 4. 환경 변수 (필요시)
- 설정할 환경 변수 추가

### 5. 배포
- "저장 및 배포" 클릭
- 자동으로 GitHub에서 변경사항을 감지하고 배포

## 배포 후:
- Pages URL 받음 (예: `plansimple.pages.dev`)
- 자동 HTTPS, CDN, 무료 SSL 포함

## 커스텀 도메인 설정:
1. Pages 프로젝트 → 설정 → 커스텀 도메인
2. 도메인 추가 및 DNS 레코드 구성

---
**빌드 실패 시 확인:**
- `npm install` 실행 가능 확인
- `npm run build` 로컬에서 작동 확인
- `dist/` 폴더 생성 확인
