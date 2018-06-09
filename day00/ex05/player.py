class Player:
    plays = {}
    def run_play(self, play):
        play_res = self.plays.get(play)
        if play is None:
            print("Don't know what the play that is")
        print(play_res)


class PointGuard(Player):
    plays = {
                "hard_foul": "punch player",
                "shoot": "shoot_ball",
                "double_team": "tag the m*ther f*cker"
            }
    

class Actor(Player):
    plays = {"shakespeare": "insert swag here",
            "hamlet": "mdkmmgkmgkfm"}

        
