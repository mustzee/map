#!/usr/bin/env python3
"""
LogMaster 전체 자동 채점 시스템
"""
import sys
import os
import subprocess


STEPS = {
    1: ("step1_basic_reader", "기본 로그 파일 리더"),
    2: ("step2_filtering", "필터링 & 검색"),
    3: ("step3_pattern_analysis", "패턴 분석 & 집계"),
    4: ("step4_numpy_stats", "NumPy 통계 분석"),
    5: ("step5_pandas_advanced", "Pandas 고급 분석"),
    6: ("step6_database", "데이터베이스 연동"),
}


def print_header(text):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def run_step_test(step_num):
    """특정 스텝의 테스트 실행"""
    if step_num not in STEPS:
        print(f"❌ Step {step_num}은(는) 존재하지 않습니다.")
        return False

    step_dir, step_name = STEPS[step_num]

    if not os.path.exists(step_dir):
        print(f"❌ {step_dir} 디렉토리를 찾을 수 없습니다.")
        return False

    test_file = os.path.join(step_dir, 'test.py')
    if not os.path.exists(test_file):
        print(f"⚠️  Step {step_num}의 test.py가 아직 준비되지 않았습니다.")
        return None

    print(f"\n🧪 Testing Step {step_num}: {step_name}")
    print("-" * 70)

    try:
        result = subprocess.run(
            [sys.executable, 'test.py'],
            cwd=step_dir,
            capture_output=True,
            text=True
        )

        print(result.stdout)
        if result.stderr:
            print(result.stderr)

        return result.returncode == 0

    except Exception as e:
        print(f"❌ 테스트 실행 오류: {e}")
        return False


def main():
    print_header("LogMaster 전체 자동 채점 시스템")

    # 인자 파싱
    if len(sys.argv) > 1:
        try:
            step_num = int(sys.argv[1])
            return 0 if run_step_test(step_num) else 1
        except ValueError:
            print("사용법: python grader.py [스텝번호]")
            return 1

    # 전체 스텝 테스트
    results = {}
    for step_num in sorted(STEPS.keys()):
        result = run_step_test(step_num)
        if result is not None:
            results[step_num] = result

    # 결과 요약
    print_header("📊 전체 결과 요약")

    passed = sum(1 for v in results.values() if v)
    tested = len(results)
    total = len(STEPS)

    for step_num, (_, step_name) in STEPS.items():
        if step_num in results:
            status = "✅ PASS" if results[step_num] else "❌ FAIL"
        else:
            status = "⏭️  SKIP (not ready)"
        print(f"  Step {step_num}: {step_name:30s} {status}")

    print("=" * 70)
    print(f"  완료된 단계: {passed}/{tested}")
    print(f"  전체 진행률: {passed}/{total} ({passed/total*100:.0f}%)")
    print("=" * 70)

    if passed == total:
        print("\n🎉 축하합니다! 모든 단계를 완료했습니다! 🎉\n")
    elif passed > 0:
        print(f"\n💪 {passed}개 단계 완료! 계속 진행하세요!\n")
    else:
        print("\n🚀 Step 1부터 시작하세요!\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
