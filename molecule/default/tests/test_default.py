import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_rustup_init_installed(host):
    rustup_init = host.file("/home/molecule/rustup-init")

    assert rustup_init.is_file
    assert rustup_init.mode == 0o0755
