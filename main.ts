//  CONSTANTS
//  Boundaries
let RIGHT_BOUNDARY = 160
let LEFT_BOUNDARY = 0
let BOTTOM_BOUNDARY = 120
let TOP_BOUNDARY = 0
//  Colors
let TRANSPARENT = 0
let WHITE = 1
let RED = 2
let PINK = 3
let ORANGE = 4
let YELLOW = 5
let TEAL = 6
let GREEN = 7
let BLUE = 8
let LIGHT_BLUE = 9
let PURPLE = 10
let LIGHT_PURPLE = 11
let DARK_PURPLE = 12
let TAN = 13
let BROWN = 14
let BLACK = 15
//  Game
let PLAYER_START_LEVEL = 9
let PLAYER_WIN_LEVEL = 10
let GHAST_APPEARANCE_LEVEL = 3
//  Sprites
let player_sprite : Sprite = null
let zombie_sprite : Sprite = null
let bullet_sprite : Sprite = null
let ghast_sprite : Sprite = null
//  Sprite lists
let bullet_list : Sprite[] = []
let zombie_list : Sprite[] = []
let ghast_list : Sprite[] = []
let deleted_zombies_list : Sprite[] = []
let explosion_particle_list : Sprite[] = []
//  Status bar Sprites
let exp_status_bar : StatusBarSprite = null
let zombie_status_bar : StatusBarSprite = null
let ghast_status_bar : StatusBarSprite = null
//  Text Sprites
let title_sprite : TextSprite = null
let text_sprite : TextSprite = null
let skip_lore_sprite : TextSprite = null
let skip_stats_sprite : TextSprite = null
//  Enemies stats
let delay_min_zombie = 0
let delay_max_zombie = 0
let delay_min_ghast = 0
let delay_max_ghast = 0
//  Zombie Stats
let zombie_speed = 0
let zombie_stun_duration = 0
let zombie_stun_speed = 0
let zombie_hp = 0
let zombie_power = 0
let ypos_bullet = 0
let xpos_bullet = 0
let ypos_zombie_sprite = 0
let zombie_xp_reward = 0
//  Ghast stats
let ghast_speed = 0
let ghast_xp_reward = 0
let ghast_hp = 0
let ypos_ghast_sprite = 0
let ghast_stun_speed = 0
let ghast_stun_duration = 0
//  Explosion stats
let explosion_power = 0
let explosion_particle_amt = 0
let explosion_min_range = 0
let explosion_max_range = 0
let blood_explosion_power = 0
let blood_explosion_particle_amt = 0
let blood_explosion_min_range = 0
let blood_explosion_max_range = 0
//  Player Stats
let direction = ""
let player_level = 0
let player_exp = 0
let player_exp_required = 0
let player_points = 0
let player_hp = 0
let player_power = 0
let player_speed = 0
let player_exp_punish = 0
let player_iframes = 0
//  Booleans
let on_menu = true
let on_zombie_screen = false
let on_lore_screen = false
let on_end_screen = false
let ghast_exists = false
let first_ghast = true
//  Stats to Display
let stat_shots = 0
let stat_missed_shots = 0
let stat_precission = 0
let stat_accurate_shots = 0
let stat_blood_explosion_damage = 0
let stat_explosion_damage = 0
let accumulated_explosion_damage = 0
let stat_zombies_escaped = 0
let stat_zombies_killed = 0
let stat_ghasts_killed = 0
let stat_damage_dealt = 0
let stat_lifes_won = 0
let stat_lifes_lost = 0
//  Timers
let zombie_timer = 0
let ghast_timer = 0
let footstep_timer = 0
let remembered_player_x = 20
let remembered_player_y = 60
//  Classes
namespace SpriteKind {
    export const projectile = SpriteKind.create()
    export const zombie = SpriteKind.create()
    export const ghast = SpriteKind.create()
    export const player = SpriteKind.create()
    export const explosion = SpriteKind.create()
    export const blood_explosion = SpriteKind.create()
}

namespace StatusBarKind {
    export const zombie_sb = SpriteKind.create()
    export const ghast_sb = SpriteKind.create()
    export const xp_sb = SpriteKind.create()
    export const route_sb = SpriteKind.create()
}

//  main
open_main_screen()
//  Screens
//  Pantalla principal
function open_main_screen() {
    
    on_menu = true
    if (on_menu == true) {
        scene.setBackgroundImage(assets.image`
                            woods
                        `)
        create_title_sprite()
        bottom_text_sprite()
    } else {
        
    }
    
}

function create_title_sprite() {
    
    title_sprite = textsprite.create("Zomb")
    title_sprite.setMaxFontHeight(20)
    title_sprite.setOutline(3, 14)
    title_sprite.setPosition(82, 20)
}

function bottom_text_sprite() {
    
    text_sprite = textsprite.create("Apreta A para jugar")
    text_sprite.setOutline(0.2, 5)
    text_sprite.setPosition(80, 110)
}

//  Pantalla de lore
function lore_screen() {
    
    on_lore_screen = true
    on_menu = false
    create_skip_lore_sprite()
    story.setSoundEnabled(true)
    story.setPagePauseLength(0, 1000)
    scene.setBackgroundImage(assets.image`earth_image`)
    story.printDialog("Una misteriosa enfermedad contagiosa está arrasando el mundo,", 80, 90, 50, 150)
    scene.setBackgroundImage(assets.image`zombie_image2`)
    story.printDialog("transformando a la gente en zombis sedientos de sangre humana.", 80, 90, 50, 150)
    scene.setBackgroundImage(img`
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
                ................................................................................................................................................................`)
    story.printDialog("Alex Byte, un joven inventor, sobrevive usando su ingenio y", 80, 90, 50, 150)
    story.printDialog("un Micro:bit modificado, capaz de guiarse y comunicarse con él.", 80, 90, 50, 150)
    story.printDialog("Con el mundo al borde del colapso, Alex debe abrirse paso entre hordas de zombis", 80, 90, 50, 150)
    story.printDialog("para llegar al último refugio humano donde poder estar a salvo.", 80, 90, 50, 150)
    story.printDialog("¿Podrá salvarse y encontrar una cura?", 80, 90, 50, 150)
}

function create_skip_lore_sprite() {
    
    skip_lore_sprite = textsprite.create("Apreta A para skipear lore")
    skip_lore_sprite.setOutline(0.2, 1)
    skip_lore_sprite.setPosition(80, 110)
}

//  Pantalla de juego
function open_zombie_screen() {
    initialize_game_data()
    gamer()
    game_over()
}

function initialize_game_data() {
    scene.setBackgroundImage(assets.image`
            cityscape
        `)
    
    on_zombie_screen = true
    on_menu = false
    on_lore_screen = false
    player_level = PLAYER_START_LEVEL
    create_player()
    story.spriteSayText(player_sprite, "ostras pedrin")
    sprites.destroy(skip_lore_sprite)
    create_exp_status_bar()
    update_exp_status_bar()
    set_game_stats(player_level)
    game.onUpdate(function on_on_update() {
        let target_x: number;
        
        let smoothing_factor = 0.1
        if (ghast_exists && Math.abs(ghast_sprite.x - player_sprite.x) < 80) {
            target_x = (player_sprite.x + ghast_sprite.x) / 2
            player_sprite.setStayInScreen(false)
        } else {
            target_x = player_sprite.x + 50
            player_sprite.setStayInScreen(true)
        }
        
        current_camera_x += (target_x - current_camera_x) * smoothing_factor
        scene.centerCameraAt(current_camera_x, 60)
        set_boundaries()
    })
    info.setLife(3)
}

//  Funcion recursiva para crear zombies en funcion del nivel
function gamer() {
    
    while (true) {
        pause(1)
        destroy_zombies()
        destroy_bullets()
        if (player_exp < player_exp_required && info.life() > 0) {
            create_enemies()
        } else {
            if (info.life() == 0) {
                music.spooky.play()
                //  Caso base 2 - Alex muere
                return
            }
            
            if (player_level + 1 > PLAYER_WIN_LEVEL) {
                //  Caso base 2 - Alex gana
                music.powerUp.play()
                return
            }
            
            next_level()
            gamer()
        }
        
    }
}

function create_exp_status_bar() {
    
    exp_status_bar = statusbars.create(80, 8, StatusBarKind.xp_sb)
    exp_status_bar.setBarBorder(1, BLACK)
    exp_status_bar.setColor(YELLOW, BLACK, RED)
    exp_status_bar.setLabel("XP", BLACK)
    exp_status_bar.setOffsetPadding(10, 0)
    exp_status_bar.positionDirection(CollisionDirection.Top)
}

function next_level() {
    
    player_level += 1
    update_stats_for_next_level()
    clear_screen()
    game.splash("Level Up! - " + player_level)
    fade_effect()
    show_game_lore(player_level)
    recreate_screen()
}

function recreate_screen() {
    create_player()
    create_exp_status_bar()
    update_exp_status_bar()
}

function fade_effect() {
    color.startFade(color.originalPalette, color.Black, 500)
    pause(500)
    color.startFade(color.Black, color.originalPalette, 500)
    scene.setBackgroundImage(assets.image`xd`)
    pause(500)
}

function update_stats_for_next_level() {
    
    player_exp = 0
    set_game_stats(player_level)
    music.baDing.play()
}

function set_game_stats(player_level: number) {
    
    set_zombie_stats(player_level)
    set_player_stats(player_level)
    set_ghast_stats(player_level)
}

function clear_screen() {
    remember_player_position(player_sprite)
    destroy_all()
    effects.starField.endScreenEffect()
    let ghast_exists = false
}

function remember_player_position(player_sprite: Sprite) {
    
    remembered_player_x = player_sprite.x
    remembered_player_y = player_sprite.y
}

function destroy_all() {
    destroy_all_zombies()
    destroy_all_bullets()
    destroy_all_ghasts()
    destroy_all_explosion_particles()
    sprites.destroy(player_sprite)
    sprites.destroy(exp_status_bar)
    scene.setBackgroundImage(assets.image`xd`)
}

function show_game_lore(player_level: number) {
    if (player_level == 2) {
        scene.setBackgroundImage(assets.image`lore_level_2_1`)
        game.showLongText("Los primeros infectados eran lentos, ahora son cada vez más rápidos y letales.", DialogLayout.Bottom)
    } else if (player_level == 3) {
        scene.setBackgroundImage(assets.image`lore_level_3_1`)
        game.showLongText("Los demonios internos de Alex empiezan a aparecer", DialogLayout.Bottom)
    } else if (player_level == 4) {
        scene.setBackgroundImage(assets.image`lore_level_4_1`)
        game.showLongText("Alex recuerda su hogar, pero ya no queda nada de él.", DialogLayout.Bottom)
    } else if (player_level == 5) {
        scene.setBackgroundImage(assets.image`lore_level_5_1`)
        game.showLongText("Un rumor dice que un refugio seguro existe al este... ¿será cierto?", DialogLayout.Top)
    } else if (player_level == 6) {
        scene.setBackgroundImage(assets.image`lore_level_6_1`)
        game.showLongText("La infección avanza más rápido que cualquier cura posible.", DialogLayout.Bottom)
    } else if (player_level == 7) {
        scene.setBackgroundImage(assets.image`lore_level_7_1`)
        game.showLongText("Sobrevive. Lucha. Escapa. Repite.", DialogLayout.Bottom)
    } else if (player_level == 8) {
        scene.setBackgroundImage(assets.image`lore_level_8_1`)
        game.showLongText("El Micro:bit interceptó una señal: 'Refugio bajo ataque, ayuda...'", DialogLayout.Bottom)
    } else if (player_level == 9) {
        scene.setBackgroundImage(assets.image`lore_level_9_1`)
        game.showLongText("Solo quedan los más fuertes. ¿Serás tú uno de ellos?", DialogLayout.Bottom)
    } else if (player_level == 10) {
        scene.setBackgroundImage(assets.image`lore_level_10_1`)
        game.showLongText("El fin no es el final... Es solo el comienzo de algo peor.", DialogLayout.Bottom)
    }
    
    scene.setBackgroundImage(assets.image`cityscape`)
}

function set_player_stats(level: number) {
    
    
    if (info.life() < 3) {
        info.changeLifeBy(+1)
        stat_lifes_won += 1
    }
    
    player_hp = 100 + (level - 1) * 50
    player_power = 50 + (level - 1) * 10
    player_speed = 200 + (level - 1) * 10
    player_exp_required = 100 * level
    player_exp_punish = 10 + level * 5
    explosion_power = 50 + (level - 3) * 15
    explosion_particle_amt = 10 + (level - 3) * 3
    explosion_min_range = 30 + (level - 1) * 7
    explosion_max_range = 30 + (level - 1) * 7
    blood_explosion_power = 5 + (level - 1) * 5
    blood_explosion_min_range = 15 + (level - 1) * 5
    blood_explosion_max_range = 25 + (level - 1) * 5
    blood_explosion_particle_amt = 10 + (level - 1) * 5
}

function set_zombie_stats(level: number) {
    
    
    zombie_hp = 100 + (level - 1) * 50
    zombie_power = 50 + (level - 1) * 10
    zombie_speed = 35 + (level - 1) * 5
    delay_min_zombie = Math.max(1500 - (level - 1) * 100, 400)
    delay_max_zombie = Math.max(2000 - (level - 1) * 100, 750)
    zombie_xp_reward = 50
    zombie_stun_duration = Math.max(2000 - (level - 1) * 200, 200)
    zombie_stun_speed = 10 + (level - 1) * 2
}

function set_ghast_stats(level: number) {
    
    
    ghast_hp = 800 + (level - 3) * 75
    ghast_speed = 50 + (level - 3) * 5
    delay_min_ghast = Math.max(10000 - (level - 3) * 250, 800)
    delay_max_ghast = Math.max(15000 - (level - 3) * 100, 1000)
    ghast_xp_reward = 100
    ghast_stun_duration = Math.max(2000 - (level - 1) * 200, 200)
    ghast_stun_speed = 10 + (level - 1) * 2
}

function destroy_bullets() {
    
    
    for (let b of bullet_list) {
        if (b.x < LEFT_BOUNDARY - player_sprite.x || b.x > RIGHT_BOUNDARY + player_sprite.x || b.y > BOTTOM_BOUNDARY + player_sprite.y || b.y < TOP_BOUNDARY - player_sprite.y) {
            sprites.destroy(b)
        }
        
    }
}

function destroy_zombies() {
    
    for (let z of zombie_list) {
        if (z.x < LEFT_BOUNDARY && deleted_zombies_list.indexOf(z) < 0) {
            sprites.destroy(z, effects.disintegrate)
            if (player_exp > 0) {
                player_exp -= player_exp_punish
                if (player_exp < 0) {
                    player_exp = 0
                }
                
            }
            
            deleted_zombies_list.push(z)
            stat_zombies_escaped += 1
            update_exp_status_bar()
        }
        
    }
}

function destroy_all_zombies() {
    sprites.destroyAllSpritesOfKind(SpriteKind.zombie)
}

function destroy_all_bullets() {
    
    
    for (let b of bullet_list) {
        sprites.destroy(b)
    }
}

function destroy_all_ghasts() {
    
    for (let g of ghast_list) {
        sprites.destroy(g)
    }
    ghast_exists = false
}

function destroy_all_explosion_particles() {
    
    for (let p of explosion_particle_list) {
        sprites.destroy(p)
    }
}

function update_exp_status_bar() {
    
    exp_status_bar.max = player_exp_required
    exp_status_bar.value = player_exp
}

//  exp_status_bar.set_label("EXP: "+ player_exp + "/" + player_exp_required, BLACK)
function game_over() {
    
    on_end_screen = true
    story.startCutscene(function end_cutscene() {
        clear_screen()
        show_end_lore(player_level)
        show_stats()
        game.over()
    })
}

info.onLifeZero(function on_life_zero() {
    
})
function show_end_lore(level: number) {
    if (level + 1 > PLAYER_WIN_LEVEL && info.life() > 0) {
        info.setLife(0)
        game.splash("GG", "¡Has logrado escapar!")
        story.printDialog("¡Felicidades, Alex! Has alcanzado el refugio humano.", 80, 90, 50, 150)
        story.printDialog("Gracias a tu ingenio, los supervivientes ahora tienen una oportunidad.", 80, 90, 50, 150)
        story.printDialog("Con tu Micro:bit, comenzará la investigación para encontrar una cura.", 80, 90, 50, 150)
        story.printDialog("El destino de la humanidad está en buenas manos.", 80, 90, 50, 150)
    } else {
        info.setLife(0)
        game.splash("NT", "Moriste")
        story.printDialog("Alex ha caído en su lucha contra las hordas de zombis.", 80, 90, 50, 150)
        story.printDialog("Aunque su esfuerzo fue valiente, los zombis han tomado el control.", 80, 90, 50, 150)
        story.printDialog("El refugio humano sigue siendo un sueño distante...", 80, 90, 50, 150)
        story.printDialog("¿Podrá la humanidad encontrar una nueva esperanza?", 80, 90, 50, 150)
    }
    
}

function show_stats() {
    let stat_missed_shots = stat_shots - stat_accurate_shots
    let stat_precission = stat_shots > 0 ? stat_accurate_shots / stat_shots * 100 : 0
    story.setPagePauseLength(0, 1000)
    story.printDialog("Balas disparadas: " + ("" + stat_shots), 80, 90, 50, 150)
    story.printDialog("Balas acertadas: " + ("" + stat_accurate_shots), 80, 90, 50, 150)
    story.printDialog("Precisión: " + ("" + stat_precission) + "%", 80, 90, 50, 150)
    story.printDialog("Zombis eliminados: " + ("" + stat_zombies_killed), 80, 90, 50, 150)
    story.printDialog("Zombis que escaparon: " + ("" + stat_zombies_escaped), 80, 90, 50, 150)
    story.printDialog("Daño infligido: " + ("" + stat_damage_dealt), 80, 90, 50, 150)
    story.printDialog("Vidas ganadas: " + ("" + stat_lifes_won), 80, 90, 50, 150)
    story.printDialog("Vidas perdidas: " + ("" + stat_lifes_lost), 80, 90, 50, 150)
}

//  Eventos
sprites.onOverlap(SpriteKind.projectile, SpriteKind.zombie, function on_projectile_collision_with_zombie(bullet: Sprite, zombie: Sprite) {
    
    stat_accurate_shots += 1
    stat_damage_dealt += player_power
    animate_bullet_collision(bullet)
    play_custom_hit_sound()
    let zombie_status_bar = statusbars.getStatusBarAttachedTo(StatusBarKind.zombie_sb, zombie)
    if (zombie_status_bar) {
        zombie_status_bar.value += -player_power
    }
    
    if (zombie) {
        zombie.setVelocity(-zombie_stun_speed, 0)
    }
    
    tint_sprite_time(zombie, ORANGE, 200)
    pause(zombie_stun_duration)
    if (zombie) {
        zombie.setVelocity(-zombie_speed, 0)
    }
    
})
sprites.onOverlap(SpriteKind.projectile, SpriteKind.ghast, function on_projectile_collision_with_ghast(bullet: Sprite, ghast: Sprite) {
    
    stat_accurate_shots += 1
    stat_damage_dealt += player_power
    animate_bullet_collision(bullet)
    play_custom_hit_sound()
    let ghast_statusbar = statusbars.getStatusBarAttachedTo(StatusBarKind.ghast_sb, ghast)
    if (ghast_statusbar) {
        ghast_statusbar.value += -player_power
    }
    
    if (ghast) {
        ghast.setVelocity(-ghast_stun_speed, 0)
    }
    
    let blue = 8
    tint_sprite_time(ghast, blue, 200)
    pause(ghast_stun_duration)
    if (ghast) {
        ghast.setVelocity(-ghast_speed, 0)
    }
    
})
function blink_sprite(sprite: Sprite, original_image: Image, blink_color: number, duration: number, interval: number) {
    /** Parpadea el sprite alternando entre su color original y un color de parpadeo. */
    control.runInParallel(function blink() {
        let tinted_image: Image;
        let end_time = game.runtime() + duration
        while (game.runtime() < end_time) {
            //  Crear imagen tintada
            tinted_image = original_image.clone()
            for (let x = 0; x < tinted_image.width; x++) {
                for (let y = 0; y < tinted_image.height; y++) {
                    if (tinted_image.getPixel(x, y) != 0) {
                        tinted_image.setPixel(x, y, blink_color)
                    }
                    
                }
            }
            sprite.setImage(tinted_image)
            pause(interval)
            sprite.setImage(original_image)
            pause(interval)
        }
    })
}

//  Ejecutar la rutina en paralelo
//  Resetear a 0
//  Temporizador en paralelo
sprites.onOverlap(SpriteKind.player, SpriteKind.zombie, function on_player_collision_with_zombie(player: Sprite, zombie: Sprite) {
    
    if (player_iframes > 0) {
        return
    }
    
    //  Si el jugador tiene iframes, no aplicar daño
    //  Configurar iframes y lógica de colisión
    player_iframes = 2000
    music.zapped.play()
    info.changeLifeBy(-1)
    stat_lifes_lost += 1
    scene.cameraShake(4, 500)
    blink_sprite(player, player.image.clone(), 1, player_iframes, 25)
    control.runInParallel(function reset_player_iframes() {
        /** Resetea los iframes del jugador después de la duración especificada. */
        
        pause(player_iframes)
        //  Esperar la duración de los iframes
        player_iframes = 0
    })
})
sprites.onOverlap(SpriteKind.player, SpriteKind.ghast, function on_player_collision_with_ghast(player: Sprite, ghast: Sprite) {
    
    if (player_iframes > 0) {
        return
    }
    
    player_iframes = 1000
    music.zapped.play()
    info.changeLifeBy(-1)
    stat_lifes_lost += 1
    ghast_exists = false
    ghast.destroy()
    scene.cameraShake(7, 500)
    blink_sprite(player, player.image.clone(), 1, player_iframes, 100)
    pause(player_iframes)
    player_iframes = 0
})
//  Eventos
sprites.onOverlap(SpriteKind.explosion, SpriteKind.zombie, function on_explosion_collision_with_zombie(explosion: Sprite, zombie: Sprite) {
    
    stat_explosion_damage += explosion_power
    sprites.destroy(explosion)
    statusbars.getStatusBarAttachedTo(StatusBarKind.zombie_sb, zombie).value += -explosion_power
})
sprites.onOverlap(SpriteKind.explosion, SpriteKind.ghast, function on_explosion_collision_with_ghast(explosion: Sprite, ghast: Sprite) {
    
    stat_explosion_damage += explosion_power
    sprites.destroy(explosion)
    statusbars.getStatusBarAttachedTo(StatusBarKind.ghast_sb, ghast).value += -explosion_power
})
sprites.onOverlap(SpriteKind.blood_explosion, SpriteKind.zombie, function on_blood_explosion_collision_with_zombie(explosion: Sprite, zombie: Sprite) {
    
    stat_blood_explosion_damage += blood_explosion_power
    sprites.destroy(explosion)
    statusbars.getStatusBarAttachedTo(StatusBarKind.zombie_sb, zombie).value += -blood_explosion_power
})
sprites.onOverlap(SpriteKind.blood_explosion, SpriteKind.ghast, function on_blood_explosion_collision_with_ghast(explosion: Sprite, ghast: Sprite) {
    
    stat_blood_explosion_damage += blood_explosion_power
    sprites.destroy(explosion)
    statusbars.getStatusBarAttachedTo(StatusBarKind.ghast_sb, ghast).value += -blood_explosion_power
})
statusbars.onZero(StatusBarKind.zombie_sb, function on_zombie_life_zero(bar: StatusBarSprite) {
    
    music.thump.play()
    let sprite = bar.spriteAttachedTo()
    stat_zombies_killed += 1
    player_exp += zombie_xp_reward
    sprite.setVelocity(0, 0)
    blood_explosion(sprite.x, sprite.y)
    bar.spriteAttachedTo().destroy(effects.disintegrate)
    update_exp_status_bar()
})
statusbars.onZero(StatusBarKind.ghast_sb, function on_ghast_life_zero(bar: StatusBarSprite) {
    
    music.thump.play()
    let sprite = bar.spriteAttachedTo()
    if (ghast_exists) {
        stat_ghasts_killed += 1
        player_exp += ghast_xp_reward
        sprite.setVelocity(0, 0)
        ghast_exists = false
        explosion(sprite.x, sprite.y)
    }
    
    bar.spriteAttachedTo().destroy(effects.disintegrate)
    update_exp_status_bar()
})
function create_enemies() {
    let first_ghast: boolean;
    
    
    let current_time = game.runtime()
    if (current_time - zombie_timer > randint(delay_min_zombie, delay_max_zombie)) {
        create_zombie()
        zombie_timer = current_time
    }
    
    if (player_level >= GHAST_APPEARANCE_LEVEL && !ghast_exists) {
        if (current_time - ghast_timer > randint(delay_min_ghast, delay_max_ghast)) {
            create_ghast()
            ghast_timer = current_time
        }
        
        if (first_ghast == true) {
            create_ghast()
            ghast_timer = current_time
            first_ghast = false
        }
        
    }
    
}

function create_player() {
    
    player_sprite = sprites.create(img`
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
        `, SpriteKind.player)
    player_sprite.setPosition(remembered_player_x, remembered_player_y)
    controller.moveSprite(player_sprite)
    player_sprite.setStayInScreen(true)
    effects.starField.startScreenEffect()
    scroller.setCameraScrollingMultipliers(1, 0)
}

function create_zombie() {
    
    ypos_zombie_sprite = randint(20, 110)
    zombie_sprite = sprites.create(assets.image`zombie_enemy`, SpriteKind.zombie)
    zombie_sprite.setPosition(player_sprite.x + RIGHT_BOUNDARY, ypos_zombie_sprite)
    animation.runImageAnimation(zombie_sprite, assets.animation`zombie_anim`, 100, true)
    zombie_sprite.setVelocity(-zombie_speed, 0)
    zombie_list.push(zombie_sprite)
    zombie_status_bar = statusbars.create(16, 2, StatusBarKind.zombie_sb)
    zombie_status_bar.max = zombie_hp
    zombie_status_bar.value = zombie_hp
    zombie_status_bar.attachToSprite(zombie_sprite)
}

function create_ghast() {
    
    ghast_exists = true
    ypos_ghast_sprite = randint(20, 110)
    ghast_sprite = sprites.create(assets.image`ghast_i`, SpriteKind.ghast)
    ghast_sprite.setPosition(player_sprite.x + RIGHT_BOUNDARY, ypos_ghast_sprite)
    animation.runImageAnimation(ghast_sprite, assets.animation`ghast`, 150, true)
    ghast_list.push(ghast_sprite)
    let ghast_statusbar = statusbars.create(24, 2, StatusBarKind.ghast_sb)
    ghast_statusbar.max = ghast_hp
    ghast_statusbar.value = ghast_hp
    ghast_statusbar.attachToSprite(ghast_sprite)
    game.onUpdateInterval(200, function update_ghast() {
        follow_player(ghast_sprite, ghast_speed)
    })
}

function follow_player(enemy_sprite: Sprite, ghast_speed: number) {
    let dx: number;
    let dy: number;
    let distance: number;
    if (enemy_sprite && player_sprite) {
        dx = player_sprite.x - enemy_sprite.x
        dy = player_sprite.y - enemy_sprite.y
        distance = Math.sqrt(dx * dx + dy * dy)
        if (distance > 0) {
            enemy_sprite.setVelocity(ghast_speed * (dx / distance), ghast_speed * (dy / distance))
        }
        
    }
    
}

//  Controls
//  Player movement
//  Up
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
    if (on_menu || on_lore_screen || on_end_screen) {
        return
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, player_sprite)
        animation.runImageAnimation(player_sprite, [img`
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
                `, img`
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
                `, img`
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
                `, img`
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
                `], 0, true)
        direction = "up"
    }
    
})
//  Left
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    
    if (on_menu || on_lore_screen || on_end_screen) {
        return
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, player_sprite)
        animation.runImageAnimation(player_sprite, [img`
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
                `, img`
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
                `, img`
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
                `, img`
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
                `], 0, true)
        direction = "left"
    }
    
})
//  Right
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    
    if (on_menu || on_lore_screen || on_end_screen) {
        return
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, player_sprite)
        animation.runImageAnimation(player_sprite, [img`
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
                `, img`
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
                `, img`
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
                `, img`
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
                `], 0, true)
        direction = "right"
    }
    
})
//  Down
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
    if (on_menu || on_lore_screen || on_end_screen) {
        return
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, player_sprite)
        animation.runImageAnimation(player_sprite, [img`
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
                `, img`
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
                `, img`
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
                `, img`
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
                `], 0, true)
        direction = "down"
    }
    
})
//  Released
//  Right
controller.right.onEvent(ControllerButtonEvent.Released, function on_right_released() {
    if (on_menu || on_lore_screen || on_end_screen) {
        return
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, player_sprite)
        animation.runImageAnimation(player_sprite, [img`
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
            `], 0, false)
    }
    
})
//  Left
//  Up
controller.up.onEvent(ControllerButtonEvent.Released, function on_up_released() {
    if (on_menu || on_lore_screen || on_end_screen) {
        return
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, player_sprite)
        animation.runImageAnimation(player_sprite, [img`
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
            `], 100, false)
    }
    
})
//  Down
controller.down.onEvent(ControllerButtonEvent.Released, function on_down_released() {
    if (on_menu || on_lore_screen || on_end_screen) {
        return
    } else {
        animation.stopAnimation(animation.AnimationTypes.All, player_sprite)
        animation.runImageAnimation(player_sprite, [img`
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
            `], 100, false)
    }
    
})
//  Button B
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    
    if (on_menu) {
        on_menu = false
        close_menu()
        open_zombie_screen()
    } else if (on_lore_screen || on_end_screen || info.life() == 0) {
        return
    } else {
        shot()
    }
    
})
//  Related functions to button B
function shot() {
    
    play_custom_shot()
    xpos_bullet = player_sprite.x
    ypos_bullet = player_sprite.y
    bullet_sprite = create_bullet()
    bullet_sprite.setPosition(xpos_bullet, ypos_bullet)
    if (direction == "up") {
        bullet_sprite.setVelocity(0, -200)
    } else if (direction == "down") {
        bullet_sprite.setVelocity(0, 200)
    } else if (direction == "left") {
        bullet_sprite.setVelocity(-200, 0)
    } else if (direction == "right") {
        bullet_sprite.setVelocity(200, 0)
    }
    
    stat_shots += 1
}

function create_bullet(): Sprite {
    let bullet_sprite = sprites.create(img`
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
        `, SpriteKind.projectile)
    bullet_list.push(bullet_sprite)
    return bullet_sprite
}

//  Button A
function on_a_pressed() {
    
    if (on_menu == true) {
        on_menu = false
        close_menu()
        story.startCutscene(function lore_cutscene() {
            lore_screen()
            story.startCutscene(function zombie_cutscene() {
                
                sprites.destroy(skip_lore_sprite)
                open_zombie_screen()
            })
        })
        on_lore_screen = true
    } else if (on_lore_screen == true) {
        story.clearAllText()
        skip_lore()
    } else if (on_zombie_screen == true) {
        story.cancelCurrentCutscene()
        on_zombie_screen = false
    } else if (on_end_screen == true) {
        story.clearAllText()
    }
    
}

controller.A.onEvent(ControllerButtonEvent.Pressed, on_a_pressed)
//  Related functions to button A
function close_menu() {
    sprites.destroy(title_sprite)
    sprites.destroy(text_sprite)
}

function skip_lore() {
    
    sprites.destroy(skip_lore_sprite)
    pause(200)
    create_skip_lore_sprite()
}

//  Función para crear la explosión
function explosion(x: number, y: number) {
    let blood: Sprite;
    let angle: number;
    let radians: number;
    
    blood_explosion_sound()
    for (let i = 0; i < explosion_particle_amt; i++) {
        blood = sprites.create(img`
                    . . .
                    . 2 4
                    . . .
        `, SpriteKind.explosion)
        explosion_particle_list.push(blood)
        blood.x = x
        blood.y = y
        angle = Math.randomRange(0, 360)
        radians = angle * Math.PI / 180
        blood.vx = Math.cos(radians) * Math.randomRange(explosion_min_range, explosion_max_range)
        blood.vy = Math.sin(radians) * Math.randomRange(explosion_min_range, explosion_max_range)
        blood.setFlag(SpriteFlag.AutoDestroy, true)
        blood.lifespan = Math.randomRange(800, 1000)
    }
}

//  Función para crear la explosión circular
function blood_explosion(x: number, y: number) {
    let blood: Sprite;
    let angle: number;
    let radians: number;
    
    for (let i = 0; i < blood_explosion_particle_amt; i++) {
        blood = sprites.create(img`
            . . .
            . 7 4
            . . .
        `, SpriteKind.blood_explosion)
        blood.x = x
        blood.y = y
        explosion_particle_list.push(blood)
        angle = Math.randomRange(0, 360)
        radians = angle * Math.PI / 180
        blood.vx = Math.cos(radians) * Math.randomRange(blood_explosion_min_range, blood_explosion_max_range)
        blood.vy = Math.sin(radians) * Math.randomRange(blood_explosion_min_range, blood_explosion_max_range)
        blood.setFlag(SpriteFlag.AutoDestroy, true)
        blood.lifespan = Math.randomRange(800, 1000)
    }
}

controller.A.onEvent(ControllerButtonEvent.Pressed, on_a_pressed)
//  Bullet animation
function animate_bullet_collision(bullet: any) {
    sprites.destroy(bullet)
}

let current_camera_x = 0
// play_foot_step()
function set_boundaries() {
    if (player_sprite.x < 0) {
        player_sprite.x = 0
    }
    
    if (player_sprite.y < 20) {
        player_sprite.y = 20
    }
    
    if (player_sprite.y > screen.height) {
        player_sprite.y = screen.height
    }
    
}

function play_foot_step() {
    let current_time: number;
    
    if (controller.left.isPressed() || controller.right.isPressed() || controller.down.isPressed() || controller.up.isPressed()) {
        current_time = game.runtime()
        if (current_time - footstep_timer > 200) {
            play_custom_footstep()
            footstep_timer = current_time
        }
        
    }
    
}

function play_custom_shot() {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 200, 100, 50, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
}

function play_custom_hit_sound() {
    let startFreq = randint(280, 320)
    let endFreq = randint(140, 160)
    let duration = randint(150, 250)
    //  Slight variation in duration
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, startFreq, endFreq, 100, 0, duration, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
}

//  High starting frequency for "punchy" effect
//  Lower ending frequency for a quick drop
//  Loud start
//  Fade out to silence
//  Duration in milliseconds
//  No extra effects
//  Smooth pitch transition
function play_custom_footstep() {
    let startFreq = randint(220, 240)
    //  Slight variation for realism
    let endFreq = randint(180, 200)
    let duration = 50
    //  Quick and subtle
    music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, startFreq, endFreq, 50, 0, duration, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.InBackground)
}

//  Triangle wave for a soft, smooth tone
//  Moderate volume for subtlety
//  Fade out for realism
//  No additional effects
//  Slightly curved transition
function blood_explosion_sound() {
    music.playTone(200, BeatFraction.Half)
    music.playTone(150, BeatFraction.Quarter)
    music.playTone(800, BeatFraction.Eighth)
    music.playTone(1000, BeatFraction.Eighth)
    music.playTone(1200, BeatFraction.Eighth)
}

function tint_sprite(sprite: Sprite, tint_color: number) {
    let color2: number;
    let original_image = sprite.image.clone()
    for (let x = 0; x < original_image.width; x++) {
        for (let y = 0; y < original_image.height; y++) {
            color2 = original_image.getPixel(x, y)
            if (color2 != 0) {
                original_image.setPixel(x, y, tint_color)
            }
            
        }
    }
    sprite.setImage(original_image)
}

function tint_sprite_time(sprite: Sprite, tint_color: number, duration: number) {
    let original_image = sprite.image.clone()
    let tinted_image = original_image.clone()
    for (let x = 0; x < tinted_image.width; x++) {
        for (let y = 0; y < tinted_image.height; y++) {
            if (tinted_image.getPixel(x, y) != 0) {
                tinted_image.setPixel(x, y, tint_color)
            }
            
        }
    }
    sprite.setImage(tinted_image)
    pause(duration)
    sprite.setImage(original_image)
}

