Ansible role ableton.rustup_init
================================

This role installs [rustup][rustup] on the target host, so that `cargo` and other Rust
utilities can be used.

Requirements
------------

Ansible >= 2.10, and a target host with one of the following platforms:

- Debian Linux (other Linux flavors may work, but haven't been tested)
- macOS
- Windows (8.1 or 10 are required)

Example Playbook
----------------

```yaml
---
- name: Install rustup on hosts
  hosts: "all"

  roles:
    - ableton.rustup_init
```

License
-------

MIT

Maintainers
-----------

This project is maintained by the following GitHub users:

- [@ala-ableton](https://github.com/ala-ableton)
- [@nre-ableton](https://github.com/nre-ableton)


[rustup]: https://rustup.rs/
