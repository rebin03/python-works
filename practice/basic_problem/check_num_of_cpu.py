# 'multiprocessing' module to work with multi-processing features.
import multiprocessing

# the number of available CPU cores.
cpu = multiprocessing.cpu_count()

print(cpu)