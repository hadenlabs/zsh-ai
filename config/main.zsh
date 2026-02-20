#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

function ai::config::main::factory {
    # shellcheck source=/dev/null
    source "${ZSH_AI_PATH}"/config/base.zsh
    case "${OSTYPE}" in
    darwin*)
        # shellcheck source=/dev/null
        source "${ZSH_AI_PATH}"/config/osx.zsh
        ;;
    linux*)
        # shellcheck source=/dev/null
        source "${ZSH_AI_PATH}"/config/linux.zsh
      ;;
    esac
}

ai::config::main::factory