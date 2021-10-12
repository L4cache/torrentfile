#! /usr/bin/python3
# -*- coding: utf-8 -*-

#####################################################################
# THE SOFTWARE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#####################################################################
"""Test main module functionality."""


import sys

import pytest

from tests.context import rmpath, tempfile
from torrentfile import TorrentFile, TorrentFileV2
from torrentfile import __main__ as entry
from torrentfile import main


@pytest.fixture(scope="module")
def tfile():
    """Create fixture for tests."""
    args = [
        "torrentfile",
        "--private",
        "--announce",
        "https://tracker1.to/announce",
        "--source",
        "TFile",
    ]
    t_file = tempfile()
    yield args, t_file
    rmpath(t_file)


def test_main():
    """Test __maine__."""
    assert entry.__doc__  # nosec


def test_main_announce_list(tfile):
    """Test main function with announce list flag."""
    args, path = tfile
    sys.argv = args + [
        "--path",
        path,
        "--announce-list",
        "https://tracker2/announce",
        "https://tracker3/announce",
        "https://tracker4/announce",
    ]
    parser = main()
    url = "https://tracker2/announce"
    assert url in parser.meta["info"]["announce list"]  # nosec
    rmpath(parser.outfile)


def test_main_annlist_single(tfile):
    """Test main function with announce list flag."""
    args, path = tfile
    sys.argv = args + [
        "--path",
        path,
        "--announce-list",
        "https://tracker2/announce",
    ]
    parser = main()
    url = "https://tracker2/announce"
    assert url in parser.meta["info"]["announce list"]  # nosec
    rmpath(parser.outfile)


def test_class_with_annlist(tfile):
    """Test TorrentFile Class with announce list arguement."""
    _, path = tfile
    kwargs = {
        "announce": "https://tracker1.to/announce",
        "path": path,
        "announce_list": (
            "https://tracker2/announce"
            " https://tracker3/announce"
            " https://tracker4/announce"
        ),
    }
    torrent = TorrentFile(**kwargs)
    url = "https://tracker2/announce"
    assert url in torrent.meta["info"]["announce list"]  # nosec


def test_class_tuple_annlist(tfile):
    """Test TorrentFile Class with tuple announce list arguement."""
    _, path = tfile
    kwargs = {
        "announce": "https://tracker1.to/announce",
        "path": path,
        "announce_list": (
            "https://tracker2/announce",
            "https://tracker3/announce",
            "https://tracker4/announce",
        ),
    }
    torfile = TorrentFile(**kwargs)
    meta = torfile.assemble()
    url = "https://tracker2/announce"
    assert url in meta["info"]["announce list"]  # nosec


def test_class_list_annlist(tfile):
    """Test TorrentFile Class with tuple announce list arguement."""
    _, path = tfile
    kwargs = {
        "announce": "https://tracker1.to/announce",
        "path": path,
        "announce_list": [
            "https://tracker2/announce",
            "https://tracker3/announce",
            "https://tracker4/announce",
        ],
    }
    torfile = TorrentFile(**kwargs)
    meta = torfile.assemble()
    url = "https://tracker2/announce"
    assert url in meta["info"]["announce list"]  # nosec


def test_main_annlist_v2(tfile):
    """Test main function with announce list flag."""
    args, path = tfile
    sys.argv = args + [
        "--path",
        path,
        "--announce-list",
        "https://tracker2/announce",
        "https://tracker3/announce",
        "https://tracker4/announce",
        "--meta-version",
        "2",
    ]
    parser = main()
    url = "https://tracker2/announce"
    assert url in parser.meta["info"]["announce list"]  # nosec
    rmpath(parser.outfile)


def test_main_annlist_v3(tfile):
    """Test main function with announce list flag."""
    args, path = tfile
    sys.argv = args + [
        "--path",
        path,
        "--announce-list",
        "https://tracker2/announce",
        "https://tracker3/announce",
        "https://tracker4/announce",
        "--meta-version",
        "3",
    ]
    parser = main()
    url = "https://tracker2/announce"
    assert url in parser.meta["info"]["announce list"]  # nosec
    rmpath(parser.outfile)


def test_main_annlist_single_v2(tfile):
    """Test main function with announce list flag."""
    args, path = tfile
    sys.argv = args + [
        "--path",
        path,
        "--announce-list",
        "https://tracker2/announce",
        "--meta-version",
        "2",
    ]
    parser = main()
    url = "https://tracker2/announce"
    assert url in parser.meta["info"]["announce list"]  # nosec
    rmpath(parser.outfile)


def test_main_annlist_single_v3(tfile):
    """Test main function with announce list flag."""
    args, path = tfile
    sys.argv = args + [
        "--path",
        path,
        "--announce-list",
        "https://tracker2/announce",
        "--meta-version",
        "3",
    ]
    parser = main()
    url = "https://tracker2/announce"
    assert url in parser.meta["info"]["announce list"]  # nosec
    rmpath(parser.outfile)


def test_main_annlist_single_v1(tfile):
    """Test main function with announce list flag."""
    args, path = tfile
    sys.argv = args + [
        "--path",
        path,
        "--announce-list",
        "https://tracker2/announce",
        "--meta-version",
        "1",
    ]
    parser = main()
    url = "https://tracker2/announce"
    assert url in parser.meta["info"]["announce list"]  # nosec
    rmpath(parser.outfile)


def test_class_annlist_v2(tfile):
    """Test TorrentFile Class with announce list arguement."""
    _, path = tfile
    kwargs = {
        "announce": "https://tracker1.to/announce",
        "path": path,
        "announce_list": (
            "https://tracker2/announce"
            " https://tracker3/announce"
            " https://tracker4/announce"
        ),
    }
    torfile = TorrentFileV2(**kwargs)
    meta = torfile.assemble()
    url = "https://tracker2/announce"
    assert url in meta["info"]["announce list"]  # nosec


def test_class_tuple_annlist_v2(tfile):
    """Test TorrentFile Class with tuple announce list arguement."""
    _, path = tfile
    kwargs = {
        "announce": "https://tracker1.to/announce",
        "path": path,
        "announce_list": (
            "https://tracker2/announce",
            "https://tracker3/announce",
            "https://tracker4/announce",
        ),
    }
    torfile = TorrentFileV2(**kwargs)
    meta = torfile.assemble()
    url = "https://tracker2/announce"
    assert url in meta["info"]["announce list"]  # nosec


def test_class_list_annlist_v2(tfile):
    """Test TorrentFile Class with tuple announce list arguement."""
    _, path = tfile
    kwargs = {
        "announce": "https://tracker1.to/announce",
        "path": path,
        "announce_list": [
            "https://tracker2/announce",
            "https://tracker3/announce",
            "https://tracker4/announce",
        ],
    }
    torfile = TorrentFileV2(**kwargs)
    meta = torfile.assemble()
    url = "https://tracker2/announce"
    assert url in meta["info"]["announce list"]  # nosec