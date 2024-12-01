//  Main
//  Sprites
let player_sprite : Sprite = null
let zombie_sprite : Sprite = null
let bullet_sprite : Sprite = null
//  Sprite lists
let bullet_list : Bullet[] = []
let zombie_list : Zombie[] = []
let deleted_zombies_list : Zombie[] = []
//  Status bar Sprites
let exp_status_bar : StatusBarSprite = null
let statusbar : StatusBarSprite = null
//  Zombie sb
//  Text Sprites
let title_sprite : TextSprite = null
let text_sprite : TextSprite = null
let skip_lore_sprite : TextSprite = null
let skip_stats_sprite : TextSprite = null
//  Enemies stats
let delay_min_enemies = 0
let delay_max_enemies = 0
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
//  Booleans
let on_menu = true
let on_zombie_screen = false
let on_lore_screen = false
let on_stats_screen = false
//  CONSTANTS
//  Boundaries
let RIGHT_BOUNDARY = 160
let LEFT_BOUNDARY = 0
let BOTTOM_BOUNDARY = 120
let TOP_BOUNDARY = 0
//  Stats to Display
let stat_shots = 0
let stat_missed_shots = 0
let stat_precission = 0
let stat_accurate_shots = 0
let stat_zombies_escaped = 0
let stat_zombies_killed = 0
let stat_damage_dealt = 0
let stat_lifes_won = 0
let stat_lifes_lost = 0
//  main
open_main_screen()
namespace SpriteKind {
    export const projectile = SpriteKind.create()
    export const enemy = SpriteKind.create()
    export const player = SpriteKind.create()
}

statusbars.onZero(StatusBarKind.EnemyHealth, function on_on_zero(status: StatusBarSprite) {
    
    status.spriteAttachedTo().destroy(effects.disintegrate)
    stat_zombies_killed += 1
    player_exp += zombie_xp_reward
    update_exp_status_bar()
})
sprites.onOverlap(SpriteKind.projectile, SpriteKind.enemy, function on_projectile_collision(bullet: Sprite, zombie: Sprite) {
    
    stat_accurate_shots += 1
    stat_damage_dealt += player_power
    animate_bullet_collision(bullet)
    statusbars.getStatusBarAttachedTo(StatusBarKind.EnemyHealth, zombie).value += -player_power
    zombie.setVelocity(-zombie_stun_speed, 0)
    pause(zombie_stun_duration)
    zombie.setVelocity(-zombie_speed, 0)
})
sprites.onOverlap(SpriteKind.player, SpriteKind.enemy, function on_player_collision_with_enemy(player: Sprite, zombie: Sprite) {
    
    info.changeLifeBy(-1)
    stat_lifes_lost += 1
    zombie.destroy()
    scene.cameraShake(4, 500)
})
//  Screens
//  Main screen
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

//  Related functions to main screen
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

function create_skip_lore_sprite() {
    
    skip_lore_sprite = textsprite.create("Apreta A para skipear lore")
    skip_lore_sprite.setOutline(0.2, 1)
    skip_lore_sprite.setPosition(80, 110)
}

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

//  First screen
function open_zombie_screen() {
    scene.setBackgroundImage(assets.image`
                cityscape
            `)
    
    on_zombie_screen = true
    on_menu = false
    on_lore_screen = false
    player_level = 1
    create_player()
    story.spriteSayText(player_sprite, "ostras pedrin")
    sprites.destroy(skip_lore_sprite)
    set_player_stats(player_level)
    set_zombie_stats(player_level)
    exp_status_bar = statusbars.create(20, 4, StatusBarKind.Energy)
    exp_status_bar.positionDirection(CollisionDirection.Top)
    controller.moveSprite(player_sprite)
    player_sprite.setStayInScreen(true)
    effects.starField.startScreenEffect()
    scroller.setCameraScrollingMultipliers(1, 0)
    game.onUpdate(function on_on_update() {
        scene.centerCameraAt(player_sprite.x, 60)
    })
    info.setLife(3)
    gamer()
}

function update_exp_status_bar() {
    
    exp_status_bar.max = player_exp_required
    exp_status_bar.value = player_exp
    exp_status_bar.setLabel("EXP: " + player_exp + "/" + player_exp_required)
}

function gamer() {
    
    update_exp_status_bar()
    while (player_exp < player_exp_required && info.life() > 0) {
        pause(randint(delay_min_enemies, delay_max_enemies))
        destroy_zombies()
        destroy_bullets()
        if (player_exp < player_exp_required && info.life() > 0) {
            create_zombie()
        } else {
            next_level()
        }
        
    }
}

function next_level() {
    
    if (info.life() > 0) {
        player_level += 1
    }
    
    if (player_level == 11) {
        game_over()
        return
    }
    
    if (info.life() == 0) {
        game_over()
        return
    }
    
    player_exp = 0
    update_exp_status_bar()
    set_zombie_stats(player_level)
    set_player_stats(player_level)
    game.splash("Level Up! - " + player_level)
    destroy_all_zombies()
    destroy_all_bullets()
    gamer()
}

info.onLifeZero(function on_life_zero() {
    game_over()
})
function game_over() {
    
    if (player_level >= 11) {
        game.splash("Game Over", "You have reached the max level!")
    } else {
        game.splash("Game Over", "You died")
    }
    
    on_stats_screen = true
    story.startCutscene(stats_cutscene)
}

function stats_screen() {
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
    if (player_level == 11) {
        story.printDialog("¡Felicidades, Alex! Has alcanzado el refugio humano.", 80, 90, 50, 150)
        story.printDialog("Gracias a tu ingenio, los supervivientes ahora tienen una oportunidad.", 80, 90, 50, 150)
        story.printDialog("Con tu Micro:bit, comenzará la investigación para encontrar una cura.", 80, 90, 50, 150)
        story.printDialog("El destino de la humanidad está en buenas manos.", 80, 90, 50, 150)
    } else {
        story.printDialog("Alex ha caído en su lucha contra las hordas de zombis.", 80, 90, 50, 150)
        story.printDialog("Aunque su esfuerzo fue valiente, los zombis han tomado el control.", 80, 90, 50, 150)
        story.printDialog("El refugio humano sigue siendo un sueño distante...", 80, 90, 50, 150)
        story.printDialog("¿Podrá la humanidad encontrar una nueva esperanza?", 80, 90, 50, 150)
    }
    
    game.over()
}

function set_player_stats(level: number) {
    
    if (info.life() < 3) {
        info.changeLifeBy(+1)
        stat_lifes_won += 1
    }
    
    if (level == 1) {
        player_hp = 100
        player_power = 50
        player_speed = 200
        player_exp_required = 100
    } else if (level == 2) {
        player_hp = 150
        player_power = 60
        player_speed = 210
        player_exp_required = 200
    } else if (level == 3) {
        player_hp = 200
        player_power = 70
        player_speed = 220
        player_exp_required = 300
    } else if (level == 4) {
        player_hp = 250
        player_power = 80
        player_speed = 230
        player_exp_required = 400
    } else if (level == 5) {
        player_hp = 300
        player_power = 90
        player_speed = 240
        player_exp_required = 500
    } else if (level == 6) {
        player_hp = 350
        player_power = 100
        player_speed = 250
        player_exp_required = 600
    } else if (level == 7) {
        player_hp = 400
        player_power = 110
        player_speed = 260
        player_exp_required = 700
    } else if (level == 8) {
        player_hp = 450
        player_power = 120
        player_speed = 270
        player_exp_required = 800
    } else if (level == 9) {
        player_hp = 500
        player_power = 130
        player_speed = 280
        player_exp_required = 900
    } else if (level == 10) {
        player_hp = 550
        player_power = 140
        player_speed = 290
        player_exp_required = 1000
    }
    
}

function set_zombie_stats(level: number) {
    
    if (level == 1) {
        zombie_hp = 100
        zombie_power = 50
        zombie_speed = 35
        delay_min_enemies = 1000
        delay_max_enemies = 1500
        zombie_xp_reward = 50
        zombie_stun_duration = 2000
        zombie_stun_speed = 10
    } else if (level == 2) {
        zombie_hp = 150
        zombie_power = 60
        zombie_speed = 40
        delay_min_enemies = 900
        delay_max_enemies = 1400
        zombie_xp_reward = 50
        zombie_stun_duration = 1800
        zombie_stun_speed = 12
    } else if (level == 3) {
        zombie_hp = 200
        zombie_power = 70
        zombie_speed = 45
        delay_min_enemies = 800
        delay_max_enemies = 1300
        zombie_xp_reward = 50
        zombie_stun_duration = 1600
        zombie_stun_speed = 14
    } else if (level == 4) {
        zombie_hp = 250
        zombie_power = 80
        zombie_speed = 50
        delay_min_enemies = 700
        delay_max_enemies = 1200
        zombie_xp_reward = 50
        zombie_stun_duration = 1400
        zombie_stun_speed = 16
    } else if (level == 5) {
        zombie_hp = 300
        zombie_power = 90
        zombie_speed = 55
        delay_min_enemies = 600
        delay_max_enemies = 1100
        zombie_xp_reward = 50
        zombie_stun_duration = 1200
        zombie_stun_speed = 18
    } else if (level == 6) {
        zombie_hp = 350
        zombie_power = 100
        zombie_speed = 60
        delay_min_enemies = 500
        delay_max_enemies = 1000
        zombie_xp_reward = 50
        zombie_stun_duration = 1000
        zombie_stun_speed = 20
    } else if (level == 7) {
        zombie_hp = 400
        zombie_power = 110
        zombie_speed = 65
        delay_min_enemies = 400
        delay_max_enemies = 900
        zombie_xp_reward = 50
        zombie_stun_duration = 800
        zombie_stun_speed = 22
    } else if (level == 8) {
        zombie_hp = 450
        zombie_power = 120
        zombie_speed = 70
        delay_min_enemies = 300
        delay_max_enemies = 800
        zombie_xp_reward = 50
        zombie_stun_duration = 600
        zombie_stun_speed = 24
    } else if (level == 9) {
        zombie_hp = 500
        zombie_power = 130
        zombie_speed = 75
        delay_min_enemies = 200
        delay_max_enemies = 700
        zombie_xp_reward = 50
        zombie_stun_duration = 400
        zombie_stun_speed = 26
    } else if (level == 10) {
        zombie_hp = 550
        zombie_power = 140
        zombie_speed = 80
        delay_min_enemies = 100
        delay_max_enemies = 600
        zombie_xp_reward = 50
        zombie_stun_duration = 200
        zombie_stun_speed = 28
    }
    
}

function destroy_bullets() {
    
    
    for (let b of bullet_list) {
        if (b.sprite.x < LEFT_BOUNDARY + player_sprite.x || b.sprite.x > RIGHT_BOUNDARY + player_sprite.x || b.sprite.y > BOTTOM_BOUNDARY + player_sprite.y || b.sprite.y < TOP_BOUNDARY + player_sprite.y) {
            sprites.destroy(b.sprite)
        }
        
    }
}

function destroy_zombies() {
    
    for (let z of zombie_list) {
        if (z.sprite.x < LEFT_BOUNDARY && deleted_zombies_list.indexOf(z) < 0) {
            sprites.destroy(z.sprite, effects.disintegrate)
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
    
    
    for (let z of zombie_list) {
        sprites.destroy(z.sprite)
    }
}

function destroy_all_bullets() {
    
    
    for (let b of bullet_list) {
        sprites.destroy(b.sprite)
    }
}

class Bullet {
    bullet_id: Number
    sprite: Sprite
    constructor(sprite: Sprite, bullet_id: Number) {
        this.bullet_id = bullet_id
        this.sprite = sprite
    }
    
}

class Zombie {
    zombie_id: Number
    sprite: Sprite
    constructor(sprite: Sprite, zombie_id: Number) {
        this.zombie_id = zombie_id
        this.sprite = sprite
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
    player_sprite.setPosition(10, 60)
    player_sprite.setVelocity(player_speed, 0)
    direction = "right"
}

function create_zombie() {
    
    ypos_zombie_sprite = randint(10, 110)
    zombie_sprite = sprites.create(img`
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
        `, SpriteKind.enemy)
    zombie_sprite.setPosition(player_sprite.x + RIGHT_BOUNDARY, ypos_zombie_sprite)
    animation.runImageAnimation(zombie_sprite, [img`
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
            `, img`
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
            `, img`
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
            `, img`
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
            `], 100, true)
    zombie_sprite.setVelocity(-zombie_speed, 0)
    zombie_list.push(new Zombie(zombie_sprite, zombie_list.length + 1))
    statusbar = statusbars.create(16, 2, StatusBarKind.EnemyHealth)
    statusbar.setLabel("HP")
    statusbar.max = zombie_hp
    statusbar.value = zombie_hp
    statusbar.attachToSprite(zombie_sprite)
}

//  Controls
//  Player movement
//  Up
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
    if (on_menu) {
        
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
                `], 200, true)
        direction = "up"
    }
    
})
//  Left
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    
    if (on_menu) {
        
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
                `], 200, true)
        direction = "left"
    }
    
})
//  Right
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    
    if (on_menu) {
        
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
                `], 200, true)
        direction = "right"
    }
    
})
//  Down
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
    if (on_menu) {
        
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
                `], 200, true)
        direction = "down"
    }
    
})
//  Released
//  Right
controller.right.onEvent(ControllerButtonEvent.Released, function on_right_released() {
    if (on_menu) {
        
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
            `], 100, false)
    }
    
})
//  Left
//  Up
controller.up.onEvent(ControllerButtonEvent.Released, function on_up_released() {
    if (on_menu) {
        
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
    if (on_menu) {
        
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
    if (on_menu || on_lore_screen || info.life() == 0) {
        
    } else {
        shot()
    }
    
})
//  Related functions to button B
function shot() {
    
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
    let bullet_id = bullet_list.length + 1
    let bullet = new Bullet(bullet_sprite, bullet_id)
    animate_bullet(bullet_sprite)
    bullet_list.push(bullet)
    return bullet_sprite
}

function stats_cutscene() {
    stats_screen()
}

//  Button A
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (on_menu == true) {
        on_menu = false
        close_menu()
        story.startCutscene(function lore_cutscene() {
            lore_screen()
            story.startCutscene(function zombie_cutscene() {
                
                sprites.destroy(skip_lore_sprite)
                open_zombie_screen()
                story.startCutscene(stats_cutscene)
            })
        })
        on_lore_screen = true
    } else if (on_lore_screen == true) {
        story.clearAllText()
        skip_lore()
    } else if (on_zombie_screen == true) {
        story.cancelCurrentCutscene()
        on_zombie_screen = false
    } else if (on_stats_screen == true) {
        story.clearAllText()
        skip_lore()
    }
    
})
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

//  Bullet animation
function animate_bullet_collision(bullet: any) {
    animation.runImageAnimation(bullet, [img`
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
            `, img`
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
            `, img`
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
            `, img`
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
            `], 0, false)
    pause(0)
    sprites.destroy(bullet)
}

function animate_bullet(bullet: Sprite) {
    while (bullet.x >= 0 && bullet.x <= 120 && (bullet.y >= 0 && bullet.y <= 120)) {
        if (direction == "left") {
            bullet.x += -1
        } else if (direction == "right") {
            bullet.x += 1
        } else if (direction == "up") {
            bullet.y += 1
        } else {
            bullet.y += -1
        }
        
    }
}

