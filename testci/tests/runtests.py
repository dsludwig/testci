'''
Created on Aug 5, 2013

@author: sean
'''
from __future__ import print_function
import unittest
from os.path import dirname,join
from argparse import ArgumentParser
from runner import ColorTextTestRunner
from coverage_report import report

def main():
    
    parser = ArgumentParser()
    parser.add_argument('--html', action='store_true')
    parser.add_argument('source_dir', nargs='?', default='')
    args = parser.parse_args()
    
    import coverage
    cov = coverage.coverage(include='**%s**' % args.source_dir if args.source_dir else '**/testci/**',
                            omit=['**/lib/python*/**', '**/site-packages/**', '**/tests/**',
                                  ])
    
    cov.start()

    import testci
    print(testci)
    loader = unittest.loader.TestLoader()
    discover_dir = join(dirname(testci.__path__[0]), args.source_dir)

    print('Discover %s' % discover_dir)
    tests = loader.discover(discover_dir)
    runner = ColorTextTestRunner(verbosity=2)
    result = runner.run(tests) 
    cov.stop()
    cov.save()
    total = report(cov)
    if args.html:
        cov.html_report(directory='coverage')
    
    runner.write_end(result, total)
    
    exit(0 if result.wasSuccessful() else -1)
    
    
if __name__ == '__main__':
    main()
