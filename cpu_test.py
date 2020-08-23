import sys
import time


def main(args):
    if len(args) != 1:
        print("Usage: cpu_test.py <type>")
        exit(1)

    # nc = no credit, fc = full credit,
    # vm = virtuak machine, pm = physical machine
    accepted_args = {'nc': 'result_no_credit.txt', 'fc': 'result_full_credit.txt',
                     'vm': 'result_vm.txt', 'pm': 'result_pm.txt'}
    if args[0] not in accepted_args:
        print("Invalid argument: accept", ", ".join(accepted_args))
        exit(1)

    test_type = args[0]

    timestamps = []
    start = time.perf_counter_ns()
    for i in range(50000):
        timer = str(time.perf_counter_ns()-start)
        if len(timer) > 9:
            timer = timer[:-9]+"."+timer[:len(timer)-9]
        else:
            timer = "0." + timer.rjust(9, "0")

        timestamps.append(
            str(i) + ", " + timer)

    f = open(accepted_args[test_type], "w")
    for e in timestamps:
        f.write(e+"\n")
    f.close()
    # print(test_type)
    # for e in timestamps:
    #     print(e)
    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
