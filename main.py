
# Main
# Sprites
player_sprite: Sprite = None
zombie_sprite: Sprite = None
bullet_sprite: Sprite = None

# Sprite lists
bullet_list:List[Bullet] = []
zombie_list:List[Zombie] = []
deleted_zombies_list:List[Zombie] = []

# Status bar Sprites
exp_status_bar:StatusBarSprite = None
statusbar: StatusBarSprite = None # Zombie sb

# Text Sprites
title_sprite: TextSprite = None
text_sprite: TextSprite = None
skip_lore_sprite: TextSprite = None
skip_stats_sprite: TextSprite = None

# Enemies stats
delay_min_enemies = 0
delay_max_enemies = 0

# Zombie Stats
zombie_speed = 0
zombie_stun_duration = 0
zombie_stun_speed = 0
zombie_hp = 0
zombie_power = 0
ypos_bullet = 0
xpos_bullet = 0
ypos_zombie_sprite = 0
zombie_xp_reward = 0


# Player Stats
direction = ""
player_level = 0
player_exp = 0
player_exp_required = 0
player_points = 0
player_hp = 0
player_power = 0
player_speed = 0
player_exp_punish = 0
# Booleans
on_menu = True
on_zombie_screen = False
on_lore_screen = False
on_stats_screen = False

# CONSTANTS
# Boundaries
RIGHT_BOUNDARY = 160
LEFT_BOUNDARY = 0
BOTTOM_BOUNDARY = 120
TOP_BOUNDARY = 0


# Stats to Display
stat_shots = 0
stat_missed_shots = 0
stat_precission = 0
stat_accurate_shots = 0


stat_zombies_escaped = 0
stat_zombies_killed = 0
stat_damage_dealt = 0
stat_lifes_won = 0
stat_lifes_lost = 0

# Classes
@namespace
class SpriteKind:
    projectile = SpriteKind.create()
    enemy = SpriteKind.create()
    player = SpriteKind.create()

class Bullet:
    def __init__(self, sprite: Sprite, bullet_id: Number):
        self.bullet_id = bullet_id
        self.sprite: Sprite = sprite

class Zombie:
    def __init__(self, sprite: Sprite, zombie_id: Number):
        self.zombie_id = zombie_id
        self.sprite: Sprite = sprite

# main
open_main_screen()

# Screens
# Pantalla principal
def open_main_screen():
    global on_menu
    on_menu = True
    if on_menu == True:
        scene.set_background_image(assets.image("""
                            woods
                        """))
        create_title_sprite()
        bottom_text_sprite()
    else:
        pass
def create_title_sprite():
    global title_sprite
    title_sprite = textsprite.create("Zomb")
    title_sprite.set_max_font_height(20)
    title_sprite.set_outline(3, 14)
    title_sprite.set_position(82, 20)

def bottom_text_sprite():
    global text_sprite
    text_sprite = textsprite.create("Apreta A para jugar")
    text_sprite.set_outline(0.2, 5)
    text_sprite.set_position(80, 110)

# Pantalla de lore
def lore_cutscene():
    lore_screen()
    story.start_cutscene(zombie_cutscene)

def lore_screen():
    global on_lore_screen, on_menu
    on_lore_screen = True
    on_menu = False
    create_skip_lore_sprite()
    story.set_sound_enabled(True)
    story.set_page_pause_length(0, 1000)
    scene.set_background_image(assets.image("""earth_image"""))
    story.print_dialog("Una misteriosa enfermedad contagiosa está arrasando el mundo,", 80, 90, 50, 150)
    scene.set_background_image(assets.image("""zombie_image2"""))
    story.print_dialog("transformando a la gente en zombis sedientos de sangre humana.", 80, 90, 50, 150)
    scene.set_background_image(img("""
        cccfffffffffffffffffffffffffffffffffffffffffffccccccceeebbbbbbbbbbbbbbcccbbbbbbcccccbbbbbbcccccfccccccccfffffffffffffffffffffffffffffffffffffffffffffcffffffffff
                cccfffffffffffffffffffffffffffffffccfffffffffccccccccceebbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbcccccccccccccccffffffffffffffffffffffffffffffffffffffffffffcccffffffff
                ccccffffffffffffffffffffffffffffffffffffffffffccccccccebbbbbbbbbbbbbbbbbbeebbbbcccccbbbbbbcccccccccccccccffffffffffffffffffffffffffffffffffffffffffcffccffffffff
                cccfcffffffffffffffffffffffffffffffcfffffffffccccccccebbbbbbbbbbbbbbbbbeeeeebbbccccbbbbbbbcccccccccccccccffffffffffffffffffffffffffffffffffffffffffcfffccfffffff
                cccccfffffffffffffffffffffffffffffcccfffffffcccccccccbbbbbbbbbbbbbbbbbeeeeceebbccceeeeeebbcccccccccccccccfffffffffffffffffffffffffffffffffffffffffffcfcccfffffff
                cccccffffffffffffffffffffffffffffccccffffffffccccccccbbbbbbbbbbbbbbbbcceeeeeceeceeeeeeeeeeccccccccccccccccfffffffffffffffffffffffffffffffffffffffffccccccfffffff
                cccccfffffffffffffffffffffffffffffcccfffffffccccccccebbbbbbbbbbbbbbbfcceeeeeeeecceeeeeeceeeccccccccccccccffffcfffffffffffffffffffffffffffffffffffcfccccfffffffff
                cccccfffffffffffffffffffffffffffffcccfffffffccccccccebbbbbbbbbbbbbbffffceeeeeeceeeeeeeeccececccccccccccccfffccfffffffffffffffffffffffffffffffffffffccccfcfffffff
                cccccffffffffffffffffffffffffffffccfffffffffccccccccebbbbbbbbbbbbbbfffffccccfcceeeeeeeccceeecccccccccccccffccccffffffffffffffffffffffffffffffffffcfcccccccffffff
                ccccffffffffffffffffffffffffffffffccfffffffffcccccccebbbbbbbbbbbbbfffffffffcccccceeeeeeeeeeeecccccccccccccffcccfffffffffffffffffffffffffffffffffffccccccccffffff
                cccccfffffffffffffffffffffffffffffccffffffffcccccccceebbbbbbbbbbbfffffffffffccccccceeeeeeeeeeeeccccccccccfffccccfffffffffffffffffffffffffffffffffffcccccccffffff
                ccccccfffffffffffffffffffffffffffccffcffffffcccccccceebbbbbbbbbfffffffffffffcccccccceeeeeeeeeeccccccccccccffcccfffcfffffffffffffffffffffffffffffffccccccccffffff
                ccccccffffffcffffffffffffffffffffffcccfffffffcccccccebbbbbbbbbffffffffffffffccccfccceeeeeeeeeeccccccccccccffccccffcfffffffffffffffffffffffffffffffccccccccffffff
                ccccccfffffcfffffffffffffffffffffffcfccffffffccccccceebbbbbbbcffffffffffffffcfcccccccceeeeeeeeeccccccccccfffccccccccfffffffffffffffffffffffffffffcccccccccffffff
                cccccffffffccfffffffffffffffffffffcccffffffffccccccceebbbbbbbffffffffffffcffccccccccceeeeeeeeeecccccccccccffcccccccccffffffffffffffffffffffffffffccccccccccfffff
                ccccccfffffccffffffffffffffffffffccccccffffffcccccccebbbbbbbffffffffffffffccccccccccceeeeeeeeeeeccccccccccffcccccccccffffffffffffffffffffffffffffcccccccccffffff
                ccccccffffffcffffffffffffffffffffccccfccfffffccccccceebbbbbbffffffffffffcfcccccccccccceeeeeeeeeeeeeeeeeeccffcccccccccffffffffffffffffffffffffffffcccccccccffffff
                cccccffffffffffffffffffffffffffffccccffffffffcccccccebbbbbbcfffffffffffffcccccccfcccceceeeeeeeeeeeeeeeeeccffccccccccfcfffffffffffffffffffffffffffccccccccfffffff
                ccccccfffffcfffffffffffffffffffffffccffffffffccccccceebbbbbffffffffffffffcccccccccccceeeeeeeeeeeeeeeeeeeccffcccccccccfffffffffffffffffffffffffffffcccccccfffffff
                ccccccfffffffcfffffffffffffffffffccccfffffffcccccccceebbbbbfffffffffffffcfccccccfcccceeeeeeeeeeeeeecccccccffcccccccccffcfffffffffffffffffffffffffcccccccccffffff
                cccccffffffffffffffffffffffffffffcfccccffffffcccccceeebbbbcfffffffffffffbeccfcccccccccceeeeeeeeeeeeeeeeeccffccccccccfffffffffffffffffffffffffffffcccccccccffffff
                cccccffffffffffffffffffffffffffffcfccccffffffcccccceeebbbbcfffffffffffffbeccfcccccccccceeeeeeeeeeeeeeeeeccffccccccccfffffffffffffffffffffffffffffcccccccccffffff
                ccccccffffffcfffffffffffffffffffffccfccffffffcccccceeebbbbffffffffffffffeecccccccccceceeeeeeeeeeeeeeeeeeccffcccccccccfffffffffffffffffffffffffffcfccccfccfffffff
                ccccccfffffffffffffffffffffffffffccccccccffffcccccceeebbbbffffffffffffffcccccceeececcceeeeeeeeeeeeeeeeeecccfcccccccccffccccfffffffffffffffffffffcccccccfcfffffff
                ccccccffffffffffffffffffffffffffffccccccccfffcccccceeeebbbffffffffffffffcccccccccccceeeeeeeeeeeeeeeeeeeeeccccccccccccffcccccfffffffffffffffffffffcccccfccfffffff
                ccccccffffffcffffffffffffffffffffcffeccfffffcccccccceeeebffffffffffffffcccccccceceeeeeeeeeeeeeeeeeeccccccccfccccccccfccccccfffffffffffffffffffffcfcccfccfcffffff
                ccccccfffffffffffffffffffffffffffcccecfffffffccccccceebbbfffffffffffffffccccccccceeeeeeeeeeeeeeeeeeccccccccccccccccccffcccccfffffffffffffffffffffccccfffcfffffff
                ccccccffffffffffffffffffffffffffffcfeecffffffcfffceeeeeebfffffffffffffcfcccccccccceececeeeeeeeeeeeecccccccffcccccccccffcccccffffffffffffffffffffcfccfffcfcffffff
                ccccccffffffcffffffffffffffffffffccceeeffffffffffffcceeeefffffffffffffcccfccccccccceceeeeeeeeeeeeeecccccccccccccccccccccccccffffffffffffffffffffccccfcccccffffff
                ccccccffffffccfffffffffffffffffffccceeeffffffffffffffcceefffffffffffffffccccccccceeeeeeeeeeeeeeeeeecccccccccccccccccffccccccffffffffffffffffffffcccccccffcffffff
                ccccccfffffcffffffffffffffffffffffccfceeffffffffffffffffcccfffffffffffccccccccccccceceeeeeeeeeeeeeeccccccccccccccccccffccccfffffffffffffffffffffccccccccfcffffff
                ccccccffffffffffffffffffffffffffffcccfeeecffffffffffffffffffecceefffffccfffccccccccccecceceeeeeeeeeccccccccccccccccccfccccccffffffffffffffffffffccccccffcfcfffff
                ccccccfffffffffffffffffffffffffffcccccfeeecffffffffffffffffccccffccfeeebdbfccccccccccecceeeeeeeeeeeeeecccccccccccccccffcccccffffffffffffffffffffcccccffffccfffff
                ccccccfffffffffffffffffffffffffffcccccccfeeecffffffffffefffffffcccceedbebdddddddddddddddbbeeeeeeeeebeeeeeeeecccccccccfcccccccfffffffffffffffffffccccccfffccfffff
                cccccccffffffffffffffffffffffffffcccccccccfeeeefffffffbdddfffffccded11ddecedddbceeee444444bbbbbbbbbbeeeeeeeeeeeeeeccccfcccccccfffffffffffffffffffcccccfffcfcffff
                ccccccfffffffffffffffffffffffffffcccccccccfffeeeeeecceddbddddddeeeeddd11dcfbeeeeeebbbbbbbbbdddbdbbdbeeeeeeeeeeeeeceeeeeeeeccccffffffffffffffffffffcccfffffcfffff
                ccccccffffffffffffffffffffffffffffcccccccccccccfceeeeeebb4eeeeffffeebbdeeebdddeeeecfcfffffffffccccccceeeeeeeeeeeeeeeeeeeeeccccfffffffffffffffffffffccfffcccfffff
                ccccccfffffffffffffffffffffffffffccccccccccfccccccfffffceecfceeeeeeeeccececccffffffffffffffffffffffffffffffcccceeeeeeeeccccccccfffffffffffffffffffffcfffffcfffff
                ccccccffffffffffffffffffffffffffcccccccccccccccccccceeecffffffffffffffffffffffffffffffffffffffffffffffffffffffffeccccccfccccccccfffffffffffffffffffffccccccfffff
                cccccccffffffffffffffffffffffffffccccccccccccccccccceeeefffffffccffcfcccfccfccfffccfcffffffffffffffffffffffffffffccccccccccccccffffffffffffffffffffffccccccfffff
                ccccccfffffffffffffffffffffffffffcccccccccfccccccccceeeeffffffffffffffffcffcffcfffffeeeecccffffffffffffffffccccccccccccfcccccccffffffffffffffffffffffffccccfffff
                cccccffffffffffffffffffffffffffffccccccfffffcccccccceeeeffffffffffffffffffcffffffffeeeeeecffccfffffefcccccccccccccccccfcccffcfffffffffffffffffffffffffcfcccfffff
                ccccfcfffffcffffffffffffffffffffffcccccccfffcccccccceebbffffcffffffffffffcfffcfffceeceeeeccfcffffffeeecccccccccccccccccfccccccfffffffffffffffffffffffffcccffffff
                ccccfcfffffcffffffffffffffffffffffcccccccfffcccccccceebbffffcffffffffffffcfffcfffceeceeeeccfcffffffeeecccccccccccccccccfccccccfffffffffffffffffffffffffcccffffff
                ccccfcfffffffffffffffffffffffffffccccccfcfffcccccccceeebffffceeffffffffcccffccebbbbbeeeeecffffffccfcececcccccccccccccccccccccccffffffffffffffffffffffffffccfffff
                cccccffffffffffffffffffffffffffffcccccccffffcccccccceeebffffceeeecfceeebbbbeeeefcbebbbeeeccfffffffffeeeeccccccccccccccccccccfccfcffffffffffffffffffffffffccfffff
                cccccffffffcccfffffffffffffffffffccccccccccffccccccceeebcfffeefcccfcbeebbbbbbbcfcecebbbeeeeffffcffffffcccccccccccccccccccccccccccfffffffffffffffffffffffffffffff
                ccccffffffffcfffffffffffffffffffffccccccccffcccccccceeebefffeeeeeeeebeeebbbbbeeeebbbbbbbeefcffffffcfcfcccccccccccccccccccccccccccccfffffffffffffffffffffffffffff
                ccccffffffffcfffffffffffffffffffffccccccccffcccccccceeeeefffeeebbbbbeeeebeebbebbbbbbeeebeeccfffffffcccccccccccccccccccccccccccccccccffffffffffffffffffffffffffff
                ccccffffffffffffffffffffffffffffffcccccccfffcccccccceebbefffeeebbbbbeeeebbeeeeebbbbbbbbbeeefcfffccffcfcccccccccccccccccccccccccccccfffffffffffffffffffffffffffff
                cccccffffffccfffffffffffffffffffffccccccfcfccccccccceeeebeffeeeeebeeeeeebeebbbbebbbbbbbbeeeeefffeecccfccccccccccccccccccccccccccfffcffffffffffffffffffffffffffff
                ccccfffffffcccffffffffffffffffffffcccccccffffccccccceebbbbffceebbeeeeeebbeebbbeebbbbbbbeeeeeefffccffcccccccccccccccccccccccccccfffffffffffffffffffffffffffffffff
                cccccffffffccffffffffffffffffffffcccccccffcffccccccceeeebbcfceeeeebeeeebbbeedbbebbbbbbbeeeeebcffccfffeefcccccccccccccccccccccccccfffffffffffffffffffffffffffffff
                cccccfffffffcfffffffffffffffffffffcccccccccfcccccccceeebbbeffeeeeeeeeebbbbbebbbbbbbbbbeeeeebbeffffcfccccccccccccccccccccccccccffffffffffffffffffffffffffffffffff
                ccccfffffffcccfffffffffffffffffffccccccccffffcccccceeebbbbbcfeeeeeebebebbebbbbbbbbbbbbbbeebbfcffffcfcfccccccccccccccccccccccccfcffffffffffffffffffffffffffffffff
                ccccffffffffccfffffffffffffffffffccccccccffcfcccccceeebbbbbcfeeeeeebeeeebbbbbbbbbbbbbbbbebbbccffcccfccceeecccccccccccccccccfcccffccfffffffffffffffffffffffffffff
                cccccfffffffccffffffffffffffffffffcccccccffcfccccccceebbbbbbceeeeeeeeeebbbbbbbbbbbbbbbbbbbbeccfccccccceececcccccccccccccccccccffffffffffffffffffffffffffffffffff
                ccccfffffffcccffffffffffffffffffffcccccccffffcccccceeeeebbbbbceeeeeeeebbbdddbbbdbbddddb3bbbccccceeccccceeeccccccccccccccccccffccffffcffffffffffffffffffffffcffff
                ccccffcffffcccffffffffffffffffffffcccccccfffcccccccceebbbbbbbceeeeeebbbdbbdddddddbbddddbbbdcccecccfcecccecccccccccccccccccccccccccccffffffffffffffffffffffcccfff
                ccccfffffffcffffffffffffffffffffffccccccfcffccccccceeeebbbbbbbeeeeebbbeebbbddbbdddddddb3bddcccceeeceeceeeeccccccccccccccccccccccfccccfffffffffffffffffffffcccfff
                ccccfffffffffffffffffffffffffffffccccccccccffcccccceeebbbbbbbbeeeeebbeefbeeceebdddddddbbbbecccceccceeeeeeeccccccccccccccccccccccfcccfcffffffffffffcfffffffccffff
                ccccfffffffffffffffffffffffffffffcccccccccccccccccceeeeeebbbbbbeeeebbeeeeeb3ddddddddbbbbbdeecfcceeeeceeeeeccccccccccccccccccccccccccfffffffffffffcccccfcffccccff
                cccfffffffffffffffffffffffffffffffcccccccccccccccccceeeeeebbbbbcceeebbeebb3ddddddddbbbbbbdcceeeeeecceecccccccccccccccccccccccccccffffcffffffffcfcfccccccffcccfff
                ccccfffffffffffffffffffffffffffffccccccccccccccccccceeeeeeebbbbbbeeeebeebbbbbddddddbbbbbddbceeccccceeeeeeeccccccccccccccccccccccffffcffffffffffcccccccccffccccff
                cccccfcffffffcfffffffffffffffffffccccccccccccccccccceeeeeeebbbbbbbeeeeebbbbbbddddbbbbbbddbdcbbeeeeeeecccccccccccccccccccccccccfcfcccffffffffffffcccccccffccfcfff
                cccccfcffffffcfffffffffffffffffffccccccccccccccccccceeeeeeebbbbbbbeeeeebbbbbbddddbbbbbbddbdcbbeeeeeeecccccccccccccccccccccccccfcfcccffffffffffffcccccccffccfcfff
                cccccffffffffffffffffffffffffffffccccccccccccccccccceeeeeeecbbbbbcfeeeeebbddddddddbbbbdddbdcebfbeeeeeccccccccccccccccccccccccccccffccfccfffffffcccccccccfffccfff
                cccccccffffffffffffffffffffffffffccccccccccccccccccceeeeeeebbbcfffffeeeebbbddddddbbbbbddcddbcecbddeeccccccccccccccccccccccccccccccccfcfcccfffffcccccccccffcccfff
                cccccfffffffffffffffffffffffffffcccccccccccccccccccceeeeeebbeffffccfceeebebbddddbeebbddbedbdceeebbbcccccccccccccccccccccccccccccccccfcccccccffccccccccccffccccff
                cccccccfffffffffffffffffffffffffffccccccccccccccccceeeebebbffffffcffceeeeeebbbeeebbbbbdcbbbdceeeeedcccccccccccccccccccccccccccccccccccccccccfccccccccccffccccfff
                cccccfcffffffffffffffffffffffffffcccccccccfcccccccceeeebbbffffcccccfceeeeeeebbbbbbbbbbccdcbfeebdccbbeeeeeecccccccccccccccccccccccccccccccccccccccccccccffffcccff
                cccccccffffffffffffffffffffffffffcccccccccfcccccccceeebbbcffffcccfcffeeeeeebbbbbbbbbeccbcbdfeebbeeedbbccccccccccccccccccccccccccccccccccccccccccccccccccfffccfff
                cccccccfffffffffffffffffffffffffffccccccccfcccccccceeebbefffcccffffffceeeeeebbbbbeeeeccbcddfbbdebbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccfffcffcff
                cccccffffffffffffffffffffffffffffccccccccfffccccccceeeecfffccffffccfcceeeeebbbbeceeeccecddfcdbbeddebbdbbeecccccccccccccccccccccccccccccccccccccccccccccfffccccff
                ccccffcfffffffffffffffffffffffffffccccccccffccccccfffffffffccccccfcfcceeeeeeebbeeccccccddcfcfbbeeebbbbbbbbbeebbdbbeccccccccccccccccccccccccccccccccccccfffccccff
                cccccfffffffffffffffffffffffffffffcccccccfffccccffffffcffffccccccfcfcceeeeeebeeeececccbddffcebceeebbbebbbebbbbbbbbeecccccccccccccccccccccccccccccccccccfffccccff
                cccccccffffffffffffffffffffffffffccccccfcfffffffffffffffffccccccccffcceeeeeeeeeeeeeccdddcfccebebbbbbbebbbbbbbbbbebbcccccccccccccccccccccccccccccccccccfffffccfff
                cccccfcffffffffffffffffffffffffffcccccccfffffffffcccffffffcccccccfffceeeebbbeeeeeecccfcdcfccfebebbbbeebbebbbbbbebebcccccccccccccccccccccccccccccccccccccffcfffff
                ccccffcffffffffffffffffffffffffffcccccccccfffffffccccffffccecccccfffceeeebbbeeeeeccccffdffcebdebbbebebeebbbbbbbeebbecccccccccccccccccccccccccccccccccccfffcccfff
                cccccffffffffffffffffffffffffffffcccccccfffffffffccccfffcccffccffffccccebbebeeeecccdcffdffedbbbebbbebbbbbbbbbbbebbbbccccccccccccccccccccccccccccccccccccffffffff
                cccccffffffffffffffffffffffffffffccccccccccffffffcecccffccffcbcffffccceebbeeeecceecdcffcfecebebfeeeebbbbebbbebebbebbcccccccccccccccccccccccccccccccccccccfcccfff
                cccccfffffffffffffffffffffffffffffcccccccfcfffffceeecfffccffedcffffcebbbbeeeeceeeccbcffcfbebbbbceeebeebebbbbeebebbeedcccccccccccccccccccccccccccccccccccfcccccff
                cccccfffffffffffffffffffffffffffffccccccccfffffccebeccfcccffebfffffceebbeeeeeeeecffcdffcfdecebbfbbfeebbeeeefcbbbbbbdbbbcccccccccccccccccccccccccccccccccffccccff
                cccccfcfffffffffffffffffffffffffffccccccffffffcfcceeeffccfffcbffffffeeeeeeeeeefffffcbffffebbebbfffcfebbecfcfcfefbbbebfceccccccccccccccccccccccccccccccffffffffff
                cccccfffffffffffffffffffffffffffffccccccffffffffcefbecfccffffbfffffceeeeeecfffffffffcffffeebbbbffffecebbeeebebbebbbbccfcbcccccccccccccccccccccccccccccfffcffffff
                cccccfffffffffffffffffffffffffffffcccccfffffffffcefeecccfffffbfffffffcffffffffffffffcffffeeeebbfffffbcbbcceebbbbbbbdddffeccccccccccccccccccccccccccccfffffffffff
                cccccfffffffffffffffffffffffffffffcccccfffffffffcececfccfffffccffffffcffffffffffffffecfffecbbbffccfffceececeebebbbdbdddceccccccccccccccccccccccccccccfffffffffff
                cccccfffffffffffffffffffffffffffffcccccfffffffffcececfccfffffccffffffcffffffffffffffecfffecbbbffccfffceececeebebbbdbdddceccccccccccccccccccccccccccccfffffffffff
                ccccccffffffffffffffffffffffffffffccccfffffffffcceecfccfffffcfcffffffffffffffffffcfcccffffebebeceeffbffeeeeceeeebdbbddddcbcccccccccccccccccccccccccccfffffffffff
                cccccfffffffffffffffffffffffffffffccccffcffffffccecffccffffbeecffffffffffffffffffcfcceffffdbebceffcfbcfeecceeebbbbdbdddddeccccccccccccccccccccccccccffffffffffff
                cccccfffffffffffffffffffffffffffffccccffcfffffcccebecfcfeffccefffffffffffffffffccccfccfffffeeeebccffbefeeeceebddddddbbdddeccccccccccccccccccccccccccffffffffffff
                cccccfffffffffffffffffffffffffffffcccccfffffffffcebffffebffcecffffffffffcfffcececccffcfffffeecebcccfbeecccceecdddbbbdbddddcccccccccccccccccccccccccccfffffffffff
                ccccccffffffffffffffffffffffffffffccccffcffffffccebffffbbffceeffffcceeeeeeeeeeccccccccfffffefeceeecfbcecccceecdddbbddbddddccccccccccccccccccccccccccffffffffffff
                cccccfffffffffffffffffffffffffffffccccffffffffffceeffffbbffceccfffceeeeeeeeeecccccccccffffccfeeceecfeecccfbecbdbbbbdbddbdddccccccccccccccccccccccccccfffffffffff
                cccccfffffffffffffffffffffffffffffccffffffffffffceccfffbeffceecfffceeeeeeeceeccccccccffffcffceeeeeecceccefeebddbbdbdbbbbdddcccccccccccccccccccccccccffffffffffff
                cccfcfffffffffffffffffffffffffffffccccfffffffffffcccfffceffceecccfceeeeeeeeececccccccffceccccfebcceffeccfcbbbdbbbbbbbbbbddddcccccccccccccccccccccccccfffffffffff
                ccccffffffffffffffffffffffffffffffcfccfffffffffffcccfffcfffceecccfceeeeeeecefeeccccccffebecceeebcceefecffeebbbbbbbbdbdbdddddcccccccccccccccccccccccccfffffffffff
                cccccfffffffffffffffffffffffffffffccccccffffffffffccfffefffeeccccfceeeeeeeeccfcccccccffeeecceeeecceefffffecbbbbbbbbbbdbbddddcccccccccccccccccccccccccfffffffffff
                ccffffffffffffffffffffffffffffffffccccccfffffffffffcfffefcfeeccccfceeeeeecccecccfccbcfceeeeccebbcccccfffcfcbbbbbbbbbbbbbdddddccccccccccccccccccccccccfffffffffff
                cccfffffffffffffffffffffffffffffffffcccfcffffffffffffffeffceecceecfeeeeeceefecccccbcffceeefeceeeffcccffffccbcbbbbbbbbbbbdbbddccccccccccccccccccccccccfffffffffff
                ccccfffffffffffffffffffffffffffffcffcfcfcfffffffffffffffffbeccceeefeeeeececcfcccccbfcfcccefeeeebffcccfffcfccbbbbbbbbbbbbbbbbdccccccccccccccccccccccccfffffffffff
                ccffffffffffffffffffffffffffffffcffffccfffffffffffffffcfffeecceeecfeeeceeececccfcbcccfbffecceeebffcccfffccccbbbbbbbbbbbbbbbbbcccccccccccccccccfccccccfffffffffff
                ccfffffffffffffffffffffffffffffffffffffffcffffffffffffcffceeeeeeeeceeeeecccecccccdccccbcfeecfeeeffcfcffffccccbbccbbbbbbbbbbbbdcccccccccccccccccccccccfffffffffff
                ccffffffffffffffffffffffffffffffffffcffcffffffffffffffcffceeeeeeeefeeeeeecceccccecccfcecceeffceeffcfccfcccccccbbbbbbbbbbbbbbbbcccccccccccccccccccccccfffffffffff
                cfffffffffffffffffffffffffffffffffffffffffffffffffffffeffceeeeeeeeceeeeeefeecccfbcccfcefffefeceeffcffcfccfccccccbbbbbbbbbbbbbbcccccccccccccccccccccccfffffffffff
                ccfffffffffffffffffffffffffffffffffffffffffffffffffcffcffeeeccccccceeeecececfcccbcccfcecfceeefeeeeccfcfffccccbbbbbbbbbbbbbbbbbccccccccccccfcccfcccccffffffffffff
                ccfffffffffffffffffffffffffffffffffffffcffffffffffcffcffceeeccccccfeeeeeecefccfcbbccfccffeeeefeeeeccfffffcccccbbbbcbbcbbbcbbbbcccccccccccccccfcccccccfffffffffff
                cffffffffffffffffffffffffffffffffffffffffffffffffffffcffccccccccccfceccccfefcccbbccffccffeceeceeeefecfffccccccbbbbccbcbbbcbbbbccccccccccccffcfcccccccfffffffffff
                cfffffffffffffffffffffffffffffffffffffffffffffffffcfccfffcccccccccfccccccfefcccfcbcffcfffcccccceeefefffffccccccccbccccbbccbbbbccccccffccffffcffccccccfffffffffff
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................
                ................................................................................................................................................................"""))
    story.print_dialog("Alex Byte, un joven inventor, sobrevive usando su ingenio y", 80, 90, 50, 150)
    story.print_dialog("un Micro:bit modificado, capaz de guiarse y comunicarse con él.", 80, 90, 50, 150)
    story.print_dialog("Con el mundo al borde del colapso, Alex debe abrirse paso entre hordas de zombis", 80, 90, 50, 150)
    story.print_dialog("para llegar al último refugio humano donde poder estar a salvo.", 80, 90, 50, 150)
    story.print_dialog("¿Podrá salvarse y encontrar una cura?", 80, 90, 50, 150)
    
def create_skip_lore_sprite():
    global skip_lore_sprite
    skip_lore_sprite = textsprite.create("Apreta A para skipear lore")
    skip_lore_sprite.set_outline(0.2, 1)
    skip_lore_sprite.set_position(80, 110)
    
def zombie_cutscene():
    global skip_lore_sprite
    sprites.destroy(skip_lore_sprite)
    open_zombie_screen()
    story.start_cutscene(stats_cutscene)

# Pantalla de juego
def open_zombie_screen():
    initialize_game_data()
    gamer()

def initialize_game_data():
    scene.set_background_image(assets.image("""
            cityscape
        """))
    global on_zombie_screen, on_menu, ypos_zombie_sprite, player_level, on_lore_screen, skip_lore_sprite, exp_status_bar, player_exp, player_exp_required
    on_zombie_screen = True
    on_menu = False
    on_lore_screen = False
    player_level = 1
    create_player()
    story.sprite_say_text(player_sprite, "ostras pedrin")
    sprites.destroy(skip_lore_sprite)
    set_player_stats(player_level)
    set_zombie_stats(player_level)
    exp_status_bar = statusbars.create(20, 4, StatusBarKind.Energy)
    exp_status_bar.position_direction(CollisionDirection.TOP)
    controller.move_sprite(player_sprite)
    player_sprite.set_stay_in_screen(True)
    effects.star_field.start_screen_effect()
    scroller.set_camera_scrolling_multipliers(1, 0)
    game.on_update(on_on_update)
    info.set_life(3)

# Funcion recursiva para crear zombies en funcion del nivel
def gamer():
    global delay_min_enemies, delay_max_enemies, player_exp, player_exp_required, player_hp
    update_exp_status_bar()
    while player_exp < player_exp_required and info.life() > 0:
        if (on_stats_screen):
            return
        pause(randint(delay_min_enemies, delay_max_enemies))

        destroy_zombies()
        destroy_bullets()
        if player_exp < player_exp_required and info.life() > 0:
            create_zombie()
        else:
            next_level()

def next_level():
    global player_level, player_exp
    if (info.life() > 0):
        player_level += 1
    if (player_level == 11): # Caso base 1
        game_over()
        return
    if (info.life() == 0): # Caso base 2
        game_over()
        return
    player_exp = 0
    update_exp_status_bar()
    set_zombie_stats(player_level)
    set_player_stats(player_level)
    game.splash("Level Up! - " + player_level)
    destroy_all_zombies()
    destroy_all_bullets()
    gamer()

def set_player_stats(level: int):
    global player_hp, player_power, player_speed, player_exp_required, stat_lifes_won, player_exp_punish
    if info.life() < 3:
        info.change_life_by(+1)
        stat_lifes_won += 1

    stats = {
        "hp": 100 + (level - 1) * 50,
        "power": 50 + (level - 1) * 10,
        "speed": 200 + (level - 1) * 10,
        "exp_required": 100 * level,
        "exp_punish": level
    }

    player_hp = stats["hp"]
    player_power = stats["power"]
    player_speed = stats["speed"]
    player_exp_required = stats["exp_required"]
    player_exp_punish = stats["exp_punish"]


def set_zombie_stats(level: int):
    global zombie_hp, zombie_power, zombie_speed, delay_min_enemies, delay_max_enemies
    global zombie_xp_reward, zombie_stun_speed, zombie_stun_duration

    stats = {
        "hp": 100 + (level - 1) * 50,
        "power": 50 + (level - 1) * 10,
        "speed": 35 + (level - 1) * 5,
        "delay_min": max(1000 - (level - 1) * 100, 100),
        "delay_max": max(1500 - (level - 1) * 100, 600),
        "xp_reward": 50,
        "stun_duration": max(2000 - (level - 1) * 200, 200),
        "stun_speed": 10 + (level - 1) * 2
    }

    zombie_hp = stats["hp"]
    zombie_power = stats["power"]
    zombie_speed = stats["speed"]
    delay_min_enemies = stats["delay_min"]
    delay_max_enemies = stats["delay_max"]
    zombie_xp_reward = stats["xp_reward"]
    zombie_stun_duration = stats["stun_duration"]
    zombie_stun_speed = stats["stun_speed"]


def destroy_bullets():
    global bullet_list
    global player_sprite
    for b in bullet_list:
        if b.sprite.x < LEFT_BOUNDARY + player_sprite.x or b.sprite.x > RIGHT_BOUNDARY + player_sprite.x or b.sprite.y > BOTTOM_BOUNDARY + player_sprite.y or b.sprite.y < TOP_BOUNDARY + player_sprite.y:
            sprites.destroy(b.sprite)

def destroy_zombies():
    global zombie_list, player_sprite, player_exp, deleted_zombies_list, player_exp_punish, stat_zombies_escaped
    for z in zombie_list:
        if z.sprite.x < LEFT_BOUNDARY and z not in deleted_zombies_list:
            sprites.destroy(z.sprite, effects.disintegrate)
            if (player_exp > 0):
                player_exp -= player_exp_punish
                if (player_exp < 0):
                    player_exp = 0
            deleted_zombies_list.append(z)
            stat_zombies_escaped+=1
            update_exp_status_bar()


def destroy_all_zombies():
    global zombie_list
    global player_sprite
    for z in zombie_list:
        sprites.destroy(z.sprite)

def destroy_all_bullets():
    global bullet_list
    global player_sprite
    for b in bullet_list:
        sprites.destroy(b.sprite)

def update_exp_status_bar():
    global player_exp_required, player_exp, exp_status_bar
    exp_status_bar.max = player_exp_required
    exp_status_bar.value = player_exp
    exp_status_bar.set_label("EXP: "+ player_exp + "/" + player_exp_required)

def game_over():
    global on_stats_screen
    on_stats_screen = True
    story.start_cutscene(stats_cutscene)

def stats_cutscene():
    stats_screen()
    game.over()

def stats_screen():
    global player_level, on_stats_screen
    stat_missed_shots = stat_shots - stat_accurate_shots
    stat_precission = (stat_accurate_shots / stat_shots) * 100 if stat_shots > 0 else 0
    story.set_page_pause_length(0, 1000)
    if (player_level >= 11):
        game.splash("Game Over", "You have reached the max level!")
    else:
        game.splash("Game Over", "You died")
    story.print_dialog("Balas disparadas: " + str(stat_shots), 80, 90, 50, 150)
    story.print_dialog("Balas acertadas: " + str(stat_accurate_shots), 80, 90, 50, 150)
    story.print_dialog("Precisión: " + str(stat_precission) + "%", 80, 90, 50, 150)
    story.print_dialog("Zombis eliminados: " + str(stat_zombies_killed), 80, 90, 50, 150)
    story.print_dialog("Zombis que escaparon: " + str(stat_zombies_escaped), 80, 90, 50, 150)
    story.print_dialog("Daño infligido: " + str(stat_damage_dealt), 80, 90, 50, 150)
    story.print_dialog("Vidas ganadas: " + str(stat_lifes_won), 80, 90, 50, 150)
    story.print_dialog("Vidas perdidas: " + str(stat_lifes_lost), 80, 90, 50, 150)

    if player_level == 11:
        story.print_dialog("¡Felicidades, Alex! Has alcanzado el refugio humano.", 80, 90, 50, 150)
        story.print_dialog("Gracias a tu ingenio, los supervivientes ahora tienen una oportunidad.", 80, 90, 50, 150)
        story.print_dialog("Con tu Micro:bit, comenzará la investigación para encontrar una cura.", 80, 90, 50, 150)
        story.print_dialog("El destino de la humanidad está en buenas manos.", 80, 90, 50, 150)
    else:
        story.print_dialog("Alex ha caído en su lucha contra las hordas de zombis.", 80, 90, 50, 150)
        story.print_dialog("Aunque su esfuerzo fue valiente, los zombis han tomado el control.", 80, 90, 50, 150)
        story.print_dialog("El refugio humano sigue siendo un sueño distante...", 80, 90, 50, 150)
        story.print_dialog("¿Podrá la humanidad encontrar una nueva esperanza?", 80, 90, 50, 150)

# Eventos
def on_projectile_collision(bullet, zombie):
    global player_power, zombie_hp, player_exp, zombie_xp_reward, zombie_stun_speed, zombie_stun_duration, stat_accurate_shots, stat_damage_dealt
    stat_accurate_shots+=1
    stat_damage_dealt+=player_power
    animate_bullet_collision(bullet)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, zombie).value += -player_power
    zombie.set_velocity(-zombie_stun_speed, 0)
    pause(zombie_stun_duration)
    zombie.set_velocity(-zombie_speed, 0)
sprites.on_overlap(SpriteKind.projectile,SpriteKind.enemy,on_projectile_collision)

def on_player_collision_with_enemy(player, zombie):
    global zombie_power, player_hp, stat_lifes_lost
    info.change_life_by(-1)
    stat_lifes_lost+=1
    zombie.destroy()
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player,SpriteKind.enemy,on_player_collision_with_enemy)

def on_zombie_life_zero(status):
    global player_exp, zombie_xp_reward, stat_zombies_killed
    status.sprite_attached_to().destroy(effects.disintegrate)
    stat_zombies_killed+=1
    player_exp += zombie_xp_reward
    update_exp_status_bar()
statusbars.on_zero(StatusBarKind.enemy_health, on_zombie_life_zero)

def on_life_zero():
    game_over()
info.on_life_zero(on_life_zero)


def create_player():
    global player_sprite, direction
    player_sprite = sprites.create(img("""
            . . . . . . f f f f f f . . . .
                                        . . . . f f e e e e f 2 f . . .
                                        . . . f f e e e e f 2 2 2 f . .
                                        . . . f e e e f f e e e e f . .
                                        . . . f f f f e e 2 2 2 2 e f .
                                        . . . f e 2 2 2 f f f f e 2 f .
                                        . . f f f f f f f e e e f f f .
                                        . . f f e 4 4 e b f 4 4 e e f .
                                        . . f e e 4 d 4 1 f d d e f . .
                                        . . . f e e e 4 d d d d f . . .
                                        . . . . f f e e 4 4 4 e f . . .
                                        . . . . . 4 d d e 2 2 2 f . . .
                                        . . . . . e d d e 2 2 2 f . . .
                                        . . . . . f e e f 4 5 5 f . . .
                                        . . . . . . f f f f f f . . . .
                                        . . . . . . . f f f . . . . . .
        """),
        SpriteKind.player)
    player_sprite.set_position(10, 60)
    player_sprite.set_velocity(player_speed, 0)
    direction = "right"

def create_zombie():
    global zombie_hp, zombie_sprite, ypos_zombie_sprite, statusbar
    ypos_zombie_sprite = randint(10, 110)
    zombie_sprite = sprites.create(img("""
            . . . . . . . c c c . . . . . .
                                        . . . . . . c b 5 c . . . . . .
                                        . . . . c c c 5 5 c c c . . . .
                                        . . c c b c 5 5 5 5 c c c c . .
                                        . c b b 5 b 5 5 5 5 b 5 b b c .
                                        . c b 5 5 b b 5 5 b b 5 5 b c .
                                        . . f 5 5 5 b b b b 5 5 5 c . .
                                        . . f f 5 5 5 5 5 5 5 5 f f . .
                                        . . f f f b f e e f b f f f . .
                                        . . f f f 1 f b b f 1 f f f . .
                                        . . . f f b b b b b b f f . . .
                                        . . . e e f e e e e f e e . . .
                                        . . e b c b 5 b b 5 b f b e . .
                                        . . e e f 5 5 5 5 5 5 f e e . .
                                        . . . . c b 5 5 5 5 b c . . . .
                                        . . . . . f f f f f f . . . . .
        """),
        SpriteKind.enemy)
    zombie_sprite.set_position(player_sprite.x + RIGHT_BOUNDARY, ypos_zombie_sprite)
    animation.run_image_animation(zombie_sprite,
        [img("""
                . . . . . . . c c . . . . . . .
                                            . . . . . . c 5 c . . . . . . .
                                            . . . . c c 5 5 5 c c c . . . .
                                            . . c c c c 5 5 5 5 c b c c . .
                                            . c b b 5 b 5 5 5 5 b 5 b b c .
                                            . c b 5 5 b b 5 5 b b 5 5 b c .
                                            . . c 5 5 5 b b b b 5 5 5 f . .
                                            . . . f 5 5 5 5 5 5 5 5 f f . .
                                            . . . . f e e e f b e e f f . .
                                            . . . . f e b b f 1 b f f f . .
                                            . . . . f b b b b b b f f . . .
                                            . . . . . f e e e e f e e . . .
                                            . . . . . f 5 b b e b b e . . .
                                            . . . . f 5 5 5 5 e b b e . . .
                                            . . . . c b 5 5 5 5 e e . . . .
                                            . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . .
                                            . . . . . . . c c . . . . . . .
                                            . . . . . . c c 5 c . . . . . .
                                            . . . . c c 5 5 5 c c c . . . .
                                            . . c c c c 5 5 5 5 c b c c . .
                                            . c b b 5 b 5 5 5 5 b 5 b b c .
                                            . c b 5 5 b b 5 5 b b 5 5 b c .
                                            . . c 5 5 5 b b b b 5 5 5 f . .
                                            . . . f 5 5 5 5 5 5 5 5 f f . .
                                            . . . . f e e e f b e e f f . .
                                            . . . . f e b b f 1 b f f f . .
                                            . . . . f b b b b e e f f . . .
                                            . . . . . f e e e b b e f . . .
                                            . . . . f 5 b b e b b e . . . .
                                            . . . . c 5 5 5 5 e e f . . . .
                                            . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . c c . . . . . . .
                                            . . . . . . c 5 c . . . . . . .
                                            . . . . c c 5 5 5 c c c . . . .
                                            . . c c c c 5 5 5 5 c b c c . .
                                            . c b b 5 b 5 5 5 5 b 5 b b c .
                                            . c b 5 5 b b 5 5 b b 5 5 b c .
                                            . . c 5 5 5 b b b b 5 5 5 f . .
                                            . . . f 5 5 5 5 5 5 5 5 f f . .
                                            . . . . f e e e f b e e f f . .
                                            . . . . f e b b f 1 b f f f . .
                                            . . . . f b b b b b b f f . . .
                                            . . . . . f e e e e f e e . . .
                                            . . . . . f 5 b b e b b e . . .
                                            . . . . f 5 5 5 5 e b b e . . .
                                            . . . . c b 5 5 5 5 e e . . . .
                                            . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . .
                                            . . . . . . . c c . . . . . . .
                                            . . . . . . c c 5 c . . . . . .
                                            . . . . c c 5 5 5 c c c . . . .
                                            . . c c c c 5 5 5 5 c b c c . .
                                            . c b b 5 b 5 5 5 5 b 5 b b c .
                                            . c b 5 5 b b 5 5 b b 5 5 b c .
                                            . . c 5 5 5 b b b b 5 5 5 f . .
                                            . . . f 5 5 5 5 5 5 5 5 f f . .
                                            . . . . f e e e f b e e f f . .
                                            . . . . f e b b f 1 b f f f . .
                                            . . . . f b b b b b b f f . . .
                                            . . . . . f e e e e e b b e . .
                                            . . . . f 5 5 b b b e b b e . .
                                            . . . . c 5 5 5 5 5 e e e . . .
                                            . . . . . f f f f f f . . . . .
            """)],
        100,
        True)
    zombie_sprite.set_velocity(-zombie_speed, 0)
    zombie_list.push(Zombie(zombie_sprite, zombie_list.length +1))
    statusbar = statusbars.create(16, 2, StatusBarKind.enemy_health)
    statusbar.set_label("HP")
    statusbar.max = zombie_hp
    statusbar.value = zombie_hp
    statusbar.attachToSprite(zombie_sprite)
# Controls
# Player movement
# Up

def on_up_pressed():
    global direction
    if on_menu:
        pass
    else:
        animation.stop_animation(animation.AnimationTypes.All, player_sprite)
        animation.run_image_animation(player_sprite,
            [img("""
                    . . . . . . f f f f . . . . . .
                                                . . . . f f e e e e f f . . . .
                                                . . . f e e e f f e e e f . . .
                                                . . f f f f f 2 2 f f f f f . .
                                                . . f f e 2 e 2 2 e 2 e f f . .
                                                . . f e 2 f 2 f f 2 f 2 e f . .
                                                . . f f f 2 2 e e 2 2 f f f . .
                                                . f f e f 2 f e e f 2 f e f f .
                                                . f e e f f e e e e f e e e f .
                                                . . f e e e e e e e e e e f . .
                                                . . . f e e e e e e e e f . . .
                                                . . e 4 f f f f f f f f 4 e . .
                                                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                                                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                                                . . . . . f f f f f f . . . . .
                                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                                . . . . . . f f f f . . . . . .
                                                . . . . f f e e e e f f . . . .
                                                . . . f e e e f f e e e f . . .
                                                . . . f f f f 2 2 f f f f . . .
                                                . . f f e 2 e 2 2 e 2 e f f . .
                                                . . f e 2 f 2 f f f 2 f e f . .
                                                . . f f f 2 f e e 2 2 f f f . .
                                                . . f e 2 f f e e 2 f e e f . .
                                                . f f e f f e e e f e e e f f .
                                                . f f e e e e e e e e e e f f .
                                                . . . f e e e e e e e e f . . .
                                                . . . e f f f f f f f f 4 e . .
                                                . . . 4 f 2 2 2 2 2 e d d 4 . .
                                                . . . e f f f f f f e e 4 . . .
                                                . . . . f f f . . . . . . . . .
                """),
                img("""
                    . . . . . . f f f f . . . . . .
                                                . . . . f f e e e e f f . . . .
                                                . . . f e e e f f e e e f . . .
                                                . . f f f f f 2 2 f f f f f . .
                                                . . f f e 2 e 2 2 e 2 e f f . .
                                                . . f e 2 f 2 f f 2 f 2 e f . .
                                                . . f f f 2 2 e e 2 2 f f f . .
                                                . f f e f 2 f e e f 2 f e f f .
                                                . f e e f f e e e e f e e e f .
                                                . . f e e e e e e e e e e f . .
                                                . . . f e e e e e e e e f . . .
                                                . . e 4 f f f f f f f f 4 e . .
                                                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                                                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                                                . . . . . f f f f f f . . . . .
                                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                                . . . . . . f f f f . . . . . .
                                                . . . . f f e e e e f f . . . .
                                                . . . f e e e f f e e e f . . .
                                                . . . f f f f 2 2 f f f f . . .
                                                . . f f e 2 e 2 2 e 2 e f f . .
                                                . . f e f 2 f f f 2 f 2 e f . .
                                                . . f f f 2 2 e e f 2 f f f . .
                                                . . f e e f 2 e e f f 2 e f . .
                                                . f f e e e f e e e f f e f f .
                                                . f f e e e e e e e e e e f f .
                                                . . . f e e e e e e e e f . . .
                                                . . e 4 f f f f f f f f e . . .
                                                . . 4 d d e 2 2 2 2 2 f 4 . . .
                                                . . . 4 e e f f f f f f e . . .
                                                . . . . . . . . . f f f . . . .
                """)],
            200,
            True)
        direction = "up"
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

# Left

def on_left_pressed():
    global direction
    if on_menu:
        pass
    else:
        animation.stop_animation(animation.AnimationTypes.All, player_sprite)
        animation.run_image_animation(player_sprite,
            [img("""
                    . . . . f f f f f f . . . . . .
                                                . . . f 2 f e e e e f f . . . .
                                                . . f 2 2 2 f e e e e f f . . .
                                                . . f e e e e f f e e e f . . .
                                                . f e 2 2 2 2 e e f f f f . . .
                                                . f 2 e f f f f 2 2 2 e f . . .
                                                . f f f e e e f f f f f f f . .
                                                . f e e 4 4 f b e 4 4 e f f . .
                                                . . f e d d f 1 4 d 4 e e f . .
                                                . . . f d d d d 4 e e e f . . .
                                                . . . f e 4 4 4 e e f f . . . .
                                                . . . f 2 2 2 e d d 4 . . . . .
                                                . . . f 2 2 2 e d d e . . . . .
                                                . . . f 5 5 4 f e e f . . . . .
                                                . . . . f f f f f f . . . . . .
                                                . . . . . . f f f . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                                . . . . f f f f f f . . . . . .
                                                . . . f 2 f e e e e f f . . . .
                                                . . f 2 2 2 f e e e e f f . . .
                                                . . f e e e e f f e e e f . . .
                                                . f e 2 2 2 2 e e f f f f . . .
                                                . f 2 e f f f f 2 2 2 e f . . .
                                                . f f f e e e f f f f f f f . .
                                                . f e e 4 4 f b e 4 4 e f f . .
                                                . . f e d d f 1 4 d 4 e e f . .
                                                . . . f d d d e e e e e f . . .
                                                . . . f e 4 e d d 4 f . . . . .
                                                . . . f 2 2 e d d e f . . . . .
                                                . . f f 5 5 f e e f f f . . . .
                                                . . f f f f f f f f f f . . . .
                                                . . . f f f . . . f f . . . . .
                """),
                img("""
                    . . . . f f f f f f . . . . . .
                                                . . . f 2 f e e e e f f . . . .
                                                . . f 2 2 2 f e e e e f f . . .
                                                . . f e e e e f f e e e f . . .
                                                . f e 2 2 2 2 e e f f f f . . .
                                                . f 2 e f f f f 2 2 2 e f . . .
                                                . f f f e e e f f f f f f f . .
                                                . f e e 4 4 f b e 4 4 e f f . .
                                                . . f e d d f 1 4 d 4 e e f . .
                                                . . . f d d d d 4 e e e f . . .
                                                . . . f e 4 4 4 e e f f . . . .
                                                . . . f 2 2 2 e d d 4 . . . . .
                                                . . . f 2 2 2 e d d e . . . . .
                                                . . . f 5 5 4 f e e f . . . . .
                                                . . . . f f f f f f . . . . . .
                                                . . . . . . f f f . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                                . . . . f f f f f f . . . . . .
                                                . . . f 2 f e e e e f f . . . .
                                                . . f 2 2 2 f e e e e f f . . .
                                                . . f e e e e f f e e e f . . .
                                                . f e 2 2 2 2 e e f f f f . . .
                                                . f 2 e f f f f 2 2 2 e f . . .
                                                . f f f e e e f f f f f f f . .
                                                . f e e 4 4 f b e 4 4 e f f . .
                                                . . f e d d f 1 4 d 4 e e f . .
                                                . . . f d d d d 4 e e e f . . .
                                                . . . f e 4 4 4 e d d 4 . . . .
                                                . . . f 2 2 2 2 e d d e . . . .
                                                . . f f 5 5 4 4 f e e f . . . .
                                                . . f f f f f f f f f f . . . .
                                                . . . f f f . . . f f . . . . .
                """)],
            200,
            True)
        direction = "left"
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

# Right

def on_right_pressed():
    global direction
    if on_menu:
        pass
    else:
        animation.stop_animation(animation.AnimationTypes.All, player_sprite)
        animation.run_image_animation(player_sprite,
            [img("""
                    . . . . . . f f f f f f . . . .
                                                . . . . f f e e e e f 2 f . . .
                                                . . . f f e e e e f 2 2 2 f . .
                                                . . . f e e e f f e e e e f . .
                                                . . . f f f f e e 2 2 2 2 e f .
                                                . . . f e 2 2 2 f f f f e 2 f .
                                                . . f f f f f f f e e e f f f .
                                                . . f f e 4 4 e b f 4 4 e e f .
                                                . . f e e 4 d 4 1 f d d e f . .
                                                . . . f e e e 4 d d d d f . . .
                                                . . . . f f e e 4 4 4 e f . . .
                                                . . . . . 4 d d e 2 2 2 f . . .
                                                . . . . . e d d e 2 2 2 f . . .
                                                . . . . . f e e f 4 5 5 f . . .
                                                . . . . . . f f f f f f . . . .
                                                . . . . . . . f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                                . . . . . . f f f f f f . . . .
                                                . . . . f f e e e e f 2 f . . .
                                                . . . f f e e e e f 2 2 2 f . .
                                                . . . f e e e f f e e e e f . .
                                                . . . f f f f e e 2 2 2 2 e f .
                                                . . . f e 2 2 2 f f f f e 2 f .
                                                . . f f f f f f f e e e f f f .
                                                . . f f e 4 4 e b f 4 4 e e f .
                                                . . f e e 4 d 4 1 f d d e f . .
                                                . . . f e e e e e d d d f . . .
                                                . . . . . f 4 d d e 4 e f . . .
                                                . . . . . f e d d e 2 2 f . . .
                                                . . . . f f f e e f 5 5 f f . .
                                                . . . . f f f f f f f f f f . .
                                                . . . . . f f . . . f f f . . .
                """),
                img("""
                    . . . . . . f f f f f f . . . .
                                                . . . . f f e e e e f 2 f . . .
                                                . . . f f e e e e f 2 2 2 f . .
                                                . . . f e e e f f e e e e f . .
                                                . . . f f f f e e 2 2 2 2 e f .
                                                . . . f e 2 2 2 f f f f e 2 f .
                                                . . f f f f f f f e e e f f f .
                                                . . f f e 4 4 e b f 4 4 e e f .
                                                . . f e e 4 d 4 1 f d d e f . .
                                                . . . f e e e 4 d d d d f . . .
                                                . . . . f f e e 4 4 4 e f . . .
                                                . . . . . 4 d d e 2 2 2 f . . .
                                                . . . . . e d d e 2 2 2 f . . .
                                                . . . . . f e e f 4 5 5 f . . .
                                                . . . . . . f f f f f f . . . .
                                                . . . . . . . f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                                . . . . . . f f f f f f . . . .
                                                . . . . f f e e e e f 2 f . . .
                                                . . . f f e e e e f 2 2 2 f . .
                                                . . . f e e e f f e e e e f . .
                                                . . . f f f f e e 2 2 2 2 e f .
                                                . . . f e 2 2 2 f f f f e 2 f .
                                                . . f f f f f f f e e e f f f .
                                                . . f f e 4 4 e b f 4 4 e e f .
                                                . . f e e 4 d 4 1 f d d e f . .
                                                . . . f e e e 4 d d d d f . . .
                                                . . . . 4 d d e 4 4 4 e f . . .
                                                . . . . e d d e 2 2 2 2 f . . .
                                                . . . . f e e f 4 4 5 5 f f . .
                                                . . . . f f f f f f f f f f . .
                                                . . . . . f f . . . f f f . . .
                """)],
            200,
            True)
        direction = "right"
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

# Down

def on_down_pressed():
    global direction
    if on_menu:
        pass
    else:
        animation.stop_animation(animation.AnimationTypes.All, player_sprite)
        animation.run_image_animation(player_sprite,
            [img("""
                    . . . . . . f f f f . . . . . .
                                                . . . . f f f 2 2 f f f . . . .
                                                . . . f f f 2 2 2 2 f f f . . .
                                                . . f f f e e e e e e f f f . .
                                                . . f f e 2 2 2 2 2 2 e e f . .
                                                . . f e 2 f f f f f f 2 e f . .
                                                . . f f f f e e e e f f f f . .
                                                . f f e f b f 4 4 f b f e f f .
                                                . f e e 4 1 f d d f 1 4 e e f .
                                                . . f e e d d d d d d e e f . .
                                                . . . f e e 4 4 4 4 e e f . . .
                                                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                                                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                                                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                                                . . . . . f f f f f f . . . . .
                                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                                . . . . . . f f f f . . . . . .
                                                . . . . f f f 2 2 f f f . . . .
                                                . . . f f f 2 2 2 2 f f f . . .
                                                . . f f f e e e e e e f f f . .
                                                . . f f e 2 2 2 2 2 2 e e f . .
                                                . f f e 2 f f f f f f 2 e f f .
                                                . f f f f f e e e e f f f f f .
                                                . . f e f b f 4 4 f b f e f . .
                                                . . f e 4 1 f d d f 1 4 e f . .
                                                . . . f e 4 d d d d 4 e f e . .
                                                . . f e f 2 2 2 2 e d d 4 e . .
                                                . . e 4 f 2 2 2 2 e d d e . . .
                                                . . . . f 4 4 5 5 f e e . . . .
                                                . . . . f f f f f f f . . . . .
                                                . . . . f f f . . . . . . . . .
                """),
                img("""
                    . . . . . . f f f f . . . . . .
                                                . . . . f f f 2 2 f f f . . . .
                                                . . . f f f 2 2 2 2 f f f . . .
                                                . . f f f e e e e e e f f f . .
                                                . . f f e 2 2 2 2 2 2 e e f . .
                                                . . f e 2 f f f f f f 2 e f . .
                                                . . f f f f e e e e f f f f . .
                                                . f f e f b f 4 4 f b f e f f .
                                                . f e e 4 1 f d d f 1 4 e e f .
                                                . . f e e d d d d d d e e f . .
                                                . . . f e e 4 4 4 4 e e f . . .
                                                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                                                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                                                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                                                . . . . . f f f f f f . . . . .
                                                . . . . . f f . . f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . .
                                                . . . . . . f f f f . . . . . .
                                                . . . . f f f 2 2 f f f . . . .
                                                . . . f f f 2 2 2 2 f f f . . .
                                                . . f f f e e e e e e f f f . .
                                                . . f e e 2 2 2 2 2 2 e f f . .
                                                . f f e 2 f f f f f f 2 e f f .
                                                . f f f f f e e e e f f f f f .
                                                . . f e f b f 4 4 f b f e f . .
                                                . . f e 4 1 f d d f 1 4 e f . .
                                                . . e f e 4 d d d d 4 e f . . .
                                                . . e 4 d d e 2 2 2 2 f e f . .
                                                . . . e d d e 2 2 2 2 f 4 e . .
                                                . . . . e e f 5 5 4 4 f . . . .
                                                . . . . . f f f f f f f . . . .
                                                . . . . . . . . . f f f . . . .
                """)],
            200,
            True)
        direction = "down"
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

# Released
# Right

def on_right_released():
    if on_menu:
            pass
    else:
        animation.stop_animation(animation.AnimationTypes.All, player_sprite)
        animation.run_image_animation(player_sprite, [img("""
        . . . . . . f f f f f f . . . .
                            . . . . f f e e e e f 2 f . . .
                            . . . f f e e e e f 2 2 2 f . .
                            . . . f e e e f f e e e e f . .
                            . . . f f f f e e 2 2 2 2 e f .
                            . . . f e 2 2 2 f f f f e 2 f .
                            . . f f f f f f f e e e f f f .
                            . . f f e 4 4 e b f 4 4 e e f .
                            . . f e e 4 d 4 1 f d d e f . .
                            . . . f e e e 4 d d d d f . . .
                            . . . . f f e e 4 4 4 e f . . .
                            . . . . . 4 d d e 2 2 2 f . . .
                            . . . . . e d d e 2 2 2 f . . .
                            . . . . . f e e f 4 5 5 f . . .
                            . . . . . . f f f f f f . . . .
                            . . . . . . . f f f . . . . . .
            """)], 100, False)
controller.right.onEvent(ControllerButtonEvent.Released, on_right_released)

# Left
def on_left_released():
    if on_menu:
        pass
    else:
        animation.stop_animation(animation.AnimationTypes.All, player_sprite)
        animation.run_image_animation(player_sprite, [img("""
        . . . . f f f f f f . . . . . .
                            . . . f 2 f e e e e f f . . . .
                            . . f 2 2 2 f e e e e f f . . .
                            . . f e e e e f f e e e f . . .
                            . f e 2 2 2 2 e e f f f f . . .
                            . f 2 e f f f f 2 2 2 e f . . .
                            . f f f e e e f f f f f f f . .
                            . f e e 4 4 f b e 4 4 e f f . .
                            . . f e d d f 1 4 d 4 e e f . .
                            . . . f d d d d 4 e e e f . . .
                            . . . f e 4 4 4 e e f f . . . .
                            . . . f 2 2 2 e d d 4 . . . . .
                            . . . f 2 2 2 e d d e . . . . .
                            . . . f 5 5 4 f e e f . . . . .
                            . . . . f f f f f f . . . . . .
                            . . . . . . f f f . . . . . . .
            """)], 100, False)
    controller.left.onEvent(ControllerButtonEvent.Released, on_left_released)

# Up
def on_up_released():
    if on_menu:
        pass
    else:
        animation.stop_animation(animation.AnimationTypes.All, player_sprite)
        animation.run_image_animation(player_sprite, [img("""
        . . . . . . f f f f . . . . . .
                            . . . . f f e e e e f f . . . .
                            . . . f e e e f f e e e f . . .
                            . . f f f f f 2 2 f f f f f . .
                            . . f f e 2 e 2 2 e 2 e f f . .
                            . . f e 2 f 2 f f 2 f 2 e f . .
                            . . f f f 2 2 e e 2 2 f f f . .
                            . f f e f 2 f e e f 2 f e f f .
                            . f e e f f e e e e f e e e f .
                            . . f e e e e e e e e e e f . .
                            . . . f e e e e e e e e f . . .
                            . . e 4 f f f f f f f f 4 e . .
                            . . 4 d f 2 2 2 2 2 2 f d 4 . .
                            . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                            . . . . . f f f f f f . . . . .
                            . . . . . f f . . f f . . . . .
            """)], 100, False)
controller.up.onEvent(ControllerButtonEvent.Released, on_up_released)

# Down
def on_down_released():
    if on_menu:
        pass
    else:
        animation.stop_animation(animation.AnimationTypes.All, player_sprite)
        animation.run_image_animation(player_sprite, [img("""
                . . . . . . f f f f . . . . . .
                        . . . . f f f 2 2 f f f . . . .
                        . . . f f f 2 2 2 2 f f f . . .
                        . . f f f e e e e e e f f f . .
                        . . f f e 2 2 2 2 2 2 e e f . .
                        . . f e 2 f f f f f f 2 e f . .
                        . . f f f f e e e e f f f f . .
                        . f f e f b f 4 4 f b f e f f .
                        . f e e 4 1 f d d f 1 4 e e f .
                        . . f e e d d d d d d e e f . .
                        . . . f e e 4 4 4 4 e e f . . .
                        . . e 4 f 2 2 2 2 2 2 f 4 e . .
                        . . 4 d f 2 2 2 2 2 2 f d 4 . .
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                        . . . . . f f f f f f . . . . .
                        . . . . . f f . . f f . . . . .
            """)], 100, False)
controller.down.onEvent(ControllerButtonEvent.Released, on_down_released)


# Button B
def on_b_pressed():
    if on_menu or on_lore_screen or info.life() == 0:
        pass
    else:
        shot()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

# Related functions to button B
def shot():
    global xpos_bullet, ypos_bullet, bullet_sprite, stat_shots
    xpos_bullet = player_sprite.x
    ypos_bullet = player_sprite.y
    bullet_sprite = create_bullet()
    bullet_sprite.set_position(xpos_bullet, ypos_bullet)
    if direction == "up":
        bullet_sprite.set_velocity(0, -200)
    elif direction == "down":
        bullet_sprite.set_velocity(0, 200)
    elif direction == "left":
        bullet_sprite.set_velocity(-200, 0)
    elif direction == "right":
        bullet_sprite.set_velocity(200, 0)
    stat_shots+=1


def create_bullet():
    bullet_sprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . 4 4 . . . . . . .
        . . . . . . 4 5 5 4 . . . . . .
        . . . . . . 2 5 5 2 . . . . . .
        . . . . . . . 2 2 . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """), SpriteKind.projectile)

    bullet_id = bullet_list.length + 1
    bullet = Bullet(bullet_sprite,bullet_id)
    bullet_list.append(bullet)
    
    return bullet_sprite

# Button A
def on_a_pressed():
    global on_menu, on_zombie_screen, on_lore_screen
    if on_menu == True:
        on_menu = False
        close_menu()
        story.start_cutscene(lore_cutscene)
        on_lore_screen = True
    elif on_lore_screen == True:
        story.clear_all_text()
        skip_lore()
    elif on_zombie_screen == True:
        story.cancel_current_cutscene()
        on_zombie_screen = False
    elif on_stats_screen == True:
        story.clear_all_text()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# Related functions to button A
def close_menu():
    sprites.destroy(title_sprite)
    sprites.destroy(text_sprite)

def skip_lore():
    global skip_lore_sprite
    sprites.destroy(skip_lore_sprite)
    pause(200)
    create_skip_lore_sprite()

# Bullet animation
def animate_bullet_collision(bullet):
    animation.run_image_animation(bullet,
        [img("""
                . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . 4 4 . . . . . . .
                                        . . . . . . 4 5 5 4 . . . . . .
                                        . . . . . . 2 5 5 2 . . . . . .
                                        . . . . . . . 2 2 . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . 4 . . . . .
                                        . . . . 2 . . . . 4 4 . . . . .
                                        . . . . 2 4 . . 4 5 4 . . . . .
                                        . . . . . 2 4 d 5 5 4 . . . . .
                                        . . . . . 2 5 5 5 5 4 . . . . .
                                        . . . . . . 2 5 5 5 5 4 . . . .
                                        . . . . . . 2 5 4 2 4 4 . . . .
                                        . . . . . . 4 4 . . 2 4 4 . . .
                                        . . . . . 4 4 . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . 3 . . . . . . . . . . . 4 . .
                                        . 3 3 . . . . . . . . . 4 4 . .
                                        . 3 d 3 . . 4 4 . . 4 4 d 4 . .
                                        . . 3 5 3 4 5 5 4 4 d d 4 4 . .
                                        . . 3 d 5 d 1 1 d 5 5 d 4 4 . .
                                        . . 4 5 5 1 1 1 1 5 1 1 5 4 . .
                                        . 4 5 5 5 5 1 1 5 1 1 1 d 4 4 .
                                        . 4 d 5 1 1 5 5 5 1 1 1 5 5 4 .
                                        . 4 4 5 1 1 5 5 5 5 5 d 5 5 4 .
                                        . . 4 3 d 5 5 5 d 5 5 d d d 4 .
                                        . 4 5 5 d 5 5 5 d d d 5 5 4 . .
                                        . 4 5 5 d 3 5 d d 3 d 5 5 4 . .
                                        . 4 4 d d 4 d d d 4 3 d d 4 . .
                                        . . 4 5 4 4 4 4 4 4 4 4 4 . . .
                                        . 4 5 4 . . 4 4 4 . . . 4 4 . .
                                        . 4 4 . . . . . . . . . . 4 4 .
            """),
            img("""
                . . . . . . . . . . . . . . . .
                                        . . . . . . . . . . . . . . . .
                                        . . . . . b b . b b b . . . . .
                                        . . . . b 1 1 b 1 1 1 b . . . .
                                        . . b b 3 1 1 d d 1 d d b b . .
                                        . b 1 1 d d b b b b b 1 1 b . .
                                        . b 1 1 1 b . . . . . b d d b .
                                        . . 3 d d b . . . . . b d 1 1 b
                                        . b 1 d 3 . . . . . . . b 1 1 b
                                        . b 1 1 b . . . . . . b b 1 d b
                                        . b 1 d b . . . . . . b d 3 d b
                                        . b b d d b . . . . b d d d b .
                                        . b d d d d b . b b 3 d d 3 b .
                                        . . b d d 3 3 b d 3 3 b b b . .
                                        . . . b b b d d d d d b . . . .
                                        . . . . . . b b b b b . . . . .
            """)],
        0,
        False)
    pause(0)
    sprites.destroy(bullet)

def on_on_update():
    scene.center_camera_at(player_sprite.x+40, 60)