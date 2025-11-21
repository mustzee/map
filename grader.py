#!/usr/bin/env python3
"""
자동 채점 시스템

각 단계별 테스트를 실행하고 결과를 출력합니다.
"""
import sys
import subprocess
import argparse
from pathlib import Path


STEPS = {
    1: "Python 리스트와 배열 기초",
    2: "NumPy 배열",
    3: "Pandas 기초",
    4: "Pandas 데이터 처리",
    5: "SQLite 데이터베이스",
    6: "Pandas-DB 연동"
}


def print_header(title):
    """헤더 출력"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_section(title):
    """섹션 출력"""
    print("\n" + "-" * 70)
    print(f"  {title}")
    print("-" * 70)


def run_step_tests(step, verbose=False):
    """특정 단계의 테스트 실행"""
    test_file = f"tests/test_step{step}.py"

    if not Path(test_file).exists():
        print(f"❌ 테스트 파일을 찾을 수 없습니다: {test_file}")
        return False

    print_section(f"Step {step}: {STEPS[step]}")

    # pytest 명령 구성
    cmd = ["pytest", test_file, "-v" if verbose else "-q", "--tb=short"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)

        if verbose:
            print(result.stdout)
            if result.stderr:
                print(result.stderr)

        # 결과 파싱
        if result.returncode == 0:
            print(f"✅ Step {step} 모든 테스트 통과!")
            return True
        else:
            print(f"❌ Step {step} 일부 테스트 실패")
            if not verbose:
                print("\n상세 결과를 보려면 --verbose 옵션을 사용하세요:")
                print(f"  python grader.py --step {step} --verbose")
            return False

    except FileNotFoundError:
        print("❌ pytest가 설치되어 있지 않습니다.")
        print("다음 명령어로 설치하세요: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return False


def run_all_tests(verbose=False):
    """모든 단계의 테스트 실행"""
    print_header("데이터 학습 프로젝트 - 자동 채점 시스템")

    results = {}
    for step in STEPS:
        results[step] = run_step_tests(step, verbose)

    # 결과 요약
    print_section("📊 전체 결과 요약")

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for step, passed_test in results.items():
        status = "✅ 통과" if passed_test else "❌ 실패"
        print(f"  Step {step}: {STEPS[step]:30s} {status}")

    print("\n" + "=" * 70)
    print(f"  전체 진행률: {passed}/{total} 단계 통과 ({passed/total*100:.1f}%)")
    print("=" * 70)

    if passed == total:
        print("\n🎉 축하합니다! 모든 단계를 완료했습니다! 🎉\n")
    else:
        print(f"\n💪 {total - passed}개 단계가 남았습니다. 계속 도전하세요!\n")

    return passed == total


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="데이터 학습 프로젝트 자동 채점 시스템",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예제:
  전체 테스트 실행:
    python grader.py

  특정 단계만 테스트:
    python grader.py --step 1

  상세 결과 보기:
    python grader.py --verbose
    python grader.py --step 1 --verbose
        """
    )

    parser.add_argument(
        '--step', '-s',
        type=int,
        choices=list(STEPS.keys()),
        help='특정 단계만 테스트 (1-6)'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='상세 결과 출력'
    )

    args = parser.parse_args()

    # 프로젝트 루트로 이동
    project_root = Path(__file__).parent
    import os
    os.chdir(project_root)

    if args.step:
        # 특정 단계만 실행
        print_header(f"Step {args.step}: {STEPS[args.step]} 테스트")
        success = run_step_tests(args.step, args.verbose)
        sys.exit(0 if success else 1)
    else:
        # 모든 테스트 실행
        success = run_all_tests(args.verbose)
        sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
