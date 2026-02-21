#!/usr/bin/env ksh
# -*- coding: utf-8 -*-

function ai::internal::opencode::load {
    [ -e "${AI_OPENCODE_BIN_PATH}" ] && export PATH="${AI_OPENCODE_BIN_PATH}:${PATH}"
}

function ai::internal::packages::install {
    message_info "Installing required ai packages"
    for package in "${AI_PACKAGES[@]}"; do
        case "${package}" in
            opencode)
                ai::internal::opencode::install
                ;;
            fabric)
                ai::internal::fabric::install
                ;;
            ollama)
                ai::internal::ollama::install
                ;;
            *)
                core::install "${package}"
                ;;
        esac
    done
    message_success "Installed required ai packages"
}
