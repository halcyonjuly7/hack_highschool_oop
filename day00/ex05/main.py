from player import PointGuard, Actor

if __name__ == "__main__":
    pg = PointGuard()
    actor = Actor()
    pg.run_play("hard_foul")
    actor.run_play("hamlet")
