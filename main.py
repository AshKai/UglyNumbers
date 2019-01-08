from time import time
import sys

if len(sys.argv) < 2:
    print("usage: py main.py <dataset_file> [-t]")

if len(sys.argv) == 2:
    import superugly_mem
    import superugly_tab
    import ugly_mem
    import ugly_tab
    n = int(input("Ugly number position to search: "))
    file = open(sys.argv[1], 'r').read().split(",")
    ugly_tab.init(n)
    ugly_mem.init(n)
    superugly_tab.init(n, file)
    superugly_mem.init(n)

if len(sys.argv) == 3 and sys.argv[2] == "-t":
    import superugly_mem
    import superugly_tab
    import ugly_mem
    import ugly_tab
    n = int(input("Ugly number position to search: "))
    file = open(sys.argv[1], 'r').read().split(",")
    startTime = time()
    ugly_tab.init(n)
    elapsedTime = time() - startTime
    print(" ", elapsedTime, "seconds to execute")
    startTime = time()
    ugly_mem.init(n)
    elapsedTime = time() - startTime
    print(" ", elapsedTime, "seconds to execute")
    startTime = time()
    superugly_tab.init(n, file)
    elapsedTime = time() - startTime
    print(" ", elapsedTime, "seconds to execute")
    startTime = time()
    superugly_mem.init(n)
    elapsedTime = time() - startTime
    print(" ", elapsedTime, "seconds to execute")
