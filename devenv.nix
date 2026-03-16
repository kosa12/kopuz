{ pkgs, lib, config, inputs, ... }:

{
  cachix.pull = [ "rusic" ];
  cachix.push = "rusic";
}
