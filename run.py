from subprocess import call

from pyngrok import ngrok


def clone_github_private_repo(email: str, name: str) -> None:
    private_repo_commands = f'sh scripts/private_repo_clone.sh {email} {name}'
    call(private_repo_commands.split())


def connect_ngork():
    url = ngrok.connect(port=9000)
    return url


if __name__ == '__main__':
    url = connect_ngork()
    print('Installing code-server for Google Colab')
    code_server_install_command = f'sh scripts/code_server_install.sh'
    call(code_server_install_command.split())

    option = input('Do you want to clone private repository from Github? (yes/no) [default: yes]: ')

    if option.lower() not in ('yes', 'y', 'no', 'n'):
        print('Invalid option.')

    if option.lower() in ('n', 'no'):
        print('Go to below address to use code-server')
        print(url)

    email = input('Give email address for git config settings: ')
    name = input('Give name for git config settings: ')
    clone_github_private_repo(email, name)
    print('Add SSH key to your GitHub account')

    print('Now go to below address to use code-server')
    print(url)
