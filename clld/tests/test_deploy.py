from mock import Mock, MagicMock, patch


@patch.multiple('clld.deploy.util',
                time=Mock(),
                getpass=Mock(return_value='password'),
                confirm=Mock(return_value=True),
                virtualenv=MagicMock(),
                sudo=Mock(),
                run=Mock(return_value='{"status": "ok"}'),
                local=Mock(),
                put=Mock(),
                env=Mock(),
                service=Mock(),
                cd=MagicMock(),
                require=Mock(),
                postgres=Mock())
#def test_deploy(confirm, virtualenv, sudo, run, local, put, env, cd, require):
def test_deploy():
    from clld.deploy.util import deploy
    from clld.deploy.config import App

    deploy(App('test', 9999), 'test')
    deploy(App('test', 9999), 'production')