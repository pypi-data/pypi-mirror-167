{ pkgs ? import <nixpkgs> {}
, py ? 310
}:
let
  python-name = "python${toString py}";
  python = builtins.getAttr python-name pkgs;
  python-with-tox = python.withPackages (p: with p; [
    tox
  ]);
in
pkgs.mkShell {
  buildInputs = [
    python-with-tox
  ];
  shellHook = ''
    set -e
    TOX_SKIP_ENV=unit-tests tox -p all
    tox -e unit-tests
    exit
  '';
}
