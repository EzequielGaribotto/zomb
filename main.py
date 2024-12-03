# Main
# Sprites
player_sprite: Sprite = None
zombie_sprite: Sprite = None
bullet_sprite: Sprite = None
ghast_sprite: Sprite = None
# Sprite lists
bullet_list:List[Bullet] = []
zombie_list:List[Sprite] = []
ghast_list:List[Sprite] = []
deleted_zombies_list:List[Sprite] = []
explosion_particle_list:List[Sprite] = []

# Status bar Sprites
exp_status_bar:StatusBarSprite = None
zombie_statusbar: StatusBarSprite = None
ghast_status_bar:StatusBarSprite = None

# Text Sprites
title_sprite: TextSprite = None
text_sprite: TextSprite = None
skip_lore_sprite: TextSprite = None
skip_stats_sprite: TextSprite = None

# Enemies stats
delay_min_enemies = 0
delay_max_enemies = 0

delay_min_ghast = 0
delay_max_ghast = 0

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

# Explosion stats
explosion_power = 0
explosion_particle_amt = 0
explosion_min_range = 0
explosion_max_range = 0

blood_explosion_power = 0
blood_explosion_particle_amt = 0
blood_explosion_min_range = 0
blood_explosion_max_range = 0

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
stat_blood_explosion_damage = 0
stat_explosion_damage = 0
accumulated_explosion_damage = 0

stat_zombies_escaped = 0
stat_zombies_killed = 0
stat_ghasts_killed = 0
stat_damage_dealt = 0
stat_lifes_won = 0
stat_lifes_lost = 0

# Ghast stats
ghast_speed = 0
ghast_xp_reward = 0
ghast_hp = 0
ypos_ghast_sprite = 0
ghast_exists = False

# Timers
zombie_timer = game.runtime()
ghast_timer = game.runtime()
footstep_timer = game.runtime()

remembered_player_x = 20
remembered_player_y = 60

# Classes
@namespace
class SpriteKind:
    projectile = SpriteKind.create()
    enemy = SpriteKind.create()
    player = SpriteKind.create()
    explosion = SpriteKind.create()
    blood_explosion = SpriteKind.create()

class Bullet:
    def __init__(self, sprite: Sprite, bullet_id: Number):
        self.bullet_id = bullet_id
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
    set_ghast_stats(player_level)
    create_exp_status_bar()
    game.on_update(on_on_update)
    info.set_life(3)

def create_exp_status_bar():
    global exp_status_bar
    exp_status_bar = statusbars.create(40, 4, StatusBarKind.Energy)
    exp_status_bar.position_direction(CollisionDirection.TOP)
# Funcion recursiva para crear zombies en funcion del nivel
def gamer():
    global delay_min_enemies, delay_max_enemies, player_exp, player_exp_required, player_hp
    update_exp_status_bar()
    if (player_level == 11): # Caso base 1
        music.power_up.play()
        game_over()
        return
    if (info.life() == 0): # Caso base 2
        music.spooky.play()
        game_over()
        return
    if (on_stats_screen):
        return
    while player_exp < player_exp_required and info.life() > 0:
        pause(1)
        destroy_zombies()
        destroy_bullets()
        if player_exp < player_exp_required and info.life() > 0:
            create_enemy()
        else:
            next_level()

def next_level():
    global player_level, player_exp, player_sprite, remembered_player_x, remembered_player_y
    if (info.life() > 0):
        player_level += 1
    if (player_level == 11): # Caso base 1
        return
    if (info.life() == 0): # Caso base 2
        return
    player_exp = 0
    update_exp_status_bar()
    set_zombie_stats(player_level)
    set_player_stats(player_level)
    music.ba_ding.play()
    remember_player_position(player_sprite)
    destroy_all()
    game.splash("Level Up! - " + player_level)
    color.start_fade(color.original_palette, color.black, 500)
    pause(500)
    color.start_fade(color.black, color.original_palette, 500)
    scene.set_background_image(assets.image("""xd"""))
    pause(500)
    show_game_lore(player_level)
    
    create_player()
    create_exp_status_bar()
    player_sprite.set_position(remembered_player_x, remembered_player_y)
    gamer()

def remember_player_position(player_sprite:Sprite):
    global remembered_player_x, remembered_player_y
    remembered_player_x = player_sprite.x
    remembered_player_y = player_sprite.y

def destroy_all():
    destroy_all_zombies()
    destroy_all_bullets()
    destroy_all_ghasts()
    destroy_all_explosion_particles()
    sprites.destroy(player_sprite)
    sprites.destroy(exp_status_bar)
    scene.set_background_image(assets.image("""xd"""))

def show_game_lore(player_level):
    if player_level == 2:
        scene.set_background_image(assets.image("""lore_level_2_1"""))
        
        game.show_long_text("Los primeros infectados eran lentos, ahora son cada vez más rápidos y letales.", DialogLayout.BOTTOM)
    elif player_level == 3:
        scene.set_background_image(assets.image("""lore_level_3_1"""))
        game.show_long_text("Los demonios internos de Alex empiezan a aparecer", DialogLayout.BOTTOM)
    elif player_level == 4:
        scene.set_background_image(assets.image("""lore_level_4_1"""))
        game.show_long_text("Alex recuerda su hogar, pero ya no queda nada de él.", DialogLayout.BOTTOM)
    elif player_level == 5:
        scene.set_background_image(assets.image("""lore_level_5_1"""))
        game.show_long_text("Un rumor dice que un refugio seguro existe al este... ¿será cierto?", DialogLayout.BOTTOM)
    elif player_level == 6:
        scene.set_background_image(assets.image("""lore_level_6_1"""))
        game.show_long_text("La infección avanza más rápido que cualquier cura posible.", DialogLayout.BOTTOM)
    elif player_level == 7:
        scene.set_background_image(assets.image("""lore_level_7_1"""))
        game.show_long_text("Encontré un diario... alguien intentó detener esto, pero fracasó.", DialogLayout.BOTTOM)
    elif player_level == 8:
        scene.set_background_image(assets.image("""lore_level_8_1"""))
        game.show_long_text("El Micro:bit interceptó una señal: 'Refugio bajo ataque, ayuda...'", DialogLayout.BOTTOM)
    elif player_level == 9:
        scene.set_background_image(assets.image("""lore_level_9_1"""))
        game.show_long_text("El refugio está cerca, pero algo acecha en la oscuridad...", DialogLayout.BOTTOM)
    elif player_level == 10:
        scene.set_background_image(assets.image("""lore_level_10_1"""))
        game.show_long_text("Todo apunta a esto: el refugio guarda un oscuro secreto.", DialogLayout.BOTTOM)
    scene.set_background_image(assets.image("""cityscape"""))

def set_player_stats(level: int):
    global player_hp, player_power, player_speed, player_exp_required, stat_lifes_won, player_exp_punish, explosion_power, blood_explosion_power, explosion_particle_amt, blood_explosion_particle_amt
    global blood_explosion_max_range, blood_explosion_min_range, explosion_min_range, explosion_max_range
    if info.life() < 3:
        info.change_life_by(+1)
        stat_lifes_won += 1

    stats = {
        "hp": 100 + (level - 1) * 50,
        "power": 50 + (level - 1) * 10,
        "speed": 200 + (level - 1) * 10,
        "exp_required": 100 * level,
        "exp_punish": level,

        "explosion_power": 50 + (level -3) * 15,
        "explosion_particle_amt": 10 + (level -3) * 3,
        "explosion_min_range":  30 + (level -1) * 7,
        "explosion_max_range":  30 + (level -1) * 7,

        "blood_explosion_power": 5 + (level -1) * 5,
        "blood_explosion_min_range":  15 + (level -1) * 5,
        "blood_explosion_max_range":  25 + (level -1) * 5,
        "blood_explosion_particle_amt": 10 + (level -1) * 5,
    }

    player_hp = stats["hp"]
    player_power = stats["power"]
    player_speed = stats["speed"]
    player_exp_required = stats["exp_required"]
    player_exp_punish = stats["exp_punish"]
    explosion_power = stats["explosion_power"]
    explosion_particle_amt = stats["explosion_particle_amt"]
    explosion_min_range = stats["explosion_min_range"]
    explosion_max_range = stats["explosion_max_range"]

    blood_explosion_power = stats["blood_explosion_power"]
    blood_explosion_particle_amt = stats["blood_explosion_particle_amt"]
    blood_explosion_min_range = stats["blood_explosion_min_range"]
    blood_explosion_max_range = stats["blood_explosion_max_range"]


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

def set_ghast_stats(level: int):
    global ghast_speed, ghast_xp_reward, ghast_hp, delay_min_ghast, delay_max_ghast

    stats = {
        "speed": 50 + (level - 3) * 5,
        "xp_reward": 50,
        "hp": 1000 + (level - 3) * 75,
        "delay_min": 10000 - (level - 3) * 1000,
        "delay_max": 15000 - (level - 3) * 500
    }
    delay_min_ghast = stats["delay_min"]
    delay_max_ghast = stats["delay_max"]
    ghast_speed = stats["speed"]
    ghast_xp_reward = stats["xp_reward"]
    ghast_hp = stats["hp"]

def destroy_bullets():
    global bullet_list
    global player_sprite
    for b in bullet_list:
        if b.sprite.x < LEFT_BOUNDARY - player_sprite.x or b.sprite.x > RIGHT_BOUNDARY + player_sprite.x or b.sprite.y > BOTTOM_BOUNDARY + player_sprite.y or b.sprite.y < TOP_BOUNDARY - player_sprite.y:
            sprites.destroy(b.sprite)

def destroy_zombies():
    global zombie_list, player_sprite, player_exp, deleted_zombies_list, player_exp_punish, stat_zombies_escaped
    for z in zombie_list:
        if z.x < LEFT_BOUNDARY and z not in deleted_zombies_list:
            sprites.destroy(z, effects.disintegrate)
            if (player_exp > 0):
                player_exp -= player_exp_punish
                if (player_exp < 0):
                    player_exp = 0
            deleted_zombies_list.append(z)
            stat_zombies_escaped+=1
            update_exp_status_bar()


def destroy_all_zombies():
    global zombie_list
    for z in zombie_list:
        sprites.destroy(z)

def destroy_all_bullets():
    global bullet_list
    global player_sprite
    for b in bullet_list:
        sprites.destroy(b.sprite)

def destroy_all_ghasts():
    global ghast_list
    for g in ghast_list:
        sprites.destroy(g)
    ghast_exists = False

def destroy_all_explosion_particles():
    global explosion_particle_list
    for p in explosion_particle_list:
        sprites.destroy(p)

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
    destroy_all()
    effects.star_field.end_screen_effect()
    if (player_level >= 11):
        game.splash("Game Over", "You have reached the max level!")
    else:
        game.splash("Game Over", "You died")
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
    story.print_dialog("Balas disparadas: " + str(stat_shots), 80, 90, 50, 150)
    story.print_dialog("Balas acertadas: " + str(stat_accurate_shots), 80, 90, 50, 150)
    story.print_dialog("Precisión: " + str(stat_precission) + "%", 80, 90, 50, 150)
    story.print_dialog("Zombis eliminados: " + str(stat_zombies_killed), 80, 90, 50, 150)
    story.print_dialog("Zombis que escaparon: " + str(stat_zombies_escaped), 80, 90, 50, 150)
    story.print_dialog("Daño infligido: " + str(stat_damage_dealt), 80, 90, 50, 150)
    story.print_dialog("Vidas ganadas: " + str(stat_lifes_won), 80, 90, 50, 150)
    story.print_dialog("Vidas perdidas: " + str(stat_lifes_lost), 80, 90, 50, 150)

# Eventos
def on_projectile_collision(bullet, zombie):
    global player_power, zombie_hp, player_exp, zombie_xp_reward, zombie_stun_speed, zombie_stun_duration, stat_accurate_shots, stat_damage_dealt
    stat_accurate_shots+=1
    stat_damage_dealt+=player_power
    animate_bullet_collision(bullet)
    play_custom_hit_sound()
    zombie_statusbar = statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, zombie)
    if (zombie_statusbar): zombie_statusbar.value += -player_power
    if (zombie): zombie.set_velocity(-zombie_stun_speed, 0)
    pause(zombie_stun_duration)
    if (zombie): zombie.set_velocity(-zombie_speed, 0)
sprites.on_overlap(SpriteKind.projectile,SpriteKind.enemy,on_projectile_collision)

def on_player_collision_with_enemy(player, zombie):
    global zombie_power, player_hp, stat_lifes_lost
    music.zapped.play()
    info.change_life_by(-1)
    stat_lifes_lost+=1
    zombie.destroy()
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player,SpriteKind.enemy,on_player_collision_with_enemy)

# Eventos
def on_explosion_collision(explosion, zombie):
    global explosion_power, stat_explosion_damage
    stat_explosion_damage+=explosion_power
    sprites.destroy(explosion)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, zombie).value += -explosion_power
sprites.on_overlap(SpriteKind.explosion,SpriteKind.enemy,on_explosion_collision)

def on_blood_explosion_collision(explosion, zombie):
    global blood_explosion_power, stat_blood_explosion_damage
    stat_blood_explosion_damage+=blood_explosion_power
    sprites.destroy(explosion)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, zombie).value += -blood_explosion_power

sprites.on_overlap(SpriteKind.blood_explosion,SpriteKind.enemy,on_blood_explosion_collision)

def on_enemy_life_zero(bar):
    global player_exp, zombie_xp_reward, stat_zombies_killed, ghast_xp_reward, stat_ghasts_killed, ghast_exists
    music.thump.play()
    sprite = bar.sprite_attached_to()
    if sprite in zombie_list:
        stat_zombies_killed+=1
        player_exp += zombie_xp_reward
        sprite.set_velocity(0, 0)
        blood_explosion(sprite.x,sprite.y)
    elif ghast_exists:
        if sprite in ghast_list:
            stat_ghasts_killed+=1
            player_exp += ghast_xp_reward
            sprite.set_velocity(0, 0)
            ghast_exists = False
            explosion(sprite.x, sprite.y)

    bar.sprite_attached_to().destroy(effects.disintegrate)
    update_exp_status_bar()
statusbars.on_zero(StatusBarKind.enemy_health, on_enemy_life_zero)


def on_life_zero():
    music.spooky.play()
    game_over()
info.on_life_zero(on_life_zero)

def create_enemy():
    global player_level, ghast_exists, delay_min_ghast, delay_max_ghast
    global ghast_timer, zombie_timer
    current_time = game.runtime()
    if (current_time - zombie_timer > randint(delay_min_enemies, delay_max_enemies)):
        create_zombie()
        zombie_timer = current_time
    if (player_level >= 1 and not ghast_exists):
        if (current_time - ghast_timer > randint(delay_min_ghast, delay_max_ghast)):
            create_ghast()
            ghast_timer = current_time

def create_player():
    global player_sprite, direction, remembered_player_x, remembered_player_y
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
    player_sprite.set_position(remembered_player_x, remembered_player_y)
    controller.move_sprite(player_sprite)
    player_sprite.set_stay_in_screen(True)
    effects.star_field.start_screen_effect()
    scroller.set_camera_scrolling_multipliers(1, 0)

def create_zombie():
    global zombie_hp, zombie_sprite, ypos_zombie_sprite, zombie_statusbar
    ypos_zombie_sprite = randint(20, 110)
    zombie_sprite = sprites.create(assets.image("""zombie_enemy"""), SpriteKind.enemy)
    zombie_sprite.set_position(player_sprite.x + RIGHT_BOUNDARY, ypos_zombie_sprite)

    animation.run_image_animation(zombie_sprite,
        assets.animation("""zombie_anim"""),
        100,
        True)
    zombie_sprite.set_velocity(-zombie_speed, 0)
    zombie_list.push(zombie_sprite)
    zombie_statusbar = statusbars.create(16, 2, StatusBarKind.enemy_health)
    zombie_statusbar.max = zombie_hp
    zombie_statusbar.value = zombie_hp
    zombie_statusbar.attachToSprite(zombie_sprite)

def create_ghast():
    global ghast_sprite, ghast_status_bar, ghast_speed, ypos_ghast_sprite, ghast_hp, ghast_exists
    ghast_exists = True
    ypos_ghast_sprite = randint(20, 110)
    ghast_sprite = sprites.create(assets.image("""ghast_i"""), SpriteKind.enemy)
    ghast_sprite.set_position(player_sprite.x + RIGHT_BOUNDARY, ypos_ghast_sprite)
    
    animation.run_image_animation(ghast_sprite,
        assets.animation("""ghast"""),
        150,
        True)
    
    ghast_list.push(ghast_sprite)
    ghast_statusbar = statusbars.create(24, 2, StatusBarKind.enemy_health)
    ghast_statusbar.max = ghast_hp
    ghast_statusbar.value = ghast_hp
    ghast_statusbar.attach_to_sprite(ghast_sprite)
    
    game.on_update_interval(200, update_ghast)

def update_ghast():
    follow_player(ghast_sprite, ghast_speed)

def follow_player(enemy_sprite: Sprite, ghast_speed: int):
    if enemy_sprite and player_sprite:
        dx = player_sprite.x - enemy_sprite.x
        dy = player_sprite.y - enemy_sprite.y
        distance = Math.sqrt(dx * dx + dy * dy)
        
        if distance > 0:
            enemy_sprite.set_velocity(ghast_speed * (dx / distance), ghast_speed * (dy / distance))


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
            0,
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
            0,
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
            0,
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
            0,
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
            """)], 0, False)
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
    global on_menu, player_level
    if on_menu == True:
            on_menu = False
            close_menu()
            player_level = 10
            open_zombie_screen()
            player_level = 10
    elif on_lore_screen or info.life() == 0:
        pass
    else:
        shot()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)


# Related functions to button B
def shot():
    global xpos_bullet, ypos_bullet, bullet_sprite, stat_shots
    play_custom_shot()
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

# Función para crear la explosión
def explosion(x: int, y: int):
    global explosion_particle_amt, explosion_particle_list
    blood_explosion_sound()
    for i in range(explosion_particle_amt):
        blood = sprites.create(img("""
                    . . .
                    . 2 4
                    . . .
        """), SpriteKind.explosion)
        explosion_particle_list.push(blood)
        blood.x = x
        blood.y = y

        angle = Math.random_range(0, 360)
        
        radians = angle * Math.PI / 180
        
        blood.vx = Math.cos(radians) * Math.random_range(explosion_min_range, explosion_max_range)
        blood.vy = Math.sin(radians) * Math.random_range(explosion_min_range, explosion_max_range)

        blood.set_flag(SpriteFlag.AUTO_DESTROY, True)
        blood.lifespan = Math.random_range(800, 1000)

# Función para crear la explosión circular
def blood_explosion(x: int, y: int):
    global blood_explosion_particle_amt
    for i in range(blood_explosion_particle_amt):
        blood = sprites.create(img("""
            . . .
            . 7 4
            . . .
        """), SpriteKind.blood_explosion)
        blood.x = x
        blood.y = y
        explosion_particle_list.push(blood)
        angle = Math.random_range(0, 360)
        
        radians = angle * Math.PI / 180
        
        blood.vx = Math.cos(radians) * Math.random_range(blood_explosion_min_range, blood_explosion_max_range)
        blood.vy = Math.sin(radians) * Math.random_range(blood_explosion_min_range, blood_explosion_max_range)

        blood.set_flag(SpriteFlag.AUTO_DESTROY, True)
        blood.lifespan = Math.random_range(800, 1000)

controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# Bullet animation
def animate_bullet_collision(bullet):
    sprites.destroy(bullet)

current_camera_x = 0

def on_on_update():
    global current_camera_x
    smoothing_factor = 0.1

    if ghast_exists and abs(ghast_sprite.x - player_sprite.x) < 80:
        target_x = (player_sprite.x + ghast_sprite.x) / 2
        player_sprite.set_stay_in_screen(False)
    else:
        target_x = player_sprite.x + 50
        player_sprite.set_stay_in_screen(True)

    current_camera_x += (target_x - current_camera_x) * smoothing_factor
    scene.center_camera_at(current_camera_x, 60)

    set_boundaries()
    play_foot_step()


def set_boundaries():
    if player_sprite.x < 0:
        player_sprite.x = 0
    if player_sprite.y < 20:
        player_sprite.y = 20
    if player_sprite.y > screen.height:
        player_sprite.y = screen.height

def play_foot_step():
    global footstep_timer
    if controller.left.is_pressed() or controller.right.is_pressed() or controller.down.is_pressed() or controller.up.is_pressed():
        current_time = game.runtime()
        if current_time - footstep_timer > 200:
            play_custom_footstep()
            footstep_timer = current_time

def play_custom_shot():
    music.play_sound_effect(music.create_sound_effect(
        waveShape=WaveShape.SQUARE,
        startFrequency=200,
        endFrequency=100,
        startVolume=50,
        endVolume=0,
        duration=100,
        effect=SoundExpressionEffect.NONE,
        interpolation=InterpolationCurve.LINEAR,
    ), mode=SoundExpressionPlayMode.IN_BACKGROUND)

def play_custom_hit_sound():
    startFreq = randint(280, 320)
    endFreq = randint(140, 160)
    duration = randint(150, 250)  # Slight variation in duration
    music.play_sound_effect(music.create_sound_effect(
        waveShape=WaveShape.SAWTOOTH,  
        startFrequency=startFreq,      # High starting frequency for "punchy" effect
        endFrequency=endFreq,        # Lower ending frequency for a quick drop
        startVolume=100,         # Loud start
        endVolume=0,             # Fade out to silence
        duration=duration,             # Duration in milliseconds
        effect=SoundExpressionEffect.NONE,  # No extra effects
        interpolation=InterpolationCurve.LINEAR,  # Smooth pitch transition
    ), mode=SoundExpressionPlayMode.IN_BACKGROUND)

def play_custom_footstep():
    startFreq = randint(220, 240)  # Slight variation for realism
    endFreq = randint(180, 200)
    duration = 50  # Quick and subtle
    music.play_sound_effect(music.create_sound_effect(
        waveShape=WaveShape.TRIANGLE,  # Triangle wave for a soft, smooth tone
        startFrequency=startFreq,
        endFrequency=endFreq,
        startVolume=50,  # Moderate volume for subtlety
        endVolume=0,  # Fade out for realism
        duration=duration,
        effect=SoundExpressionEffect.NONE,  # No additional effects
        interpolation=InterpolationCurve.CURVE,  # Slightly curved transition
    ), mode=SoundExpressionPlayMode.IN_BACKGROUND)

def blood_explosion_sound():
    music.play_tone(200, BeatFraction.HALF)
    music.play_tone(150, BeatFraction.QUARTER)
    music.play_tone(800, BeatFraction.EIGHTH)
    music.play_tone(1000, BeatFraction.EIGHTH)
    music.play_tone(1200, BeatFraction.EIGHTH)
