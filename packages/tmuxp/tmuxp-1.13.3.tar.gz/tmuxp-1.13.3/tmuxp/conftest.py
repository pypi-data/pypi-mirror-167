import getpass
import logging
import os
import pathlib
import typing as t

import pytest

from _pytest.doctest import DoctestItem
from _pytest.fixtures import SubRequest

from libtmux import exc
from libtmux.common import which
from libtmux.server import Server
from libtmux.test import TEST_SESSION_PREFIX, get_test_session_name, namer
from tests.fixtures import utils as test_utils

if t.TYPE_CHECKING:
    from libtmux.session import Session

logger = logging.getLogger(__name__)
USING_ZSH = "zsh" in os.getenv("SHELL", "")


@pytest.fixture(autouse=True, scope="session")
def home_path(tmp_path_factory: pytest.TempPathFactory):
    return tmp_path_factory.mktemp("home")


@pytest.fixture(autouse=True, scope="session")
def user_path(home_path: pathlib.Path):
    p = home_path / getpass.getuser()
    p.mkdir()
    return p


@pytest.mark.skipif(USING_ZSH, reason="Using ZSH")
@pytest.fixture(autouse=USING_ZSH, scope="session")
def zshrc(user_path: pathlib.Path):
    """This quiets ZSH default message.

    Needs a startup file .zshenv, .zprofile, .zshrc, .zlogin.
    """
    p = user_path / ".zshrc"
    p.touch()
    return p


@pytest.fixture(autouse=True)
def home_path_default(user_path: pathlib.Path):
    os.environ["HOME"] = str(user_path)


@pytest.fixture(scope="function")
def monkeypatch_plugin_test_packages(monkeypatch):
    paths = [
        "tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bwb/",
        "tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_bs/",
        "tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_r/",
        "tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_owc/",
        "tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_awf/",
        "tests/fixtures/pluginsystem/plugins/tmuxp_test_plugin_fail/",
    ]
    for path in paths:
        monkeypatch.syspath_prepend(os.path.abspath(os.path.relpath(path)))


@pytest.fixture(scope="function")
def socket_name(request) -> str:
    return "tmuxp_test%s" % next(namer)


@pytest.fixture(scope="function")
def server(
    request: SubRequest, monkeypatch: pytest.MonkeyPatch, socket_name: str
) -> Server:
    tmux = Server(socket_name=socket_name)

    def fin() -> None:
        tmux.kill_server()

    request.addfinalizer(fin)

    return tmux


@pytest.fixture(scope="function")
def session(server):
    session_name = "tmuxp"

    if not server.has_session(session_name):
        server.cmd(
            "-f",
            "/dev/null",  # use a blank config to reduce side effects
            "new-session",
            "-d",  # detached
            "-s",
            session_name,
            "/bin/sh",  # use /bin/sh as a shell to reduce side effects
            # normally, it'd be -c, but new-session is special
        )

    # find current sessions prefixed with tmuxp
    old_test_sessions = [
        s.get("session_name")
        for s in server._sessions
        if s.get("session_name").startswith(TEST_SESSION_PREFIX)
    ]

    TEST_SESSION_NAME = get_test_session_name(server=server)

    try:
        session = server.new_session(session_name=TEST_SESSION_NAME)
    except exc.LibTmuxException as e:
        raise e

    """
    Make sure that tmuxp can :ref:`test_builder_visually` and switches to
    the newly created session for that testcase.
    """
    session_id = session.get("session_id")
    assert session_id is not None
    try:
        server.switch_client(target_session=session_id)
    except exc.LibTmuxException:
        # server.attach_session(session.get('session_id'))
        pass

    for old_test_session in old_test_sessions:
        logger.debug("Old test test session %s found. Killing it." % old_test_session)
        server.kill_session(old_test_session)
    assert TEST_SESSION_NAME == session.get("session_name")
    assert TEST_SESSION_NAME != "tmuxp"

    return session


@pytest.fixture(autouse=True)
def add_doctest_fixtures(
    request: SubRequest,
    doctest_namespace: t.Dict[str, t.Any],
) -> None:
    if isinstance(request._pyfuncitem, DoctestItem) and which("tmux"):
        doctest_namespace["server"] = request.getfixturevalue("server")
        session: "Session" = request.getfixturevalue("session")
        doctest_namespace["session"] = session
        doctest_namespace["window"] = session.attached_window
        doctest_namespace["pane"] = session.attached_pane
        doctest_namespace["test_utils"] = test_utils
