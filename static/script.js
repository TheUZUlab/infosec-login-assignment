// 로그인 모드 상태 (true: 로그인, false: 회원가입)
let isLogin = true;

/**
 * 로그인 <-> 회원가입 모드 전환 함수
 * 버튼 텍스트, 제목, 폼 액션, 안내 문구를 모두 전환
 */
function toggleForm() {
    isLogin = !isLogin;

    const formTitle = document.getElementById('form-title');
    const submitButton = document.querySelector('button');
    const authForm = document.getElementById('auth-form');
    const toggleText = document.getElementById('toggle-text');

    formTitle.innerText = isLogin ? '로그인' : '회원가입';
    submitButton.innerText = isLogin ? '로그인' : '회원가입';
    authForm.action = isLogin ? '/login' : '/register';
    toggleText.innerText = isLogin ? '계정이 없으신가요?' : '이미 계정이 있으신가요?';
}

/**
 * 폼 유효성 검사
 * 아이디는 6자 이상, 비밀번호는 8자 이상이어야 함
 */
function validateForm() {
    const id = document.getElementById('username').value.trim();
    const pw = document.getElementById('password').value.trim();

    if (id.length < 6 || pw.length < 8) {
        alert('아이디는 6자 이상, 비밀번호는 8자 이상 입력해주세요.');
        return false;
    }

    return true;
}

/**
 * 초기 설정: 로그인 폼 액션을 기본으로 설정
 * HTML이 완전히 로드된 후 실행되도록 보장
 */
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('auth-form').action = '/login';
});
