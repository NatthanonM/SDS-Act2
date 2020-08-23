# SDS-Act2
Activity 2: Resource management on clouds and virtual environments

# Write cpu_test.py

Write a python program called "cpu_test.py" that will loop 50,000 times.

In each iteration, the program simply gets the current time by either calling
- time.time_ns() on Python 3.7+ or
- time.time() on older versions of Python

and appends the timestamp into a list in memory.

After your finish looping for 50,000 iterations, the program writes all the saved timestamps in the
list from memory to a file on disk. Do not write to disk while looping.

The file ought to look something like this where the first column is the iteration and the second
column is the time (in seconds) since the 0'th round.

0, 0.00000000\
1, 0.00000286\
2, 0.00001502\
3, 0.00001597\
4, 0.00001693\
5, 0.00001884\
6, 0.00002003\
7, 0.00002098\
8, 0.00002193\
9, 0.00002384\
10, 0.00002503\
11, 0.00002599

Normally, if the program is executed continuously, all loop iterations should take a similar
amount of time.

# Running cpu_test.py
You will run cpu_test.py in 4 scenarios.
1. (Cloud Instance No Credits) Once in an Amazon EC2 t2.micro instance with no CPU
credits left. You must completely deplete the CPU credits yourself. This could take 30-40
minutes. So, start early. (Hmm...why does it take so long?)
2. (Cloud Instance with Credits) Once in an Amazon EC2 t2.micro instance that has just be
provisioned and has sufficient CPU credits to run your program.
3. (Virtual Machine) Once in a Linux VM running in VirtualBox on your notebook. This must
be a VM.
4. (Physical Machine) Once on your notebook computer. If you are using Windows, make
sure you are using Python 3.7+ or your results will not be valid.
While running cpu_test.py, take screenshots and make observations on your CPU utilization and
CPU credits. Notice the difference in behavior between all 4 scenarios.
