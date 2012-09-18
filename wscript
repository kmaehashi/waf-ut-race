import sys
from waflib.Tools import waf_unit_test

def options(opt):
  opt.load('compiler_cxx')
  opt.load("waf_unit_test")

def configure(conf):
  conf.load('compiler_cxx')
  conf.load("waf_unit_test")

def build(bld):
  bld.recurse("tests")
  bld.add_post_fun(waf_unit_test.summary)
