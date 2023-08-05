import unittest

from .LineFeeder import feedText

from PyFoam.LogAnalysis.TimeLineAnalyzer import TimeLineAnalyzer

class TimeLineAnalyzerClassTest(unittest.TestCase):

    def setTime(self,time):
        self.time=time

    def testNormal(self):
        self.time = None
        ta = TimeLineAnalyzer()
        ta.tryFallback = False
        ta.addListener(self.setTime)

        assert self.time is None

        feedText(ta,
"""Nix
Time = 1.23
nix"""
        )
        assert self.time == 1.23

        feedText(ta,
"""Nix
Time = constant
nix"""
        )
        assert self.time != "constant"
        assert self.time == 1.23

        feedText(ta,
"""Nix
Time = 1.4 23
nix"""
        )

        assert self.time == 1.23

        feedText(ta,
"""Nix
Iteration: 23
nix"""
        )

        assert self.time == 23

        feedText(ta,
"""Nix
RunTime = 1.23
nix"""
        )
        assert self.time == 23

    def test_normal_of10(self):
        self.time = None
        ta = TimeLineAnalyzer()
        ta.tryFallback = False
        ta.addListener(self.setTime)

        assert self.time is None

        feedText(ta,
"""Nix
Time = 1.23s
nix"""
        )
        assert self.time == 1.23

        feedText(ta,
"""Nix
Time = 1.23s no
nix"""
        )
        assert self.time == 1.23
