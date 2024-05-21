from ball import Ball
class BallLaunch:
    display = False
    def handle_keystroke(self, keystroke, game):
        try:
            if keystroke.name in ("KEY_ENTER"):
                try:
                    game.get_agent_by_name('theball')
                except:
                    a=Ball(game.get_agent_by_name('arrow').position[1],game.get_agent_by_name('meter').position[0]-22)
                    a.name='theball'
                    game.add_agent(a)
        except:
            None