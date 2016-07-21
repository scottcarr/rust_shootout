#!/usr/bin/python
import sys
import os
from subprocess import Popen, call
from timeit import default_timer
import numpy as np

N = 1

def rebuild_bench():
  cmd = "cargo build --release --verbose".format(sys.argv[1])
  #print "Calling: ", cmd
  call("cargo clean", shell=True)
  start = default_timer()
  call(cmd, shell=True)
  end = default_timer()
  print("Compiling took: {}".format(end - start))

def run_bench():
  f = open("bench.out", 'w')
  print "Running {} iterations".format(N)
  runs = np.zeros((N,1))
  for i in range(N): 
    start = default_timer()
    p = Popen(["cargo", "run", "--release", "--verbose"], stdout=f)
    p.wait()
    end = default_timer()
    runs[i] = end - start
  print "avg: {}, std: {}".format(np.average(runs), np.std(runs))

def go_new(rustc):
  os.environ["RUSTC"] = rustc
  os.environ["RUSTFLAGS"]="-Z orbit"
  os.chdir(start_dir)
  os.chdir('new')

def go_baseline(rustc):
  os.environ["RUSTC"] = rustc
  os.environ["RUSTFLAGS"]="-Z orbit"
  os.chdir(start_dir)
  os.chdir('baseline')

if len(sys.argv) != 3:
  print "USAGE: bench.py path-to-baseline-rustc path-to-new-rustc"
else:
  start_dir = os.getcwd()
  go_baseline(sys.argv[1])
  rebuild_bench()
  run_bench()
  go_new(sys.argv[2])
  rebuild_bench()
  run_bench()
