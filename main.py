
# Main
# Sprites
player_sprite: Sprite = None
zombie_sprite: Sprite = None
bullet_sprite: Sprite = None

# Sprite lists
bullet_list:List[Bullet] = []
zombie_list:List[Zombie] = []

# Text Sprites
title_sprite: TextSprite = None
text_sprite: TextSprite = None
skip_lore_sprite: TextSprite = None

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

# Booleans
on_menu = True
on_zombie_screen = False
on_lore_screen = False
next_lore = False

# CONSTANTS
# Boundaries
RIGHT_BOUNDARY = 160
LEFT_BOUNDARY = 0
BOTTOM_BOUNDARY = 120
TOP_BOUNDARY = 0
statusbar: StatusBarSprite = None
# main
open_main_screen()
@namespace
class SpriteKind:
    projectile = SpriteKind.create()
    enemy = SpriteKind.create()
    player = SpriteKind.create()
    
def on_projectile_collision(bullet, zombie):
    global player_power, zombie_hp, player_exp, zombie_xp_reward, zombie_stun_speed, zombie_stun_duration
    animate_bullet_collision(bullet)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, zombie).value += -player_power
    zombie.set_velocity(-zombie_stun_speed, 0)
    pause(zombie_stun_duration)
    zombie.set_velocity(-zombie_speed, 0)

def on_on_zero(status):
    global player_power, zombie_hp, player_exp, zombie_xp_reward
    status.sprite_attached_to().destroy(effects.disintegrate)
    player_exp += zombie_xp_reward
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.enemy,
    on_projectile_collision)

def on_player_collision_with_enemy(player, zombie):
    global zombie_power, player_hp
    info.change_life_by(-1)
    zombie.destroy()
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player,
    SpriteKind.enemy,
    on_player_collision_with_enemy)

# Screens
# Main screen
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

# Related functions to main screen
def create_title_sprite():
    global title_sprite
    title_sprite = textsprite.create("Zombie Game")
    title_sprite.set_max_font_height(12)
    title_sprite.set_outline(1, 15)
    title_sprite.set_position(82, 43)

def bottom_text_sprite():
    global text_sprite
    text_sprite = textsprite.create("Press A to start the game")
    text_sprite.set_outline(0.2, 1)
    text_sprite.set_position(80, 110)

def create_skip_lore_sprite():
    global skip_lore_sprite
    skip_lore_sprite = textsprite.create("Press A to Skip Lore")
    skip_lore_sprite.set_outline(0.2, 1)
    skip_lore_sprite.set_position(80, 110)

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

# First screen
def open_zombie_screen():
    scene.set_background_image(assets.image("""
                cityscape
            """))
    global on_zombie_screen, on_menu, ypos_zombie_sprite, player_level, on_lore_screen, skip_lore_sprite
    on_zombie_screen = True
    on_menu = False
    on_lore_screen = False
    player_level = 1
    create_player()
    story.sprite_say_text(player_sprite, "ostras pedrin")
    sprites.destroy(skip_lore_sprite)
    set_player_stats(player_level)
    set_zombie_stats(player_level)
    controller.move_sprite(player_sprite)
    player_sprite.set_stay_in_screen(True)
    effects.star_field.start_screen_effect()
    scroller.set_camera_scrolling_multipliers(1, 0)
    game.on_update(on_on_update)
    info.set_life(3)
    gamer()

def gamer():
    global delay_min_enemies, delay_max_enemies, player_exp, player_exp_required, player_hp
    while player_exp < player_exp_required and info.life() > 0:
        pause(randint(delay_min_enemies, delay_max_enemies))
        destroy_zombies()
        destroy_bullets()
        if player_exp < player_exp_required and info.life() > 0:
            create_zombie()
        else:
            next_level()



def next_level():
    global player_level, player_exp, player_exp_required, player_hp, player_power, zombie_hp, zombie_power, zombie_speed

    if (info.life() > 0):
        player_level += 1
    if (player_level == 11):
        game_over()
    player_exp = 0
    set_zombie_stats(player_level)
    set_player_stats(player_level)
    game.splash("Level Up! - " + player_level)
    destroy_all_zombies()
    player_sprite.set_position(10, 60)
    gamer()

def on_life_zero():
    game_over()
info.on_life_zero(on_life_zero)

def game_over():
    global player_level
    if (player_level >= 11):
        game.splash("Game Over", "You have reached the max level!")
    else:
        game.splash("Game Over", "You died")
    stats_screen()
    game.over()


def stats_screen():
    game.splash("Stats")

def set_player_stats(level: number):
    global player_hp, player_power, player_speed, player_exp_required
    # depending on the level, the player will upgrade different stats
    if level == 1:
        player_hp = 100
        player_power = 50
        player_speed = 200
        player_exp_required = 100
    elif level == 2:
        player_hp = 150
        player_power = 60
        player_speed = 210
        player_exp_required = 100
    elif level == 3:
        player_hp = 200
        player_power = 70
        player_speed = 220
        player_exp_required = 100
        if (info.life() < 3):
            info.change_life_by(+1)
    elif level == 4:
        player_hp = 250
        player_power = 80
        player_speed = 230
        player_exp_required = 100
    elif level == 5:
        player_hp = 300
        player_power = 90
        player_speed = 240
        player_exp_required = 100
    elif level == 6:
        player_hp = 350
        player_power = 100
        player_speed = 250
        player_exp_required = 100
        if (info.life() < 3):
            info.change_life_by(+1)
    elif level == 7:
        player_hp = 400
        player_power = 110
        player_speed = 260
        player_exp_required = 100
    elif level == 8:
        player_hp = 450
        player_power = 120
        player_speed = 270
        player_exp_required = 100
    elif level == 9:
        player_hp = 500
        player_power = 130
        player_speed = 280
        player_exp_required = 100
        if (info.life() < 3):
            info.change_life_by(+1)
    elif level == 10:
        player_hp = 550
        player_power = 140
        player_speed = 290
        player_exp_required = 100

def set_zombie_stats(level: number):
    global zombie_hp, zombie_power, zombie_speed, delay_min_enemies, delay_max_enemies, zombie_xp_reward, zombie_stun_speed, zombie_stun_duration
    # depending on the level, the zombie will upgrade different stats
    if level == 1:
        zombie_hp = 100
        zombie_power = 50
        zombie_speed = 35
        delay_min_enemies = 1000
        delay_max_enemies = 1500
        zombie_xp_reward = 50
        zombie_stun_duration = 2000
        zombie_stun_speed = 10
    elif level == 2:
        zombie_hp = 150
        zombie_power = 60
        zombie_speed = 40
        delay_min_enemies = 900
        delay_max_enemies = 1400
        zombie_xp_reward = 50
        zombie_stun_duration = 1800
        zombie_stun_speed = 12
    elif level == 3:
        zombie_hp = 200
        zombie_power = 70
        zombie_speed = 45
        delay_min_enemies = 800
        delay_max_enemies = 1300
        zombie_xp_reward = 50
        zombie_stun_duration = 1600
        zombie_stun_speed = 14
    elif level == 4:
        zombie_hp = 250
        zombie_power = 80
        zombie_speed = 50
        delay_min_enemies = 700
        delay_max_enemies = 1200
        zombie_xp_reward = 50
        zombie_stun_duration = 1400
        zombie_stun_speed = 16
    elif level == 5:
        zombie_hp = 300
        zombie_power = 90
        zombie_speed = 55
        delay_min_enemies = 600
        delay_max_enemies = 1100
        zombie_xp_reward = 50
        zombie_stun_duration = 1200
        zombie_stun_speed = 18

    elif level == 6:
        zombie_hp = 350
        zombie_power = 100
        zombie_speed = 60
        delay_min_enemies = 500
        delay_max_enemies = 1000
        zombie_xp_reward = 50
        zombie_stun_duration = 1000
        zombie_stun_speed = 20

    elif level == 7:
        zombie_hp = 400
        zombie_power = 110
        zombie_speed = 65
        delay_min_enemies = 400
        delay_max_enemies = 900
        zombie_xp_reward = 50
        zombie_stun_duration = 800
        zombie_stun_speed = 22

    elif level == 8:
        zombie_hp = 450
        zombie_power = 120
        zombie_speed = 70
        delay_min_enemies = 300
        delay_max_enemies = 800
        zombie_xp_reward = 50
        zombie_stun_duration = 600
        zombie_stun_speed = 24

    elif level == 9:
        zombie_hp = 500
        zombie_power = 130
        zombie_speed = 75
        delay_min_enemies = 200
        delay_max_enemies = 700
        zombie_xp_reward = 50
        zombie_stun_duration = 400
        zombie_stun_speed = 26

    elif level == 10:
        zombie_hp = 550
        zombie_power = 140
        zombie_speed = 80
        delay_min_enemies = 100
        delay_max_enemies = 600
        zombie_xp_reward = 50
        zombie_stun_duration = 200
        zombie_stun_speed = 28

def destroy_bullets():
    global bullet_list
    global player_sprite
    for b in bullet_list:
        if b.sprite.x < LEFT_BOUNDARY + player_sprite.x or b.sprite.x > RIGHT_BOUNDARY + player_sprite.x or b.sprite.y > BOTTOM_BOUNDARY + player_sprite.y or b.sprite.y < TOP_BOUNDARY + player_sprite.y:
            sprites.destroy(b.sprite)

def destroy_zombies():
    global zombie_list
    global player_sprite
    for z in zombie_list:
        if z.sprite.x < LEFT_BOUNDARY:
            sprites.destroy(z.sprite, effects.disintegrate)

def destroy_all_zombies():
    global zombie_list
    global player_sprite
    for z in zombie_list:
        sprites.destroy(z.sprite, effects.disintegrate)

class Bullet:
    def __init__(self, sprite: Sprite, bullet_id: Number):
        self.bullet_id = bullet_id
        self.sprite: Sprite = sprite

class Zombie:
    def __init__(self, sprite: Sprite, zombie_id: Number):
        self.zombie_id = zombie_id
        self.sprite: Sprite = sprite

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
    if on_menu:
        pass
    else:
        shot()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

# Related functions to button B
def shot():
    global xpos_bullet, ypos_bullet, bullet_sprite
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
    animate_bullet(bullet_sprite)
    bullet_list.append(bullet)
    
    return bullet_sprite
    
def zombie_cutscene():
    global skip_lore_sprite
    open_zombie_screen()
    sprites.destroy(skip_lore_sprite)
def lore_cutscene():
    lore_screen()
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
        story.start_cutscene(zombie_cutscene)
    elif on_zombie_screen == True:
        story.cancel_current_cutscene()
        on_zombie_screen = False
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
def animate_bullet(bullet:Sprite):
    while bullet.x >= 0 and bullet.x <= 120 and (bullet.y >= 0 and bullet.y <= 120):
        if direction == "left":
            bullet.x += -1
        elif direction == "right":
            bullet.x += 1
        elif direction == "up":
            bullet.y += 1
        else:
            bullet.y += -1

def on_on_update():
    scene.center_camera_at(player_sprite.x, 60)
