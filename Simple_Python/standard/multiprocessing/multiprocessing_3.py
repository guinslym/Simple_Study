#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import multiprocessing
import multiprocessing_import

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(
            target=multiprocessing_import.worker,
            )
        jobs.append(p)
        p.start()