{ pkgs, lib, config, inputs, ... }:

{
  languages = {
    python = {
      enable = true;
      poetry.enable = true;
      poetry.activate.enable = true;
    };
    javascript = {
      enable = true;
      npm.enable = true;
    };
  };
}
