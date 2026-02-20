#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

function ai::core::main::factory {
    # shellcheck source=/dev/null
    source "${ZSH_AI_PATH}"/core/base.zsh
    case "${OSTYPE}" in
    darwin*)
        # shellcheck source=/dev/null
        source "${ZSH_AI_PATH}"/core/osx.zsh
        ;;
    linux*)
        # shellcheck source=/dev/null
        source "${ZSH_AI_PATH}"/core/linux.zsh
      ;;
    esac
}

ai::core::main::factory