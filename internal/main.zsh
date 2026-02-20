#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

function ai::internal::main::factory {
    # shellcheck source=/dev/null
    source "${ZSH_AI_PATH}"/internal/base.zsh
    case "${OSTYPE}" in
    darwin*)
        # shellcheck source=/dev/null
        source "${ZSH_AI_PATH}"/internal/osx.zsh
        ;;
    linux*)
        # shellcheck source=/dev/null
        source "${ZSH_AI_PATH}"/internal/linux.zsh
      ;;
    esac
    # shellcheck source=/dev/null
    source "${ZSH_AI_PATH}"/internal/helper.zsh
}

ai::internal::main::factory