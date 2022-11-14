#!/usr/bin/env python3
import cheatdice

class Cheat_mulligan(Player):
    # re-roll if total dice sum is less than 9
    def cheat(self):
        while sum(self.dice)<9:
            self.roll()
