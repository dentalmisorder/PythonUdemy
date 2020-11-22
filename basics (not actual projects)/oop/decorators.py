import colorama
colorama.init(autoreset=True)

admins = ('ErgoProxy', 'doulikedarkness', 'TheLegend27', 'BABYMETAL')
adm_pass = 'tharja_fire_emblem'

users_registered = {
    'kickme':'123',
    'shantae_lover':'rottytops',
    'BABYMETAL':'road_of_resistance123'
}

info_str = """
    Personal ID: 666777
    HOLO-Card: ..:L..SJ..:..S.S:::...
    Personal Auth Code: GRJ5223 [DO NOT SHOW IT TO ANYONE!]
    """

def box_labels(func):
    def wrap_up(text):
        print('===============START==============')
        func(text)
        print('================END===============')

    return wrap_up

def login_required(func):

    def wrap_up(user):
        user_login = user
        user_password = ''

        if user not in admins:
            print(f'{colorama.Fore.RED}Whoopsie :c')
            print(f'{colorama.Fore.RED}This page requires log-in, sumimasen master')

            while user_login not in users_registered:
                print(f'{colorama.Fore.YELLOW} There is not user registered with name {colorama.Fore.MAGENTA} {user_login}')
                user_login = input(f"{colorama.Fore.MAGENTA}Type in ur username: ")

            while user_password != users_registered[user_login]:
                user_password = input(f'{colorama.Fore.MAGENTA}Type password from {user_login} account: ')
                if user_password == users_registered[user_login]:
                    print(f'{colorama.Fore.GREEN}Logged successfully!')
                    break
            func()
        else:
            adm_pass_in = ''
            while adm_pass_in != adm_pass:
                adm_pass_in = input(f'{colorama.Fore.MAGENTA}Type in adm password: ')
            print(f'{colorama.Fore.GREEN}Logged successfully!')
            func()
    
    return wrap_up

@box_labels
def welcome_msg(text):
    print(f'{colorama.Fore.YELLOW} {text}')

@login_required
def show_info():
    welcome_msg(info_str)


if __name__ == "__main__":
    show_info('bla bla bla username')

colorama.deinit()