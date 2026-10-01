"""PRO-99 Kleiner Perkins, judge j07: the one country left open in batch 13. Run: NQ_TAG=j07 python3 judgments-j07c.py"""
import judge_lib as jl
from judge_lib import cls, ARCH

L = [cls("elcomax", country="DE", country_src="web_verified", country_cite=ARCH("elcomax"),
         note="elcomax (fuel cell combined heat and power, partners Brook Porter and Jan van Dokkum, 2013-18 pages) is a "
              "German company: the firm's own page links its site at elcomax.de, a domain that no longer resolves; its "
              "fate and city are not established and no round is named.")]
jl.write("j07c", L)
